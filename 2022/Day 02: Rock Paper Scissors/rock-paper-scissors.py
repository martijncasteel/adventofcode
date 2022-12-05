# A, X for Rock
# B, Y for Paper
# C, Z for Scissors.

score = 0
games = {}

# all possible outcomes of the game
games['A', 'X'] = 1 + 3
games['A', 'Y'] = 2 + 6
games['A', 'Z'] = 3

games['B', 'X'] = 1
games['B', 'Y'] = 2 + 3
games['B', 'Z'] = 3 + 6

games['C', 'X'] = 1 + 6
games['C', 'Y'] = 2
games['C', 'Z'] = 3 + 3


# translate win, lose, or draw to actual hand for part 2
def translate(opponent, strategy) -> str:

  # X means losing the game
  # Y play for a draw
  # Z win it!
  
  strategies = {}

  strategies['A', 'X'] = 'Z'
  strategies['A', 'Y'] = 'X'
  strategies['A', 'Z'] = 'Y'

  strategies['B', 'X'] = 'X'
  strategies['B', 'Y'] = 'Y'
  strategies['B', 'Z'] = 'Z'

  strategies['C', 'X'] = 'Y'
  strategies['C', 'Y'] = 'Z'
  strategies['C', 'Z'] = 'X'

  return strategies[opponent, strategy]



with open('input.txt', 'r') as file:
  for line in file:

    opponent, player = line.strip().split(' ')[:2]
    score += games[opponent, player]
    

print(f'part 1: {score}')

score = 0

with open('input.txt', 'r') as file:
  for line in file:

    opponent, player = line.strip().split(' ')[:2]
    score += games[opponent, translate(opponent, player)]
    

print(f'part 2: {score}')
exit(0)
