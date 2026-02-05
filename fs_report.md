This file is a merged representation of the entire codebase, combined into a single document

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block or first three lines for files with .csv extensions

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- This file includes only .ipynb and .csv file contents in full or partial form
- All other file types are represented only through the directory structure
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files

# Directory Structure

````
./
fs_report.md
main.py
online_retail.csv
````

# Files

## File: online_retail.csv
````
,InvoiceNo,StockCode,Description,Quantity,InvoiceDate,UnitPrice,CustomerID,Country
0,536370,22728,ALARM CLOCK BAKELIKE PINK,24,01.12.2010 08:45,3.75,12583.0,France
1,536370,22727,ALARM CLOCK BAKELIKE RED ,24,01.12.2010 08:45,3.75,12583.0,France
````

## File: main.py
````
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load subset for performance
df = pd.read_csv("online_retail.csv")
df.info()
# Your code starts here
#calculate revenue
df['Revenue']=df['Quantity']*df['UnitPrice']

#Aggregate total revenue by country and sorted
country_revenue=df.groupby('Country')['Revenue'].sum().sort_values(ascending=False)

#Print exact values for later parsing
print('Total Revenue by Crountry(GBP:')
print(country_revenue.to_dict())

#plot thr bar chart
plt.figure(figsize=(12,6))
sns.barplot(x=country_revenue.index, y=country_revenue.values)
plt.xticks(rotation=90)
plt.ylabel('Total Revenue')
plt.xlabel('Country')
plt.title('Total revenue by Country')
plt.tight_layout()
plt.show()

df.head(10)

#calculate the frequency of purchased products
frequency_purchased_product=df.groupby('Description')['Quantity'].sum().sort_values(ascending=False)
top_10=frequency_purchased_product.head(10)
print('the top 10 most frequently purchased product:')
print(top_10.to_dict())

#plot the bar chart
plt.figure(figsize=(12,6))
sns.barplot(x=top_10.index, y=top_10.values)
plt.xticks(rotation=90)
plt.ylabel('purchase counts')
plt.xlabel('product')
plt.title('theh top 10 most frenquently purchased products')
plt.tight_layout()
plt.show()

````
