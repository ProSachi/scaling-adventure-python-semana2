

#while condicion: 
# Bloque de código a ejecutar mientras la condición sea True

contador = 0
while contador < 5:
    
    contador += 1
    if contador % 2 == 0:
        continue
    if contador % 3 == 0:
        break
    print("Contador:", contador)

print("Ciclo 'while' terminado.")
        
    