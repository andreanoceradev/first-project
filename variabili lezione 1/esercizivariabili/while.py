numero = int(input("inserisci un numero positivo"))
while numero <= 0:
    numero = int(input("numero non valido. inserisci un numero positivo:"))
    print(f"hai inserito il numero positivo:{numero}")