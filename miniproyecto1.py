import random

numeroazar= int(random.randint (1,100)) 
nombrejugador=input("Ingresa tu nombre: ")
intentosrealizados = 0 

print("Bienvenido al juego "+ nombrejugador)

while True:
    numerousuario= int(input("¿Que número crees que es del 1-100 ?: "))
    distancia= abs(numerousuario - numeroazar)
    if numerousuario==0:
        print ("No lo lograste a pesar de tratar ", intentosrealizados , " veces, mas suerte para la próxima vez")
        break

    if numerousuario==numeroazar:
        print("¡Felicitaciones! "+nombrejugador+", Acertaste en", intentosrealizados , "intentos")
        numerousuario==0
        break

    elif distancia < 5:
        print("Sorry" , nombrejugador , "ese no es pero estas a una distancia menor a 5")
        intentosrealizados= intentosrealizados+1

    elif distancia > 5 and distancia < 10:
        print("Sorry", nombrejugador, "ese no es pero estas a una distancia mayor que 5 y menor que 10")
        intentosrealizados= intentosrealizados+1

    elif distancia >10 and distancia < 20:
        print("Sorry", nombrejugador ,"ese no es pero estas a una distancia mayor que 10 y menor que 20")
        intentosrealizados= intentosrealizados+1

    elif distancia > 20:
        print("Sorry", nombrejugador , "ese no es pero estas a una distancia mayor que 20")
        intentosrealizados= intentosrealizados+1
