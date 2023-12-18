def add(a, b):
  answer = a + b
  print(f'{a} + {b} = {answer}\n')

def sub(a, b):
  answer = a - b
  print(f'{a} - {b} = {answer}\n')

def mul(a, b):
  answer = a * b
  print(f'{a} * {b} = {answer}\n')

def div(a, b):
  answer = a / b
  print(f'{a} / {b} = {answer}\n')

choice = ''
while (choice != 'e'):
  print('A. Addition')
  print('B. Subtraction')
  print('C. Multiplication')
  print('D. Division')
  print('E. Exit')

  a = ''
  b = ''
  choice = input('Input your choice: ').lower()

  if choice in ['a', 'b', 'c', 'd']:
    try:
      a = int(input('Input first number: '))
      b = int(input('Input second number: '))
    except ValueError:
      print('Please enter a valid number')
      continue
  
  if choice == 'a':
    add(a,b)
  elif choice == 'b':
    sub(a,b)
  elif choice == 'c':
    mul(a,b)
  elif choice == 'd':
    div(a,b)
  elif choice == 'e':
    print('Program ended')
    break
  else:
    print('Please, enter a valid choice')