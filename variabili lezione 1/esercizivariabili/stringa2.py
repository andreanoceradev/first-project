testo = ("Python")
print("primo carattere : " , testo[0])
print("ultimo carattere :" , testo[-1])


testo = "AnDrEa"
print(testo.upper())
print(testo.lower())

testo = "Andrea studia durante il weekend"
lettera = "a"
conteggio = testo.count(lettera)
print(f"la lettera ' {lettera}' compare {conteggio} volte." )

testo = "fantastico"
print(testo.startswith("f"))
print(testo.endswith("o"))

testo = "il lupo perde il pelo ma non il vizio"
print(testo[::-1])

testo = "                          ciao come stai?"
print(testo.strip())




parola = "programmazione"
print(parola[:3]*3)

