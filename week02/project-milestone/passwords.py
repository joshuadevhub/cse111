"""
CSE 111 - Password Strength Checker (Milestone)

This program is the milestone outline for the password strength checker project.
The purpose of this milestone is to create the basic structure of the program
before implementing the full functionality.

The program includes:
- Constants that define character groups used to measure password complexity
  (lowercase letters, uppercase letters, digits, and special characters).
- Function definitions required by the project design:
  word_in_file, word_has_character, word_complexity, password_strength, and main.
- Placeholder bodies for the functions using pass so the program structure
  exists before adding the full logic.
- A main function that provides a loop allowing the user to enter passwords
  for testing until they choose to quit by entering 'q' or 'Q'.

At this stage, the password strength calculation is not yet implemented.
The program simply displays the password entered by the user.
The full functionality will be implemented in the final project completion.

Author: Elemide Joshua Damilare
Date: 12 - 03 - 2026
"""

LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

DIGITS = ["0","1","2","3","4","5","6","7","8","9"]

SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

def word_in_file(word, filename, case_sensitive=False):
  pass

def word_has_character(word, character_list):
  pass

def word_complexity(word):
  pass

def password_strength(password, min_length=10, strong_length=16):
  pass

def main():
  while True:
    user_password = input("Enter password to test (q to quit): ")
    if(user_password == "q" or user_password == "Q"):
      break
    else:
      print(f"Testing Password: {user_password}")
      continue


if __name__ == "__main__":
  main()