# Prettify JSON

prety print JSON format text from file

# Quickstart


Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py <path to file>
[
    {
        "Cells": {
            "Address": "улица Академика Павлова, дом 10",
            "AdmArea": "Западный административный округ",
            "ClarificationOfWorkingHours": null,
            "District": "район Кунцево",
            "IsNetObject": "да",
            "Name": "Ароматный Мир",
            "OperatingCompany": "Ароматный Мир",
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 777-51-95"
                }
            ],
            "TypeService": "реализация продовольственных товаров",
            "WorkingHours": [
                {
                    ....
                }
            ],
            "geoData": {
                "coordinates": [
                    37.58803599964753,
                    55.89020100016689
                ],
                "type": "Point"
            },
            "global_id": 14937274
        },
        "Id": "a16c8154-09d8-4207-8e13-cb8db654e95c",
        "Number": 3
    }
]

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
