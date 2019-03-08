#Crear un algorito que permita revisar si a es divisible entre b
#Primero damos un mensaje de bienvenida y recibimos el primer valor y segundo
x=int(input("Bienvenido! Vamos a ver si un número es exactamente divisible entre otro. Por favor ingresa el primer valor: "))
y=int(input("Por favor ingresa el segundo valor: "))
#Ponemos un if para poner la condicional
if x%y==0 :
    print("El número se divide exactamente.")
else:
    print("El número no se divide exactamente.")
#Desarrollado por Pedro Gómez / ID:000396221