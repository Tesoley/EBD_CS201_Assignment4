import csv
import json
import matplotlib.pyplot as plt
import pandas as pd

with open('regional_tariffs.json', 'r', encoding = 'utf-8') as file:
    regional_tariffs = json.load(file)

with open('global_sales.csv', 'r', encoding = 'utf-8') as file:
    reader = csv.DictReader(file)
    sales_data = list(reader)

    # successfully