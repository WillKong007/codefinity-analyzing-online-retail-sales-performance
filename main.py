import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load subset for performance
df = pd.read_csv("online_retail.csv")
df.info()
# Your code starts here
#1
# calculate revenue
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


#task 2
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

#task 3