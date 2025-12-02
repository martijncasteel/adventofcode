#!/usr/bin/env python3

import sys

exact_match = 0
passed_zero = 0

dial = 50

for line in sys.stdin:
  
  dir, amount = line.strip()[0], line.strip()[1:]

  print(dir, amount)

  match dir:
    case "L":
      for i in range(0, int(amount)):
        dial -= 1

        if dial < 0:
          dial += 100
        
        if dial == 0:
          passed_zero += 1
      
      if dial == 0:
        exact_match += 1

    case "R":
      for i in range(0, int(amount)):
        dial += 1

        if dial >= 100:
          dial -= 100
        
        if dial == 0:
          passed_zero += 1
      
      if dial == 0:
        exact_match += 1




print(f'part 1: {exact_match}')
print(f'part 2: {passed_zero}')

exit(0)
