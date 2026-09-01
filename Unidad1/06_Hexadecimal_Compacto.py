Numero, hexa = 10, "" #Definimos la variable con el numero a convertir y la variable que contendra el numero convertido
while Numero>0: #inicializamos el ciclo para convertir los valores decimale en hexadecimales
    residuo = Numero%16 #Obtenemos el residuo para cocatenarlo en el resultado final
    if (residuo == 10):residuo = "A" #Convertimos el residuo en A si este es igual a 10
    elif (residuo == 11):residuo = "B" #Convertimos el residuo en A si este es igual a 11
    elif (residuo == 12):residuo = "C" #Convertimos el residuo en B si este es igual a 12
    elif (residuo == 13):residuo = "D" #Convertimos el residuo en C si este es igual a 13
    elif (residuo == 14):residuo = "E" #Convertimos el residuo en D si este es igual a 14
    elif (residuo == 15):residuo = "F" #Convertimos el residuo en E si este es igual a 15
    hexa,Numero = str(residuo) + hexa, Numero//16 #Concatenamos el residuo para formar el numero convertido y dividimos el numero inicial entre la base del sistema numerico
print(hexa) #Imprimimos el numero convertido