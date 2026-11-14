# kyle_potchka_stadium.py

def calculate_income(class_a, class_b, class_c):
    A_PRICE = 30
    B_PRICE = 25
    C_PRICE = 20

    total = (class_a * A_PRICE) + (class_b * B_PRICE) + (class_c * C_PRICE)
    return total


def main():
    # Get user input
    class_a = int(input("Enter number of Class A tickets sold: "))
    class_b = int(input("Enter number of Class B tickets sold: "))
    class_c = int(input("Enter number of Class C tickets sold: "))

    # Call worker function
    total_income = calculate_income(class_a, class_b, class_c)

    # Display result
    print("Total income from ticket sales: $", format(total_income, ",.2f"))


if __name__ == "__main__":
    main()
