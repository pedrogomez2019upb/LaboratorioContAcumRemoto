#Ciclo for dentro de otro ciclo for
#Mensaje de bienvenida al programa
print("Bienvenido! Vamos a imprimir una secuencia 1.1|1.2|...")
#Se crea la condicional for para el primer digito
for x in range (1,4):
    #Después hacemos un for para los decimales solamente sumandole un número más
    for y in range (1,5):
        print (x,y)
#Desarrollado por Pedro Gómez / ID:000396221