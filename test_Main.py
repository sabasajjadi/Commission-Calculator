'''
Goal: Test Main function (total_commission)
Date: 03/30/2023
Author: Saba Sajjadi
'''

# Import the Commission class from the Main module
# This allows us to create a Commission object in this file and use its methods
from Main import Commission

# Create an instance of the Commission class to access its methods
commission = Commission()

def test_total_commission():
    # Test case 1 - Valid input
    result = commission.total_commission(sales_rep_name="Ian", start_date="2023-01-01", end_date="2023-04-30")
    expected_result = 55350.00
    assert result == expected_result, f"Test case 1 failed: expected {expected_result:.2f} but got {result:.2f}"

    # Test case 2 - Non-existing sales rep
    result = commission.total_commission(sales_rep_name="Non-existing Sales Rep", start_date="2023-01-01", end_date="2023-04-30")
    expected_result = None 
    assert result == expected_result, f"Test case 2 failed: expected {expected_result:.2f} but got {result:.2f}"

        
    # Test case 3 - Non-existing date range
    result = commission.total_commission(sales_rep_name="Ian", start_date="2024-01-01", end_date="2024-04-30")
    expected_result = 0
    assert result == expected_result, f"Test case 3 failed: expected {expected_result:.2f} but got {result:.2f}"


    # Test case 4 - Invalid start date
    result = commission.total_commission(sales_rep_name="Ian", start_date="Invalid date", end_date="2023-04-30")
    expected_result = None
    assert result == expected_result, f"Test case 5 failed: expected {expected_result} but got {result}"

    # Test case 5 - Invalid end date
    result = commission.total_commission(sales_rep_name="Ian", start_date="2023-01-01", end_date="Invalid date")
    expected_result = None
    assert result == expected_result, f"Test case 6 failed: expected {expected_result} but got {result}"

    print("All test cases passed")


#call test_total_commission function above
test_total_commission()