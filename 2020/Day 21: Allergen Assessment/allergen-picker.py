import re

pattern = re.compile(r'^([a-z ]+)\(contains ([a-z ,]+)\)$')

food = []
allergens = {}
solution = {}

with open('input', 'r') as file:
  for line in file:
    match = re.match(pattern, line)
    ingred = set(match.group(1).strip().split())
    allerg = match.group(2).strip().split(', ')

    # create list with all foods
    food.append((ingred, allerg))

    for a in allerg:
      if not a in allergens:
        allergens[a] = ingred
        continue

      # try to find a commen ingredient for an allergy
      allergens[a] = allergens[a].intersection(ingred)

while len(solution) < len(allergens):
  for allergen, ingredients in allergens.items():

    ingredients = list(ingredients - solution.keys())

    # find allergen with only one ingredient
    if len(ingredients) == 1:
        solution[ingredients[0]] = allergen

# count all ingredient not having an allergen
part1 = len([i for ig, a in food for i in ig if i not in solution.keys()])
print(part1, '\n')

for ingredient, allergen in sorted(solution.items(), key=lambda a: a[1]):
  print(ingredient, end=',')
