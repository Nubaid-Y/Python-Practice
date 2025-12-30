import random

computer = random.randint(1,3)

choices = {
    1: "✊",
    2: "✋",
    3: "✌️",
    4: "🦎",
    5: "🖖"
}

print("Welcome to Rock Paper Scissors Lizard Spock!\n1) ✊\n2) ✋\n3) ✌️\n4) 🦎\n5) 🖖")
player = int(input("Pick a number "))

while player <1 or player >5:
    print ("invalid input.")
    player = int(input("Pick a number "))


print(f"You chose {choices[player]}")
print(f"CPU chose {choices[computer]}")

if choices[player] == choices[computer]:
    print("its a tie!")
elif choices[player] == "✊" and choices[computer] == "✌️" or choices[computer] == "🦎":
    print("Player wins!")
elif choices[player] == "✋" and choices[computer] == "✊" or choices[computer] == "🖖":
    print("Player wins!")
elif choices[player] == "✌️" and choices[computer] == "✋" or choices[computer] == "🦎":
    print("Player wins!")
elif choices[player] == "🦎" and choices[computer] == "✋" or choices[computer] == "🖖":
    print("Player wins!")
elif choices[player] == "🖖" and choices[computer] == "✌️" or choices[computer] == "✊":
    print("Player wins!")
else:
    print("CPU wins!")