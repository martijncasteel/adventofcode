import math

class Key:
  def __init__(self, public_key):
    self.public_key = int(public_key)

    # super secret
    self.__loop_size = self.__get_loop_size()


  def __get_loop_size(self) -> int:
    # calculate loopsize for public key

    loop_size = 0
    subject_number = 1
  
    while subject_number != self.public_key:
        subject_number = (subject_number * 7) % 20201227
        loop_size += 1

    return loop_size


  def get_encryption_key(self, public_key) -> int:
    # calculate encryption key with others public key

    encryption_key = 1
    for _ in range(self.__loop_size):
        encryption_key = (public_key * encryption_key) % 20201227

    return encryption_key


with open('input', 'r') as file:
  card = Key(file.readline().strip())
  door = Key(file.readline().strip())

  print(card.get_encryption_key(door.public_key))
