
from .definitions import *
from .symbol      import load_symbol


class ElfSection:

    def __init__(self, buffer, hdr):
        self.hdr     = hdr
        self.type    = ElfSectionType(hdr.sh_type)
        self.flags   = ElfSectionFlags(hdr.sh_flags)
        self.data    = self.__get_data(buffer)
        self.name    = ''
        self.segment = None

    def __getattr__(self, name):
        return getattr(self.hdr, f'sh_{name}')

    def __get_data(self, buffer):
        if self.type == ElfSectionType.NOBITS:
            return b''
        start = self.offset
        stop  = self.offset + self.size
        return buffer[start:stop]

    def post_init(self, elf):
        # Sets the name of the section.
        if elf.shstrndx != ElfSectionIndice.UNDEF:
            if elf.shstrndx == ElfSectionIndice.XINDEX:
                index = elf.sections[0].sh_link
            else:
                index = elf.shstrndx
            strtab    = elf.sections[index]
            self.name = strtab.get_str(self.hdr.sh_name)


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

    def post_init(self, elf):
        super().post_init(elf)
        strtab = elf.sections[self.link]
        for symbol in self.symbols:
            symbol.name = strtab.get_str(symbol.hdr.st_name)


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

