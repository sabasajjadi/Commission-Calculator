'''
Goal: Test total_commission_Sales function 
Date: 03/30/2023
Author: Saba Sajjadi
'''

# Import the Commission_Calculator class from the Error Handling
# This allows us to create a Commission calculator object in this file and use its methods
from Error_Handling import Commission_Calculator
# Create an instance of the class
commission_calculator = Commission_Calculator()

#example 1: All inputs are valid
commission_calculator.total_commission_Sales(sales_rep_name="Ian", start_date="2023-01-01", end_date="2023-04-30")


#example 2: sales_rep_name is not valid
commission_calculator.total_commission_Sales(sales_rep_name="Saba", start_date="2023-01-01", end_date="2023-04-30")

#example 3: start_date is greater than end_date
commission_calculator.total_commission_Sales(sales_rep_name="Ian", start_date="2025-01-01", end_date="2023-04-30")