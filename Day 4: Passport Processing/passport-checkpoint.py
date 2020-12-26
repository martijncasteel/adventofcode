class Document:
  def __init__(self):
    self.byr = None
    self.iyr = None
    self.eyr = None
    self.hgt = None
    self.hcl = None
    self.ecl = None
    self.pid = None
    self.cid = None

  def is_valid(self):
    return self.byr is not None and self.iyr is not None and self.eyr is not None and self.hgt is not None and self.hcl is not None and self.ecl is not None and self.pid is not None

  def __repr__(self):
    return "byr:{}\niyr:{}\neyr:{}\nhgt:{}\nhcl:{}\necl:{}\npid:{}\ncid:{}\n".format(self.byr, self.iyr, self.eyr, self.hgt, self.hcl, self.ecl, self.pid, self.cid)

doc = Document()
correct = 0

with open('input', 'r') as file:
  for line in file:
    
    # if line was empty
    if line.strip() == "":
      
      #check if valid
      if doc.is_valid():
        correct += 1

      doc = Document()
      continue

    for pair in line.strip().split(' '):
      key, value = pair.split(':')
      setattr(doc, key.lower(), value.strip())

  #check if valid
  if doc.is_valid():
    correct += 1

print(correct)
exit(0)
