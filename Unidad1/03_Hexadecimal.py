Numero = 10
hexa = ""
if Numero == 0:
    print(0)
while Numero>0:
    residuo = Numero%16
    if (residuo == 10):
        residuo = "A"
    elif (residuo == 11):
        residuo = "B"
    elif (residuo == 12):
        residuo = "C"
    elif (residuo == 13):
        residuo = "D"
    elif (residuo == 14):
        residuo = "E"
    elif (residuo == 15):
        residuo = "F"
    hexa = str(residuo) + hexa
    Numero = Numero//16
print(hexa)