nombre = input("¿Cómo te llamas?")
print(f"Hola {nombre} ¿Cómo estas?")
edad = int(input("¿Cuántos años tienes?"))
if edad>=18:
    print("Eres mayor de edad")
elif edad >= 0 and edad < 18 :
    print("Eres menor de edad")
else:
    print("Error al ingresar la edad")