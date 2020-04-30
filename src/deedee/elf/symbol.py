
from .definitions import *


class ElfSymbol:

    def __init__(self, buffer, hdr):
        self.hdr        = hdr
        self.bind       = ElfSymbolBind(self.hdr.st_info >> 4)
        self.type       = ElfSymbolType(self.hdr.st_info & 0xf)
        self.visibility = ElfSymbolVisibility(self.hdr.st_other & 0x3)
        self.name       = ''
        self.section    = None


def load_symbol(buffer, offset, size):
    raw_hdr = buffer[offset:offset+size]
    hdr     = ElfSym.from_buffer_copy(raw_hdr)
    return ElfSymbol(buffer, hdr)

