frase = input("Andrea sta imparando l uso delle stringhe")

frase_invertita = " ".join(frase.split()[::-1])
print("frase_inverita")

frase_pulita = frase.raplace(" ", "").lower()
print(frase_pulita ==frase_pulita[::-1])

