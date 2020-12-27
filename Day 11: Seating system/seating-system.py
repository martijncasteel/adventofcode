seating = []

with open('input', 'r') as file:
  for line in file:
    if line:
      seating.append(list(line.strip()))

def count_occupied_adjacent_seats(seating, seat_x, seat_y):
  sum = 0

  for x in range(seat_x - 1, seat_x + 2):
    for y in range(seat_y - 1, seat_y + 2):

      # skip own chair
      if x == seat_x and y == seat_y:
        continue
      
      # skip if over the edge
      if y < 0 or y >= len(seating):
        continue

      if x < 0 or x >= len(seating[y]):
        continue

      if seating[y][x] == '#':
        sum += 1
  
  return sum



def print_seats(seating):
  for y in range(len(seating)):
    print(''.join(seating[y]))
  print('')

print_seats(seating)

previous = []
while True:

  if previous == seating:
    break

  # create a copy, one for comparing, one for setting
  previous = [row[:] for row in seating] 

  for y in range(len(previous)):
    for x in range(len(previous[y])):

      if previous[y][x] == '.':
        continue

      elif previous[y][x] == 'L':
        if count_occupied_adjacent_seats(previous, x, y) == 0:
          seating[y][x] = '#'

      elif previous[y][x] == '#':
        if count_occupied_adjacent_seats(previous, x, y) > 3:
          seating[y][x] = 'L'

      # print((x,y), previous[y][x], '->', seating[y][x], f'[{count_occupied_adjacent_seats(previous, x, y)}]')

  print_seats(seating)

print(sum(s.count('#') for s in seating))
