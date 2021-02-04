answers = set()
total = 0

with open('input', 'r') as file:
  for line in file:

    line = line.strip()
    
    # upcoming new group
    if line == "":
      total += len(answers)

      answers = set()
      continue

    for question in list(line):
      answers.add(question)


total += len(answers)
print(total)