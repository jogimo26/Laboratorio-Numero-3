def suma(num1,num2):
    suma = num1 + num2
    return suma

def resta(num1,num2):
    resta = num1 - num2
    return resta

def multiplicacion(num1,num2):
    mult = num1 * num2
    return mult

def division(divisor,dividendo):
    div = divisor/dividendo
    return div

def potenciacion(base,exp):
    pot = 1
    for i in range(0,exp,1):
        pot *= base
    return pot

def raizcuadrada(rad,precision): # Debido a que por restricciones no se puede hacer con el operador **, se hizo la raíz cuadrada por medio del método de aproximación de herón
    if rad < 0:
        print("La raíz cuadrada de un número negativo no está definida dentro de los números reales")
    estimacion = rad
    while abs(estimacion * estimacion - rad) > precision: # Mientras el valor absoluto del producto entre la estimación y la estimación menos el radicando es mayor que la precisión, da el código en el bucle
        estimacion = 0.5 * (estimacion + rad/estimacion) # Fórmula de Herón para raíces cuadradas
    return estimacion

def factorial(numero):
    for i in range(numero-1,0,-1):
        numero *= i
    if numero == 0: # Por definición 0! es 1
        numero = 1
    return numero

def seno(radianes, terminos):
    aprox = 0
    for n in range(terminos): # Serie de taylor
        numerador = potenciacion(radianes,2*n+1)
        denominador = factorial(2*n+1)
        aprox += potenciacion(-1,n)*(numerador/denominador)
    return aprox

def coseno(radianes,terminos):
    aprox = 0
    for n in range(terminos): # Serie de taylor
        numerador = potenciacion(radianes,2*n)
        denominador = factorial(2*n)
        aprox += potenciacion(-1,n)*(numerador/denominador)
    return aprox

def tangente(radianes,terminos): # Se usa la identidad trigonométrica en lugar de la serie de taylor por conveniencia
    tangente = seno(radianes,terminos)/coseno(radianes,terminos)
    return tangente

def promedio(tmuestra,muestra):
    sumadatos = sum(muestra)
    promedio = sumadatos/tmuestra
    return promedio

def varianza(tmuestra,muestra): 
    promediom = promedio(tmuestra,muestra)
    potenciaresta = 0 # Hace la operación de (dato-promedio)^2 en el bucle, para asi llegar al numerador dentro de la fórmula
    sumatoriaacum = 0 # Acumulador para la variable de arriba
    for dato in muestra:
        restadato = dato-promediom
        potenciaresta = potenciacion(restadato,2)
        sumatoriaacum += potenciaresta
    varianza = (sumatoriaacum)/(tmuestra-1) # Se usa la fórmula para la varianza de una muestra, no de una población
    return varianza # Al resultado se le puede sacar raíz cuadrada para hallar la desviación estándar

def desviacionestandar(tmuestra,muestra):
    varianzamuestra = varianza(tmuestra,muestra)
    desvestandar = raizcuadrada(varianzamuestra,0.000000001)
    return desvestandar

print("Bienvenido al programa, por favor elija una elección:\n")
print("1. Operaciones básicas aritméticas\n2. Complemento para funciones trigonométricas\n3. Operaciones con matrices\n4. Estadística Descriptiva\nCualquier otro número: Salir del programa")
seleccion = int(input("Ingrese una selección para la calculadora: "))

while seleccion in [1,2,3,4]:
        while seleccion == 1:
            print("Escoja la operacion que desea realizar:\n")
            print("1. Sumar 2 números\n2. Restar 2 números\n3. Multiplicar 2 números\n4. Dividir 2 números\n5. Potenciación (Base, Exponente)\n6. Raíz Cuadrada (Radicando, Precisión de la estimación)\n7. Factorial de un número\n8. Salir del menú")
            seleccion2 = int(input("Ingrese una selección para la calculadora: "))
            match seleccion2:
                case 1:
                    num1 = int(input("Ingrese el primer número para sumar: "))
                    num2 = int(input("Ingrese el segundo número para sumar: "))
                    suma1 = suma(num1,num2)
                    print(f"La suma de los 2 números es: {suma1}\n")
                case 2:
                    num1 = int(input("Ingrese el primer número para restar: "))
                    num2 = int(input("Ingrese el segundo número para restar: "))
                    resta1 = resta(num1,num2)
                    print(f"La restar de los 2 números es: {resta1}\n")
                case 3:
                    num1 = int(input("Ingrese el primer número para multiplicar: "))
                    num2 = int(input("Ingrese el segundo número para multiplicar: "))
                    mult = multiplicacion(num1,num2)
                    print(f"El producto de los 2 números es: {mult}\n")
                case 4:
                    divisor = int(input("Ingrese el divisor: "))
                    dividendo = int(input("Ingrese el dividendo: "))
                    div = division(divisor,dividendo)
                    print(f"La división de los 2 números es: {div}\n")
                case 5:
                    base = int(input("Ingrese la base para la potencia: "))
                    exp = int(input("Ingrese el exponente para la potencia: "))    
                    pot = potenciacion(base,exp)
                    print(f"Su potencia es: {pot}\n")
                case 6:
                    rad = int(input("Ingrese el radicando para la raíz: "))
                    precision = float(input("Ingrese la precisión con la cual calcular la raíz (mientras más cerca sea a 0, más precisa será): "))
                    estimacion = raizcuadrada(rad,precision)
                    print(f"La aproximación de la raiz es: {estimacion}\n")
                case 7:
                    numero = int(input("Ingrese el número a el cual se le va a hacer el factorial: "))
                    fact = factorial(numero)
                    print(f"El factorial del número es: {fact}\n")
                case 8:
                    print("Saliendo del menú...\n")
                    seleccion = int(input("Ingrese una selección para la calculadora: "))
        if seleccion == 2:
            print("Escoja la operacion que desea realizar:\n")
            print("1. Razón trigonométrica Sin(x)\n2. Razón trigonométrica Cos(x)\n3. Razón trigonométrica Tan(x)\n4. Salir del programa")
            seleccion2 = int(input("Ingrese una selección para la calculadora: "))
            match seleccion2:
                case 1:
                    x = float(input("Ingrese un valor para x (En grados): "))

                    while x > 360 or x < 0: # Para evitar conflictos toca hacer que los ángulos dados por el usuario estén entre 0 y 360, usando ángulos complementarios lo podemos hacer fácil
                        if x > 360:
                            x -= 360
                        elif x < 0:
                            x += 360

                    terminos = int(input("Ingrese la cantidad de términos para la cual calcular la función seno: "))
                    xrad = x*3.1415/180 # Se convierte a radianes para que funcione "bien" de 0 a 360 grados
                    aprox = seno(xrad,terminos)
                    print(f"Una aproximación de la función seno hasta {terminos} terminos es: {aprox}\n")
                case 2:
                    x = float(input("Ingrese un valor para x (En grados): "))

                    while x > 360 or x < 0: # Lo mismo que dentro del comentario de la razón seno
                        if x > 360:
                            x -= 360
                        elif x < 0:
                            x += 360

                    terminos = int(input("Ingrese la cantidad de términos para la cual calcular la función coseno: "))
                    xrad = x*3.1415/180
                    aprox = coseno(xrad,terminos)
                    print(f"Una aproximación de la función coseno hasta {terminos} términos es: {aprox}\n")
                case 3:
                    x = float(input("Ingrese un valor para x (En grados): "))

                    while x > 360 or x < 0:
                        if x > 360:
                            x -= 360
                        elif x < 0:
                            x += 360

                    terminos = int(input("Ingrese la cantidad de términos para la cual calcular la función tangente: "))
                    xrad = x*3.1415/180
                    aprox = tangente(xrad,terminos)
                    print(f"Una aproximación de la función tangente hasta {terminos} términos es: {aprox}\n")
                case 4:
                    print("Saliendo del menú...\n")
                    seleccion = int(input("Ingrese una selección para la calculadora: "))       
        if seleccion == 3:
            print("Escoja la operacion que desea realizar:\n")
            print("1. Suma de matrices 2x2\n2. Resta de matrices 2x2\n3. Multiplicación de matrices 2x2\n4. Determinante de una matriz 2x2\n5. Salir del programa")
            seleccion2 = int(input("Ingrese una selección para la calculadora: "))
            match seleccion2:
                case 1:
                    continue
                case 2:
                    continue
                case 3:
                    continue
                case 4:
                    continue
                case 5:
                    print("Saliendo del menú...\n")
                    seleccion = int(input("Ingrese una selección para la calculadora: "))
        if seleccion == 4:
            print("Escoja la operacion que desea realizar:\n")
            print("1. Promedio de una muestra\n2. Desviación estándar de una muestra\n3. Varianza de una muestra\n4. Salir del programa")
            seleccion2 = int(input("Ingrese una selección para la calculadora: "))
            match seleccion2:
                case 1:
                    muestra = []
                    tmuestra = int(input("Ingrese el tamaño de la muestra que va a ingresar: "))
                    for i in range(1,tmuestra+1):
                        datoagreg = int(input(f"Ingrese el dato {i} para agregar a la muestra: "))
                        muestra.append(datoagreg)
                    prom = promedio(tmuestra,muestra)
                    print(f"El promedio de su muestra escogida es: {prom}\n")
                case 2:
                    muestra = []
                    tmuestra = int(input("Ingrese el tamaño de la muestra que va a ingresar: "))
                    for i in range(1,tmuestra+1):
                        datoagreg = int(input(f"Ingrese el dato {i} para agregar a la muestra: "))
                        muestra.append(datoagreg)
                    desvestandar = desviacionestandar(tmuestra,muestra)
                    print(f"La desviación estándar de la muestra escogida es: {desvestandar}\n")
                case 3:
                    muestra = []
                    tmuestra = int(input("Ingrese el tamaño de la muestra que va a ingresar: "))
                    for i in range(1,tmuestra+1):
                        datoagreg = int(input(f"Ingrese el dato {i} para agregar a la muestra: "))
                        muestra.append(datoagreg)
                    var = varianza(tmuestra,muestra)
                    print(f"La varianza estadística de la muestra escogida es: {var}\n")
                case 4:
                    print("Saliendo del menú...\n")
                    seleccion = int(input("Ingrese una selección para la calculadora: "))
