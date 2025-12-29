import random
num = random.randint(1, 9)

question = input("Question:")

M8BallText = ("Magic 8 Ball:  ")

if num == 1:
  print(M8BallText, "Yes - definitely.")
elif num == 2:
  print(M8BallText, "It is decidedly so.")
elif num == 3:
  print(M8BallText, "Without a doubt.")
elif num == 4:
  print(M8BallText, "Reply hazy, try again.")
elif num == 5:
  print(M8BallText, "Ask again later.")
elif num == 6:
  print(M8BallText, "Better not tell you now.")
elif num == 7:
  print(M8BallText, "My sources say no.")
elif num == 8:
  print(M8BallText, "Outlook not so good.")
else:
  print(M8BallText, "Very doubtful.")