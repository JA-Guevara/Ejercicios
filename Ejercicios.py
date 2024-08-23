'''def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Solicita al usuario que ingrese un número
numero = int(input("Ingresa un número: "))
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")'''

def es_primo(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# Solicita al usuario ingresar un número
n = int(input('Ingrese un número: '))

# Verifica si el número es primo y muestra el resultado
if es_primo(n):
    print(f"{n} es un número primo.")
else:
    print(f"{n} no es un número primo.")