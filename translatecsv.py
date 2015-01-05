# -*- coding: utf-8 -*-
"""Translate a CSV file.

This module provides functions to translate a CSV file, using a JSON
reference file.
It translates lists of words.

"""

__author__ = "hdurand"
__license__ = "GPLv2"

import json
import csv

def load_reference(jsonfile):
	"""Return the content of a JSON reference file."""
	with open(jsonfile, 'r') as data:
		filecontent = data.read()
	reference = json.loads(filecontent)
	return reference

def translate_row(row, csv_id, column, reference, ref_id, language):
	"""Translate an element of a row of a CSV file.

	Parameters:
	row (list of str): the row
	csv_id (int): index of the string identifying the element to translate
	column (int): index of the element to translate in the row
	reference (list of dict): reference for translation
	ref_id (str): key of objects identifying the terms in the reference
	language (str): key of the translated terms in the reference

	"""
	# Check value of csv_id and column.
	if csv_id < 0 or csv_id >= len(row) or column < 0 or column >= len(row):
		if len(row) > 0:
			max = str(len(row))
			raise ValueError('csv_id and column must be >= 0 and < ' + max)

	# Translate row.
	translated = 'NOT TRANSLATED: '
	for element in reference:
		if ref_id not in element:
			raise KeyError(ref_id + ' is not a key')
		if language not in element:
			raise KeyError(language + ' is not a key')
		if isinstance(element[ref_id], str):
			if row[csv_id] == element[ref_id]:
				translated = element[language][0]
		elif isinstance(element[ref_id], list):
			if row[csv_id] in element[ref_id]:
				translated = element[language][0]
	if translated == 'NOT TRANSLATED: ':
		translated += row[column]
	row[column] = translated
	new_row = ','.join('"' + item + '"' for item in row)
	print(new_row)

def translate_csv(csvfile, csv_id, column, reference, ref_id, language):
	"""Translate a column of a CSV file.

	Parameters:
	csvfile (file): the CSV file
	csv_id (int): index of the column identifying the terms to translate
	column (int): index of the column to translate in the CSV file
	reference (list of dict): reference for translation
	ref_id (str): key of objects identifying the terms in the reference
	language (str): key of the translated terms in the reference

	"""
	with open(csvfile, 'r') as data:
		reader = csv.reader(data)
		for row in reader:
			translate_row(row, csv_id, column, reference, ref_id, language)
