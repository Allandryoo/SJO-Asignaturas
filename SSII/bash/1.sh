#!/bin/bash
echo "CALCULADORA"
echo "---------------------"
echo "Elija dos numeros:"
read n1
read n2
echo "Estas son las opciones posibles:"
echo "Sumar: +"
echo "Restar: -"
echo "Multiplicar: *"
echo "Dividir: /"
echo "Que desea hacer?"
read opcion

case $opcion in
    +)
        suma=$((n1+n2))
        echo "La suma de $n1 y $n2 es: $suma"
        ;;
    -)
        resta=$((n1-n2))
        echo "La resta de $n1 y $n2 es : $resta"
        ;;
    /)
        division=$((n1/n2))
        echo "La division de $n1 y $n2 es: $division"
        ;;
    *)
        multiplicacion=$((n1*n2))
        echo "La multiplicacion de $n1 y $n2 es: $multiplicacion"
        ;;
esac

unset n1
unset n2
unset opcion
unset suma
unset resta
unset multiplicacion
unset division