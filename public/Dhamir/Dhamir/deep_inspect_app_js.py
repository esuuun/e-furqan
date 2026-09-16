#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deep inspection of Portuguese i18n keys and functions in app.js
"""

import re
import json

with open('app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# Check dropdown population
print("--- Checking populateBentukDropdown ---")
idx_bentuk = code.find('function populateBentukDropdown')
idx_bentuk_end = code.find('function populateNoKataDropdown')
print(code[idx_bentuk:idx_bentuk_end])

print("\n--- Checking populateNoKataDropdown ---")
idx_nokata = code.find('function populateNoKataDropdown')
idx_nokata_end = code.find('function getDefaultJenis')
print(code[idx_nokata:idx_nokata_end])

print("\n--- Checking btnCopyAll ---")
idx_copy = code.find('elements.btnCopyAll.addEventListener')
print(code[idx_copy:idx_copy+800])
