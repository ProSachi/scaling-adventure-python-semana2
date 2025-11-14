numero = int(input("Ingresa un número entero: "))

if numero > 0 and numero % 5==0:
    print("El número es positivo y múltiplo de 5")
elif numero > 0 and numero % 5!=0:
    print("El número es positivo y pero no múltiplo de 5")
elif numero < 0 and numero % 2 ==0:
    print("El número es negativo y par")
elif numero < 0 and numero % 2 !=0:
    print("El número es negativo e impar")
else :
    print("El número es cero")

