frase = input("Scrivi una frase: " )
frase_invertita = " ".join(frase.split()[::-1])
print("frase invertita :", frase_invertita)
frase_pulita = frase.replace("","").lower()
print("è un palindromo?", frase_pulita ==frase_pulita[::-1])


