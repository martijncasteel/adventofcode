adapters = []

with open('input', 'r') as file:
  for line in file:
    adapters.append(int(line.strip()))

# initial socket
adapters.append(0)
adapters.sort()

# target voltage for hacking device
adapters.append(adapters[-1] + 3)

# this one took more time than I would admit
# list per voltage on how many ways to get 
# there starting from 1 joltage
possibilities = [1] * (adapters[-1] + 1)
for adapter in adapters[1:]:
  sum = 0

  # find possibilities for every joltage
  for joltage in range(adapter -3, adapter):
    if joltage in adapters:
      sum += possibilities[joltage]
  
  possibilities[adapter] = sum

print(possibilities[-1])