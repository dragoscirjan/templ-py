
from setuptools import setup, find_packages
from pytempl.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='pytempl',
    version=VERSION,
    description='Pre-Commit Python Lint/Formatter Configurator',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Dragos Cirjan',
    author_email='dragos.cirjan@gmail.com',
    url='https://github.com/dragoscirjan/templ-py',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'pytempl': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        pytempl = pytempl.main:main
    """,
)
