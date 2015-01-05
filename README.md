translate-csv
-------------

`translatecsv.py` is a Python module. It provides functions to translate a CSV file, using a JSON reference file.

`translatecsv.py` is built to translate lists of words like country names.

### Getting started

#### Get translate-csv

+ Download `translatecsv.py` on GitHub.
  
#### JSON reference file

+ Download the reference file `json/countries.json` on GitHub to translate country names or create your own reference file.  
The format of the JSON file must be:

```
[
	{
		"id": [
			"id_value"
		],
		...,
		"language_1": [
			"language_1_value_1",
			"language_1_value_2",
			...
		],
		"language_2": [
			"language_2_value_1",
			"language_2_value_2",
			...
		],
		...
	},
	...
]
```

Only those elements are not optional in the JSON file:

```
[
	{
		"key_1": [
			"key_1_value_1"
		],
		"key_2": [
			"key_2_value_1"
		]
	}
]
```

For example, `json/countries.json` looks like:

```
[
	...,
    {
        "iso_a3": [
            "MEX"
        ],
        "iso_n3": [
            "484"
        ],
        "french": [
            "Mexique"
        ],
        "english": [
            "Mexico"
        ]
    },
	...,
    {
        "iso_a3": [
            "GBR"
        ],
        "iso_n3": [
            "826"
        ],
        "french": [
            "Royaume-Uni",
            "Royaume-Uni de Grande-Bretagne et d'Irlande du Nord"
        ],
        "english": [
            "United Kingdom",
            "United Kingdom of Great Britain and Northern Ireland"
        ]
    },
    ...
]
```

#### Translate

+ Import the functions of the module:  

`from translatecsv import load_reference, translate_csv`

+ Load the reference file:  

`countries = load_reference('json/countries.json')`

+ Translate:  

For example, the CSV file `csv/example.csv` looks like:

```
"AUT","Austria"
"BEL","Belgium"
"CHE","Switzerland"
"FRA","France"
"HRV","Croatia"
"HUN","Hungary"
"ITA","Italy"
"LTU","Lithuania"
"ROU","Romania"
"DNK","Denmark"
```

Let's translate the country names to French using ISO alpha-3 country codes and `json/countries.json`:

```python
from translatecsv import load_reference, translate_csv

countries = load_reference('json/countries.json')

translate_csv('csv/example.csv', 0, 1, countries, 'iso_a3', 'french')
```

It translates the column `1` of the CSV file `csv/example.csv`.  
The column `0` identifies elements of the column `1`.  
The key `iso_a3` identifies the same elements in the JSON file.  
It replaces each element of the column `1` with the first value of the key `french` in the JSON file.

The result is:

```
"AUT","Autriche"
"BEL","Belgique"
"CHE","Suisse"
"FRA","France"
"HRV","Croatie"
"HUN","Hongrie"
"ITA","Italie"
"LTU","Lituanie"
"ROU","Roumanie"
"DNK","Danemark"
```

For more examples, see `examples.py`.

+ If an element is not translated, you'll see:

`"NOT TRANSLATED: element"` instead of `"element"` in the CSV file.

If necessary, you can edit the JSON reference file to take this `"element"` into account.