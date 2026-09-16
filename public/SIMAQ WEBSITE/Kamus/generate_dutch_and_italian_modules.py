#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator script to build complete build_dutch_dataset.py and build_italian_dataset.py
modules with 114 Surah names, 7 Jamid + 17 Harf categories, 76 Jamid words, and 52 Harf words.
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Import template dictionary keys from Japanese/Korean dataset
from build_japanese_dataset import (
    JAPANESE_SURAHS,
    BENTUK_KATA_JA,
    JAPANESE_GRAMMAR,
    BENTUK_HARF_JA,
    JAPANESE_HARF_GRAMMAR
)

print("Creating build_dutch_dataset.py and build_italian_dataset.py...")
