numero=int(input("Ingresa un numero: "))
i=2
primo=1
while i < numero:
    if numero%i == 0:
        primo=0
        break
    i=i+1
if primo==0:
    print("No Primo")
if primo==1:
    print("Primo")