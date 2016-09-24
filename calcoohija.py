#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo

class CalculadoraHija(calcoo.Calculadora) :

    def div(op1, op2):
        if op2 == 0:
            return ('Division by zero is not allowed')
        else:
            return op1 / op2

    def mul(op1, op2):
        return op1 * op2

if __name__ == '__main__':
    
    calcoohija = CalculadoraHija
    
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit('Non numerical parameters')
     
    if sys.argv[2] == 'divide':
        resultado = calcoohija.div(operando1, operando2)
    elif sys.argv[2] == 'multiplica':
        resultado = calcoohija.mul(operando1, operando2)
    elif sys.argv[2] == 'suma':
        resultado =  calcoohija.plus(operando1, operando2)
    elif sys.argv[2] == 'resta':
        resultado = calcoohija.minus(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser suma, resta, multiplica o divide')
        
    print(resultado)
