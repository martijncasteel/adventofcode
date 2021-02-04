program = []
pointer = 0

history = set()
accumulator = 0

# well python is not the best language, but it'll do
with open('input', 'r') as file:
  program = file.readlines()

while pointer not in history:

  op, arg = program[pointer].strip().split(' ')
  history.add(pointer)

  if op == "jmp":
    pointer += int(arg)
    continue

  elif op == "acc":
    accumulator += int(arg)

  elif op == "nop":
    pass

  pointer += 1
  

print(accumulator)