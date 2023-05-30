"""
1. Realice un programa que imprima el promedio de 4 calificaciones ingresadas por el teclado
"""

def ej01():
    calif1 = float(input("Calificacion 1: "))
    calif2 = float(input("Calificacion 2: "))
    calif3 = float(input("Calificacion 3: "))
    calif4 = float(input("Calificacion 4: "))

    promedio = (calif1 + calif2 + calif3 + calif4) / 4

    print("El promedio de las calificaciones es:", promedio)

"""
2. Realiza un programa que determine el área del cuadrado
"""

def ej02():
    lado = float(input("Medida de cada lado del cuadrado: "))

    area = lado ** 2

    print(area)

"""
3. Realiza un programa que realice las operaciones básicas de suma, resta, multiplicación 
y división  
"""

def ej03():
    num1 = float(input("Numero 1: "))
    num2 = float(input("Numero 2: "))

    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2 
    division = num1 / num2 

    print("Suma:", suma)
    print("Resta:", resta)
    print("Multiplicacion:", multiplicacion)
    print("Division:", division)


"""
4. Realiza un programa que pida tu nombre e imprima un saludo personalizado. 
"""

def ej04():
    nombre = input("Ingresa tu nombre: ")

    print("Muy buenos dias " + nombre + ", espero que hayas disfrutado escribiendo tu nombre!")


"""
5. Realiza un programa que permita calcular la distancia recorrida (m) por un móvil que tiene velocidad constante (m/s) durante un tiempo T (Sg), considerar que es un (Movimiento Rectilíneo Uniforme)
"""

def ej05():
    velocidad = float(input("Velocidad del móvil: "))
    tiempo = float(input("Tiempo en movimiento: "))

    distancia = velocidad / tiempo 

    print("La distancia recorrida por el móvil fue de " + str(distancia) + "m")

"""
6. Realice un programa que muestre en pantalla el resultado final de un examen de 10 preguntas, donde el profesor ingresada el total de preguntas correctas e incorrectas. El valor de cada pregunta es 10 ptos.
"""

def ej06():
    preg_cor = int(input("Numero de preguntas correctas: "))
    preg_inc = int(input("Numero de preguntas incorrectas: "))

    resultado = preg_cor * 10

    print("El resultado final del examen es", resultado, "puntos.")

"""
7. Elabora un programa que permita calcular la nómina semana de un empleado. Para lo cual se dispone del total de horas laboradas en la semana, así como la tarifa por hora. 
"""

def ej07():
    horas_semana = int(input("Horas trabajadas en la semana: "))
    tarifa_hora = float(input("Tarifa por hora: "))

    nomina = horas_semana * tarifa_hora

    print("La nómina semanal del empleado en la semana es de RD$" + str(nomina))

