lines = []
crates = {}

# readlines for easy seperating in two
with open('input.txt', 'r') as file:
  for line in file:
    lines.append(line.replace('\n', ''))

# find empty line
seperator = lines.index('')

# creates stacks for crate storage
for index in lines[(seperator-1)].replace(' ', ''):
  crates[index] = []

# build stacks with crates, revert the list so top is at end of array
for line in lines[:(seperator-1)][::-1]:
  for index, column in enumerate([line[i:i+4] for i in range(0, len(line), 4)]):
    if column[1] != ' ':
      crates[str(index+1)].append(column[1])

# create a clone for part two
original = {}
for stack in crates:
  original[stack] = crates[stack].copy()



# execute produce one by one, crane9000
for line in lines[(seperator+1):]:
  if line.strip() == '':
    continue

  # move 1 from 2 to 1
  _, count, _, origin, _, to = line.split(' ')
  
  # pick up crate and place in on top of the to stack
  for moves in range(int(count)):
    crate = crates[origin].pop(-1)
    crates[to].append(crate)

# print top crate for all stacks
print('part 1: ', end='')
for stack in crates:
  print(crates[stack][-1], end='')
print('')



# move count in one go, crane9001
crates = original

for line in lines[(seperator+1):]:
  if line.strip() == '':
    continue

  # move 1 from 2 to 1
  _, count, _, origin, _, to = line.split(' ')

  # the crane 9001, moves multiple at the same time
  stack = [crates[origin].pop(-1) for _ in range(int(count))]

  for crate in stack[::-1]:
    crates[to].append(crate) 

# print top crate for all stacks
print('part 2: ', end='')
for stack in crates:
  print(crates[stack][-1], end='')
print('')