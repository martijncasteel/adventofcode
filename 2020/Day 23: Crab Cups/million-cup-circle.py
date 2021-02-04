

class Game:
  def __init__(self, cups, total):
    self.cups = [int(c) for c in list(cups)]
    self.cups += range(len(self.cups), total)

    self.len = len(self.cups)
    self.index = 0

  def __repr__(self):
    # encircle index
    return ' '.join(['(' + str(c) + ')' if i == self.index else str(c) for i, c in enumerate(self.cups)])


  def slice(self):
    current = self.cups[self.index]
    three = []

    for _ in range(0,3):
      three.append(self.cups.pop((self.cups.index(current) + 1) % len(self.cups)))


    return (current, three, self.cups)


  def insert(self, current, three):
    # set cups in new order
    index = self.cups.index(current) % len(self.cups) + 1

    for cup in three[::-1]:
      self.cups.insert(index, cup)


with open('input', 'r') as file:
  cups, number_of_moves, total = file.readline().split()
  game = Game(cups, int(total))

# execute number_of_moves loops
for move in range(int(number_of_moves)):
  # print(f'\n-- move { move + 1 } --') 

  # print('cups:', game)
  current, three, _ = game.slice()
  current_cup = current

  # print('pick up:', ', '.join([str(c) for c in three]))
  
  while True:
    current -= 1

    if (current) in game.cups:
      # print('destination:', current)
      game.insert(current, three)
      break

    elif current < min(game.cups):
      # print('destination:', max(game.cups))
      game.insert(max(game.cups), three)
      break


  # get new position in list and go to the next
  game.index = game.cups.index(current_cup)
  game.index = (game.index + 1) % game.len


print('\n-- final --')
# print('cups:', game)

current_index = game.cups.index(1)
print(game.cups[(current_index + 1) % game.len] * game.cups[(current_index + 2) % game.len])