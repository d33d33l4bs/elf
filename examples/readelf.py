
import argparse

from deedee.elf             import Elf
from deedee.elf.definitions import ElfSectionType


if __name__ == '__main__':
    parser = argparse.ArgumentParser('A dumb Python readelf')
    path   = parser.add_argument('path')
    args   = parser.parse_args()

    elf = Elf.from_path(args.path)

    print('machine:', elf.machine.name)
    print('entry:', hex(elf.entry))

    print(f'segments ({len(elf.segments)}):')
    for n, segment in enumerate(elf.segments):
        print(f'    - {n}: {segment.type.name}')

    print(f'sections ({len(elf.sections)}):')
    for section in elf.sections:
        print(f'    - {section.name}: {section.type.name}')

    print('section to segment mappings:')
    for n, segment in enumerate(elf.segments):
        sections = ', '.join(s.name for s in segment.sections)
        print(f'    - {n}: {sections}')

    print('symbols:')
    for section in elf.get_sections(lambda s: s.type == ElfSectionType.SYMTAB or s.type == ElfSectionType.DYNSYM):
        print(f'  - {section.name}:')
        for symbol in section.symbols:
            print(f'    - {symbol.name}')

