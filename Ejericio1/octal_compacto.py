Numero,octal = 8, ""  #Definimos la variable con el numero a convertir y la variable octal como una cadena vacía
if Numero == 0:print(0) #Descartamos el resultado en caso que el número a convertir sea 0, imprimiendo 0 automáticamente
while Numero>0: octal,Numero = str(Numero%8) + octal, Numero//8 #Definimos el ciclo que extraerá el módulo de 8 del numero a convertir y lo concatenará a la variable octal del lado izquierdo, para despúes dividir el numero entre 8 hasta que sea menor que 0
print(octal) #Imprimimos el resultado