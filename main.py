import csv
import json
import matplotlib.pyplot as plt
import pandas as pd

with open('regional_tariffs.json', 'r', encoding = 'utf-8') as file:
    regional_tariffs = json.load(file)

with open('global_sales.csv', 'r', encoding = 'utf-8') as file:
    reader = csv.DictReader(file)
    sales_data = list(reader)

for key, value in regional_tariffs.items():
    if value == 'N/A':
        regional_tariffs[key] = float(0)
    else:
        regional_tariffs[key] = float(value)

cleaned_dict = {key: float(0) if value == 'N/A' else float(value)
                for key, value in regional_tariffs.items()}