
class Assignment: 

  def __init__(self, line) -> None:
    self.min, self.max = [int(i) for i in line.split('-', 1)]

  def contains(self, other) -> bool:
    if self.min <= other.min and self.max >= other.max:
      return True
    return False

  def overlaps(self, other) -> bool:
    if self.min <= other.min <= self.max:
      return True

    if self.min <= other.max <= self.max:
      return True
    return False

  def __repr__(self) -> str:
    return f"{self.min}-{self.max}"


fully_contains = 0
overlaps = 0

with open('input.txt', 'r') as file:
  for line in file:

    one, two = line.strip().split(',', 1)

    one = Assignment(one)
    two = Assignment(two)

    if one.contains(two):
      fully_contains += 1

    elif two.contains(one):
      fully_contains += 1

    if one.overlaps(two):
      overlaps +=1

    elif two.overlaps(one):
      overlaps +=1

print(f'part 1: {fully_contains}')
print(f'part 2: {overlaps}')