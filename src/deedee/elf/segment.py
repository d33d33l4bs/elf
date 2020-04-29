
from .definitions import *


class ElfSegment:

    def __init__(self, buffer, hdr):
        self.hdr = hdr
        try:
            self.type = ElfSegmentType(self.hdr.p_type)
        except ValueError:
            self.type = ElfSegmentType.UNKNOWN
        self.flags    = ElfSegmentFlags(self.hdr.p_flags)
        self.sections = {}

    def __getattr__(self, name):
        return getattr(self.hdr, f'p_{name}')


def load_segment(buffer, offset, phentsize):
    raw_hdr = buffer[offset:offset+phentsize]
    hdr     = ElfPhdr.from_buffer_copy(raw_hdr)
    return ElfSegment(buffer, hdr)

