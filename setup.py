# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='AMFM_decompy',
    version='1.0.4',
    author='Bernardo J.B. Schmitt',
    author_email='bernardo.jb.schmitt@gmail.com',
    packages=['amfm_decompy'],
    scripts=['bin/AMFM_test.py'],
    package_data = {'amfm_decompy': ['*.wav']},
    url='https://github.com/bjbschmitt/AMFM_decompy/',
    license='LICENSE.txt',
    description='Package to decompose the voiced part of a speech signal into \
                    its modulated components, aka AM-FM decomposition.',
    long_description=open('README.txt').read(),
)

