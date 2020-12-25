from array import *

def increment(coordinates, width):
  x = coordinates[0] + 3
  y = coordinates[1] + 1
  return x % width, y

map = []

with open('input', 'r') as file:
  for line in file:
    map.append(list(line.strip()))

width = len(map[0])
trees = 0
coordinates = (0, 0)

while True:
  coordinates = increment(coordinates, width)

  if coordinates[1] >= len(map):
    break

  if map[coordinates[1]][coordinates[0]] == "#":
    trees += 1

print(trees)
exit(0)
