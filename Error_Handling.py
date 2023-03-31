'''
Goal: Calculate the total commission earned by a sales rep for a given period of time(Advanced version with error handling)
Date: 03/30/2023
Author: Saba Sajjadi
'''



import pandas as pd
import json 
from datetime import datetime

import pandas as pd

class Commission_Calculator:
    def __init__(self):
        # Initialize the deals and products dataframes as None
        self.deals = None
        self.products = None
    
    def load_dataframes(self):
        try:
            # Load the datasets as dataframes
            with open('Deals.json') as f:
                self.deals = pd.read_json(f)
            with open('Products.json') as f:
                self.products = pd.read_json(f)
        except FileNotFoundError:
            print("One or both of the data files are missing.")
        except ValueError:
            print("One or both of the data files have an invalid format.")
    
    def total_commission_Sales(self, sales_rep_name, start_date, end_date):
        # Load dataframes if they have not been loaded yet
        if self.deals is None or self.products is None:
            self.load_dataframes()
        
        # Check if the sales rep name is valid
        if sales_rep_name not in self.deals['sales_rep_name'].unique():
            print(f"{sales_rep_name} is not a valid sales rep name.")
            return None
        
        # Check if the start date and end date are valid dates
        try:
            start_date = pd.to_datetime(start_date)
            end_date = pd.to_datetime(end_date)
        except ValueError:
            print("The start date or end date is not a valid date.")
            return None
        
        # Check if the start date is before the end date
        if start_date > end_date:
            print("The start date must be before the end date.")
            return None
        
        # Filter the deals dataframe based on the sales rep name and date range
        deals = self.deals[(self.deals['sales_rep_name'] == sales_rep_name) & (self.deals['date'] >= start_date) & (self.deals['date'] <= end_date)]

        # Merge the filtered deals dataframe with the products dataframe
        merged = pd.merge(deals, self.products, left_on='product_id', right_on='id', how='left')

        # Calculate the commission for each sale
        merged['commission'] = merged['quantity_products_sold'] * merged['product_amount'] * merged['commission_rate']

        # Group the merged dataframe by sales rep name and sum the commissions
        result = merged.groupby('sales_rep_name')['commission'].sum().get(sales_rep_name, 0)

        return result

