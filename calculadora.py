def add(a,b):
    return a+b

def substract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def es_primo(a):
    if a <= 1:
        return False
    i = 2
    while i * i <= a:
        if a % i == 0:
            return False
        i += 1
    return True

def factorial(a):
    factorial = 1
    i = 1
    while i <= a:
        factorial *= i
        i += 1
    return factorial

def fibonacci(n):
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci



def calculator():
    while True:
        print("0. Salir")
        print("Seleccione una operación")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5.Es_primo")
        print("6.Factorial")
        print("7.Fibonacci")
      
        option = input("Ingrese su opción (0,1,2,3,4,5,6,7,8,9): ")

        if option == "0":
            print("Saliendo de la calculadora")
            break

        if option in ["1","2","3","4"]:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))

            if option == "1":
                print("La suma es:", add(num1, num2))
            elif option == "2":
                print("La resta es:", substract(num1, num2))
            elif option == "3":
                print("La división es:", divide(num1, num2))
            elif option == "4":
                print("La multiplicación es:", multiply(num1, num2))
    
        if option in ["5","6","7"]:
            num1 = float(input("Ingrese el valor : "))

            if option == "5":
                 if es_primo(num1):
                        print(f"{num1} es un número primo.")
                 else:
                        print(f"{num1} no es un número primo.") 
            elif option == "6":
                print("El factorial es:", factorial(num1))
            elif option == "7":
                print(f"Los primeros {num1} terminos de la serie fibonacci son:", fibonacci(num1))


    else:
        print("Opción no válida, por intenta de nuevo")

calculator()        