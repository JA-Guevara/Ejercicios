jugador1 = input("Ingresa tu opción: ")
jugador2 = input("Ingresa tu opción: ")
valores = ['Piedra', 'Papel', 'Tijera']

if jugador1 not in valores or jugador2 not in valores:
    print('No ingresaron el valor correcto')
else:
    if (jugador1 == 'Piedra' and jugador2 == 'Tijera') or \
       (jugador1 == 'Tijera' and jugador2 == 'Papel') or \
       (jugador1 == 'Papel' and jugador2 == 'Piedra'):
        print("El ganador es el jugador 1")
    elif jugador1 == jugador2:
        print("Empate")
    else:
        print("El ganador es el jugador 2")
