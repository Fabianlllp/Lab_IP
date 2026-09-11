total=float(input("Introduce el total de la cuenta: "))
porPropina=float(input("Introduce el porcentaje de propina: "))
personas=int(input("Introduce el numero de personas :"))
propina = (total*porPropina)/100
pagoTotal= total+propina
pagoIndividual = pagoTotal/personas
print(f"El total de la propina es: {propina:.2f}")
print(f"El monto por perosna es: {pagoIndividual:.2f}")
print(f"El monto total es: {pagoTotal:.2f}")