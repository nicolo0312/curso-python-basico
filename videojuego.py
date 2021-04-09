import random

def run():
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input('Elige un numero: '))
    vidas = 5
    if vidas == 0:
        print('Perdiste, vuelve a intentarlo')
    while numero_elegido != numero_aleatorio :
        if numero_aleatorio > numero_elegido:
            print('Elige un numero mas grande')
            vidas = vidas -1
        else:
            print('Elige un numero mas chico')
        numero_elegido = int(input('Elige otro numero: '))
    print('Felicitaciones, ganaste!')


if __name__ == '__main__':
    run()