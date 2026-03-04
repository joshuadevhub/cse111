"""
Program: Tire Volume Calculator
Description: This program accepts tire width (mm), aspect ratio, and wheel diameter (inches),
calculates the tire volume, displays the result, and logs the tire information into
a text file including the current date (without time).

Author: Elemide Joshua Damilare
Date: Tuesday, March 03 2026
"""

# Import the datetime and math modules
from datetime import datetime
import math

# Get todays date and format it
today = datetime.now()
currentYearAndDate = today.strftime("%Y-%m-%d")

# Get the vital user input
tireWidth = float(input("Enter the Width of the Tire in mm (ex 205): "))
tireAspectRatio = float(input("Enter the Aspect Ratio of the Tire (ex 60): "))
tireDiameter = float(input("Enter the Diameter of the Wheel in Inches (ex 15): "))

pi = round(math.pi, 3)

# Calculate the volume using a standard formulae for Tire
firstCalculation = pi * (tireWidth ** 2) * tireAspectRatio
secondCalculation = (tireWidth * tireAspectRatio) + (2540 * tireDiameter)
tireVolume = (firstCalculation * secondCalculation) / 10000000000

# Display the results in a text file called "Volumes.txt"
with open("../text-files/volumes.txt", "a") as file:
  file.write(f"\nCurrent Year, Month and Day: {currentYearAndDate}\n")
  file.write(f"Width of the Tire: {tireWidth}mm\n")
  file.write(f"Aspect Ratio of Tire: {tireAspectRatio}\n")
  file.write(f"Diameter of the Wheel: {tireDiameter} inches\n")
  file.write(f"Volume of the Tire: {tireVolume:.2f} liters\n")

print()
print(f"The approximate volume of the tire is {tireVolume:.2f} liters")