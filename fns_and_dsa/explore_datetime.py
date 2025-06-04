from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in a readable format.
    """
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date

def calculate_future_date(days_to_add):
    """
    Calculate a future date by adding specified number of days to current date.
    
    Args:
        days_to_add (int): Number of days to add to the current date
        
    Returns:
        datetime: The calculated future date
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    return future_date

def main():
    display_current_datetime()
    
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Error: Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    main()