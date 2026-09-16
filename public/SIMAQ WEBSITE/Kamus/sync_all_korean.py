#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sync and enrich all datasets with complete Korean translations.
"""

import sys
from build_korean_dataset import enrich_dhamir_data, enrich_harf_data

if __name__ == '__main__':
    print("==================================================")
    print("SYNCING ALL DATASETS WITH KOREAN (KO)")
    print("==================================================")
    enrich_dhamir_data()
    enrich_harf_data()
    print("==================================================")
    print("KOREAN SYNC COMPLETED SUCCESSFULLY!")
    print("==================================================")
