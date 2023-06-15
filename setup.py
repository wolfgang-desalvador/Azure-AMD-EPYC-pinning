from setuptools import setup, Command

from distutils.command.build_py import build_py

with open('README.md') as infile:
    long_description = infile.read()

from az_pinning import __version__

setup(name='az_pinning',
      version=__version__,
      description='Python package to facilitate MPI pinning on Azure HPC VMs',
      long_description=long_description,
      url='https://github.com/wolfgang-desalvador/Azure-AMD-EPYC-pinning',
      license='MIT License',
      author='Wolfgang De Salvador',
      author_email='',
      packages=['az_pinning', 'az_pinning.tests'],
      provides=['az_pinning'],
      install_requires=[],
      cmdclass={'build_py': build_py},
      entry_points={'console_scripts': ['az_pinning = az_pinning.main:main']},
      classifiers=[
                   "Development Status :: 3 - Alpha",
                   "Programming Language :: Python",
                   "License :: OSI Approved :: MIT License",
                  ],
     )