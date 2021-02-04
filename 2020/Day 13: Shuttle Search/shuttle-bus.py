with open('input', 'r') as file:
  time = t = int(file.readline().strip())
  busses = [int(bus) for bus in file.readline().strip().split(',') if bus != 'x']


while True:

  for bus in busses:
    if t % bus == 0.0:
      # found a bus that leaves on t
      print(bus, t - time, bus * (t - time))
      exit(0)
    
  t += 1
