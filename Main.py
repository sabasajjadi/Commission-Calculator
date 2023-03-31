
'''
Goal: Calculate the total commission earned by a sales rep for a given period of time
Date: 03/30/2023
Author: Saba Sajjadi
'''

#Importing required python packages
import pandas as pd
import json
from datetime import datetime

class Commission:
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
             # If one or both of the data files are missing, print a message and exit the function
            print("One or both of the data files are missing.")
    
    def total_commission(self, sales_rep_name, start_date, end_date):
        # If the deals or products dataframes have not been loaded yet, load them
        if self.deals is None or self.products is None:
            self.load_dataframes()
        
        # Check if the sales rep name is valid
        if sales_rep_name not in self.deals['sales_rep_name'].unique():
            # Print an error message and return None
            print(f"{sales_rep_name} is not a valid sales rep name.")
            return None
        
        # Check if the start date and end date are valid dates
        try:
            start_date = pd.to_datetime(start_date)
            end_date = pd.to_datetime(end_date)
        except ValueError:
            # Print an error message and return None
            print("The start date or end date is not a valid date.")
            return None
        
        # Filter the deals dataframe based on the sales rep name and date range
        deals = self.deals[(self.deals['sales_rep_name'] == sales_rep_name) & (self.deals['date'] >= start_date) & (self.deals['date'] <= end_date)]

        # Merge the filtered deals dataframe with the products dataframe
        merged = pd.merge(deals, self.products, left_on='product_id', right_on='id', how='left')

        # Calculate the commission for each sale
        merged['commission'] = merged['quantity_products_sold'] * merged['product_amount'] * merged['commission_rate']

        # Group the merged dataframe by sales rep name and sum the commissions
        result = merged.groupby('sales_rep_name')['commission'].sum().get(sales_rep_name, 0)

        # Return the total commission for the given sales rep name
        return result
