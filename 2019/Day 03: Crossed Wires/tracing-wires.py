green = []
red = [] 

def coordinates(actions):
  path = [(0,0)]

  for action in actions.split(','):
    path += traverse(path[-1], action)

  return path

def traverse(start, action):
  x, y = start
  direction, count = action[0], int(action[1:])

  if direction == 'U':
    return [(x, b + 1) for b in range(y, y+count)]

  if direction == 'L':
    return [(a, y) for a in range(x-count, x)][::-1]

  if direction == 'R':
    return [(a + 1, y) for a in range(x, x+count)]

  if direction == 'D':
    return [(x, b) for b in range(y-count, y)][::-1]

def intersection(green, red):
  return [(x, y, x+y) for (x,y) in green if (x,y) in red]


with open('input','r') as file:
  green = coordinates(file.readline().strip())
  red = coordinates(file.readline().strip())

crossing = intersection(green, red)
print(f'part 1: { min([l for (x,y,l) in crossing if l > 0]) }')
