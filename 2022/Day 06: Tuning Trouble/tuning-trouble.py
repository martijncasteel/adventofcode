with open('input.txt') as file:
  datastream = file.readline().strip()

for index in range(len(datastream) - 4):
  packet = datastream[index:index+4]

  if len(set(packet)) == 4:
    print('part 1:', index + 4)
    break

for index in range(len(datastream) - 14):
  packet = datastream[index:index+14]

  if len(set(packet)) == 14:
    print('part 2:', index + 14)
    break

    

