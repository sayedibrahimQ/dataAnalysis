import pandas as pd
import matplotlib.pyplot as plt
import seaborn as ss
df = pd.read_csv('Resturant_dataset.csv')
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# •	What is the Distribution of Item Types?
def firstObjective():
    plt.figure(figsize=(4, 8))
    ss.countplot(df, y='item_type', order = df['item_type'].value_counts().index,  legend=False, hue=None)
    plt.title('Item Type Distrbution')
    plt.xlabel('count')
    plt.ylabel('item type')
    plt.show()

# •	What is the Distribution of Item Types?
def secondObjective():
    fast_food = df[df['item_type'] == 'Fastfood']
    ss.displot(fast_food, x = 'item_name')
    plt.title('Fast Food Sold Quantity ')
    plt.xlabel('item name')
    plt.ylabel('count')
    plt.show()

# •	Which Beverage Items Have the Highest Quantity Sold?
def thirdObjectice():
    beverage = df[ df['item_type'] == 'Beverages']
    ss.displot(beverage , x = 'item_name')
    plt.title("Beverage Sold Quantity")
    plt.xlabel("beverage")
    plt.ylabel("count")
    plt.show()
    
# •	What is the Most selling item?
def fourthObjective():
    ss.displot(df, x = 'item_name',)
    plt.title('Fast Food Sold Quantity ')
    plt.xlabel('item name')
    plt.ylabel('count')
    plt.show()
    
# •	When were the highest total costs recorded?
def fifthObjective():
    total_cost_by_time = df.groupby("time_of_sale")["transaction_amount"].sum().reset_index()

    plt.figure(figsize=(8, 5))
    ss.barplot(data=total_cost_by_time, x="time_of_sale", y="transaction_amount")
    plt.title("Total Cost")
    plt.xlabel("Time of Sale")
    plt.ylabel("Total Cost")
    plt.show()
    
# •	Distribution of Total Cost?
def sixthObjective():
    plt.figure(figsize=(8, 5))
    ss.histplot(df['transaction_amount'])
    plt.title('Total Cost Distribution')
    plt.xlabel('Total Cost')
    plt.ylabel('Count')
    plt.show()

# •	What is the Distribution of item type?
def seventhObjective():
    plt.figure(figsize=(8,16))
    ss.histplot(df['item_type'])
    plt.title('Total Cost Distribution')
    plt.xlabel('Item Type')
    plt.ylabel('Dis')
    plt.show()


# •	Which transaction type is used more frequently?
def eighthObjective():
    plt.figure(figsize=(8, 5))
    ss.countplot(df['transaction_type'])
    plt.title('Transaction Type Distribution')
    plt.xlabel('Transaction Type')
    plt.ylabel('Count')
    plt.show()

# •	At what time of day are items sold the most frequently?
def ninthObjective():
    plt.figure(figsize=(8, 5))
    ss.countplot(df['time_of_sale'])
    plt.title('Time of Sale Distribution')
    plt.xlabel('Time of Sale')
    plt.ylabel('Count')
    plt.show()
    