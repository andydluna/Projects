'''
Program with a dictionary of questions, each with
values equal to another dictionary with the question
and the answer. The program then runs through each
question and asks for the user input. If the input
matches the answer, a point is given to the user.
Prints the number of questions right at the end.
'''

quiz = {
  'Question1': {
    'question': 'What is the capital of France?',
    'answer': 'Paris'
  },
  'Question2': {
    'question': 'What is the capital of Germany?',
    'answer': 'Berlin'
  },
  'Question3': {
    'question': 'What is the capital of Italy?',
    'answer': 'Rome'
  },
  'Question4': {
    'question': 'What is the capital of Spain?',
    'answer': 'Madrid'
  },
  'Question5': {
    'question': 'What is the capital of Portugal?',
    'answer': 'Lisbon'
  },
  'Question6': {
    'question': 'What is the capital of Switzerland?',
    'answer': 'Bern'
  },
  'Question7': {
    'question': 'What is the capital of Austria?',
    'answer': 'Vienna'
  }
}

score = 0
for key, value in quiz.items():
  print(value['question'])
  answer = input('Answer? ')

  if answer.lower() == value['answer'].lower():
    print('Correct!')
    score += 1
    print(f'Your score is: {score}')
  else:
    print('Wrong!')
    print(f'The answer is {value["answer"]}')
    print(f'Your score is: {score}')
  print()

percentage = round(score / 7 * 100)
print(f'You got {score} / 7 questions right!')
print(f'Your percentage is {percentage} %')