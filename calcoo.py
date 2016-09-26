#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora:

    def minus(self, op1, op2):
        return op1 - op2

    def plus(self, op1, op2):
        return op1 + op2

    def div(self, op1, op2):
        if op2 == 0:
            return ('No se puede dividir por 0')
        else:
            return op1 / op2

    def mul(self, op1, op2):
        return op1 * op2

if __name__ == '__main__':

    calcoo = Calculadora()
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit('Non numerical parameters')

    if sys.argv[2] == 'suma':
        resultado = calcoo.plus(operando1, operando2)
    elif sys.argv[2] == 'resta':
        resultado = calcoo.minus(operando1, operando2)
    elif sys.argv[2] == 'division':
        resultado = calcoo.div(operando1, operando2)
    elif sys.argv[2] == 'multiplicacion':
        resultado = calcoo.mul(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser suma, resta, multiplicación o \
división')

    print('Resultado = ' + str(resultado))
