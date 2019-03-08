#Algoritmo que lea un número entero a , lea los numeros y imprima el residuo de su división entre ellos 
#primero nos toca hacer un contador igual a 0 para el for
y= 0
#Recibimos los números a analizar
a=int(input("Bienvenido !  Ingresa el número: "))
#Ponemos la condicional for para empezar el ejercicio
for i in range (1,a+1,1):
    if a % i  ==0:
        y = y +1
#Para saber si es primo utilzamos un if then después del for
if y > 2:
        print("El número {} no es primo . Gracias por utilizar el programa.".format(y))
else:
        print("El número {} es primo. Gracas por utilizar el programa.".format(y))
#Desarrollado por Pedro Gómez / ID:000396221