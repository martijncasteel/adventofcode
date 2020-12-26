program = []
sources = {}

# well python is not the best language, but it'll do
with open('input', 'r') as file:
  for index, line in enumerate(file):
    op, arg = line.strip().split(' ')
    program.append((op, int(arg)))

    # add dictionary where code can be called from, leave it empty for now
    sources[index] = []

  # add line for after last instruction
  sources[len(program)] = []


# list through all lines to determine source
for index, line in enumerate(program):
  if line[0] == "acc":
    sources[index + 1].append(index)

  elif line[0] == "nop":
    sources[index + 1].append(index)
    
  elif line[0] == "jmp":
    # (index + arg) can be reached from this op
    sources[index + line[1]].append(index)
    
  else:
    exit(1)


# find al terminating ops
history = set()
final = [len(program)]

for index in final:
    if index not in history:
        history.add(index)
        final.extend(sources[index])




pointer = 0
accumulator = 0
fixed = False

# run the program again but keep in mind a nop can 
# become jmp and visa versa
while pointer != len(program):
  op = program[pointer][0]
  arg = program[pointer][1]


  if op == "acc":
    accumulator += int(arg)


  elif op == "jmp":
    if not fixed and (pointer +1) in final:
      print(f'change jmp to nop ({pointer})')
      fixed = True # if fixed don't jump!

    else:
      pointer += int(arg)
      continue

  elif op == "nop":
    if not fixed and (pointer + arg) in final:
      print(f'change nop to jmp ({pointer})')
      pointer += int(arg)
      fixed = True
      continue

  pointer += 1
  
print(accumulator)