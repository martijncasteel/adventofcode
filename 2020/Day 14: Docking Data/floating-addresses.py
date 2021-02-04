import re
address_reg = re.compile(r'^mem\[(\d+)\]$')

program = {}

def addresses(value, bitmask):
  value = "{0:0>36b}".format(int(value))
  chars = list(value)

  for index, mask in enumerate(bitmask):

    # overwrite all characters first
    if mask != '0':
      chars[index] = mask

  if 'X' not in chars:
    yield int(''.join(chars), 2)
    return

  positions = [i for i, v in enumerate(chars) if v == 'X']
  mask = 0

  while True:
    
    options = list("{0:0>37b}".format(mask))[-len(positions):]

    for index, position in enumerate(positions):
      chars[position] = options[-index]      

    yield int(''.join(chars), 2)

    # we have dried out our options
    if options.count('1') >= len(positions):
      return
  
    mask += 1
  

with open('input', 'r') as file:
  for line in file:
    param, value = line.strip().split(' = ', 2)

    # update the mask to the latest value
    if param == 'mask':
      mask = value

    # compute the given memory addresses
    else:
      for address in addresses(address_reg.findall(param)[0], mask):
        program[address] = int(value)
        print(address, '\t', "{0:0>36b}".format(int(value)))

  sum = 0
  for address, value in program.items():
    sum += value
  print('\n', sum)