'''numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    print("Aquí i es igual a:",i+1)

for i in range(3,10):
    print(i)

fruits = ["Manzana", "Pera", "Uva", "Naranja", "Tomate"]
for fruit in fruits:
    print(fruit)
    if fruit == "Naranja":
        print("Naranja encontrada")

x = 0
while x<5:
    if x ==3:
        break
    print(x) 
    x +=1

numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    if i ==3:
        break
    print("Aquí i es igual a:",i)'''

x=int(input("insertar el numero:"))
factorial = 1
i=1
while i <= x:
    factorial *= i
    i += 1

print("El factorial es:", factorial)

x=int(input("insertar el numero:"))
factorial = 1
for i in range(1, x + 1):
    factorial *= i
    
print("El factorial es:", factorial)