import re
pattern = re.compile(r'^(\d+) ([+|*]) (\d+)(.+)?')

# remove all parentheses
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

  return str(precedence(line))

# ensure addition is done before multiplication
def precedence(line):
  parts = []

  for subset in line.split('*'):
    if '+' in subset:
      parts.append(calculate(subset.strip()))
    else:
      parts.append(subset.strip())

  if len(parts) < 2:
    return parts[0]

  return calculate(' * '.join(parts))


# no parentheses in the this line
def calculate(line):
  match = pattern.match(line)
  if match:
    a, oper, b, rest = match.groups()

    if oper == '+':
      val = int(a) + int(b)
    elif oper == '*':
      val = int(a) * int(b)

    if rest is None:
      return str(val)

    return calculate(str(val) + rest)       
 

sum = 0
with open('input') as file:
  for line in file:
    result = compute(line.strip())
    sum += int(result)
    print(result)

  print('')
  print(sum)