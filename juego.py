import random

def jugar():
    numero_secreto = random.randint(1, 100)
    adivinado = False
    # Adherido Isuss intentos.
    intentos = 0

    print("¡Bienvenido al  juego del número secreto!")
    print("Adivina el número del 1 al 100")

    while not adivinado:
        intento = int(input("Ingresa un número: "))
        # Adherido Isuss intentos.
        intentos = intentos + 1
        if intento == numero_secreto:
            # Adherido Isuss intenros en print.
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            adivinado = True
        elif intento < numero_secreto:
            print("El número es mayor.")
        else:
            print("El número es menor.")

if __name__ == "__main__":
    jugar()