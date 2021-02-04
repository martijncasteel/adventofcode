import sys, logging

# with input and printing it all it takes too long 
# _debug_ for all, _info_ for the answer only
logging.basicConfig(format='%(message)s', stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger()

max_game_number = 0

class Player: 
  def __init__(self, data = []):
    self.cards = []

    for card in data[1:]:
      if card == '':
        continue

      self.cards.append(int(card))


  def calculate(self):
    self.cards.reverse()
    sum = 0

    for i, card in enumerate(self.cards, start=1):
      sum += i * card

    self.cards.reverse()
    return sum

  
  def draw(self):
    return self.cards.pop(0)


  def copy(self, n):
    p = Player()
    p.cards = [self.cards[i] for i in range(n)]
    return p

def game(p1, p2, game_number = 1):
  history = set()
  round = 1

  logger.debug(f'\n=== Game {game_number} ===')

  # so I probably shouldn't use global
  global max_game_number
  if game_number > max_game_number:
    max_game_number = game_number 

  while True:

    if len(p1.cards) == 0:
      logger.debug(f'The winner of game {game_number} is player 2!')
      return 2

    elif len(p2.cards) == 0:
      logger.debug(f'The winner of game {game_number} is player 1!')
      return 1

    logger.debug(f'\n-- Round {round} (Game {game_number}) --')
    logger.debug(f'Player 1\'s deck: { ", ".join([str(c) for c in p1.cards]) }')
    logger.debug(f'Player 2\'s deck: { ", ".join([str(c) for c in p2.cards]) }')

    # if this game occurred before player 1 wins
    round_hash = (p1.calculate(), p2.calculate())

    # draw a card each, current play
    draw = (round, p1.draw(), p2.draw())
    logger.debug(f'Player 1 plays: { draw[1] }')
    logger.debug(f'Player 2 plays: { draw[2] }')


    # check if history repeats itself
    if round_hash in history:
      logger.debug('-- history repeats itself, player 1 wins --')
      return 1

    history.add(round_hash)

    if len(p1.cards) >= draw[1] and len(p2.cards) >= draw[2]:
      # play another game as rules depict
      logger.debug('Playing a sub-game to determine the winner...')

      winner = game(p1.copy(draw[1]), p2.copy(draw[2]), max_game_number + 1)
      winner = p1 if winner == 1 else p2

      logger.debug(f'\n...anyway, back to game {game_number}.')

    else:
      # game like in previous part, simply highest card wins
      winner = p1 if draw[1] > draw[2] else p2

      
    # give the winner the cards
    if winner == p1:
      # player 1 won this round!
      p1.cards.append(draw[1])
      p1.cards.append(draw[2])

      logger.debug(f'Player 1 wins round {round} of game {game_number}!')

    else:
      # player 2 won!
      p2.cards.append(draw[2])
      p2.cards.append(draw[1])

      logger.debug(f'Player 2 wins round {round} of game {game_number}!')

    round += 1



with open('input', 'r') as file:
  data = file.read()
  data = data.split('\n\n')

p1 = Player(data[0].split('\n'))
p2 = Player(data[1].split('\n'))

winner = game(p1, p2)
winner = p1 if winner == 1 else p2

logger.info('\n== Post-game results ==')
logger.info(f'Player 1\'s deck: { ", ".join([str(c) for c in p1.cards]) }')
logger.info(f'Player 2\'s deck: { ", ".join([str(c) for c in p2.cards]) }')
logger.info(winner.calculate())


