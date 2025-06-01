#!/usr/bin/env python3
"""
Multiplication Table Generator
This script generates a multiplication table from 1 to 10 for a user-provided number.
"""

def generate_multiplication_table():
    # Prompt user for a number
    try:
        number = int(input("Enter a number to see its multiplication table: "))
        
        # Generate and print the multiplication table
        for i in range(1, 11):
            product = number * i
            print(f"{number} * {i} = {product}")
    
    except ValueError:
        print("Please enter a valid number.")

generate_multiplication_table()