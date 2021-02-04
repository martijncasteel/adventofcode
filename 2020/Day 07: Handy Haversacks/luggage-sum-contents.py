# key has the following bags
bags = {}

# light red bags contain 1 bright white bag, 2 muted yellow bags.
def process(line):
  if line == "":
    return

  bag, contains = line.split(" contain ", 2)

  # remove bags from name
  bag = ' '.join(bag.split(' ')[:-1])

  if contains == "no other bags.":
    return
  else:

    # retrieve color from every bag
    for b in contains.split(", "):
      count, color = b.split(' ')[:1], ' '.join(b.split(' ')[1:3])

      # swapped these around
      bags.setdefault(bag,{})
      bags[bag][color] = int(count[0])


with open('input', 'r') as file:
  for line in file:
    process(line.strip())


# count the number of bags a gold bag has
def count(color):
  sum = 0

  if color in bags:
    for bag, number in bags[color].items():
      sum += number + number * count(bag)

  return sum


print(f'part2 -> {count("shiny gold")}')


