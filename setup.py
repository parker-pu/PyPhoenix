# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='pyphoenix',
    version='0.1.0',
    description=(
        '使用Python与java jar操作phoenix'
    ),
    long_description=open('README.rst').read(),
    author='parker',
    author_email='i54605@outlook.com',
    maintainer='parker',
    maintainer_email='i54605@outlook.com',
    license='Apache License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/parker-pu/PyPhoenix',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
        'jaydebeapi',
        'JPype1==0.6.3',
    ],
)
