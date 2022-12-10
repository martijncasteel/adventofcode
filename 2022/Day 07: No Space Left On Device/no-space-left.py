folders = []

class Folder:
  def __init__(self, name, parent):
    self.name = name
    self.parent = parent

    self.folders = []
    
    self.files = []
    self.size = 0

    folders.append(self)

  def create_or_find(name, parent):

    l = [f for f in folders if f.name == name and f.parent == parent]

    if len(l) > 0:
      return l[0]
    
    return Folder(name, parent)

  def add_file(self, name, size):
    self.files.append((name, int(size)))
    self.add_size(int(size))

  def add_size(self, size):
    self.size += size

    if self.name != self.parent.name:
      self.parent.add_size(size)


  def __repr__(self) -> str:
    return f'{self.name} ({self.parent.name}) [{",".join([name for name, _ in self.files])}] size={self.size}'
  


pointer = Folder('/', None)
pointer.parent = pointer

# with open('input.txt') as file:
with open('input.txt') as file:
  for line in file:
    line = line.strip()

    if line == '':
      continue

    # move pointer
    elif line == '$ cd ..':
      if pointer.name != '/':
        pointer = pointer.parent


    # create dir if not present and move
    elif line[:4] == '$ cd':
      p = Folder.create_or_find(line[5:], pointer)
      pointer = p


    # ensure pointer is in correct place
    elif line[0:4] == '$ ls':
      continue


    # list of files and folders
    else:
      type, name = line.split(' ', 2)

      if type == 'dir': # TODO probably folders with same name
        p = Folder.create_or_find(name, pointer)
        pointer.folders.append(p)

      else:
        pointer.add_file(name, type)



size = 0
for folder in folders:
  if(folder.size <= 100000):
    size += folder.size

print('part 1:', size)


folders.sort(key=lambda f: f.size)

total_space = 70000000
update_size = 30000000
used_space = folders[-1].size
free_space = total_space - used_space
space_needed = update_size - free_space

print(space_needed)

for folder in folders:
  # print(folder)
  if folder.size >= space_needed:
    print('part 2:', folder.name, space_needed)
    exit(0)