import urllib.request as urllib

def main(url):
  print('Checking connectivity...')
  response = urllib.urlopen(url)
  print('Connected to {} succesfully'.format(url))
  print('Status code: {}'.format(response.getcode()))

print('This is a site connectivity checker program')
input_url = input('Enter the url fo the site you want to check: ')
main(input_url)
  