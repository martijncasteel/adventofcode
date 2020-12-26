def half(number):
  return int( number / 2 )

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

highest_seat = 0

with open('input', 'r') as file:
  for line in file:
    
    boarding_pass = line.strip()
    row = parse_letter(boarding_pass[:7], 0, 127)
    seat = row * 8 + parse_letter(boarding_pass[7:], 0, 7)

    if seat > highest_seat:
      highest_seat = seat

print(highest_seat)
exit(0)

    