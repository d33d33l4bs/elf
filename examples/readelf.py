
import argparse

import deedee.elf as elf


if __name__ == '__main__':
    parser = argparse.ArgumentParser('A dumb Python readelf')
    path   = parser.add_argument('path')
    args   = parser.parse_args()

    e = elf.Elf.from_path(args.path)

    print('machine:', e.machine.name)
    print('entry:', hex(e.entry))

    print(f'segments ({len(e.segments)}):')
    for n, segment in enumerate(e.segments):
        print(f'    - {n}: {segment.type.name}')

    print(f'sections ({len(e.sections)}):')
    for name, section in e.sections.items():
        print(f'    - {name}: {section.type.name}')

    print('section to segment mappings:')
    for n, segment in enumerate(e.segments):
        print(f'    - {n}: {", ".join(segment.sections.keys())}')

