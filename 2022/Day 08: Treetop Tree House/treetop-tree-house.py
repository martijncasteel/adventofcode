map = []

with open('input.txt') as file:
  for line in file:
    map.append(line.strip())

height = len(map)
width = len(map[0])

sum = (width * 2) + (height * 2) - 4

def is_visible(tx, ty, tree) -> bool:
  # print('\n')
  # print((tx,ty), tree)

  def from_the_left() -> bool:
    for y in range(0, ty):
      # print('left', (tx, y),map[tx][y], tree > map[tx][y])
      if tree <= map[tx][y]:
        return False
    return True

  def from_the_right() -> bool:
    for y in range(ty + 1, width):
      # print('right', (tx, y), map[tx][y], tree > map[tx][y])
      if tree <= map[tx][y]:
        return False
    return True

  def from_the_top() -> bool:
    for x in range(0, tx):
      # print('top', (x, ty), map[x][ty], tree > map[x][ty])
      if tree <= map[x][ty]:
        return False
    return True

  def from_the_bottom() -> bool:
    for x in range(tx + 1, height):
      # print('bottom', (x, ty),map[x][ty], tree > map[x][ty])
      if tree <= map[x][ty]:
        return False
    return True


  if from_the_left():
    return True

  if from_the_right():
    return True

  if from_the_top():
    return True

  if from_the_bottom():
    return True

  return False

def viewing_distance(tx, ty, tree) -> int:
  def look_left() -> int:
    cl = 1

    for y in range(ty - 1, 0, -1):
      if map[tx][y] < tree:
        cl += 1
      else:
        break

    return cl
  
  def look_right() -> int:
    cr = 1

    for y in range(ty + 1, width - 1):
      if map[tx][y] < tree:
        cr += 1
      else:
        break
    return cr

  def look_up() -> int:
    cr = 1

    for x in range(tx - 1, 0, -1):
      if map[x][ty] < tree:
        cr += 1
      else:
        break

    return cr

  def look_down() -> int:
    cr = 1
  
    for x in range(tx + 1, height - 1):
      if map[x][ty] < tree:
        cr += 1
      else:
        break

    return cr

  # print((tx,ty), look_up(), look_left(), look_right(), look_down())
  return look_left() * look_right() * look_up() * look_down()


for x in range(1, height-1):
  for y in range(1, width-1):
    if is_visible(x, y, map[x][y]):
      sum += 1

print('part 1:', sum)

current = 0

for x in range(height):
  for y in range(width):
    distance = viewing_distance(x,y, map[x][y])

    if distance > current:
      current = distance

print('part 2:', current)

