most_calories = 0
current_calories = 0

calories = []

with open('input.txt', 'r') as file:
  for line in file:
    if line.strip() == '':
      # if current elf has more calores, store it
      if current_calories > most_calories:
        most_calories = current_calories

      calories.append(current_calories)
      current_calories = 0

    else:
      current_calories += int(line)

print(f'part 1: {most_calories}')

calories.sort(reverse=True)
print(f'part 2: {sum(calories[:3])}')

exit(0)
