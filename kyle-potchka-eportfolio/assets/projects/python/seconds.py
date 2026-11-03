# firstname_lastname_seconds.py

def calculate_seconds(hours, minutes):
    seconds = (hours * 3600) + (minutes * 60)
    return seconds


def main():
    # Get user input
    hours = int(input("Enter number of hours worked: "))
    minutes = int(input("Enter number of minutes worked: "))
    
    # Call worker function
    total_seconds = calculate_seconds(hours, minutes)
    
    # Display result
    print("Total seconds worked:", total_seconds)


if __name__ == "__main__":
    main()
