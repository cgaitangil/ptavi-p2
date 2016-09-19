#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def multiplicar(op1, op2):
    return op1 * op2
    
def dividir(op1, op2):
    if op2 == 0:
        return 'No se puede dividir por 0'
    else:
        return op1 / op2



def plus(op1, op2):
    """ Function to sum the operands """
    return op1 + op2


def minus(op1, op2):
    """ Function to substract the operands """
    return op1 - op2

if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = minus(operando1, operando2)
    elif sys.argv[2] == 'mult':
        result = multiplicar(operando1, operando2)
    elif sys.argv[2] == 'divi':
        result = dividir(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser suma, resta, multiplicación o división')

    print(result)
