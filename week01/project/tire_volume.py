"""
Program: Tire Volume Calculator

Description: This program accepts tire width (mm), aspect ratio, and wheel diameter (inches),
calculates the tire volume, displays the result, and logs the tire information into
a text file including the current date (without time).

Enhancement Features Added:
- Implemented tire price lookup for four or more tire sizes using if/elif/else statements based on user input dimensions.
- Added an option for the user to purchase the tire after viewing the calculated volume.
- If the user chooses to buy, the program requests and validates the user's phone number before recording it in the log file.
- The program records tire details, current date (without time), calculated volume rounded to two decimal places, and user contact information in the log file.

Author: Elemide Joshua Damilare
Date: Wednesday, March 04 2026
"""

from datetime import datetime
import math

with open("../text-files/volumes.txt", "a") as file:
  
  today = datetime.now().strftime("%Y-%m-%d")
  file.write(f"Current Date and Time: {today}\n")

  tireWidth = float(input("Enter the Width of the Tire in mm (ex 205): "))
  while tireWidth > 205:
    print("Tire Width must not exceed 205mm")
    print()
    tireWidth = float(input("Enter the Width of the Tire in mm (ex 250): "))
  else:
    file.write(f"Width of Tire: {tireWidth}mm\n")
    print()

  tireAspectRatio = float(input("Enter the Aspect Ratio of the Tire (ex 60): "))
  while tireAspectRatio > 60:
    print("Aspect Ratio must not exceed 60!")
    print()
    tireAspectRatio = float(input("Enter the Aspect Ratio of the Tire (ex 60): "))
  else:
    file.write(f"Aspect Ratio of Tire: {tireAspectRatio}\n")
    print()

  tireDiameter = float(input("Enter the Diameter of the Wheel in Inches (ex 15): "))
  while tireDiameter > 15:
    print("Wheel Diameter must not exceed 15 Inches!")
    print()
    tireDiameter = float(input("Enter the Diameter of the Wheel in Inches (ex 15): "))
  else:
    file.write(f"Diameter of Wheel: {tireDiameter} Inches\n")


  # Calculate the Volume of Tire from User Input
  pi = math.pi
  firstCalculation = pi * (tireWidth ** 2) * tireAspectRatio
  secondCalculation = (tireWidth * tireAspectRatio) + (2540 * tireDiameter)

  volumeOfTire = (firstCalculation * secondCalculation) / 10000000000
  file.write(f"The approximate Volume of Tire is {volumeOfTire:.2f}\n")
  print()

  print(f"The approximate Volume of Tire is {volumeOfTire:.2f}")
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

  print(f"The Price of the Selected Tire is ${price}")
  print()
  
  # Ask the User if they want to Get the Tire
  userResponse = input("Do you want to Get the Tire with the Selected Dimensions (yes / no)? ").lower()
  if userResponse == "yes":
    print("Great choice! Your selected tire size is available. Please provide your phone number so we can proceed with your order and contact you for confirmation.")
    print()
    userPhoneNumber = input("Enter Phone Number: ")
    while not userPhoneNumber.isdigit() or len(userPhoneNumber) != 11:
      print("The phone number you entered is invalid. Please enter a valid phone number (digits only and 11 character) so we can process your order.")
      print()
      userPhoneNumber = input("Enter Phone Number again: ")
    else:
      print("Thanks for Patronizing Us")
      file.write(f"User Phone Number: {userPhoneNumber}\n")
      file.write("--------------------------------------------------\n")
  else:
    print("No problem. If you would like to check another tire size or make a different selection, please enter the new dimensions. We're here to help!")