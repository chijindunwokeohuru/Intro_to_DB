#!/usr/bin/env python3

def safe_divide(numerator, denominator):
    """
    Perform division with robust error handling.
    
    Args:
        numerator: The number to be divided
        denominator: The number to divide by
        
    Returns:
        str: The result of the division or an error message
    """
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except (ValueError, TypeError):
        return "Error: Please enter numeric values only."

    if denominator == 0:
        return "Error: Cannot divide by zero."

    try:
        result = numerator / denominator
        return f"The result of the division is {result}"
    except Exception as e:
        return f"Error: An unexpected error occurred: {str(e)}"


def main():
    # Test cases
    test_cases = [
        (10, 5),      
        (10, 0),      
        (0, 5),       
        ("ten", 5),
    ]

    print("Testing Division Calculator:")
    print("-" * 30)
    
    for numerator, denominator in test_cases:
        print(f"\nDividing {numerator} by {denominator}:")
        result = safe_divide(numerator, denominator)
        print(result)


if __name__ == "__main__":
    main()