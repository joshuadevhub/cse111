"""
Program: Tire Volume Calculator
Description: This program calculates the volume of a tire based on user input for
width (mm), aspect ratio, and wheel diameter (inches). It displays the volume
to the terminal, logs all tire details along with the current date, price, and
user phone number (if provided) into a text file in a single line per run.
Enhancement Features:
- Price lookup for common tire sizes
- Optional purchase flow with phone number validation
- Logs all relevant information in a single line in volumes.txt
Author: Elemide Joshua Damilare
Date: 2026-03-11
"""

from datetime import datetime
import math

# Prompt user for three numbers and convert to float
tireWidth = float(input("Enter the width of the tire in mm (e.g., 205): "))
tireAspectRatio = float(input("Enter the aspect ratio of the tire (e.g., 60): "))
tireDiameter = float(input("Enter the diameter of the wheel in inches (e.g., 15): "))

# Calculate tire volume
volumeOfTire = math.pi * (tireWidth ** 2) * tireAspectRatio * ((tireWidth * tireAspectRatio) + (2540 * tireDiameter)) / 10000000000

# Print volume to terminal with 2 decimal places
print(f"The approximate volume of the tire is {volumeOfTire:.2f} liters")

# Price lookup for creativity feature
if tireWidth == 185 and tireAspectRatio == 60 and tireDiameter == 15:
    price = 85
elif tireWidth == 195 and tireAspectRatio == 60 and tireDiameter == 15:
    price = 95
elif tireWidth == 205 and tireAspectRatio == 60 and tireDiameter == 15:
    price = 110
elif tireWidth == 185 and tireAspectRatio == 55 and tireDiameter == 15:
    price = 80
elif tireWidth == 195 and tireAspectRatio == 55 and tireDiameter == 15:
    price = 100
elif tireWidth == 205 and tireAspectRatio == 55 and tireDiameter == 15:
    price = 115
elif tireWidth == 175 and tireAspectRatio == 60 and tireDiameter == 15:
    price = 75
elif tireWidth == 185 and tireAspectRatio == 60 and tireDiameter == 14:
    price = 70
else:
    price = 90

print(f"The price of the selected tire is ${price}")

# Optional purchase flow
userResponse = input("Do you want to get the tire with the selected dimensions (yes/no)? ").lower()
userPhoneNumber = ""  # default empty
if userResponse == "yes":
    phoneNumber = input("Enter your phone number (11 digits): ")
    while not phoneNumber.isdigit() or len(phoneNumber) != 11:
        phoneNumber = input("Invalid. Enter 11-digit phone number: ")
    userPhoneNumber = phoneNumber
    print("Thanks for your purchase!")

# Get current date
today = datetime.now().strftime("%Y-%m-%d")

# Log all relevant info in a single line in volumes.txt
with open("../text-files/volumes.txt", "a") as file:
    file.write(f"{today}, {tireWidth}, {tireAspectRatio}, {tireDiameter}, {volumeOfTire:.2f}, {price}, {userPhoneNumber}\n")