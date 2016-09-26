#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import csv

if __name__ == '__main__':

    lineas = csv.reader(open(sys.argv[1]))    #Lo guarda como lista con los 
                                                #componentes ya separados por
                                                #linea y sin \n

    calc = calcoohija.CalculadoraHija() #sin () seria puntero
    
    DiccOper = {'suma': calc.plus, 'resta': calc.minus, 'multiplica': calc.mul, 'divide': calc.div}               

    for linea in lineas:
    
        operandos = linea[1:]         #Le quitamos el primer componente
        operacion = linea[0]          #La operacion sera el perimer comp.
        
        resultado = int(operandos[0])
        operandos = operandos[1:]   #Empieza a sumar desde el 2º comp.
        
        for operando in operandos:   
            if operacion == 'divide' and operando == 0:
                sys.exit('Division by 0 is not allowed')
            else:
                try:
                    resultado = DiccOper[operacion](resultado, int(operando))
                except KeyError:
                    sys.exit('Operación sólo puede ser suma, resta, multiplica o divide')           
       
        print('Resultado = ' + str((resultado)))
