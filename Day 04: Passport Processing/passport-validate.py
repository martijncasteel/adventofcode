import re

hex_pattern = re.compile(r'#[0-9a-f]{6}')
pid_pattern = re.compile(r'\d{9}')

def is_number(string):
  try: 
    int(string)
    return True
  except ValueError:
    print(string)
    return False

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
    # check for presence
    if self.byr is not None and self.iyr is not None and self.eyr is not None and self.hgt is not None and self.hcl is not None and self.ecl is not None and self.pid is not None:

      # byr (Birth Year) - four digits; at least 1920 and at most 2002.
      # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
      # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
      # hgt (Height) - a number followed by either cm or in:
      # If cm, the number must be at least 150 and at most 193.
      # If in, the number must be at least 59 and at most 76.
      # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
      # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
      # pid (Passport ID) - a nine-digit number, including leading zeroes.
      # cid (Country ID) - ignored, missing or not.

      if is_number(self.byr):
        if int(self.byr) < 1920 or int(self.byr) > 2002:
          return False

      if is_number(self.iyr):
        if int(self.iyr) < 2010 or int(self.iyr) > 2020:
          return False

      if is_number(self.eyr):
        if int(self.eyr) < 2020 or int(self.eyr) > 2030:
          return False

      if self.hgt.endswith('cm'):
        if int(self.hgt[:-2]) < 150 or int(self.hgt[:-2]) > 193:
          return False
      elif self.hgt.endswith("in"):
        if int(self.hgt[:-2]) < 59 or int(self.hgt[:-2]) > 76:
          return False
      else:
        return False

      if not hex_pattern.fullmatch(self.hcl):
        return False
       
      if self.ecl not in ["amb","blu","brn","gry","grn","hzl","oth"]:
        return False

      if not pid_pattern.fullmatch(self.pid):
        return False

      # print(self)
      return True
    return False

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
