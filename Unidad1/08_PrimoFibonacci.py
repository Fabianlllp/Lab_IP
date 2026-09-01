numero=int(input("Ingresa un numero: "))
i=2
primo=1
while i < numero:
    if numero%i == 0:
        primo=0
    i=i+1
if primo==0 or numero==1:
    print("No Primo")
elif primo==1:
    print("Primo")
    a=0
    b=1
    while a<numero:
        siguiente = a+b
        a=b
        b=siguiente
    if a==numero:
        print("Esta en Fibonacci")
    else:
        print("No esta en fibonacci")