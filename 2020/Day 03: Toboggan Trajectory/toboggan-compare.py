from array import *

def increment(coordinates, slope, width):
  x = coordinates[0] + slope[0]
  y = coordinates[1] + slope[1]
  return x % width, y

map = []

with open('input', 'r') as file:
  for line in file:
    map.append(list(line.strip()))

width = len(map[0])
trees = [0,0,0,0,0]
total = 1

slopes = [
  (1,1),
  (3,1),
  (5,1),
  (7,1),
  (1,2)
]

for index, slope in enumerate(slopes):
  coordinates = (0, 0)

  while True:
    coordinates = increment(coordinates, slope, width)

    if coordinates[1] >= len(map):
      total *= trees[index]
      break

    if map[coordinates[1]][coordinates[0]] == "#":
      trees[index] += 1

print(total)
exit(0)
