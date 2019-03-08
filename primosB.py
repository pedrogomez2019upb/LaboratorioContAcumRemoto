#Algoritmo que lea un número entero a , lea los numeros y imprima el residuo de su división entre ellos (while)
#Se crean los contadores necesarios
i=0
y=0
#Recibimos los números a analizar
a=int(input("Bienvenido !  Ingresa el número: "))
#Ponemos la condicional for para empezar el ejercicio
while i <= a :
    i= i +1
    if a % i  ==0:
        y = y +1
#Para saber si es primo utilzamos un if then después del for
if y > 2:
        print("El número {} no es primo . Gracias por utilizar el programa.".format(a))
else:
        print("El número {} es primo. Gracas por utilizar el programa.".format(a))
#Desarrollado por Pedro Gómez / ID:000396221