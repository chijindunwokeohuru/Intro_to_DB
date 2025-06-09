#!/usr/bin/env python3
class DivisionCalculator:
    def __init__(self):
        """Initialize the division calculator."""
        self.last_result = None
        self.error_message = None

    def divide(self, dividend, divisor):
        """
        Perform division with robust error handling.
        
        Args:
            dividend: The number to be divided
            divisor: The number to divide by
            
        Returns:
            float: The result of the division if successful
            None: If division fails
        """
        # reset error message
        self.error_message = None
        
        # check if inputs are numbers
        try:
            dividend = float(dividend)
            divisor = float(divisor)
        except (ValueError, TypeError):
            self.error_message = "Error: Both inputs must be numbers"
            return None

        # check for division by zero
        if divisor == 0:
            self.error_message = "Error: Division by zero is not allowed"
            return None

        # check for infinity
        if abs(dividend) == float('inf') or abs(divisor) == float('inf'):
            self.error_message = "Error: Cannot perform division with infinity"
            return None

        # check for NaN
        if dividend != dividend or divisor != divisor:  # NaN check
            self.error_message = "Error: Cannot perform division with NaN"
            return None

        # perform division
        try:
            result = dividend / divisor
            self.last_result = result
            return result
        except Exception as e:
            self.error_message = f"Error: An unexpected error occurred: {str(e)}"
            return None

    def get_last_result(self):
        """Get the last successful division result."""
        return self.last_result

    def get_error_message(self):
        """Get the last error message if any."""
        return self.error_message


def main():
    calculator = DivisionCalculator()
    
    # Test cases
    test_cases = [
        (10, 2),      # Normal division
        (10, 0),      # Division by zero
        (0, 5),       # Zero dividend
        ("abc", 2),   # Invalid input
        (float('inf'), 2),  # Infinity
        (2, float('inf')),  # Infinity
        (float('nan'), 2),  # NaN
        (2, float('nan')),  # NaN
    ]

    print("Testing Division Calculator:")
    print("-" * 30)
    
    for dividend, divisor in test_cases:
        print(f"\nDividing {dividend} by {divisor}:")
        result = calculator.divide(dividend, divisor)
        
        if result is not None:
            print(f"Result: {result}")
        else:
            print(f"Error: {calculator.get_error_message()}")


if __name__ == "__main__":
    main()