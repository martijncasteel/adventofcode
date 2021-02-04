def half(number):
  return int( number / 2 )

# recursive function taking first letter of the string
def parse_letter(boarding_pass, min, max):
  if len(boarding_pass) < 1:
    return min

  letter = boarding_pass[0]

  if letter in ["F", "L"]:
    return parse_letter(boarding_pass[1:], min, min + half(max - min))

  elif letter in ["B", "R"]:
    return parse_letter(boarding_pass[1:], min + half(max - min) + 1, max)

  else:
    exit(1)

seats = []

with open('input', 'r') as file:
  for line in file:
    
    boarding_pass = line.strip()
    row = parse_letter(boarding_pass[:7], 0, 127)
    seat = row * 8 + parse_letter(boarding_pass[7:], 0, 7)

    seats.append(seat)

seats.sort()

# this probably can be done more efficient, but hey it works
for i in range(seats[0], seats[len(seats) - 1]):
  if i not in seats:
    print(i)

exit(0)

    