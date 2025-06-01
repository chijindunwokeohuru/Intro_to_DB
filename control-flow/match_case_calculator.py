#!/usr/bin/env python3
"""
Simple Calculator with Match Case
This script implements a calculator that performs basic arithmetic operations
using Python's match-case statement.
"""

def calculate():
    # Get user input for numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    # Get operation choice
    operation = input("Choose the operation (+, -, *, /): ")

    # Perform calculation using match-case
    match operation:
        case "+":
            result = num1 + num2
            print(f"The result is {result}.")
        case "-":
            result = num1 - num2
            print(f"The result is {result}.")
        case "*":
            result = num1 * num2
            print(f"The result is {result}.")
        case "/":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"The result is {result}.")
        case _:
            print("Invalid operation. Please use +, -, *, or /.")

calculate()

