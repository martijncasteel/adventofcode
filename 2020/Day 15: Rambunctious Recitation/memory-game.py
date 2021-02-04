def indexes(list, value):

  clone = list.copy()
  clone.reverse()

  length = len(list)
  i = clone.index(value)

  if value not in clone[i+1:]:
    return length -i, -1

  j = clone[i+1:].index(value) 
  return length - i, length - j - 1


with open('input', 'r') as file:
  for line in file:

    numbers = [int(i) for i in line.strip().split(',')]

    while len(numbers) < 2020:
      consider = numbers[-1]

      # this is a new number
      if consider not in numbers[3:]:
        numbers.append(0)
        continue

      # the number has been spoken before
      else:
        i, j = indexes(numbers, consider)

        if j == -1:
          numbers.append(0)
        else:
          numbers.append(i - j)

    print(numbers[-1])
  exit(0)