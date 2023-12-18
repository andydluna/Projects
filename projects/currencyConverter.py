def main():
  print('This program converts U.S. Dollars to Pounds Sterling')
  print()

  dollars = eval(input('Enter the amount in dollars: '))

  pounds = convert_to_pounds(dollars)
  print('That is {:.2f} pounds'.format(pounds))

convert_to_pounds = lambda dollars: dollars * 0.82

main()