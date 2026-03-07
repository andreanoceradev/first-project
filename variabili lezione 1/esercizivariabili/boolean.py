# verificare se un numero é positivo

x = 10
risultato =  x > 0
print(risultato)


# verificare se sono uguali

s1 = " ciao Andrea "
s2 = " ciao Andrea "
print (s1 == s2)

# verificare se due numeri sono contenute in variabili a , b sono positivi

a = 5
b = 10
risultato = (a>0) and (b>0)
print(risultato)

età = input("inserisci la tua età") 
patente = input("hai la patente? (si/no)")
età =int(età)
puo_guidare = età >= 18 and patente == "si"
print(puo_guidare)


ritardobiblioteca = input("sei in ritardo? (si/no)")
premium = input("hai accesso premium? (si/no)")
puo_entrare = ritardobiblioteca == "no" or premium == "si"
print(puo_entrare)