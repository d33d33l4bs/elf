
'''Some ELF parsing classes.'''


from .definitions import *
from .section     import *
from .segment     import *


class Elf:

    @classmethod
    def from_path(cls, path):
        with open(path, 'rb') as f:
            data = f.read()
        return cls(data)

    def __init__(self, buffer):
        self.hdr      = ElfEhdr.from_buffer_copy(buffer)
        self.type     = ElfType(self.hdr.e_type)
        self.machine  = ElfMachine(self.hdr.e_machine)
        self.version  = ElfVersion(self.hdr.e_version)
        self.sections = [
            load_section(buffer, offset, self.shentsize)
            for offset in range(
                self.shoff,
                self.shoff + self.shnum * self.shentsize,
                self.shentsize
            )
        ]
        self.segments = [
            load_segment(buffer, offset, self.phentsize)
            for offset in range(
                self.phoff,
                self.phoff + self.phnum * self.phentsize,
                self.phentsize
            )
        ]
        self.__post_init()

    def __getattr__(self, name):
        return getattr(self.hdr, f'e_{name}')

    def __post_init(self):
        for section in self.sections:
            section.post_init(self)
        for segment in self.segments:
            segment.post_init(self)

    def get_sections(self, pred):
        return filter(pred, self.sections)

    def get_segments(self, pred):
        return filter(pred, self.segments)

