
from .definitions import *
from .symbol      import load_symbol


class ElfSection:

    def __init__(self, buffer, hdr):
        self.hdr   = hdr
        self.type  = ElfSectionType(hdr.sh_type)
        self.flags = ElfSectionFlags(hdr.sh_flags)
        self.name  = ''
        if self.type == ElfSectionType.NOBITS:
            self.data = b''
        else:
            self.data = buffer[hdr.sh_offset:hdr.sh_offset+hdr.sh_size]

    def __getattr__(self, name):
        return getattr(self.hdr, f'sh_{name}')


class ElfSectionStrtab(ElfSection):

    def get_str(self, offset):
        size = self.data[offset:].index(b'\x00')
        return self.data[offset:offset+size].decode()


class ElfSectionSymtab(ElfSection):

    def __init__(self, buffer, hdr):
        super().__init__(buffer, hdr)
        self.symbols = [
            load_symbol(buffer, offset, self.entsize)
            for offset in range(
                self.offset,
                self.size,
                self.entsize
            )
        ]


SECTIONS_TAB = {
    ElfSectionType.STRTAB: ElfSectionStrtab,
    ElfSectionType.SYMTAB: ElfSectionSymtab,
    ElfSectionType.DYNSYM: ElfSectionSymtab
}


def load_section(buffer, offset, shentsize):
    raw_hdr = buffer[offset:offset+shentsize]
    hdr     = ElfShdr.from_buffer_copy(raw_hdr)
    type_   = ElfSectionType(hdr.sh_type)
    cls     = SECTIONS_TAB.get(type_, ElfSection)
    return cls(buffer, hdr)

