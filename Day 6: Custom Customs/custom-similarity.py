possible_answers = answers = set('abcdefghijklmnopqrstuvwxyz')
total = 0

with open('input', 'r') as file:
  for line in file:

    line = line.strip()
    
    # upcoming new group
    if line == "":
      total += len(answers)
      answers = possible_answers
      continue

    answers = answers.intersection(line)


total += len(answers)
print(total)