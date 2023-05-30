"""
Realizar  un  programa  que  indique  cuál  es  el  mayor  de  cuatro  números  enteros ingresados por el teclado
"""
def ej01():
    print("Buscador del valor mayor")

    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))
    n3 = int(input("Número 3: "))
    n4 = int(input("Número 4: "))

    if (n1 > n2) and (n1 > n3) and (n1 > n4):
        print(f"El valor mayor es: {n1}")
    elif (n2 > n1) and (n2 > n3) and (n2 > n4):
        print(f"El valor mayor es: {n2}")
    elif (n3 > n1) and (n3 > n2) and (n3 > n4):
        print(f"El valor mayor es: {n3}")
    else:
        print(f"El valor mayor es: {n4}")


"""
Realice un programa que indique si un número es divisible entre 10
"""
def ej02():
    print("Validar dividendo de 10")

    num = float(input("Número a validar: "))

    if (num % 10 == 0):
        print(f"{num} es divisible")
    else:
        print(f"{num} no es divisible")


"""
Realice un programa que indique si un número es múltiplo de 4
"""
def ej03():
    print("Validar múltiplo de 4")

    num = float(input("Número a validar: "))

    if (num % 4 == 0) and num >= 0:
        print(f"{num} es múltiplo de 4")
    else:
        print(f"{num} no es múltiplo de 4")


"""
Realice un programa que indique si la suma de dos valores es positiva, negativa o cero
"""
def ej04():
    print("Signo de la suma")

    num1 = float(input("Número 1: "))
    num2 = float(input("Número 2: "))
    result = num1 + num2

    if (result > 0): 
        print("El valor de la suma es positivo")
    elif (result < 0): 
        print("El valor de la suma es negativo")
    else: 
        print("El valor de la suma es 0")

"""
Realice un programa que indique si un número es divisible entre dos y cinco (a la 
vez)
"""
def ej05():
    print("Validar dividendo de 2 y 5")

    num = float(input("Número a validar: "))

    if (num % 2 == 0) and (num % 5 == 0):
        print("Es divisible entre dos y cinco")
    else:
        print("No es divisible")

"""
Escribir  un  programa  que  indique  si  una  persona  tiene  sobrepeso
"""
def ej06():
    print("Comprobar sobrepeso")

    altura = float(input("Ingrese su altura en metros: "))
    peso = float(input("Ingrese su peso en kilogramos: "))


    if (altura >= 1.45) and (altura <= 1.91):
        if (altura*100) % 2 == 0:
            altura += 0.01

        if (altura == 1.45) and (peso > 52.5):
            print("Tiene sobrepeso")
        elif (altura == 1.47) and (peso > 54):
            print("Tiene sobrepeso")
        elif (altura == 1.49) and (peso > 55.5):
            print("Tiene sobrepeso")
        elif (altura == 1.51) and (peso > 57):
            print("Tiene sobrepeso")
        elif (altura == 1.53) and (peso > 58.5):
            print("Tiene sobrepeso")
        elif (altura == 1.55) and (peso > 60):
            print("Tiene sobrepeso")
        elif (altura == 1.57) and (peso > 61.6):
            print("Tiene sobrepeso")
        elif (altura == 1.59) and (peso > 63.2):
            print("Tiene sobrepeso")
        elif (altura == 1.61) and (peso > 64.8):
            print("Tiene sobrepeso")
        elif (altura == 1.63) and (peso > 66.4):
            print("Tiene sobrepeso")
        elif (altura == 1.65) and (peso > 68):
            print("Tiene sobrepeso")
        elif (altura == 1.67) and (peso > 69.7):
            print("Tiene sobrepeso")
        elif (altura == 1.69) and (peso > 71.4):
            print("Tiene sobrepeso")
        elif (altura == 1.71) and (peso > 73.1):
            print("Tiene sobrepeso")
        elif (altura == 1.73) and (peso > 74.8):
            print("Tiene sobrepeso")
        elif (altura == 1.75) and (peso > 78.3):
            print("Tiene sobrepeso")
        elif (altura >= 1.77) and (altura <= 1.79) and (peso > 80.1):
            print("Tiene sobrepeso")
        elif (altura == 1.81) and (peso > 83.7):
            print("Tiene sobrepeso")
        elif (altura == 1.83) and (peso > 85.5):
            print("Tiene sobrepeso")
        elif (altura == 1.85) and (peso > 87.1):
            print("Tiene sobrepeso")
        elif (altura == 1.87) and (peso > 89.3):
            print("Tiene sobrepeso")
        elif (altura == 1.91) and (peso > 91.2):
            print("Tiene sobrepeso")
        else:
            print("No tiene sobrepeso")
    else:    
        print("Altura no contemplada en este programa")

"""
Escribir un programa que calcule la devuelta que debe darse a un cliente luego de realizado una compra, los datos capturados deben ser positivos y tomar en cuenta que se captura el monto de la compra y el monto de pago dado por el cliente
"""
def ej07():
    print("Calculadora de devuelta")

    monto_compra = float(input("Monto de compra: "))
    monto_pagado = float(input("Monto entregado: "))

    if (monto_compra < 0) or (monto_pagado < 0):
        print("Los valores introducidos deben ser positivos")
    else:
        devuelta = monto_pagado - monto_compra

        if (devuelta < 0):
            print(f"El cliente sigue debiendo RD${devuelta * -1}")
        else:
            print(f"La devuelta del cliente es de RD${devuelta}")

"""
Realiza  un  programa  dado  la  opción  elegida  en  un  menú  calcule  (1)  velocidad promedio de un vehículo; (2) la distancia recorrida; (3) Tiempo y (4) aceleración promedio. Se entiende que los datos introducidos están en las medidas de metros y segundos
"""

def ej08():
    print(
        """
        Calculadora de propiedades físicas de un vehículo  - Opciones
        (1) Velcodiad promedio
        (2) Distancia recorrida
        (3) Tiempo
        (4) Aceleración promedio
        """
    )

    op = int(input("Opción > "))

    if (op == 1):
        print("Calculando velcodiad promedio...")
        
        distancia = float(input("Introduzca la distancia recorrida: "))
        tiempo = float(input("Introduzca el tiempo: "))
        velocidad = distancia / tiempo

        print(f"Velocidad promedio de {velocidad}m/s")
    elif (op == 2):
        print("Calculando distancia recorrida...")

        velocidad = float(input("Introduzca la velocidad promedio: "))
        tiempo = float(input("Introduzca el tiempo: "))
        distancia = velocidad * tiempo

        print(f"Distancia recorrida de {distancia}m")
    elif (op == 3):
        print("Calculando tiempo del recorrido...")

        distancia = float(input("Introduzca la distancia recorrida: "))
        velocidad = float(input("Introduzca la velocidad promedio: "))
        tiempo = distancia / velocidad

        print(f"Distancia recorrida en {tiempo}s")
    elif (op == 4):
        print("Calculando aceleración promedio...")

        velocidad = float(input("Introduzca la velocidad promedio: "))
        tiempo = float(input("Introduzca el tiempo: "))
        aceleracion = velocidad / tiempo

        print(f"Aceleración promedio de {aceleracion}m/s2")
    else:
        print("No se selección ninguna opción")

