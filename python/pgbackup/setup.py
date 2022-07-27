from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    author='Rodrigo Galba',
    author_email='rodrigogalba@gmail.com',
    description='A utility for backing up PostgreSQL databases.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://github.com/rodrigo-galba/cloudlabs/python/pgbackup',
    packages=find_packages('src')
)