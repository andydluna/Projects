def main():
  print('Welcome to the email slicer')
  print()

  email_input = input('Please, enter you email address: ')
  (username, domain) = email_input.split('@')
  (domain, extension) = domain.split('.')

  print(f'username: {username}')
  print(f'domain: {domain}')
  print(f'extension: {extension}')

main()