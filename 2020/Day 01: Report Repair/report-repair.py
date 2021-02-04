with open('input', 'r') as file:
  expenses = file.readlines()

# so this results in a n^3 complexity. As this was done very 
# early I couldn't come up with a better solution
for index1, expense1 in enumerate(expenses):
  for index2, expense2 in enumerate(expenses):
    for index3, expense3 in enumerate(expenses):

      if index1 == index2:
        continue

      if index2 == index3:
        continue

      if index1 == index3:
        continue

      if int(expense1) + int(expense2) + int(expense3) == 2020:
        print(int(expense1) * int(expense2) * int(expense3))
        exit(0)

    
