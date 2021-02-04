# initial position, using simple x,y
waypoint = (1,10)
position = (0,0)


# vector addition would be nice
def move(pos, vector):
  return (pos[0] + vector[0], pos[1] + vector[1])
  
def rotate(pos, degrees):
  x = pos[0]
  y = pos[1]

  # turning to the right 90 degrees;
  # +x -> +e
  # +e -> -s
  # -s -> -w
  # -w -> +n
  for _ in range(degrees//90):
    x, y = -y, x

  return (x, y)

# move the ship
def forward(pos, waypoint, value):
   return (pos[0] + value * waypoint[0], pos[1] + value * waypoint[1])


with open('input', 'r') as file:
  for line in file:

    action, value = line[0], int(line.strip()[1:])
    print(position, waypoint, '->', action, value)
    
    if action == 'N':
      waypoint = move(waypoint, (value, 0))
    elif action == 'S':
      waypoint = move(waypoint, (-value, 0))
    elif action == 'E':
      waypoint = move(waypoint, (0, value))
    elif action == 'W':
      waypoint = move(waypoint, (0, -value))


    elif action == 'L':
      waypoint = rotate(waypoint, -value % 360)
    elif action == 'R':
      waypoint = rotate(waypoint, value)

    elif action == 'F':
      position = forward(position, waypoint, value)


print(position, waypoint, '=', abs(position[0]) + abs(position[1]))