#!/usr/bin/python2.4 -tt
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
    if len(s)>= 3:
        if s[-3:] == "ing":
            resultado = s + "ly"
        else:
            resultado = s + "ing"
    else:
        resultado = s
    return resultado


# E. not_bad
# Dada una cadena, encontrar la primera aparición de la
# subcadena 'not' y 'bad'. Si el 'bad' sigue a
# la 'not', reemplazar la subcadena completa 'not'...'bad'
# con 'good'.
# Retornar la cadena resultante.
# Así, 'This dinner is not that bad!' devuelve:
# This dinner is good!
def not_bad(s):
    cadena_not = s.find("not")
    cadena_bad = s.find("bad")
    if cadena_not < cadena_bad:
        s = s[:cadena_not] + "good" + s[cadena_bad+3:]
    return s


# F. front_back
# Considerar dividir una cadena en 2 mitades.
# Si la longitud es par, las mitades primera y final tienen la misma longitud.
# Si la longitud es impar, haremos que el caracter extra vaya en la primer mitad.
# ej. 'abcde', la primer mitad es 'abc', la final es 'de'.
# Dadas 2 cadenas, a y b, retornar una cadena de la forma
#    a-primera + b-primera + a-final + b-final
# Por ej: front_back('Gato', 'Rosca') devuelve 'GaRostoca'
def front_back(a, b):
    s = ""
    if (len(a)%2 == 0):
        a = par
    else:
        a = impar
    if (len(b)%2 == 0):
        b = par
    else:
        b = impar
    if (a == par and b == par):
        s = a[:len(a)/2] + b[len(b)/2:] + a[len(a)/2:] + b[len(b)/2:]
    elif (a == par and b == impar):
        s = a[:len(a)/2] + b[(len(b)/2)+1:] + a[len(a)/2:] + b[(len(b)/2)+1:]
    elif (a == impar and b == par):
        s = a[:(len(a)/2)+1] + b[len(b)/2:] + a[(len(a)/2)+1:] + b[len(b)/2:]
    elif (a == impar and b == impar):
        s = a[:(len(a)/2)+1] + b[(len(b)/2)+1:] + a[(len(a)/2)+1:] + b[(len(b)/2)+1:]
    print s
    

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
