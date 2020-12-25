import re

with open('input', 'r') as file:
  passwords = file.readlines()

correct = 0

for line in passwords:
  match = re.match(r"^(\d+)-(\d+) (.{1})\: (\w*)$", line)

  if match:
    min, max, letter, password = match.group(1,2,3,4)
    count = password.count(letter)

    if count <= int(max) and count >= int(min):
      correct += 1

print(correct)
exit(0)