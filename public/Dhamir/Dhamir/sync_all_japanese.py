#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sync and enrich all datasets with complete Japanese translations.
"""

import sys
from build_japanese_dataset import enrich_dhamir_data, enrich_harf_data

if __name__ == '__main__':
    print("==================================================")
    print("SYNCING ALL DATASETS WITH JAPANESE (JA)")
    print("==================================================")
    enrich_dhamir_data()
    enrich_harf_data()
    print("==================================================")
    print("JAPANESE SYNC COMPLETED SUCCESSFULLY!")
    print("==================================================")
