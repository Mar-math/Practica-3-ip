# ==========================================================
# PARTE 1: PROGRAMAS QUE MUESTRAN NUMEROS
# ==========================================================

# ==========================================================
# EJERCICIO 1:
#a) Hacer un programa que muestre, mediante un ciclo, los primeros 5 números naturales
#(1, 2, 3, 4 y 5).
#b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
#primeros n números naturales (1, 2, · · · , n).
# ==========================================================

#a)CON WHILE

inicio=1
fin=5
numero=inicio
while numero<=fin:
    print(numero, end="-")
    numero=numero+1
print("fin")

#a)CON FOR

for i in range (1,6,1): #inicio en 1, fin en 6 porque es uno menos y va de uno en uno
    print(i, end="-")
print("Fin")

#b)CON WHILE

inicio=1
n=int(input("Ingrese un numero natural:"))
numero=inicio
while numero<=n:
    print(numero, end="-")
    numero=numero+1
print("fin")

#b)CON FOR

n=int(input("Ingrese un nro natural:"))
for n in range (1,n+1,1):
    print(n, end="-")
print ("Fin")

# ==========================================================
# EJERCICIO 2:
#a) Hacer un programa que muestre, mediante un ciclo, los números desde el 4 hasta el
#7 (4, 5, 6 y 7).
#b) Hacer un programa que permita al usuario elegir un número m y un n y luego
#muestre todos los naturales entre m y n (m, m + 1, m + 2, · · · , n − 1, n). ¾Qué pasa
#si n es menor que m?
# ==========================================================

#a)CON WHILE
inicio=4
fin=7
numero=inicio
while numero<=fin:
    print(numero, end="-")
    numero=numero+1
print("fin")

#a)CON FOR

for i in range(4,8,1):
    print(i, end="-")
print("Fin")

#b)CON WHILE

inicio=int(input("Ingrese el inicio"))
fin=int(input("Ingrese el fin:"))
numero=inicio
while numero<=fin:
    print(numero, end="-")
    numero=numero+1
print("fin")
#Si n es menor que m no entra al ciclo y muestra fin

#b)CON FOR

n=int(input("ingrese el inicio:"))
m=int(input("ingrese el fin:"))
for i in range (n, m+1, 1):
    print(i)
print("Fin")

# ==========================================================
# EJERCICIO 3:
#a) Hacer un programa que muestre, mediante un ciclo, los 5 números naturales que le
#siguen al 10 (11, 12, · · · , 15).
#b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
#5 números naturales que le siguen a n (n + 1, n + 2, · · · , n + 5).
#c) Hacer un programa que permita al usuario elegir un número n y un número c, y
#luego muestre los c números naturales que le siguen a n (n + 1, n + 2, · · · , n + c).
# ==========================================================

#a)CON WHILE
inicio=10
fin=10+5
numero=inicio
while numero<=fin:
    print(numero, end="-")
    numero=numero+1
print("fin")

#b)CON FOR
for i in range (10,16,1):
    print(i, end="-")
print("Fin")

#b)CON WHILE

n=int(input("ingrese un numero:"))
fin=n+5
numero=n
while numero<=fin:
    print(numero, end="-")
    numero=numero+1
print("fin")

#b)CON FOR
n=int(input("ingrese un numero:"))
for i in range(n, n+6,1):
    print(i, end="-")
print("Fin")

#c)CON WHILE
n = int(input("Ingrese un número: "))
c = int(input("Ingrese cantidad de números a mostrar: "))
cont = 1
while cont <= c:
    print(n + cont, end="-")
    cont = cont + 1
print("Fin")

#c)CON FOR
n = int(input("Ingrese un número: "))
c = int(input("Ingrese cantidad de números a mostrar: "))
for i in range(n, n+(c+1), 1):
    print(i, end="-")
print("Fin")

# ==========================================================
#EJERCICIO 4:
#a) Hacer un programa que muestre, mediante un ciclo, los números desde el 5 hasta el
#11 salteando de a 2 elementos (5, 7, 9 y 11)
#b) Hacer un programa que permita al usuario elegir un número m y un n y luego
#muestre todos los naturales entre m y n, pero salteando de a 3. Por ejemplo, si el
#usuario ingresara un n igual a 2 y un m igual a 14, el programa deberá mostrar
#2, 5, 8, 11, 14.
#c) Hacer un programa que permita al usuario elegir un número n, un m y un p y
#luego muestre todos los naturales entre m y n, pero salteando de a p números. Por
#ejemplo, si el usuario ingresara un n igual a 2 y un m igual a 14, y un p igual a 4,
#el programa deberá mostrar 2, 6, 10, 14.
# ==========================================================

#a)CON WHILE

inicio=5
fin=11
numero=inicio
while numero<=fin:
    print(numero, end="-")
    numero=numero+2
print("fin")

#a)CON FOR
for i in range(5,12,2):
    print(i, end="-")

#b)CON WHILE

inicio=int(input("Ingrese un nro:"))
fin=int(input("Ingrese otro nro:"))
numero=inicio
while numero<=fin:
    print(numero, end="-")
    numero=numero+3
print("fin")

#b) CON FOR

inicio=int(input("Ingrese un nro:"))
fin=int(input("Ingrese otro nro:"))
for i in range(inicio, fin+1, 3):
    print(i, end="-")
print("fin")

#c) CON WHILE

inicio=int(input("Ingrese un nro:"))
fin=int(input("Ingrese otro nro:"))
p=int(input("ingrese cada cuanto el salto:"))
numero=inicio
while numero<=fin:
    print(numero, end="-")
    numero=numero+p
print("fin")

#C) CON FOR 

inicio=int(input("Ingrese un nro:"))
fin=int(input("Ingrese otro nro:"))
p=int(input("ingrese cada cuanto el salto:"))
for i in range(inicio, fin+1,p):
    print(i, end="-")
print("fin")

# ==========================================================
#EJERCICIO 5:
#a) Hacer un programa que muestre, mediante un ciclo, los números desde el 8 hasta el
#3 (8, 7, 6, 5, 4, 3).
# ==========================================================

#a)CON WHILE

inicio=8
fin=3
numero=inicio
while numero>=fin:
    print(numero, end="-")
    numero=numero-1
print("fin")

#a)CON FOR

for i in range(8,3-1, -1):
    print(i, end="-")
print("fin")

# =========================================================
#EJERCICIO 6:
#a) Hacer un programa que muestre, mediante un ciclo, los números desde el 15 hasta
#el 6 pero salteando de a tres (15, 12, 9, 6).
# ==========================================================

#a)CON WHILE

inicio=15
fin=6
numero=inicio
while numero>=fin:
    print(numero, end="-")
    numero=numero-3
print("fin")

#a)CON FOR 

for i in range(15, 6-1, -3):
    print(i, end="-")
print("fin")

# ==========================================================
#EJERCICIO 7:
#Hacer todos los ejercicios anteriores de nuevo, pero esta vez utilizando la sentencia while en
#lugar de for. De haberlos hecho con while, rehacerlos utilizando for.
# ==========================================================
#LISTORTI

# ==========================================================
#EJERCICIO 8:
#a) Hacer un programa que reciba un número n y muestre todas las potencias de 2
#menores a n. Por ejemplo, si el usuario ingresa 20, el programa mostrará: 1 2 4 8
#16. Ayuda: pensar primero si sería más práctico utilizar la sentencia while o for.
#b) Hacer un programa que reciba un número n (n > 0) y muestre las n primeras
#potencias de 2. Por ejemplo, si el usuario ingresa 6, el programa mostrará: 1 2 4 8
#16 32.
#c) Hacer un programa que reciba un número n (n > 0) y muestre las n primeras
#potencias de n. Por ejemplo, si el usuario ingresa 4, el programa mostrará: 1 4 27
#256. Es decir, 1
#1 2
#2 3
#3 4
#4
# ==========================================================

#a) CON WHILE
n=int(input("Ingrese un nro:"))
m=1
while m**2<n:
    print(m**2)
    m=m+1

#a)CON FOR 

n=int(input("Ingrese un nro:"))
for i in range(1, int((n**2))+1):
    print(i, end="-")

#b) CON WHILE

n=int(input("Ingrese un nro:"))
m=0
while m<n:
    print(2**m, end="-")
    m=m+1

#c)
n=int(input("Ingrese un nro:"))
m=0
while m<n:
    print(n**m, end="-")
    m=m+1

# ==========================================================
#EJERCICIO 9:
#) Hacer un programa que permita al usuario elegir un número positivo n y luego
#muestre en pantalla todos los divisores de n.
#b) Hacer un programa que permita al usuario elegir un número positivo n y luego
#muestre en pantalla todos los divisores pares de n.
#c) Hacer un programa que permita al usuario elegir un número positivo n y luego
#muestre en pantalla la cantidad de divisores de n.
#d) Hacer un programa que permita al usuario elegir un número positivo n y luego
#muestre en pantalla la suma de los divisores de n.
#e) Hacer un programa que permita al usuario elegir dos números positivos c y n y luego
#muestre en pantalla los primeros c divisores de n.
#f) Hacer un programa que permita al usuario elegir dos números positivos c y n y luego
#muestre en pantalla los últimos c divisores de n.
# ==========================================================

#a)Divisores de n

n=int(input("Ingrese un nro: "))
print( f"los divisores de {n} son")
for i in range(1,n+1):
    if n%i==0:
        print(i, end="-")

#b)Divisores de n pares

n=int(input("Ingrese un nro: "))
print( f"los divisores de {n} son")
for i in range(1,n+1):
    if n%i==0 and i%2==0:
        print(i, end="-")

#c)Cantidad de divisores

n=int(input("Ingrese un nro: "))
print( f"la cantidad de divisores de {n} es:")
cantDivisores=0
for i in range(1,n+1):
    if n%i==0:
        cantDivisores=cantDivisores+1
print(cantDivisores)
        
#d)Suma de los divisores de n

n=int(input("Ingrese un nro positivo:"))
print(f"la suma de los divisores de {n} es:")
sumaDivisores=0
for i in range(1, n+1):
    if n%%i==0:
        sumaDivisores=sumaDivisores+i
print(sumaDivisores)


# ==========================================================
#EJERCICIO 10:

# ==========================================================

# ==========================================================
#EJERCICIO 11:

# ==========================================================

# ==========================================================
#EJERCICIO 12:

# ==========================================================

# ==========================================================
#EJERCICIO 13:

# ==========================================================

# ==========================================================
#EJERCICIO 14:

# ==========================================================

# ==========================================================
#EJERCICIO 15:

# ==========================================================

# ==========================================================
#EJERCICIO 16:

# ==========================================================

# ==========================================================
#EJERCICIO 17:

# ==========================================================

# ==========================================================
#EJERCICIO 18:

# ==========================================================

# ==========================================================
#EJERCICIO 19:

# ==========================================================

# ==========================================================
#EJERCICIO 20:

# ==========================================================

# ==========================================================
#EJERCICIO 21:

# ==========================================================

# ==========================================================
#EJERCICIO 22:

# ==========================================================

# ==========================================================
#EJERCICIO 23:

# ==========================================================

# ==========================================================
#EJERCICIO 24:

# ==========================================================

# ==========================================================
#EJERCICIO 25:

# ==========================================================

# ==========================================================
#EJERCICIO 26:

# ==========================================================

# ==========================================================
#EJERCICIO 27:

# ==========================================================

# ==========================================================
#EJERCICIO 28:

# ==========================================================

# ==========================================================
#EJERCICIO 29:

# ==========================================================

# ==========================================================
#EJERCICIO 30:

# ==========================================================
