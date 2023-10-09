'''
Program that uses a binary search algorithm to find
a value in an ordered list.
'''
def binary_search(list, element):
  middle = 0
  start = 0
  end = len(list) 
  steps = 0

  while (start <= end):
    steps += 1
    print(f'Step {steps}: {list[start:end]}')
    middle = (start + end) // 2

    if element == list[middle]:
      return f'Result = {list[middle]}'
    elif element < list[middle]:
      end = middle - 1
    elif element > list[middle]:
      start = middle 

  return -1

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
target = 12

print(binary_search(my_list, target))