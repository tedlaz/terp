import sys
from setuptools import setup


if sys.hexversion < 0x3040000:
    msg = "Python version %s is unsupported, >= 3.4.0 is needed"
    print(msg % (".".join(map(str, sys.version_info[:3]))))
    exit(1)


setup(name='qterp',
      version='0.1.1',
      description='Accounting and Greek Payroll',
      long_description='A basic ERP system for accounting and payroll',
      url='https://github.com/tedlaz/tedutil',
      keywords=["util", "Greek"],
      author='Ted Lazaros',
      author_email='tedlaz@gmail.com',
      # install_requires=['reportlab'],
      license='GPLv3',
      packages=['terp'],
      # see http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=["Development Status :: 4 - Beta",
                   "Environment :: X11 Applications",
                   "Environment :: X11 Applications :: GTK",
                   "Intended Audience :: End Users/Desktop",
                   "Natural Language :: Greek",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python :: 3 :: Only",
                   "Topic :: Office/Business :: Financial :: Accounting"]
      )
