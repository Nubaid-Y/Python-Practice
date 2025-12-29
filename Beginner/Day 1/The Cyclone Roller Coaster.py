height = int(input("What is your height in centimeters?"))

credit = int(input("How many credits do you have?"))

if height >= 137 and credit >= 10:
  print("Enjoy the ride!")
elif height >= 137:
  print("You dont have enough credits.")
elif credit >= 10:
  print("You are not tall enough to ride.")
else:
  print("You havent met either requirement")