import math
required_fuel, required_fuel_incl = 0, 0

with open('input', 'r') as file:
  for line in file:
    
    # get the mass
    mass = int(line.strip())

    required_fuel += math.floor(mass / 3) - 2

print(f'part 1: {required_fuel:.0f}')

def fuel(mass) -> float:
  f = math.floor(mass / 3) - 2
  
  if f <= 0:
    return 0

  return fuel(f) + f


with open('input', 'r') as file:
  for line in file:
    
    # get the mass
    mass = int(line.strip())
    required_fuel_incl += fuel(mass)

print(f'part 2: {required_fuel_incl:.0f}')
exit(0)
