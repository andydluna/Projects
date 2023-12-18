from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
  word = input("Enter a word: ") 
  if word == '':
    break
    
  meaning = dictionary.meaning(word)
  if meaning is not None:
    print(meaning)
  else:
    print("No meaning found")