from gettext import install
from importlib.metadata import entry_points
from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='restcli',
    version='0.1.0',
    author='Rodrigo Galba',
    author_email='rodrigogalba@gmail.com',
    description='A utility to consume REST APIs.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://github.com/rodrigo-galba/cloudlabs/python/rest-cli',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['click'],
    python_requires='>=3.9',
    entry_points='''
        [console_scripts]
        restcli=restcli.cli:cli
    ''',
)