def main():
  # Get an odometer value in U.S. miles from the user.
  startOdometer = float(input("Enter the first odometer reading (miles): "))

  # Get another odometer value in U.S. miles from the user.
  endOdometer = float(input("Enter the second odometer reading (miles): "))

  # Get a fuel amount in U.S. gallons from the user.
  fuelAmountInGallon = float(input("Enter the amount of fuel used (gallons): "))

  # Call the miles_per_gallon function and store
  # the result in a variable named mpg.
  mpg = miles_per_gallon(startOdometer, endOdometer, fuelAmountInGallon)

  # Call the lp100k_from_mpg function to convert the
  # miles per gallon to liters per 100 kilometers and
  # store the result in a variable named lp100k.
  lp100k = lp100k_from_mpg(mpg)
  
  # Display the results for the user to see.
  print(f"The fuel efficiency of your vehicle in Miles Per Gallon is {mpg:.2f} MPG")
  print()
  print(f"The fuel efficiency of your vehicle in Litre Per 100k is {lp100k:.2f} LP100K")
  # pass

def miles_per_gallon(start_miles, end_miles, amount_gallons):
  """Compute and return the average number of miles
  that a vehicle traveled per gallon of fuel.
  Parameters
  start_miles: An odometer value in miles.
  end_miles: Another odometer value in miles.
  amount_gallons: A fuel amount in U.S. gallons.
  Return: Fuel efficiency in miles per gallon.
  """
  milesPerGallon = (end_miles - start_miles) / amount_gallons
  return milesPerGallon

def lp100k_from_mpg(mpg):
  """Convert miles per gallon to liters per 100
  kilometers and return the converted value.
  Parameter mpg: A value in miles per gallon
  Return: The converted value in liters per 100km.
  """
  litrePer1000K = 235.215 / mpg
  return litrePer1000K

# Call the main function so that
# this program will start executing.
main()