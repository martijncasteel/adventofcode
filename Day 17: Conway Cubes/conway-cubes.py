cycles = []
pockets = {}

class Cube:
  def __init__(self, vector, active=False):
    self.vector = vector
    self.active = active

  def compute(self, previous):
    sum = 0

    # another 3 dimensional loop
    for x in range(self.vector[0] -1, self.vector[0] +2):
      for y  in range(self.vector[1] -1, self.vector[1] +2):
        for z  in range(self.vector[2] -1, self.vector[2] +2):

          if (x,y,z) == self.vector:
            continue

          if (x,y,z) not in previous:
            continue
          
          if previous[(x,y,z)].active:
            sum += 1

    if self.active and sum >= 2 and sum <= 3:
      self.active = True
      return
    
    if not self.active and sum == 3:
      self.active = True
      return
    
    self.active = False

        
  def __repr__(self):
    if self.active:
      return '#'
    return '.'

  # some method to sort a single pocket for printing
  def __lt__(a, b):
    if a.vector[2] != b.vector[2]:
      return a.vector[2] < b.vector[2]

    if a.vector[1] != b.vector[1]:
      return a.vector[1] < b.vector[1]

    if a.vector[0] != b.vector[0]:
      return a.vector[0] < b.vector[0]

    #should never happen
    raise AttributeError()

  def __gt__(a, b):
    if a.vector[2] != b.vector[2]:
      return a.vector[2] > b.vector[2]

    if a.vector[1] != b.vector[1]:
      return a.vector[1] > b.vector[1]

    if a.vector[0] != b.vector[0]:
      return a.vector[0] > b.vector[0]



    raise AttributeError()



def print_pockets(dict):
  previous = None
  for cube in sorted(dict.values()):
    
    if not previous:
      print(f'z={cube.vector[2]}')
      print(cube, end ='')

    elif previous.vector[2] != cube.vector[2]:
      print(f'\n\nz={cube.vector[2]}')

    elif previous.vector[1] != cube.vector[1]:
      print(f'\n{cube}', end='')

    else:
      print(cube, end ='')

    previous = cube
  print('')



with open('test', 'r') as file:
  for y, line in enumerate(file):
    characters = list(line.strip())

    for x, char in enumerate(characters):
      pockets[(x,y,0)] = Cube((x, y, 0), char == "#")

  cycles.append(pockets.copy())
  pockets = {}
  
# print starting point 
print_pockets(cycles[0])
sum = 0

# for 6 cycles compute next cycle
while len(cycles) < 7:

  start = min(cycles[-1].items())[0]
  end = max(cycles[-1].items())[0]
  sum = 0
  
  for x in range(start[0] -1, end[0] +2):
    for y in range(start[1] -1, end[1] +2):
      for z in range(start[2] -1, end[2] +2):
        
        #create new cube
        cube = Cube((x,y,z))
        cube.compute(cycles[-1])
        pockets[(x,y,z)] = cube

        if cube.active:
          sum += 1


  cycles.append(pockets.copy())
  pockets = {}

  print(f'\nAfter{len(cycles) -1} cycle:\n')
  print_pockets(cycles[-1])
  
# count of active cubes in last cycle
print(f'part1 => {sum}')
exit(0)