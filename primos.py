#Algoritmo que lea un número entero a , lea los numeros y imprima el residuo de su división entre ellos 
#primero nos toca hacer un contador igual a 0 para el for
y= 0
#Recibimos los números a analizar
a=int(input("Bienvenido ! Vamos a revisar la división de a números entre ellos . ¿Cuan número quieres analizar?: "))
#Ponemos la condicional for para empezar el ejercicio
for i in range (1,a+1,1):
    if a % i  ==0:
        y = y +1
print("La división entre estos números son: {}. Gracias por utilizar el programa.".format(y))
#Desarrollado por Pedro Gómez / ID:000396221