# firstname_lastname_miles.py

def miles_to_kilometers(miles):
    KILOMETER_CONVERSION = 1.60934
    kilometers = miles * KILOMETER_CONVERSION
    return kilometers


def main():
    # Get user input
    miles = float(input("Enter number of miles driven: "))
    
    # Call worker function
    kilometers = miles_to_kilometers(miles)
    
    # Display result
    print("Kilometers driven:", format(kilometers, ".2f"))


if __name__ == "__main__":
    main()
