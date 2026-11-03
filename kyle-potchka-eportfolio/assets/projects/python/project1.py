# Corner Store Program
# Purpose: This is a sales tracking program

cash_drawer = 100.00
productID = 0
quantity = 0
price = 0.0
subtotal = 0.0
sales_tax = 0.0
total_sale = 0.0
tax_rate = 0.075
another_sale = "y"

print()
print("----------[ C o r n e r   S t o r e ]----------")
print()

# Loop for each sale
while another_sale == "y":

    print()
    productID = int(input("Enter the first Product ID (-1 to end): "))

    # Loop for each product
    while productID != -1:

        quantity = int(input("Enter quantity: "))

        # Look up price and taxability
        if productID == 101:
            price = 3.95
            taxable = False
        elif productID == 102:
            price = 1.85
            taxable = True
        elif productID == 103:
            price = 2.49
            taxable = True
        elif productID == 104:
            price = 5.19
            taxable = True
        elif productID == 105:
            price = 4.99
            taxable = False
        else:
            print("Invalid Product ID")
            productID = int(input("Enter next Product ID (-1 to end): "))
            continue

        subtotal += price * quantity

        if taxable:
            sales_tax += price * quantity * tax_rate

        productID = int(input("Enter next Product ID (-1 to end): "))

    total_sale = subtotal + sales_tax

    print()
    print(f"Subtotal: ${subtotal:7.2f}")
    print(f"Sales Tax: ${sales_tax:7.2f}")
    print(f"Total Sale: ${total_sale:7.2f}")

    cash_drawer += total_sale

    subtotal = 0.0
    sales_tax = 0.0
    total_sale = 0.0

    another_sale = input("Would you like another sale ('y' or 'n')? ")

print()
print(f"Total in cash drawer: ${cash_drawer:7.2f}")
