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
        print(f'sum not found for {number}')
        exit(0)


    numbers.append(number)
exit(1)



    