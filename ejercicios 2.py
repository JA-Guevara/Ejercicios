'''def generar_fibonacci(n):
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

# Solicita al usuario que ingrese la cantidad de números de Fibonacci
cantidad = int(input("Ingresa la cantidad de números Fibonacci: "))
print(f"Los primeros {cantidad} números Fibonacci son: {generar_fibonacci(cantidad)}")'''

def fibonacci(limite):
    a=1
    b=0
    while a<limite:
        yield a
        a,b=b,a+b
     
x = int(input("Ingresa la cantidad de números Fibonacci: "))
print(f"Los primeros {x} números Fibonacci son:")
for num in fibonacci(x):
    print(num)