# CSE 111 - W05 Project: Grocery Store Receipt
# This program reads product data from products.csv and customer orders from request.csv.
# It uses a dictionary to look up product information and prints a receipt that includes
# item names, quantities, prices, subtotal, sales tax, total amount, and the current date and time.

# Exceed Requirement:
# This program calculates and displays a "return by" date that is 30 days after the purchase date.

import csv
from datetime import datetime
from datetime import timedelta


def main():
  try:
    print("Inkom Emporium.")
    print()

    products_dict = read_dictionary("products.csv", 0)
    total_items = 0
    subtotal = 0

    with open("request.csv", "r") as file:
      reader = csv.reader(file)
      next(reader)

      for row in reader:
        product_id = row[0]
        quantity = int(row[1])

        # Get product from dictionary
        product = products_dict[product_id]

        # Extract name and price
        name = product[1]
        price = float(product[2])
      
        print(f"{name}: {quantity} @ {price:.2f}")

        total_items += quantity
        subtotal += quantity * price

    tax = subtotal * 0.06
    total = subtotal + tax

    print()
    print(f"Number of Items: {total_items}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax: {tax:.2f}")
    print(f"Total: {total:.2f}")
    print("Thank you for shopping at the Inkom Emporium.")

    current_date = datetime.now()
    print(current_date.strftime("%a %b %d %H:%M:%S %Y"))

    return_date = current_date + timedelta(days=30)
    print(f"Return by: {return_date.strftime('%a %b %d %H:%M:%S %Y')}")

  except FileNotFoundError as e:
        print("Error: missing file")
        print(e)

  except PermissionError:
        print("Error: permission denied")

  except KeyError as e:
        print("Error: unknown product ID in the request.csv file")
        print(e)


def read_dictionary(filename, key_column_index):
  product_dict = {}

  with open(filename, "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
      key = row[key_column_index]
      product_dict[key] = row

  return product_dict


if __name__ == "__main__":
  main()