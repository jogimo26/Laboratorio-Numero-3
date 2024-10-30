def suma(num1,num2):
    suma = num1 + num2
    print(f"La suma de los 2 números es: {suma}")

def resta(num1,num2):
    resta = num1 - num2
    print(f"La restar de los 2 números es: {resta}")

def multiplicacion(num1,num2):
    mult = num1 * num2
    print(f"El producto de los 2 números es: {mult}")

def division(divisor,dividendo):
    div = divisor/dividendo
    print(f"La división de los 2 números es: {div}")

def potenciacion(base,exp):
    pot = 1
    for i in range(0,exp,1):
        pot *= base
    print(f"Su potencia es: {pot}")

def raizcuadrada(rad,precision): # Debido a que por restricciones no se puede hacer con el operador **, se hizo la raíz cuadrada por medio del método de aproximación de herón
    if rad < 0:
        print("La raíz cuadrada de un número negativo no está definida dentro de los números reales")
    estimacion = rad
    while abs(estimacion * estimacion - rad) > precision: # Mientras el valor absoluto del producto entre la estimación y la estimación menos el radicando es mayor que la precisión, da el código en el bucle
        estimacion = 0.5 * (estimacion + rad/estimacion) # Fórmula de Herón para raíces cuadradas
    print(f"La aproximación de la raiz es: {estimacion}")

def factorial(numero):
    for i in range(numero-1,0,-1):
        numero *= i
    print(f"El factorial del número es: {numero}")

def seno(x,terminos):
    pass

print("Bienvenido al programa, por favor elija una elección:\n")
print("1. Operaciones básicas aritméticas\n2. Complemento para funciones trigonométricas\n3. Operaciones con matrices\n4. Estadística Descriptiva")
seleccion = int(input("Ingrese una selección para la calculadora: "))
if seleccion in (1,2,3,4):
    if seleccion == 1:
        print("Escoja la operacion que desea realizar:\n")
        print("1. Sumar 2 números\n2. Restar 2 números\n3. Multiplicar 2 números\n4. Dividir 2 números\n5. Potenciación (Base, Exponente)\n6. Raíz Cuadrada (Radicando, Precisión de la estimación)\n7. Factorial de un número")
        seleccion2 = int(input("Ingrese una selección para la calculadora: "))
        match seleccion2:
            case 1:
                num1 = int(input("Ingrese el primer número para sumar: "))
                num2 = int(input("Ingrese el segundo número para sumar: "))
                suma(num1,num2)
            case 2:
                num1 = int(input("Ingrese el primer número para restar: "))
                num2 = int(input("Ingrese el segundo número para restar: "))
                resta(num1,num2)
            case 3:
                num1 = int(input("Ingrese el primer número para multiplicar: "))
                num2 = int(input("Ingrese el segundo número para multiplicar: "))
                multiplicacion(num1,num2)
            case 4:
                divisor = int(input("Ingrese el divisor: "))
                dividendo = int(input("Ingrese el dividendo: "))
                division(divisor,dividendo)
            case 5:
                base = int(input("Ingrese la base para la potencia: "))
                exp = int(input("Ingrese el exponente para la potencia: "))    
                potenciacion(base,exp)
            case 6:
                rad = int(input("Ingrese el radicando para la raíz: "))
                precision = float(input("Ingrese la precisión con la cual calcular la raíz (mientras más cerca sea a 0, más precisa será): "))
                raizcuadrada(rad,precision)
            case 7:
                numero = int(input("Ingrese el número a el cual se le va a hacer el factorial: "))
                factorial(numero)
    if seleccion == 2:
        print("Escoja la operacion que desea realizar:\n")
        print("1. Razón trigonométrica Sin(x)\n2. Razón trigonométrica Cos(x)\n3. Razón trigonométrica Tan(x)")
        seleccion2 = int(input("Ingrese una selección para la calculadora: "))
        match seleccion2:
            case 1:
                x = float(input("Ingrese un valor para x: "))
                terminos = int(input("Ingrese la cantidad de términos para la cual calcular la función seno: "))
                seno(x,terminos)
            case 2:
                pass
            case 3:
                pass
