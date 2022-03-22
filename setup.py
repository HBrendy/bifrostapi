from setuptools import setup, find_packages

def read_file(filename):
  fh = open(filename, "r")
  try:
      return fh.read()
  finally:
      fh.close()

setup(
    name='beoneapi',
    version='0.2.0',
    description='Datahandling API of the OH EJP project BeONE. Fork of the discontinued bifrostapi by Martin Basterrechea.',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/HBrendy/bifrostapi',
    author="Holger Brendebach",
    author_email="pypi@brendy.de",
    packages=find_packages(),
    install_requires=['pymongo', 'sshtunnel'],
    python_requires='>=3.6'
    )
