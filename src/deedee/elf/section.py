
from .definitions import *


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

    def __init__(self, buffer, hdr):
        super().__init__(buffer, hdr)

    def get_str(self, offset):
        size = self.data[offset:].index(b'\x00')
        return self.data[offset:offset+size].decode()


SECTIONS_TAB = {
    ElfSectionType.STRTAB: ElfSectionStrtab
}


def load_section(buffer, offset, shentsize):
    raw_hdr = buffer[offset:offset+shentsize]
    hdr     = ElfShdr.from_buffer_copy(raw_hdr)
    type_   = ElfSectionType(hdr.sh_type)
    cls     = SECTIONS_TAB.get(type_, ElfSection)
    return cls(buffer, hdr)

