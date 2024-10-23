def suma():
    num1 = int(input("Ingrese el primer número para sumar: "))
    num2 = int(input("Ingrese el segundo número para sumar: "))
    suma = num1 + num2
    print(f"La suma de los 2 números es: {suma}")

def resta():
    num1 = int(input("Ingrese el primer número para restar: "))
    num2 = int(input("Ingrese el segundo número para restar: "))
    resta = num1 - num2
    print(f"La restar de los 2 números es: {resta}")

def multiplicacion():
    num1 = int(input("Ingrese el primer número para multiplicar: "))
    num2 = int(input("Ingrese el segundo número para multiplicar: "))
    mult = num1 * num2
    print(f"El producto de los 2 números es: {mult}")

def division():
    divisor = int(input("Ingrese el divisor: "))
    dividendo = int(input("Ingrese el dividendo: "))
    div = divisor/dividendo
    print(f"La división de los 2 números es: {div}")

def potenciacion():
    base = int(input("Ingrese la base para la potencia: "))
    exp = int(input("Ingrese el exponente para la potencia: "))
    pot = base**exp
    print(f"La potencia de los 2 números es: {pot}")

def radicacion():
    ind = int(input("Ingrese el índice para esa raíz: "))
    rad = int(input("Ingrese el radicando para la raíz: "))
    raiz = ind**(1/rad)
    print(f"La raiz es: {raiz:.2f}")

print("Bienvenido al programa, por favor elija una elección:\n")
print("1. Operaciones básicas aritméticas\n2. Complemento para funciones trigonométricas\n3. Operaciones con matrices\n4.Estadística Descriptiva")
seleccion = int(input("Ingrese una selección para la calculadora: "))
if seleccion in (1,2,3,4):
    print("Escoja la operacion que desea realizar:\n")
    print("1. Sumar 2 números\n2. Restar 2 números\n3. Multiplicar 2 números\n4. Dividir 2 números\n5. Potenciación (Base, Exponente)\n6. Radicación (Índice, Radicando)\n7. Factorial de un número")
    seleccion = int(input("Ingrese una selección para la calculadora: "))
    if seleccion in (1,2,3,4,5,6,7):
        if seleccion == 1:
            suma()
        elif seleccion == 2:
            resta()
        elif seleccion == 3:
            multiplicacion()
        elif seleccion == 4:
            division()
        elif seleccion == 5:
            potenciacion()
        elif seleccion == 6:
            radicacion()
        elif seleccion == 7:
            pass
        elif seleccion == 8:
            pass