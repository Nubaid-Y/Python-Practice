secretmessage = 'This is a secret message'
unsentmessage = 'Message has been unsent'

with open("SecretMesasge.txt", "w") as file:
    file.write(secretmessage)

with open("SecretMesasge.txt", "r+") as file:
    originalmessage = file.read()
    file.seek(0)
    file.write(unsentmessage)
    file.truncate()

print('Original text:' + originalmessage)

print('Now:')
with open("SecretMesasge.txt", "r") as file:
    print(file.read())