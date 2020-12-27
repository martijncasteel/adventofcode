seating = []

with open('input', 'r') as file:
  for line in file:
    if line:
      seating.append(list(line.strip()))


def find_next_seat(seating, x, y, dx, dy):
  if (y + dy) < 0 or (y + dy) >= len(seating):
    return '.'

  if (x + dx) < 0 or (x + dx) >= len(seating[(y + dy)]):
    return '.'

  seat = seating[y + dy][x + dx]

  if seat == '.':
    return find_next_seat(seating, (x + dx), (y + dy), dx, dy)
  else:
    return seat



def count_occupied_viewable_seats(seating, seat_x, seat_y):
  sum = 0

  for dx in range(-1, 2):
    for dy in range(-1, 2):

      # skip own chair
      if dx == 0 and dy == 0:
        continue

      seat = find_next_seat(seating, seat_x, seat_y, dx, dy)

      if seat == '#':
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
        if count_occupied_viewable_seats(previous, x, y) == 0:
          seating[y][x] = '#'

      elif previous[y][x] == '#':
        if count_occupied_viewable_seats(previous, x, y) > 4:
          seating[y][x] = 'L'

      # print((x,y), previous[y][x], '->', seating[y][x], f'[{count_occupied_viewable_seats(previous, x, y)}]')

  print_seats(seating)

print(sum(s.count('#') for s in seating))
