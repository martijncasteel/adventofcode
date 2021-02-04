import re

pattern = re.compile(r'([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)') 

def read_tickets(raw):
  for line in raw.splitlines()[1:]:
    yield [int(number) for number in line.split(',')]

with open('input', 'r') as file:
  raw = file.read().split('\n\n')
  rules = {}

  # read rules
  for line in pattern.finditer(raw[0]):
    name, amin, amax, bmin, bmax = line.groups()

    a = range(int(amin), int(amax) + 1)
    b = range(int(bmin), int(bmax) + 1)

    rules[name] = set.union(set(a), b)

  # all possible values
  valid_numbers = set.union(*rules.values())

  my_ticket = next(read_tickets(raw[1]))
  nearby_tickets = list(read_tickets(raw[2]))

  invalid_numbers = []
  for ticket in nearby_tickets:
    for number in ticket:
      if number not in valid_numbers:
        invalid_numbers.append(number)

  print(sum(invalid_numbers))


  # remove invalid tickets
  valid_tickets = [ticket for ticket in list(nearby_tickets) if all(number in valid_numbers for number in ticket)]
  
  # possible columns for ticket name
  columns = {name: [*range(len(my_ticket))] for name in rules}

  for ticket in valid_tickets:
    for index, number in enumerate(ticket):

      # eliminate columns
      for name in columns: 
        
        if number not in rules[name]:
          columns[name].remove(index)

          # if only one column is left, remove this from the other lists
          if len(columns[name]) == 1:
            for n in columns:
              if n != name and columns[name][0] in columns[n]:
                columns[n].remove(columns[name][0])

          continue


  # determine the column names
  for name in sorted(columns, key=lambda column: len(columns[column]), reverse=False):

    if len(columns[name]) > 1:
      raise AttributeError()

    # remove this column from all other columns
    for column in columns:
      if column == name: 
        continue

      if columns[name][0] in columns[column]:
        columns[column].remove(columns[name][0])

print(columns)

# find names starting with departure and multiply
result = 1
for name, value in columns.items():
  if name.startswith("departure"):
    result *= my_ticket[value[0]]

print(result)