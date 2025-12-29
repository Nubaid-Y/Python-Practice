pesos = int(input("What do you have left in pesos?"))
soles = int(input("What do you have left in soles?"))
reais = int(input("What do you have left in reais?"))

USD1 = pesos*0.00027
USD2 = soles*0.30
USD3 = reais*0.18

RealUSD = USD1 + USD2 + USD3

print(RealUSD)