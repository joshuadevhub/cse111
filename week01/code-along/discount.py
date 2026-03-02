"""
Program Description:
This program calculates the amount a customer needs to pay after purchasing items.

It repeatedly asks the user to enter an item price and quantity.
The loop stops when the user enters 0 for quantity.

If the subtotal is at least $50 and the current day is either Tuesday or Wednesday,
the program applies a 10% discount.

If it is Tuesday or Wednesday but the subtotal is less than $50,
the program shows how much more the customer needs to spend to qualify.

After applying the discount (if applicable), a 6% sales tax is added.

Finally, the program displays the discount amount (if any),
the sales tax amount, and the total amount due.
"""

import datetime

# Get today's weekday (0 = Monday, 1 = Tuesday, 2 = Wednesday, ...)
today = datetime.datetime.today().weekday()

subtotal = 0

# Loop to collect items
while True:
    print()
    itemPrice = float(input("Input the Item Price: $"))
    quantity = int(input("Enter the number of Quantity (Enter 0 to finish): "))

    if quantity == 0:
        break

    subtotal += itemPrice * quantity

print("\nSubtotal: ${:.2f}".format(subtotal))

discount = 0

# Check for Tuesday (1) or Wednesday (2)
if today == 1 or today == 2:
    if subtotal >= 50:
        discount = 0.10 * subtotal
        print("Discount Amount: ${:.2f}".format(discount))
    else:
        remainingBalance = 50 - subtotal
        print("You need ${:.2f} more to receive the discount.".format(remainingBalance))

# Apply discount
subtotal_after_discount = subtotal - discount

# Calculate sales tax (6%)
sales_tax = 0.06 * subtotal_after_discount
print("Sales Tax Amount: ${:.2f}".format(sales_tax))

# Final total
total_due = subtotal_after_discount + sales_tax
print("Total Amount Due: ${:.2f}".format(total_due))