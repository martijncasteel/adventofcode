numbers = []

def find_sum(list, sum):
  for number in list:

    # so if the sum is found in the list
    if (sum - number) in list:
      return True

  return False



with open('input', 'r') as file:
  for line in file:
    number = int(line.strip())

    if len(numbers) > 25:
      if not find_sum(numbers[-25:], number):
        break

    numbers.append(number)

for index, first in enumerate(numbers):
  list = [first]

  # add until you'll get the magic number, or
  # if larger skip to start with next number
  for second in numbers[index+1:]:
    list.append(second)

    if sum(list) == number:
      print(min(list) + max(list))
    elif sum(list) > number:
      break








    