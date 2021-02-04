adapters = []

with open('input', 'r') as file:
  for line in file:
    adapters.append(int(line.strip()))

# initial socket
adapters.append(0)
adapters.sort()

# target voltage for hacking device
adapters.append(adapters[-1] + 3)

differences = []
for index in range(1, len(adapters)):
  differences.append(adapters[index] - adapters[index - 1])

print(differences.count(1) * differences.count(3))
