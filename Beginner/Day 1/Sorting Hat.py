import math
Gryffindor = (0)
Ravenclaw = (0)
Hufflepuff = (0)
Slytherin = (0)

Q1 = int(input("Q1) Do you like Dawn or Dusk?\n1) Dawn\n2) Dusk\n"))

if Q1 == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif Q1 == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print("Wrong input")

Q2 = int(input("Q2) When I’m dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\n"))

if Q2 == 1:
  Hufflepuff += 2
elif Q2 == 2:
  Slytherin += 2
elif Q2 == 3:
  Ravenclaw += 2
elif Q2 == 4:
  Ravenclaw += 2
else:
  print("Wrong input")

Q3 = int(input("Q3) Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\n"))

if Q3 == 1:
  Slytherin += 4
elif Q3 == 2:
  Hufflepuff += 4
elif Q3 == 3:
  Ravenclaw += 4
elif Q3 == 4:
  Gryffindor += 4
else:
  print("Wrong input")


print(Gryffindor)
print(Ravenclaw)
print(Hufflepuff)
print(Slytherin)
