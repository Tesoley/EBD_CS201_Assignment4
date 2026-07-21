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

for key, value in regional_tariffs.items():
    if value == 'N/A':
        regional_tariffs[key] = float(0)
    else:
        regional_tariffs[key] = float(value)

cleaned_dict = {key: float(0) if value == 'N/A' else float(value)
                for key, value in regional_tariffs.items()}


for row in sales_data:
    if row['quantity'] == 'N/A':
        row['quantity'] = int(0)
    else:
        row['quantity'] = int(row['quantity'])

    if row['revenue'] == 'N/A':
        row['revenue'] = float(0)
    else:
        row['revenue'] = float(row['revenue'])

for row in sales_data:
    revenue = row['revenue']
    region = row['region']
    tariff = cleaned_dict[region]
    net_profit = revenue - (revenue * (tariff / 100))
    row['net_profit'] = net_profit

