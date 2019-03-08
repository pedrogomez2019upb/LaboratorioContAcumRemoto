#Algoritmo que lea un número entero a , lea los numeros y imprima el residuo de su división entre ellos 
#primero nos toca hacer un contador igual a 0 para el for y tambien para la division
i= 0
division = 0
#Recibimos los números a analizar
a=int(input("Bienvenido ! Vamos a revisar la división de a números entre ellos . ¿Cuántos números quieres analizar?: "))
#Ponemos la condicional for para empezar el ejercicio
for i in range (1,a+1):
    x=int(input("Ingresa el valor: "))
    division += a
    division_resultado = division/x


print("La división entre estos números son:{}. Gracias por utilizar el programa.".format(division_resultado)


#Desarrollado por Pedro Gómez / ID:000396221