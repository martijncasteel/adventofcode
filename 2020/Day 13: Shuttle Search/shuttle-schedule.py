with open('input', 'r') as file:
  _ = file.readline()
  busses = { int(bus): i for i, bus in enumerate(file.readline().split(',')) if bus != 'x'}

print(busses)

def check_time(list, time):
  for bus, offset in list.items():

    if (time + offset) % bus != 0:
      return False
  
  return True

time = 0
step = max(busses)
offset = busses[step]

while True:

  if check_time(busses, time * step - offset):

    # found a t with subsequent busses
    print(time * step - offset)
    exit(0)

  time += 1


