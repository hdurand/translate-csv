# -*- coding: utf-8 -*-
"""This script tests the module translatecsv.

"""

__author__ = "hdurand"
__license__ = "GPLv2"

from translatecsv import load_reference, translate_csv

# Load the reference for translation.
countries = load_reference('json/countries.json')

# Example 1:
# Translate country names from English to French
# using ISO numeric-3 country codes as identifiers

translate_csv('csv/example-en.csv', 0, 1, countries, 'iso_n3', 'french')

# Example 2:
# Translate country names from English to French
# using ISO alpha-3 country codes as identifiers

#translate_csv('csv/example-en.csv', 2, 1, countries, 'iso_a3', 'french')

# Example 3:
# Translate country names from English to French
# using English names as identifiers

#translate_csv('csv/example-en.csv', 1, 1, countries, 'english', 'french')

# Example 4:
# Translate country names from French to English
# using French names as identifiers

#translate_csv('csv/example-fr.csv', 1, 1, countries, 'french', 'english')

# Example 5:
# Add ISO alpha-3 country codes
# using English country names as identifiers

#translate_csv('csv/example-iso.csv', 1, 0, countries, 'english', 'iso_a3')