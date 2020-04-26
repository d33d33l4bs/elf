
from setuptools import setup, find_packages
from pathlib    import Path


setup(
    name        = 'deedee.elf',
    version     = Path(__file__).resolve().parents[0].joinpath('version').read_text(),
    package_dir = {'': 'src'},
    packages    = find_packages(where='src'),
    author      = 'Dee Dee',
    description = 'A simple toolbox library allowing to parse ELF files.',
    url         = 'https://github.com/d33d33l4bs/elf'
)

