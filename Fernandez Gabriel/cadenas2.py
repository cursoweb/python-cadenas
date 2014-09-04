#!/u6600sr/bin/python2.4 -tt
# -*- coding: UTF-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Ejercicios adicionales básicos de cadenas
# Llenar el código de las funciones abajo. main() ya está armado
# para llamar a las funciones con algunas entradas,
# imprime 'OK' cuando cada función es correcta.
# El código inicial para cada función incluye un 'return'
# que es sólo un comodín para tu código.


# D. verbing
# Dada una cadena, si su longitud es por lo menos 3,
# agregar 'ing' al final.
# Esto a no ser que ya termine en 'ing', en cuyo caso
# agregar 'ly'.
# Si la longitud de la cadena es menor a 3, dejarla sin cambiar.
# Retornar la cadena resultante.
def verbing(s):
    # +++tu código aquí+++
    
    if len(s) >= 3:
        final = s[-3:]

        if final != "ing":
            cadena = s + "ing"
        else:
            cadena = s + "ly"
    else:
        cadena = s

    return cadena


# E. not_bad
# Dada una cadena, encontrar la primera aparición de la
# subcadena 'not' y 'bad'. Si el 'bad' sigue a
# la 'not', reemplazar la subcadena completa 'not'...'bad'
# con 'good'.
# Retornar la cadena resultante.
# Así, 'This dinner is not that bad!' devuelve:
# This dinner is good!
def not_bad(s):
    # +++tu código aquí+++
    

    indice_not = s.find("not")
    indice_bad = s.find('bad')
    caracter = s[indice_bad+3:]

    if indice_not and indice_bad != -1:
        if indice_bad > indice_not:
            cadena = s[0:indice_not]
            cadenafinal = cadena + "good" + caracter
        else:
            cadenafinal = s
    else:
        cadenafinal = s
   
    return cadenafinal



# F. front_back
# Considerar dividir una cadena en 2 mitades.
# Si la longitud es par, las mitades primera y final tienen la misma longitud.
# Si la longitud es impar, haremos que el caracter extra vaya en la primer mitad.
# ej. 'abcde', la primer mitad es 'abc', la final es 'de'.
# Dadas 2 cadenas, a y b, retornar una cadena de la forma
#    a-primera + b-primera + a-final + b-final
# Por ej: front_back('Gato', 'Rosca') devuelve 'GaRostoca'
def front_back(a, b):
    # +++tu código aquí+++
    if len(a)%2 == 0:
        mitad_a = len(a)/2
        a_primera = a[:mitad_a]
        a_final = a[mitad_a:]
    else:
        mitad_a = (len(a)+1)/2
        a_primera = a[:mitad_a]
        a_final = a[mitad_a:]

    if len(a)%2 == 0:
        mitad_b = len(b)/2
        b_primera = b[:mitad_b]
        b_final = b[mitad_b:]
    else:
        mitad_b = (len(b)+1)/2
        b_primera = b[:mitad_b]
        b_final = b[mitad_b:]
    
    resultado = a_primera + b_primera + a_final + b_final

    return resultado

# Función simple test() utilizada en main() para mostrar
# lo que retorna cada función vs lo que debería retornar.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '    X '
    print '%s obtuvo: %s esperaba: %s' % (prefix, repr(got), repr(expected))


# Función main() llama a las funciones de arribacon entradas interesantes,
# utilizando test() para verificar si cada resultado es correcto o no.
def main():
    print 'verbing'
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print
    print 'not_bad'
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print
    print 'front_back'
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
    main()