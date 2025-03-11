#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Calculate tip and tax
    tip = (tip_percent / 100) * meal_cost
    tax = (tax_percent / 100) * meal_cost
    
    # Calculate total cost and round to nearest integer
    total_cost = round(meal_cost + tip + tax)
    
    # Print the result
    print(total_cost)

# Read inputs
meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())

# Call the function
solve(meal_cost, tip_percent, tax_percent)
