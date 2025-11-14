print("Hola apreciado usuario")
cuenta = float(input("¿Valor de la cuenta?"))
propina = int(input("¿Cuál es el porcentaje de propina que desear dejar? 5 10 15 20 "))

total_propina = cuenta * (propina/100)
cuenta = cuenta + total_propina

print(f"El valor de la propina es: {total_propina}")
print(f"El total de la cuenta con propina es: {cuenta}")
