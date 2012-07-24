#!/usr/bin/python
#coding:utf-8
# Author:  Dan-Erik Lindberg -- <aideasypea@dan-erik.com>
# Created: 2012-07-12
# License: GPL-3

import os
import sys

import distutils

distutils.core.setup(
    name='aideasypea',
    version='12.10',
    license='GPL-3',
    author='Dan-Erik Lindberg',
    author_email='aideasypea@dan-erik.com',
    keywords=["ADCP","current","stream","water","fluid","ADV"],
    description='AidEasyPea reads ADCP data (Advanced Doppler Current Profiler).',
    long_description = """\
AidEasyPea
-------------------------------------

Works with data from Teledyne ADCP equipment. Tested hardware is RiverBoat Workhorse and StreamPro.
Data is extracted either from binary files (*.000) or from ASCII files with a .ttf template.

This application requires Python 3 or later.
""",
    classifiers = [
           "Programming Language :: Python",
           #"Programming Language :: Python :: 3",
           "Operating System :: Windows",
           "Operating System :: Linux",
           "Operating System :: OS Independent"
           ],
    url='https://launchpad.net/aideasypea'
    )

