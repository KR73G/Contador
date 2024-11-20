#Ciclo while 

contador = 1

while contador <= 10:
    if contador % 2 == 0:
        print(f"{contador} es un número par")
    else:
        print(f"{contador} es un número impar")
    contador += 1  # Incrementa el contador en 1

#Ciclo do while

contador = 1

while True:
    print(contador)
    contador += 1  # Incrementa el contador en 1
    
    # Condición de salida
    if contador > 10:
        break

#Ciclo for

for i in range(3):
    print(i)

