import string
import random

characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')

def generatePassword():
  password_length = int(input('How long would you like your password to be? '))

  random.shuffle(characters)
  
  password = []

  for _ in range(password_length):
    password.append(random.choice(characters))

  random.shuffle(password)

  password = ''.join(password)

  print(password)

option = input('Do you want to generate a password? (Yes/No): ' ).lower()

if option == 'yes' or option == 'y':
  generatePassword()
elif option == 'no' or option == 'n':
  print('Exiting program...')
  quit()
else:
  print('Invalid input! Please input yes or no')
  quit()