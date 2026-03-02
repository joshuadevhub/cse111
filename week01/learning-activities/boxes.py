"""
Problem Statement:
In today's global economy, products are manufactured in large quantities,
packaged into boxes, and shipped to distribution centers and retail stores.
A common question during packaging is: “How many boxes are required?”

Assignment:
Write a Python program named boxes.py that asks the user for:
1. The total number of manufactured items.
2. The number of items that can be packed in each box.

The program must calculate and display the total number of boxes required.
The result must be a whole number. If the final box does not contain the
maximum number of items, it should still be counted as a box.

"""
import math

numberOfItems = int(input("Enter the Number of Items: "))
itemsPerBox = int(input("Enter the Number of Items Per Box: "))

totalBoxNeeded = math.ceil(numberOfItems / itemsPerBox)

print(f"For {numberOfItems} items, packing {itemsPerBox} items in each box, you will need {totalBoxNeeded} boxes.")