def replace_word():
  str = "hi guys, I'm Andy. hi hi hi hi!"
  words_to_replace = input('Enter the word to replace: ')
  word_replacement = input('Enter the word replacement: ')

  print(str.replace(words_to_replace, word_replacement))

replace_word()