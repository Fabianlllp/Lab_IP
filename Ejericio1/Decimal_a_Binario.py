Numero = 8
if Numero == 0:
    print(0)
Binario = ""
while Numero>0:
    residuo = Numero%2
    Binario = str(residuo) + Binario
    Numero = Numero//2
print(Binario) 