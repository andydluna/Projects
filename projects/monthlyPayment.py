def main():
  print('This is a monthly payment loan calculator')
  print('')

  try:
    principal = float(input('Enter the loan amount: '))
    apr = float(input('Enter the anual interest rate: '))
    years = int(input('Enter the amount of years: '))
  except ValueError:
    print('Please, enter a valid number.')
    main()

  monthly_interest_rate = apr / 1200
  amount_of_months = years * 12
  monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))
  monthly_payment = round(monthly_payment, 2)
  
  print(f'The monthly payment for this month is {monthly_payment}')

main()