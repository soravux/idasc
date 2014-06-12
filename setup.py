#!/usr/bin/env python

from setuptools import setup


setup(
    name='',
    version="0.1",
    description='Image Downloader',
    long_description='Generates an image database using a keyword.',
    author='Yannick Hold',
    author_email='yannickhold@gmail.com',
    url='',
    download_url='',
    install_requires=[
        'gdata>=2.0.18'
        'Pillow>=2.4.0'
        'requests>=2.3.0',
    ],
    py_modules=[
        'imdown.py',
    ],
    packages=[],
    platforms=['any'],
    keywords=[
        'web scraper',
        'image database',
        'image downloader',
    ],
    license='LGPL',
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: GNU Library or Lesser General Public '
    'License (LGPL)',
    'Programming Language :: Python',
    'Topic :: Multimedia :: Graphics :: Capture',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Scientific/Engineering :: Image Recognition',
    ],
)
