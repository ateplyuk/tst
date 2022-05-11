from setuptools import setup

requirements = read('requirements.txt').splitlines()

setup(name='tst',
      version='1.0.0',
      description='test',
      url='https://github.com/ateplyuk/tst'
      packages=['tst'],
      install_requires=requirements
      )