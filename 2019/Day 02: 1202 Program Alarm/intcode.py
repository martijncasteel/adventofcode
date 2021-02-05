ints = []

def load():
  ''' (re)load program '''
  with open('input', 'r') as file:
    line = file.readline().strip()
    return [int(i) for i in line.split(',')]


def next(i):
  ''' next returns next 4 from the list'''
  opscode = ints[i]

  try:
    a = ints[i+1] 
    b = ints[i+2] 
    c = ints[i+3]
  except IndexError:
    return opscode, 0, 0, 0 

  return opscode, a, b, c

def run(ints, noun = 12, verb = 2):
  i = 0

  # set 1202 in code
  ints[1] = noun
  ints[2] = verb

  opcode, a, b, c = next(i)

  # run program
  while opcode != 99:

    if opcode == 1:
      ints[c] = ints[a] + ints[b]

    elif opcode == 2:
      ints[c] = ints[a] * ints[b]

    else:
      exit(1)

    i += 4
    opcode, a, b, c = next(i)

  return ints[0]

# take first set
ints = load()
print(f'part 1: {run(ints)}')


for noun in range(0,100):
  for verb in range(0,100):

    ints = load()
    output = run(ints, noun, verb)

    if output == 19690720:
      print(f'part 2: {100 * noun + verb}')
      exit(0)