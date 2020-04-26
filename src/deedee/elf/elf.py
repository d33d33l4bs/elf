
'''Some ELF parsing classes.'''


from ctypes import *
from enum   import IntEnum, Flag


class ElfType(IntEnum):
    NONE   = 0
    REL    = 1
    EXEC   = 2
    DYN    = 3
    CORE   = 4
    NUM    = 5
    LOOS   = 0xfe00
    HIOS   = 0xfeff
    LOPROC = 0xff00
    HIPROC = 0xffff


class ElfMachine(IntEnum):
    NONE             = 0
    M32              = 1
    SPARC            = 2
    _386             = 3
    _68K             = 4
    _88K             = 5
    IAMCU            = 6
    _860             = 7
    MIPS             = 8
    S370             = 9
    MIPS_RS3_LE      = 10
    PARISC           = 15
    VPP500           = 17
    SPARC32PLUS      = 18
    _960             = 19
    PPC              = 20
    PPC64            = 21
    S390             = 22
    SPU              = 23
    V800             = 36
    FR20             = 37
    RH32             = 38
    RCE              = 39
    ARM              = 40
    FAKE_ALPHA       = 41
    SH               = 42
    SPARCV9          = 43
    TRICORE          = 44
    ARC              = 45
    H8_300           = 46
    H8_300H          = 47
    H8S              = 48
    H8_500           = 49
    IA_64            = 50
    MIPS_X           = 51
    COLDFIRE         = 52
    _68HC12          = 53
    MMA              = 54
    PCP              = 55
    NCPU             = 56
    NDR1             = 57
    STARCORE         = 58
    ME16             = 59
    ST100            = 60
    TINYJ            = 61
    X86_64           = 62
    PDSP             = 63
    PDP10            = 64
    PDP11            = 65
    FX66             = 66
    ST9PLUS          = 67
    ST7              = 68
    _68HC16          = 69
    _68HC11          = 70
    _68HC08          = 71
    _68HC05          = 72
    SVX              = 73
    ST19             = 74
    VAX              = 75
    CRIS             = 76
    JAVELIN          = 77
    FIREPATH         = 78
    ZSP              = 79
    MMIX             = 80
    HUANY            = 81
    PRISM            = 82
    AVR              = 83
    FR30             = 84
    D10V             = 85
    D30V             = 86
    V850             = 87
    M32R             = 88
    MN10300          = 89
    MN10200          = 90
    PJ               = 91
    OPENRISC         = 92
    ARC_COMPACT      = 93
    XTENSA           = 94
    VIDEOCORE        = 95
    TMM_GPP          = 96
    NS32K            = 97
    TPC              = 98
    SNP1K            = 99
    ST200            = 100
    IP2K             = 101
    MAX              = 102
    CR               = 103
    F2MC16           = 104
    MSP430           = 105
    BLACKFIN         = 106
    SE_C33           = 107
    SEP              = 108
    ARCA             = 109
    UNICORE          = 110
    EXCESS           = 111
    DXP              = 112
    ALTERA_NIOS2     = 113
    CRX              = 114
    XGATE            = 115
    C166             = 116
    M16C             = 117
    DSPIC30F         = 118
    CE               = 119
    M32C             = 120
    TSK3000          = 131
    RS08             = 132
    SHARC            = 133
    ECOG2            = 134
    SCORE7           = 135
    DSP24            = 136
    VIDEOCORE3       = 137
    LATTICEMICO32    = 138
    SE_C17           = 139
    TI_C6000         = 140
    TI_C2000         = 141
    TI_C5500         = 142
    TI_ARP32         = 143
    TI_PRU           = 144
    MMDSP_PLUS       = 160
    CYPRESS_M8C      = 161
    R32C             = 162
    TRIMEDIA         = 163
    QDSP6            = 164
    _8051            = 165
    STXP7X           = 166
    NDS32            = 167
    ECOG1X           = 168
    MAXQ30           = 169
    XIMO16           = 170
    MANIK            = 171
    CRAYNV2          = 172
    RX               = 173
    METAG            = 174
    MCST_ELBRUS      = 175
    ECOG16           = 176
    CR16             = 177
    ETPU             = 178
    SLE9X            = 179
    L10M             = 180
    K10M             = 181
    AARCH64          = 183
    AVR32            = 185
    STM8             = 186
    TILE64           = 187
    TILEPRO          = 188
    MICROBLAZE       = 189
    CUDA             = 190
    TILEGX           = 191
    CLOUDSHIELD      = 192
    COREA_1ST        = 193
    COREA_2ND        = 194
    ARC_COMPACT2     = 195
    OPEN8            = 196
    RL78             = 197
    VIDEOCORE5       = 198
    _78KOR           = 199
    _56800EX         = 200
    BA1              = 201
    BA2              = 202
    XCORE            = 203
    MCHP_PIC         = 204
    KM32             = 210
    KMX32            = 211
    EMX16            = 212
    EMX8             = 213
    KVARC            = 214
    CDP              = 215
    COGE             = 216
    COOL             = 217
    NORC             = 218
    CSR_KALIMBA      = 219
    Z80              = 220
    VISIUM           = 221
    FT32             = 222
    MOXIE            = 223
    AMDGPU           = 224
    RISCV            = 243
    BPF              = 247
    CSKY             = 252
    NUM              = 253
    ALPHA            = 0x9026


class ElfVersion(IntEnum):
    NONE    = 0
    CURRENT = 1
    NUM     = 2


class ElfSegmentType(IntEnum):
    NULL         = 0
    LOAD         = 1
    DYNAMIC      = 2
    INTERP       = 3
    NOTE         = 4
    SHLIB        = 5
    PHDR         = 6
    TLS          = 7
    NUM          = 8
    LOOS         = 0x60000000
    GNU_EH_FRAME = 0x6474e550
    GNU_STACK    = 0x6474e551
    GNU_RELRO    = 0x6474e552
    LOSUNW       = 0x6ffffffa
    SUNWBSS      = 0x6ffffffa
    SUNWSTACK    = 0x6ffffffb
    HISUNW       = 0x6fffffff
    HIOS         = 0x6fffffff
    LOPROC       = 0x70000000
    HIPROC       = 0x7fffffff
    UNKNOWN         = -1


class ElfSegmentFlags(Flag):
    X        = 1 << 0
    W        = 1 << 1
    R        = 1 << 2
    MASKOS   = 0x0ff00000
    MASKPROC = 0xf0000000


class ElfSectionIndice(IntEnum):
    UNDEF     = 0
    LORESERVE = 0xff00
    LOPROC    = 0xff00
    BEFORE    = 0xff00
    AFTER     = 0xff01
    HIPROC    = 0xff1f
    LOOS      = 0xff20
    HIOS      = 0xff3f
    ABS       = 0xfff1
    COMMON    = 0xfff2
    XINDEX    = 0xffff
    HIRESERVE = 0xffff


class ElfSectionType(IntEnum):
    NULL           = 0
    PROGBITS       = 1
    SYMTAB         = 2
    STRTAB         = 3
    RELA           = 4
    HASH           = 5
    DYNAMIC        = 6
    NOTE           = 7
    NOBITS         = 8
    REL            = 9
    SHLIB          = 10
    DYNSYM         = 11
    INIT_ARRAY     = 14
    FINI_ARRAY     = 15
    PREINIT_ARRAY  = 16
    GROUP          = 17
    SYMTAB_SHNDX   = 18
    NUM            = 19
    LOOS           = 0x60000000
    GNU_ATTRIBUTES = 0x6ffffff5
    GNU_HASH       = 0x6ffffff6
    GNU_LIBLIST    = 0x6ffffff7
    CHECKSUM       = 0x6ffffff8
    LOSUNW         = 0x6ffffffa
    SUNW_move      = 0x6ffffffa
    SUNW_COMDAT    = 0x6ffffffb
    SUNW_syminfo   = 0x6ffffffc
    GNU_verdef     = 0x6ffffffd
    GNU_verneed    = 0x6ffffffe
    GNU_versym     = 0x6fffffff
    HISUNW         = 0x6fffffff
    HIOS           = 0x6fffffff
    LOPROC         = 0x70000000
    HIPROC         = 0x7fffffff
    LOUSER         = 0x80000000
    HIUSER         = 0x8fffffff


class ElfSectionFlags(Flag):
    WRITE            = 1 << 0
    ALLOC            = 1 << 1
    EXECINSTR        = 1 << 2
    MERGE            = 1 << 4
    STRINGS          = 1 << 5
    INFO_LINK        = 1 << 6
    LINK_ORDER       = 1 << 7
    OS_NONCONFORMING = 1 << 8
    GROUP            = 1 << 9
    TLS              = 1 << 10
    COMPRESSED       = 1 << 11
    MASKOS           = 0x0ff00000
    MASKPROC         = 0xf0000000


class ElfEhdr(Structure):
    _pack_   = True
    _fields_ = [
        ('e_ident',     c_ubyte * 16),
        ('e_type',      c_ushort),
        ('e_machine',   c_ushort),
        ('e_version',   c_uint),
        ('e_entry',     c_void_p),
        ('e_phoff',     c_ulonglong),
        ('e_shoff',     c_ulonglong),
        ('e_flags',     c_uint),
        ('e_ehsize',    c_ushort),
        ('e_phentsize', c_ushort),
        ('e_phnum',     c_ushort),
        ('e_shentsize', c_ushort),
        ('e_shnum',     c_ushort),
        ('e_shstrndx',  c_ushort)
    ]

class ElfPhdr(Structure):
    _pack_   = True
    _fields_ = [
        ('p_type',   c_uint),
        ('p_flags',  c_uint),
        ('p_offset', c_ulonglong),
        ('p_vaddr',  c_ulonglong),
        ('p_paddr',  c_ulonglong),
        ('p_filesz', c_ulonglong),
        ('p_memsz',  c_ulonglong),
        ('p_align',  c_ulonglong)
    ]


class ElfShdr(Structure):
    _pack_   = True
    _fields_ = [
        ('sh_name',      c_uint),
        ('sh_type',      c_uint),
        ('sh_flags',     c_ulonglong),
        ('sh_addr',      c_ulonglong),
        ('sh_offset',    c_ulonglong),
        ('sh_size',      c_ulonglong),
        ('sh_link',      c_uint),
        ('sh_info',      c_uint),
        ('sh_addralign', c_ulonglong),
        ('sh_entsize',   c_ulonglong)
    ]


class ElfSym(Structure):
    _pack_   = True
    _fields_ = [
        ('st_name',  c_uint),
        ('st_info',  c_ubyte),
        ('st_other', c_ubyte),
        ('st_shndx', c_ushort),
        ('st_value', c_ulonglong),
        ('st_size',  c_ulonglong)
    ]


class ElfSection:
    
    def __init__(self, data):
        self.hdr   = ElfShdr.from_buffer_copy(data)
        self.type  = ElfSectionType(self.hdr.sh_type)
        self.flags = ElfSectionFlags(self.hdr.sh_flags)
        for hdr_field, _ in self.hdr._fields_:
            field = hdr_field[3:]
            if not hasattr(self, field):
                value = getattr(self.hdr, hdr_field)
                setattr(self, field, value)

    def __repr__(self):
        return f'Section({repr(self.name)}, {self.type.name})'


class ElfSegment:

    def __init__(self, data):
        self.hdr = ElfPhdr.from_buffer_copy(data)
        try:
            self.type = ElfSegmentType(self.hdr.p_type)
        except ValueError:
            self.type = ElfSegmentType.UNKNOWN
        self.flags    = ElfSegmentFlags(self.hdr.p_flags)
        self.sections = {}
        for hdr_field, _ in self.hdr._fields_:
            field = hdr_field[2:]
            if not hasattr(self, field):
                value = getattr(self.hdr, hdr_field)
                setattr(self, field, value)


class Elf:

    def __init__(self, data):
        self.hdr       = ElfEhdr.from_buffer_copy(data)
        self.type      = ElfType(self.hdr.e_type)
        self.machine   = ElfMachine(self.hdr.e_machine)
        self.version   = ElfVersion(self.hdr.e_version)
        self.sections  = {}
        self.has_shstr = False
        self.segments  = {}
        for hdr_field, _ in self.hdr._fields_:
            field = hdr_field[2:]
            if not hasattr(self, field):
                value = getattr(self.hdr, hdr_field)
                setattr(self, field, value)
        self.__load_sections(data)
        self.__load_segments(data)

    def __load_sections(self, data):
        sections = [
            ElfSection(data[offset:offset+self.shentsize])
            for offset in range(
                self.shoff,
                self.shoff + self.shnum * self.shentsize,
                self.shentsize
            )
        ]
        # load the sections name if possible
        if self.shstrndx == ElfSectionIndice.UNDEF:
            # if no shstr, the name of the section is its index
            self.has_shstr = False
            # why not just self.sections = sections?
            #   -> in order to give the same type to self.sections (dict)
            self.sections  = dict((n, s) for n, s in enumerate(sections))
        else:
            # if shstr, get the name inside
            self.has_shstr = True
            self.sections  = {}
            if self.shstrndx == ElfSectionIndice.XINDEX:
                shstr_index = sections[0].sh_link
            else:
                shstr_index = self.shstrndx
            shstr = sections[shstr_index]
            strs  = data[shstr.offset:shstr.offset+shstr.size]
            for section in sections:
                start = section.name
                end   = start + strs[start:].index(b'\x00')
                name  = strs[start:end].decode()
                section.name = name
                self.sections[name] = section

    def __load_segments(self, data):
        self.segments = [
            ElfSegment(data[offset:offset+self.phentsize])
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
                if section.offset >= segment_start and section.offset < segment_end:
                    segment.sections[name] = section

