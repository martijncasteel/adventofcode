import math

# initial position, using simple x,y
position = (0,0)
facing = 90 # facing east


# vector addition would be nice
def move(pos, vector):
  return (pos[0] + vector[0], pos[1] + vector[1])


with open('input', 'r') as file:
  for line in file:

    action, value = line[0], int(line.strip()[1:])
    print(position, facing, '->', action, value)
    
    if action == 'N':
      position = move(position, (value, 0))
    elif action == 'S':
      position = move(position, (-value, 0))
    elif action == 'E':
      position = move(position, (0, value))
    elif action == 'W':
      position = move(position, (0, -value))


    elif action == 'L':
      facing = (facing - value) % 360

    elif action == 'R':
      facing = (facing + value) % 360


    # i was trying to keep out libraries but math 
    # results in a neat solution, so I'll allow it
    elif action == 'F':
      angle = math.radians(facing)
      vector = (value * int(math.cos(angle)), value * int(math.sin(angle)))
      position = move(position, vector)


print(position, facing, '=', abs(position[0]) + abs(position[1]))
 