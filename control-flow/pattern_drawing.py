#!/usr/bin/env python3
"""
Pattern Drawing with Nested Loops
This script draws a square pattern of asterisks (*) based on user input.
"""

def draw_square_pattern():
    try:
        # Prompt user for pattern size
        size = int(input("Enter the size of the pattern: "))
        
        # Validate input
        if size <= 0:
            print("Please enter a positive integer.")
            return
        
        # Initialize row counter for while loop
        row = 0
        
        # Use while loop to iterate through rows
        while row < size:
            # Use for loop to print asterisks in each row
            for col in range(size):
                print("*", end="")
            
            # Move to the next line after completing a row
            print()
            
            # Increment row counter
            row += 1
            
    except ValueError:
        print("Please enter a valid integer.")

draw_square_pattern()