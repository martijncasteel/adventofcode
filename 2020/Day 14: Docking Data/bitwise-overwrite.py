import re
address_reg = re.compile(r'^mem\[(\d+)\]$')

program = {}

def overwrite(value, bitmask):

  value = "{0:0>36b}".format(int(value))
  chars = list(value)

  for index, mask in enumerate(bitmask):

    # if not X overwrite with mask
    if mask != 'X':
      chars[index] = mask

  return ''.join(chars)

with open('input', 'r') as file:
  for line in file:
    param, value = line.strip().split(' = ', 2)

    # update the mask to the latest value
    if param == 'mask':
      mask = value

    # compute the given memory addresses
    else:
      address = address_reg.findall(param)[0]

      program[address] = overwrite(value, mask)
      print(address, '\t', program[address])

  sum = 0
  for address, value in program.items():
    sum += int(value, 2)
  print('\n', sum)