# -*- coding: utf-8 -*-
"""
Ejercicios del curso de Programación en Lenguajes Estadísticos
"""

# Ejercicio 1: Control condicional con `if`
def ejercicio01():
    # Asigna un valor a num de manera que el valor que se devuelve en resultado sea True
    num = None  # ingresa valor aquí

    if num > 10:
        resultado = True
    else:
        resultado = False
    return resultado


# Ejercicio 2: Control condicional con `if`
def ejercicio02():
    # Asigna un valor a num de manera que el valor que se devuelve en resultado sea 5
    num = None  # ingresa valor aquí

    if (num > 100) and (num < 110):
        resultado = 5
    else:
        resultado = 0
    return resultado


# Ejercicio 3: Control condicional con `if`
def ejercicio03():
    # Asigna valores en los espacios indicados de manera que el valor que se devuelve en resultado sea 200
    num = 10

    if num == 5:
        resultado = None  # Ingresa valor aquí
    elif num == 10:
        resultado = None  # Ingresa valor aquí
    else:
        resultado = None  # Ingresa valor aquí

    resultado = 0.5 * resultado
    return resultado


# Ejercicio 4: Números pares con `while`
def ejercicio04():
    # Retorna un vector con los primeros 'n' números pares contados a partir de 1
    n = 5
    pares = []
    i = 1
    maxiter = 2*n
    itercount = 0
    while len(pares) < n:
        if i % 2 == 0:
            pares.append(i)
        i = None # Modifica apropiadamente esta expresión de manera que en pares se almacenen los 5 primeros números pares
        
        itercount=+1
        if itercount>maxiter:
            break
        
    return pares


# Ejercicio 5: Encuentra el primer múltiplo de 3 usando `while`
def ejercicio05():
    # Retorna el primer múltiplo de 3 mayor o igual a 'n' usando un bucle while
    n = 10
    multiplo = n
    maxiter = 20
    itercount= 1
    condicion = True
    while condicion:
        multiplo += 1
        itercount += 1
        if itercount > maxiter:
            break
        condicion = None  # Ingresa condición aquí
    return multiplo


# Ejercicio 6: Sumatoria con `for`
def ejercicio06():
    # Calcula la sumatoria de los primeros 'n' números naturales usando un bucle for
    n = 10
    suma = 0  # Ingresa valor aquí
    for i in range(1, n + 1):
        suma = None # Ingresa expresión aquí
    return suma


# Ejercicio 7: Factorial con `for`
def ejercicio07():
    # Calcula el factorial de 'n' usando un bucle for
    n = 5
    fact = None  # Ingresa expresión aquí
    for i in range(1, n + 1):
        fact = None  # Ingresa expresión aquí
    return fact


# Ejercicio 8: Filtrar valores mayores que un umbral
def ejercicio08():
    # Devuelve un vector con los valores de 'vector' mayores que 'umbral' usando un bucle for
    vector = [1, -2, 8, 12, -2, 5, 6, 4, 10, 11, 9, 8, 3, 2]
    umbral = 4
    resultado = []
    for valor in vector:
        if valor > umbral:
            None # Ingresa expresión aquí
    return resultado


# Ejercicio 9: Calcula suma de elementos de vector
def ejercicio09():
    # Calcula la suma de los elementos del vector vec omitiendo los valores None
    vec = [1, -2, 8, 12, -2, None, 6, 4, 10, None, 9, 8, None, 2]
    sumvec = 0
    for v in vec:
        if v is not None:
            sumvec = None # Ingresa expresión aquí
    return sumvec


# Ejercicio 10: Calcula promedio de elementos de vector
def ejercicio10():
    # Calcula promedio de los elementos del vector vec omitiendo los valores NA
    vec = [1, -2, 8, 12, -2, None, 6, 4, 10, None, 9, 8, None, 2]
    sumvec = 0
    cont = 0  # Ingresa valor aquí
    for v in vec:
        if v is not None:
            sumvec = None # Ingresa expresión aquí
            cont += 1
    promedio = None # Ingresa expresión aquí
    return promedio
