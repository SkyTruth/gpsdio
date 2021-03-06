# encoding:utf-8


"""
AIS I/O with Python, dictionaries, and the GPSd AIVDM schema.
"""


from gpsdio.io import open
from gpsdio.io import GPSDIOReader
from gpsdio.io import GPSDIOWriter

import logging

logging.basicConfig()
logger = logging.getLogger('gpsdio')


__all__ = ('open', 'GPSDIOReader', 'GPSDIOWriter')


__version__ = '0.0.9-dev'
__author__ = 'Kevin Wurster, Egil Moeller'
__email__ = 'kevin@skytruth.org, egil@skytruth.org'
__source__ = 'https://github.com/SkyTruth/gpsdio'
__license__ = """
Copyright 2014-2019 SkyTruth

Authors:
Kevin Wurster <kevin@skytruth.org>
Egil Möller <egil@skytruth.org>
Paul Woods <paul@skytruth.org>


Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
