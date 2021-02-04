import re, regex

rules = {}

# for this one I needed some help and fount it on the internet
# at first I was planning to compute all possible allowed messages
# however I couldn't get my head around it.
#
# So I looked around and learned a few things, such as nested functions
# and once again the power of regular expressions.
def unpack_rules(rule):

  def expand(value):
    if not value.isdigit(): 
      return value

    # build a regular expression string from the rules
    return "(?:" + "".join(map(expand, rules[value].split())) + ")"

  # print('^' + expand(rule) + '$')
  return '^' + expand(rule) + '$'
      
with open('input', 'r') as file:
  input, messages = file.read().split('\n\n')

  # list all rules in a dict, then start with 0 and find valid_messages
  rules = {line.split(': ')[0]: line.split(': ')[1].strip('"') for line in input.splitlines()}
  pattern = re.compile(unpack_rules('0'))

  valid_messages = 0
  for message in messages.splitlines():
    if pattern.match(message):
      valid_messages += 1

  print(valid_messages)

  # part two add, two new rules
  rules["8"] = "42 +"
  rules["11"] = "(?P<R> 42 (?&R)? 31 )"

  # unfortunately re does not support recursive methods 
  pattern = regex.compile(unpack_rules('0'))

  valid_messages = 0
  for message in messages.splitlines():
    if pattern.match(message):
      valid_messages += 1

  print(valid_messages)
    
    


