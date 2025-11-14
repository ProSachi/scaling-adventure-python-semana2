""" nombre = "Juan"      # tipo str
edad = 20          # tipo int
estudiante = True    # tipo bool
x, y, z = "Orange", "Banana", "Cherry"

#Conocer el tipo de dato
print(type(nombre), type(edad))
 """

""" 
# 1. Python crea un objeto de tipo 'int' con el valor 10 en la memoria.
# 2. Python crea un nombre 'x'.
# 3. Python "apunta" el nombre 'x' a ese objeto 'int(10)'.
x = 10

# 1. Python busca el objeto al que apunta 'x' (el int(10)).
# 2. Python crea un nuevo nombre 'y'.
# 3. Python "apunta" el nombre 'y' AL MISMO objeto 'int(10)'.
y = x

# 1. Python crea un NUEVO objeto 'int(11)'.
# 2. Python "re-apunta" el nombre 'x' a este nuevo objeto.
# 3. 'y' NO SE VE AFECTADO. Sigue apuntando al 'int(10)' original.
x = 11

print(x) # Imprime 11
print(y) # Imprime 10 """


""" nombre = input("Cual es tu nombre")
print(nombre) """

""" fecha_nacimiento =  int(input("¿Cuál es su fecha de nacimiento?: "))
edad = 2025 - fecha_nacimiento
print(edad) """
""" 
valor = int(input("Escribe un número: "))
doble = valor * 2
print("El doble es:", doble)
 """

# El usuario nos da un texto
edad_texto = input("Dime tu edad: ")
edad = int(edad_texto) # Convertimos (casting) a número

# 1. La condición a evaluar. Usa operadores (==, !=, >, <, >=, <=)
if edad >= 18:
    # 2. El bloque de código indentado (4 espacios)
    #    Se ejecuta SÓLO SI la condición (1) es Verdadera.
    print("Puedes entrar al bar.")

# 3. (Opcional) 'Else If'. Se evalúa SÓLO SI el 'if' (1) fue Falso.
elif edad < 0:
    print("No puedes tener una edad negativa.")

# 4. (Opcional) 'Else'. Se ejecuta SÓLO SI TODAS las
#    condiciones anteriores (if y elif) fueron Falsas.
else:
    print("Eres menor de edad, no puedes entrar.")

# 5. Este código está fuera del bloque. Se ejecuta SIEMPRE.
print("Gracias por usar el verificador.")
