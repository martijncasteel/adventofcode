import string 

# 10:62 are a-zA-Z, added the 9 to have a index 1
chars = string.printable[9:62]

class Rucksack:
  def __init__(self, line):
    self.line = line
    self.size = int(len(line)/2)

    self.compartiments = [self.line[:self.size], self.line[self.size:]]

  
  def intersection(self): # TODO combine intersection and badges
    return [value for value in self.compartiments[0] if value in self.compartiments[1]][0]

  def badges(one, two, three):
    return [value for value in one.line if value in two.line and value in three.line][0]


  def __repr__(self):
    return f"{''.join(self.line)}"

sum_compartiments = 0
sum_badges = 0
groups = []

with open('input.txt', 'r') as file:
  for line in file:
    rucksack = Rucksack(line.strip())
    intersection = rucksack.intersection()

    sum_compartiments += chars.index(intersection)

    groups.append(rucksack)

    # part 2, groups of three
    if len(groups) == 3:
      badge = Rucksack.badges(*groups)
      sum_badges += chars.index(badge)

      groups = []


print(f'part 1: {sum_compartiments}')
print(f'part 2: {sum_badges}')
exit(0)
