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

Enhancement:
Added a password strength description so the program displays a
readable rating (Very Weak to Very Strong) in addition to the
numeric strength score.

Author: Elemide Joshua Damilare
Date: 14 - 03 - 2026
"""

LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

DIGITS = ["0","1","2","3","4","5","6","7","8","9"]

SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]


def word_has_character(word, character_list):
  for char in word:
    if char in character_list:
      return True
  return False

def word_complexity(word):
  complexity = 0

  if word_has_character(word, LOWER):
    complexity = complexity + 1
  
  if word_has_character(word, UPPER):
    complexity = complexity + 1

  if word_has_character(word, DIGITS):
    complexity = complexity + 1

  if word_has_character(word, SPECIAL):
    complexity = complexity + 1

  return complexity


def word_in_file(word, filename, case_sensitive=False):
  with open(filename, "r", encoding="utf-8") as file:
    for line in file:
      file_word = line.strip()

      if case_sensitive:
        if word == file_word:
          return True
      else:
        if word.lower() == file_word.lower():
          return True
  return False
    

def password_strength(password, min_length=10, strong_length=16):
  if word_in_file(password, "wordlist.txt"):
    print("Password is a dictionary word and is not secure")
    return 0
  
  if word_in_file(password, "toppasswords.txt", True):
    print("Password is a commonly used password and is not secure.")
    return 0
  
  if len(password) < min_length:
    print("Password is too short and is not secure")
    return 1
  
  if len(password) > strong_length:
    print("Password is long, length trumps complexity this is a good password")
    return 5
  
  complexity = word_complexity(password)
  return 1 + complexity


def strength_description(score):
  if score == 0:
    return "Very Weak"
  elif score == 1:
    return "Weak"
  elif score == 2:
    return "Fair"
  elif score == 3:
    return "Good"
  elif score == 4:
    return "Strong"
  else:
    return "Very Strong"



def main():
  while True:
    user_password = input("Enter password to test (q to quit): ")
    if(user_password == "q" or user_password == "Q"):
      break
    else:
      strength = password_strength(user_password)
      score = strength_description(strength)
      print(f"{strength} ({score})")


if __name__ == "__main__":
  main()