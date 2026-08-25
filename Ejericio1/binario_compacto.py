Numero,Binario=8,"" #Definimos la variable con el numero a convertir y la variable Binario como una cadena vacía
if Numero == 0:print(0) #Descartamos el resultado en caso que el número a convertir sea 0, imprimiendo 0 automáticamente
while Numero>0: Binario,Numero = str(Numero%2) + Binario, Numero//2 #Definimos el ciclo que extraerá el módulo de 2 del numero a convertir y lo concatenará a la variable Binario del lado izquierdo, para despúes dividir el numero entre 2 hasta que sea menor que 0 
print(Binario) #Imprimimos el resultado