import re, enum

# pattern to find all directions
direction_pattern = re.compile(r'[ns]?[ew]')

DIRECTIONS = {
  'e':  (2, 0), 
  'w' : (-2, 0), 

  'nw': (-1, 1), 
  'ne': (1, 1),
  
  'sw': (-1, -1), 
  'se': (1, -1), 
}


class Color(enum.Enum):
  white = 0
  black = 1


# black tile directionary, middle is (0, 0)
tile_colors = {}
tile_neighbors = {}

with open('input', 'r') as file:
  for line in file:

    # parse line sum all steps towards the tile
    path = direction_pattern.findall(line.strip())
    dirs = [DIRECTIONS[step] for step in path]

    coordinate = ( sum(x for x, y in dirs), sum(y for x, y in dirs) )

    
    if coordinate in tile_colors:
      # if tile exists toggle between black and white
      if (tile_colors[coordinate] + 1) % 2 == Color.white.value:
        del tile_colors[coordinate]

    else:
      # if tile not exists it was white and now black
      tile_colors[coordinate] = Color.black.value


# count number of ones
print('part1:', sum(color for color in tile_colors.values()))


def neighbors_coordinates(coordinate):
  # calculate neighbors of this coordinates

  for x, y in DIRECTIONS.values():
    yield coordinate[0] + x, coordinate[1] + y


for day in range(0, 100):

  # init new neighbors dictionary
  tile_neighbors = {}
  changes = set()
  
  # calculate all tiles, including neighbours
  for coordinate, color in tile_colors.items():

    black_tiles_around = 0

    # look to all neighbours
    for neighbor in neighbors_coordinates(coordinate):

      # count the black tiles around the current
      if neighbor in tile_colors:
        black_tiles_around += 1

      # calculate if tiles can become black
      if neighbor in tile_neighbors:
        tile_neighbors[neighbor] += 1
        
      else:
        tile_neighbors[neighbor] = 1


    if black_tiles_around == 0 or black_tiles_around > 2:
      # remove current tile to become white
      changes.add(coordinate)


  # add black tiles if it has two black neighbors
  for coordinate, count in tile_neighbors.items():

    # no black tiles
    if coordinate not in tile_colors:
      if count == 2:
        tile_colors[coordinate] = Color.black.value


  # add changes to tile_colors
  for coordinate in changes:
    if coordinate in tile_colors:
      del tile_colors[coordinate]


  print(f'Day {str(day + 1).zfill(3)}:  ', sum(color for color in tile_colors.values()))