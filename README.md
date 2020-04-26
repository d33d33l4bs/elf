# Introduction

`deedee.elf` is a simple library allowing to parse ELF files.
As my other tools, this one is made to ease the development of POCs.


# Warnings

You can use this one but remember that its primary goal is to store some ugly pieces of code I wrote for my proof of concepts.
Therefore don't expect to see a beautiful code or a pretty architecture.


# Install

```bash
git clone https://github.com/d33d33l4bs/proc.git
cd proc
pip install .
```


# Example

To display some information about an ELF file:

```python
import deedee.elf as elf


with open('/bin/ls', 'rb') as f:
    data = f.read()

ls = elf.Elf(data)

print('machine:', ls.machine.name)
print('entry:', hex(ls.entry))

print(f'segments ({len(ls.segments)}):')
for n, segment in enumerate(ls.segments):
    print(f'    - {n}: {segment.type.name}')

print(f'sections ({len(ls.sections)}):')
for name, section in ls.sections.items():
    print(f'    - {name}: {section.type.name}')

print('section to segment mappings:')
for n, segment in enumerate(ls.segments):
    print(f'    - {n}: {", ".join(segment.sections.keys())}')

```

Here is the output:

```
machine: X86_64
entry: 0x68a0
segments (13):
    - 0: PHDR
    - 1: INTERP
    - 2: LOAD
    - 3: LOAD
    - 4: LOAD
    - 5: LOAD
    - 6: DYNAMIC
    - 7: NOTE
    - 8: NOTE
    - 9: UNKNOWN
    - 10: GNU_EH_FRAME
    - 11: GNU_STACK
    - 12: GNU_RELRO
sections (31):
    - : NULL
    - .interp: PROGBITS
    - .note.gnu.property: NOTE
    - .note.gnu.build-id: NOTE
    - .note.ABI-tag: NOTE
    - .gnu.hash: GNU_HASH
    - .dynsym: DYNSYM
    - .dynstr: STRTAB
    - .gnu.version: GNU_versym
    - .gnu.version_r: GNU_verneed
    - .rela.dyn: RELA
    - .rela.plt: RELA
    - .init: PROGBITS
    - .plt: PROGBITS
    - .plt.sec: PROGBITS
    - .text: PROGBITS
    - .fini: PROGBITS
    - .rodata: PROGBITS
    - .eh_frame_hdr: PROGBITS
    - .eh_frame: PROGBITS
    - .init_array: INIT_ARRAY
    - .fini_array: FINI_ARRAY
    - .data.rel.ro: PROGBITS
    - .dynamic: DYNAMIC
    - .got: PROGBITS
    - .data: PROGBITS
    - .bss: NOBITS
    - .gnu.build.attributes: NOTE
    - .gnu_debuglink: PROGBITS
    - .gnu_debugdata: PROGBITS
    - .shstrtab: STRTAB
section to segment mappings:
    - 0:
    - 1: .interp
    - 2: , .interp, .note.gnu.property, .note.gnu.build-id, .note.ABI-tag, .gnu.hash, .dynsym, .dynstr, .gnu.version, .gnu.version_r, .rela.dyn, .rela.plt
    - 3: .init, .plt, .plt.sec, .text, .fini
    - 4: .rodata, .eh_frame_hdr, .eh_frame
    - 5: .init_array, .fini_array, .data.rel.ro, .dynamic, .got, .data
    - 6: .dynamic
    - 7: .note.gnu.property
    - 8: .note.gnu.build-id, .note.ABI-tag
    - 9: .note.gnu.property
    - 10: .eh_frame_hdr
    - 11:
    - 12: .init_array, .fini_array, .data.rel.ro, .dynamic, .got
```

