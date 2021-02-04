import re, math

class Image():
  def __init__(self, rows):
    self.data = []
    self.sum = 0

  def parse(self, index, data):
    if len(self.data) <= index:
      self.data.append([])

    # add list to row index and count #
    self.data[index].extend(data)
    self.sum += data.count('#')


  def __repr__(self):
    return '\n'.join([''.join(d) for d in self.data])


  def __compare(self, offset, monster):

    for y in range(0, len(monster)):
      for x in range(0, len(monster[0])):

        if monster[y][x] != '#':
          continue

        if monster[y][x] != self.data[y + offset[1]][x + offset[0]]:
          return False

    # checked all # and found a monster!
    return True


  def find_monsters(self, monster, offset = 0, flipped = False):
    # find monsters by flipping and rotating the monster
    monsters = []

    for y in range(0, len(self.data) - len(monster)):    
      for x in range(0, len(self.data[0]) - len(monster[0])):
        
        if self.__compare((x, y), monster):
          self.sum -= sum([row.count('#') for row in monster])
          monsters.append((x,y, offset, flipped, monster))
    
    if len(monsters) > 1: 
      return monsters

    elif offset > 3:
      if not flipped:

        # rotate once more, to original position and flip
        monster = list(zip(*monster))[::-1]
        return self.find_monsters(monster[::-1], 0, True)

      return []

    else:
      # rotate monster and keep track of times it's rotated
      monster = list(zip(*monster))[::-1]
      return self.find_monsters(monster, offset + 1, flipped)


  def draw_monsters(self, monsters):
    image = self.data

    if len(monsters) < 1:
      return

    # draw all monsters, using (a,b) offset
    for a, b, _, _, data in monsters:
      
      # loop through monster's data
      for y in range(0, len(data)):
        for x in range(0, len(data[0])):

          if data[y][x] != '#':
            continue

          # overwrite # in image
          image[b + y][a + x] = 'O'
    

    # get rotation from a monster
    _, _, offset, flipped, _ = monsters[0]

    # flip image
    if flipped:
      image = image[::-1]

    # rotate it 
    for _ in range(0, offset):
      image = list(zip(*image[::-1]))

    # print new image
    print('\n'.join([''.join(d) for d in image]))


class Puzzle:
  def __init__(self, tile):
    self.pieces = {}
    self.spaces = {}

    self.pieces[(0, 0)] = tile
    self.__calculate_empty_spaces((0, 0))
    

  def add(self, position, tile):
    # add to puzzle on the table and remove
    # from pile of pieces
    self.pieces[position] = tile
    del self.spaces[position]

    # re-calculate spaces
    self.__calculate_empty_spaces(position)


  def __calculate_empty_spaces(self, position):
    for x, y in self.__positions_around(*position):

      # if there is a piece it cannot be a space
      if (x, y) in self.pieces:
        continue

      self.spaces[(x, y)] = [''] * 4

      # find edges around (x, y)
      for a, b in self.__positions_around(x, y):

        # check tiles on the left and right
        if (a, b) in self.pieces:
          if a - x < 0:
            self.spaces[(x,y)][3] = self.pieces[(a,b)].edges[1][::-1]
          elif a - x > 0:
            self.spaces[(x,y)][1] = self.pieces[(a,b)].edges[3][::-1]

          # look for tiles above and below
          elif b - y < 0:
            self.spaces[(x,y)][0] = self.pieces[(a,b)].edges[2][::-1]
          elif b - y > 0:
            self.spaces[(x,y)][2] = self.pieces[(a,b)].edges[0][::-1]
    

  def __positions_around(self, a, b):
    for x in range(a - 1, a + 2):
      for y in range(b - 1, b + 2):

        if x == a and y == b:
          continue

        # later on I thought about it and
        # we don't have to check the diagonal
        if x != a and y != b:
          continue

        yield x, y     


  def to_list(self):
    for pos in sorted(self.pieces.keys() , key=lambda key: [key[1], key[0]]):
      yield pos, self.pieces[pos]


  def corners(self):
    positions = sorted(self.pieces.keys() , key=lambda key: [key[1], key[0]])

    for x in [min([x for x, _ in positions]), max([x for x, _ in positions])]:
      for y in [min([y for _, y in positions]), max([y for _, y in positions])]:

        yield (x, y), self.pieces[(x,y)]

  
  def to_image(self):
    # parse solved puzzle to Image
    offset = None
    image = Image(int(math.sqrt(len(self.pieces)) * 8))

    for x, y in sorted(self.pieces.keys() , key=lambda key: [key[1], key[0]]):
      if offset is None:
        offset = (-x, -y)

      # create one large image, index is using the tile position normalized 
      # and the row in the tile 
      for index, data in enumerate(self.pieces[(x, y)].image):
        image.parse((y + offset[1]) * 8  + index, data)

    return image


class Tile:

  def __init__(self, data):
    self.id = re.match(r'^Tile (\d+):$', data[0]).group(1)
    self.__parse_data(data[1:])
    

  def __parse_data(self, data):
    # parse data to the four edges of this tile

    north = data[0]
    south = data[-1][::-1]

    west = ''.join([string[0] for string in data[::-1]])
    east = ''.join([string[-1] for string in data])

    self.edges = [north, east, south, west]

    # store image part without edges
    self.image = [list(d[1:-1]) for d in data[1:-1]]

  def __flip(self):
    # flip tile over to find a spot

    self.edges = [
      self.edges[2][::-1],
      self.edges[1][::-1],
      self.edges[0][::-1],
      self.edges[3][::-1]
    ]

    self.image = self.image[::-1]

  def __rotate(self, offset):
    # turn to the left since we look to index + offset

    for _ in range(0, offset):
      self.edges.append(self.edges.pop(0))

      # rotate the image using zip
      self.image = list(zip(*self.image))[::-1]
  
  def has_edges(self, edges, offset = 0, flipped = False):
    # checks if this tile had edges, also rotates it
    for index, edge in enumerate(edges):

      # this side has no requirements
      if edge == '':
        continue

      # made a complete circle and flipped it around,
      # it just not going to fit here
      if offset > 3:
        if not flipped:
          self.__flip()
          return self.has_edges(edges, 0, True)

        return False

      # specific edge not found
      if edge != self.edges[(index + offset) % 4]:

        # rotate and try again
        return self.has_edges(edges, offset + 1, flipped)

    self.__rotate(offset)
    return True


  @staticmethod
  def find_edges(tiles, edges):
    # find tiles having the same edge and not occupied
    for tile in tiles:

      if tile.has_edges(edges):
        yield tile

tiles = []

with open('test', 'r') as file:

  # parse all tiles
  for tile in file.read().strip().split('\n\n'):
    tiles.append(Tile(tile.splitlines()))

# lay down one piece
puzzle = Puzzle(tiles[0])
del tiles[0]

# loop until the pile of tiles is empty
while(len(tiles) > 0):

  # find next piece to put next to it
  for position, edges in puzzle.spaces.items():

    options = list(Tile.find_edges(tiles, edges))

    # no tiles found for this space
    if len(options) < 1:
      continue

    # exactly one adjacent tile found
    if len(options) < 2:
      puzzle.add(position, options[0])
      tiles.remove(options[0])
      break

print(f'part1:\t{math.prod([ int(tile.id) for _, tile in puzzle.corners()])}\n')

# retrieve single image from solved puzzle
image = puzzle.to_image()

# flip to match example in README
# image.data = image.data[::-1]
# print(image)

with open('monster') as file:
  monster = [list(row) for row in file.read().splitlines()]

# print('\n'.join([''.join(d) for d in monster]))
monsters = image.find_monsters(monster)
image.draw_monsters(monsters)

print(f'\npart2:\t{image.sum}')


