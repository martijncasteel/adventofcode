# key sits inside values
bags = {}

# light red bags contain 1 bright white bag, 2 muted yellow bags.
def process(line):
  bag, contains = line.split(" contain ", 2)

  # remove bags from name
  bag = ' '.join(bag.split(' ')[:-1])

  if contains == "no other bags.":
    return
  else:

    # retrieve color from every bag
    for b in contains.split(", "):
      color = ' '.join(b.split(' ')[1:3])
      bags.setdefault(color,[]).append(bag)


with open('input', 'r') as file:
  for line in file:
    process(line.strip())


# use bags to find possible bags to find a shiny gold bag
def find(color):
  yield color

  if color in bags:
    for bag in bags[color]:

      # for every bag it can contain yield it
      for b in find(bag):
        yield b


options = set(find("shiny gold"))
options.remove("shiny gold")
print(f'part1 -> {len(options)}')


