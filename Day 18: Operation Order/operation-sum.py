import re
pattern = re.compile(r'^(\d+) ([+|*]) (\d+)(.+)?')

def compute(line):
  if '(' in line:
    start = end = -1
    for index, char in enumerate(line):

      if char == '(':
        start = index
      elif char == ')':
        end = index
        break

    # replace inner strings and compute again
    return compute(line[:start] + str(compute(line[start+1:end])) + line[end+1:])

  # no parentheses in the this line
  match = pattern.match(line)
  if match:
    a, oper, b, rest = match.groups()

    if oper == '+':
      val = int(a) + int(b)
    elif oper == '*':
      val = int(a) * int(b)

    if rest is None:
      return str(val)

    return compute(str(val) + rest)
 

sum = 0
with open('input') as file:
  for line in file:
    result = compute(line.strip())
    print(result)
    sum += int(result)

  print('')
  print(sum)