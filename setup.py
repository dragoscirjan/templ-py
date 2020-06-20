from setuptools import find_packages, setup

from python_template import get_static_version

VERSION = get_static_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

r = open('requirements.txt')
REQUIREMENTS = list(filter(lambda req: req, r.read().split("\n")))
r.close()

setup(
    name='python_template',
    version=VERSION,
    description='Python Template :: Template for Coding with Python',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Dragos Cirjan',
    author_email='dragos.cirjan@gmail.com',
    url='https://github.com/templ-project/python',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'main': ['python_template/*']},
    include_package_data=True,
    # comment this if you're not creating an application
    entry_points="""
        [console_scripts]
        python_template = main:main
    """,
    install_requires=REQUIREMENTS
)
