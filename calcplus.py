#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

if __name__ == '__main__':

    fichero = open('/home/cgaitan/ptavi-p2/operaciones.txt', 'r')

    lineas = fichero.readlines()

    calc = calcoohija.CalculadoraHija
    
    DiccOper = {'suma': calc.plus, 'resta': calc.minus, 'multiplica': calc.mul, 'divide': calc.div}               

    for linea in lineas:
    
        elems_lista = linea.split(',')
        
        operandos = elems_lista[1:]         #Le quitamos el primer componente
        operandos[-1] = operandos[-1][:-1]  #Le quitamos el \n al último comp.
        operacion = elems_lista[0]          #La operacion sera el perimer comp.
        
        print(operandos)
        
        resultado = int(operandos[0])
        operandos = operandos[1:]   #Empieza a sumar desde el 2º comp.
        
        for operando in operandos:   
            if operacion == 'divide' and int(operando) == 0:
                sys.exit('Division by 0 is not allowed')
            else:
                try:
                    resultado = DiccOper[operacion](resultado, int(operando))
                except KeyError:
                    sys.exit('Operación sólo puede ser suma, resta, multiplica o divide')           
       
        print('Resultado = ' + str(int(resultado)))
