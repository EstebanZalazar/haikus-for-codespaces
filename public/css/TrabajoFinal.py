from matplotlib import pyplot

def Menu():
    while True:
        print("\n1) Juego piedra, papel o tijeras")
        print("2) Tirar un dado")
        print("3) Adivinar un numero contra la pc")
        print("4) Crea una función")
        print("5) salir")
        opcion=input("Op: ")
        if opcion == '1':
            PPT()
        elif opcion == '2':
            TD()
        elif opcion == '3':
            AN()
        elif opcion == '4':
            GF()
        elif opcion == '5':
            break
        else:
            print("Comnado desconocido, elija una de las opciones mostradas")

def PPT():
    import random

    while True:
        print("\n")
        aleatorio = random.randrange(1,4)
        elijePc = ""
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijera")
        opcion = int(input("Elije tu opcion: "))

        if opcion == 1:
            elijeUsuario = "Piedra"
        elif opcion == 2:
            elijeUsuario = "Papel"
        elif opcion == 3:
            elijeUsuario = "Tijera"
        print("Elejiste: ",elijeUsuario)

        if aleatorio == 1:
            elijePc = "Piedra"
        elif aleatorio == 2:
            elijePc = "Papel"
        elif aleatorio == 3:
            elijePc = "Tijera"
        print("La maquina elijió: ",elijePc)
        print("...")
        if elijePc == "Piedra" and elijeUsuario == "Papel":
            print("Ganaste, papel envuelve piedra\n")
        elif elijePc == "Papel" and elijeUsuario == "Tijera":
            print("Ganaste, tijera corta papel\n")
        elif elijePc == "Tijera" and elijeUsuario == "Piedra":
            print("Ganaste, piedra rompe tijera\n")
        if elijePc == "Papel" and elijeUsuario == "Piedra":
            print("Perdiste, papel envuelve piedra\n")
        elif elijePc == "Tijera" and elijeUsuario == "Papel":
            print("Perdiste, tijera corta papel\n")
        elif elijePc == "Piedra" and elijeUsuario == "Tijera":
            print("Perdiste, piedra rompe tijera\n")
        elif elijePc == elijeUsuario:
            print("Empate\n")
    
        play_again = input("Quieres jugar de nuevo? (s/n): ")
        if play_again.lower() != "s":
            break

def TD():
    from random import randint
    repetir_tirada = True
    while repetir_tirada:
        print("\nTu tirada fue: ",randint(1,6))
        repetir_tirada = input("Quieres tirar los dados de nuevo? (s/n): ")
        if repetir_tirada.lower() != "s":
            break

def AN():
    import random

    adivinar_numero = True

    while adivinar_numero:
        intentos = 1
        aleatorio = random.randint(1,100)
        while intentos <= 10:
            num_usuario = int(input("\nIngrese un numero entre el 1 y el 100: "))
            if num_usuario == aleatorio:
                print("\nFelicitaciones, has adivinado el numero en",intentos,"intentos")
                break
            elif num_usuario > aleatorio:
                print("El numero ingresado es mayor al numero aletorio")
                intentos += 1
            elif num_usuario < aleatorio:
                print("El numero ingresado es menor al numero aleatorio")
                intentos += 1
        if intentos > 10:
            print("\nTe has quedado sin intentos")
        adivinar_numero = input("Quieres intentarlo de nuevo? (s/n): ")
        if adivinar_numero.lower() != "s":
            break

def f(x):
    return 2*(x**2)+5*x-2

def GF():
    print("\nA continuacion se graficara una funcion cuadratica\n")
    
    x=range(-10,15)
    pyplot.plot(x,[f(i) for i in x])
    pyplot.xlim(-10,10)
    pyplot.ylim(-10,10)
    pyplot.savefig("2x^2+5x-2.png")
    pyplot.show()

print("Bienvenido al Menu del TP integrador\n")
Menu()