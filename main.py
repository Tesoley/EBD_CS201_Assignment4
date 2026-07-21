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

with open('cleaned_sales_updated.csv', 'w', encoding = 'utf-8') as file:
    writer = csv.DictWriter(file, fieldnames = sales_data[0].keys())
    writer.writeheader()
    writer.writerows(sales_data)
    # print(sales_data)


profit_by_category = {}

with open('cleaned_sales_updated.csv', 'r', encoding = 'utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        category = row['product_category']
        net_profit = float(row['net_profit'])
        if category in profit_by_category:
            profit_by_category[category] += net_profit
        else:
            profit_by_category[category] = net_profit
    # print(profit_by_category)