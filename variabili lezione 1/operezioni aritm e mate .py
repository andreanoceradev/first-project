a = 15
b = 4
print ("somma :" ,a + b)
print ("differenza :" ,a - b )
print ("prodotto:" ,a * b)
print ("divisione:" ,a / b)



import math
x = -8.5
print ( "floor :" , math.floor(x))
print ( "trunc :" , math.trunc(x))
print ( "ceil : ", math.ceil (x))
print ( "fabs :", math.fabs(x))


euro = int(input("Quanti euro hai ?"))
prezzo =int(input("Quanto costa un singolo oggetto?"))
unita = euro // prezzo
resto = euro % prezzo 
print ("puoi comprare", unita , "oggetti")
print( "ti restano",resto ," euro ")