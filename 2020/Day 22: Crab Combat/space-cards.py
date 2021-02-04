# a bit overkill, but he it makes it readable!
class Player: 
  def __init__(self, data):
    self.id = data[0]
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

    print(sum)
    return sum

with open('input', 'r') as file:
  data = file.read()
  data = data.split('\n\n')

  p1 = Player(data[0].split('\n'))
  p2 = Player(data[1].split('\n'))

while True:

  if len(p1.cards) == 0:
    p2.calculate()
    break

  elif len(p2.cards) == 0:
    p1.calculate()
    break


  if p1.cards[0] > p2.cards[0]:
    # player 1 won this round!
    p1.cards.append(p1.cards.pop(0))
    p1.cards.append(p2.cards.pop(0))


  else:
    # player 2 won!
    p2.cards.append(p2.cards.pop(0))
    p2.cards.append(p1.cards.pop(0))

