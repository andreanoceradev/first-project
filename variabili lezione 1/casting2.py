n_int = 8
n_float = float(n_int)
print(n_int, n_float)



n_float = 3.5
n_int = int(n_float)
print(n_int)



n_str = "123"
n_int = int(n_str)
print(n_int)


num_str = "3.14"
num_float = float(num_str)
print(num_float)


n_str = "ciao Andrea"

try:
    num_int =int(n_str)

except ValueError:
    print("non si puo convertire ciao Andrea in intero")   
