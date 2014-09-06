#!/usr/bin/python -tt
# -*- coding: UTF-8 -*-
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
# Ejercicios b�sicos de cadenas
# Llenar el c�digo de las funciones abajo. main() ya est� armado
# para llamar a las funciones con algunas entradas,
# imprime 'OK' cuando cada funci�n es correcta.
# El c�digo inicial para cada funci�n incluye un 'return'
# que es s�lo un comod�n para tu c�digo.
# A. donuts
# dado un contador entero de un n�mero de donas, retornar una cadena
# de la forma 'Numero de donas: <contador>', donde <contador> es el
# n�mero pasado. Sin embargo, si el contador es 10 o m�s, entonces usar
# la palabra "muchas" en vez del contador verdadero.
# As� donuts(5) devuelve 'Numero de donas: 5'
# y donuts(23) devuelve 'Numero de donas: muchas'
def donuts(contador):
	# +++tu c�digo aqu�+++
	cadena_donas = 'Numero de donas: '
	if contador >= 10:
		cadena_donas += 'muchas'
	else:
		cadena_donas += str(contador)

	return cadena_donas


# B. both_ends
# Dada una cadena s, devuelva una cadena hecha de los primeros 2
# y los �ltimos 2 caracteres de la cadena original,
# as� 'spring' devuelve 'spng'. Sin embargo, si la longitud de la cadena
# es menos de 2, returnar una cadena vac�a en su lugar.
def both_ends(s):
    # +++tu c�digo aqu�+++
    str_both_ends = ''
    if len(s) >= 2:
        str_both_ends = s[0:2] + s[len(s)-2:len(s)]

    return str_both_ends


# C. fix_start
# Dada una cadena s, devuelva una cadena
# donde todas las ocurrencias del primer caracter han
# cambiado a '*', excepto por el primer caracter mismo.
# ej: 'babble' retorna 'ba**le'
# Asuma que la cadena es de 1 o m�s caracteres.
# Ayuda: s.replace(stra, strb) retorna una versi�n de la cadena s
# donde todas las instancias de stra han sido reemplazadas por strb.
def fix_start(s):
    # +++tu c�digo aqu�+++
    first_char = s[0]
    new_string = first_char
    for i in range(1,len(s)):
        if s[i] == first_char:
            new_string += '*'
        else:
            new_string += s[i]

    return new_string


# D. MixUp
# Dadas las cadenas a y b, retornar una cadena simple con a y b separados
# pon un espacio '<a> <b>', excepto que hay que intercambiar los
# 2 primeros caracteres de cada cadena.
# ej.
# 'mix', pod' -> 'pox mid'
# 'dog', 'dinner' -> 'dig donner'
# Asumir a y b tienen una longitud de 2 o m�s.
def mix_up(a, b):
    # +++tu c�digo aqu�+++
    if len(a) + len(b) >= 4:
        str_mixed = b[0:2] + a[2:len(a)] + ' ' + a[0:2] + b[2:len(b)]

    return str_mixed


# Funci�n simple test() utilizada en main() para mostrar
# lo que retorna cada funci�n vs lo que deber�a retornar.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = ' X '
    print '%s obtuvo: %s se esperaba: %s' % (prefix, repr(got), repr(expected))


# Funci�n main() llama a las funciones de arribacon entradas interesantes,
# utilizando test() para verificar si cada resultado es correcto o no.
def main():
    print 'donuts'
    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Numero de donas: 4')
    test(donuts(9), 'Numero de donas: 9')
    test(donuts(10), 'Numero de donas: muchas')
    test(donuts(99), 'Numero de donas: muchas')
    print
    print 'both_ends'
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')
    print
    print 'fix_start'
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')
    print
    print 'mix_up'
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()