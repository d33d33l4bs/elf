
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
        self.hdr       = ElfEhdr.from_buffer_copy(buffer)
        self.type      = ElfType(self.hdr.e_type)
        self.machine   = ElfMachine(self.hdr.e_machine)
        self.version   = ElfVersion(self.hdr.e_version)
        self.sections  = {}
        self.segments  = {}
        self.has_shstr = False
        self.__load_sections(buffer)
        self.__load_segments(buffer)

    def __getattr__(self, name):
        return getattr(self.hdr, f'e_{name}')

    def __load_sections(self, buffer):
        sections = [
            load_section(buffer, offset, self.shentsize)
            for offset in range(
                self.shoff,
                self.shoff + self.shnum * self.shentsize,
                self.shentsize
            )
        ]
        # load the sections name if possible
        if self.shstrndx == ElfSectionIndice.UNDEF:
            self.has_shstr = False
            # If no shstr, the name of the section is its index.
            # It's possible to just write `self.sections = sections` but
            # I want the type of `self.section` remains the same.
            self.sections  = dict(enumerate(sections))
        else:
            # if shstr, get the names inside
            self.has_shstr = True
            self.sections  = {}
            if self.shstrndx == ElfSectionIndice.XINDEX:
                shstr_index = sections[0].sh_link
            else:
                shstr_index = self.shstrndx
            strtab = sections[shstr_index]
            for section in sections:
                offset              = section.hdr.sh_name
                name                = strtab.get_str(offset)
                section.name        = name
                self.sections[name] = section

    def __load_segments(self, buffer):
        self.segments = [
            load_segment(buffer, offset, self.phentsize)
            for offset in range(
                self.phoff,
                self.phoff + self.phnum * self.phentsize,
                self.phentsize
            )
        ]
        # attach sections to segments (not optimized)
        for segment in self.segments:
            segment_start = segment.offset
            segment_end   = segment_start + segment.filesz
            for name, section in self.sections.items():
                if segment_start <= section.offset < segment_end:
                    segment.sections[name] = section

