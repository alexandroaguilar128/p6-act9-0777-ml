# Alexandro Aguialr NC = 0007
# Ejemplos de variables

print("+-+-+-+-+-+ Variables +-+-+-+-+")

x = 5
y = "John"
print(type(x))
print(type(y))

a = 4
A = "Sally"
#A no sobreescribe a

x = str(3)    # x sera '3'
y = int(3)    # y sera 3
z = float(3)  # z sera 3.0

print("+-+-+-+-+-+-+-+ Variables multiples +-+-+-+-+-+-+-+")

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

print("+-+-+-+-+-+-+-+ Data types +-+-+-+-+-+-+-+")

x = float(20.5)

x = int(20)

x = str("Hello World")

print("+-+-+-+-+-+-+-+ Operadores aritmeticos  +-+-+-+-+-+-+-+")

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

x = 12
y = 5

print(x / y)

x = 12
y = 5

print(x // y)

print("+-+-+-+-+-+-+-+ Operadores comparativos  +-+-+-+-+-+-+-+")

x = 10
y = 10
print(x == y)  # Devuelve True

edad = 20
print(edad > 18)  # Devuelve True

clave_ingresada = "1234"
clave_correcta = "abcd"
print(clave_ingresada != clave_correcta)  # Devuelve True

print("+-+-+-+-+-+-+-+ Operadores logicos  +-+-+-+-+-+-+-+")
edad = 25
tiene_licencia = True
print(edad >= 18 and tiene_licencia)  # Devuelve True

es_fin_de_semana = False
es_feriado = True
print(es_fin_de_semana or es_feriado)  # Devuelve True

usuario_bloqueado = False
print(not usuario_bloqueado)  # Devuelve True

print("Programa realizado por Alexandro Aguilar NC = 0007")