#!/usr/bin/env python

from setuptools import setup, find_packages

exec(open('opty/version.py').read())

setup(
    name='opty',
    version=__version__,
    author='Jason Keith Moore',
    author_email='moorepants@gmail.com',
    packages=find_packages(),
    url='http://github.com/csu-hmc/opty',
    license='LICENSE.txt',
    description=('Tools for optimizing dynamic systems using direct '
                 'collocation.'),
    long_description=open('README.rst').read(),
    install_requires=['numpy>=1.8.1',
                      'scipy>=0.14.1',
                      'sympy>=0.7.6',
                      'cython',
                      'ipopt',  # cyipopt
                      ],
    extras_require={'examples': ['pydy>=0.2.1',
                                 'matplotlib>=1.3.1',
                                 'tables',
                                 ],
                    'doc': ['sphinx',
                            'numpydoc',
                            ],
                    },
    tests_require=['nose'],
    test_suite='nose.collector',
    classifiers=['Programming Language :: Python',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Operating System :: OS Independent',
                 'Development Status :: 4 - Beta',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: BSD License',
                 'Natural Language :: English',
                 'Topic :: Scientific/Engineering',
                 'Topic :: Scientific/Engineering :: Physics']
)
