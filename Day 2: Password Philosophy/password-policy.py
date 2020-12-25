import re

with open('input', 'r') as file:
  passwords = file.readlines() 

correct = 0

for line in passwords:
  match = re.match(r"^(\d+)-(\d+) (.{1})\: (\w*)$", line)

  if match:
    index1, index2, letter, password = match.group(1,2,3,4)

    index1 = int(index1) -1
    index2 = int(index2) -1

    if password[index1] == letter:
      if password[index2] == letter:
        continue
      correct += 1
      continue

    elif password[index2] == letter:
      correct += 1

print(correct)
exit(0)