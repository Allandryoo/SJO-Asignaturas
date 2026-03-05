#!/bin/bash

if [ -z $1 ]; then
    echo "Formato de uso: $0 [argumento] n1 n2 n3 ... nn"
    echo ""
    echo "  -e  Muestra para cada numero si es par o impar (por defecto)"
    echo "  -c  Muestra los pares agrupados y los impares agrupados"
    echo "  -p  Muestra solo los pares"
    echo "  -i  Muestra solo los impares"
fi

modo="e"

case $1 in
    -e) modo="e" ; shift ;;
    -c) modo="c" ; shift ;;
    -p) modo="p" ; shift ;;
    -i) modo="i" ; shift ;;
esac

if [ -z $1 ]; then
    echo "Error: no has introducido ningun numero"
fi

case $modo in
    e)
        for num in "$@"; do
            (( resto = num % 2 ))
            if [ $resto -eq 0 ]; then
                echo "El numero $num es un numero par"
            else
                echo "El numero $num es un numero impar"
            fi
        done
        ;;
    c)
        echo "Pares introducidos:"
        for num in "$@"; do
            (( resto = num % 2 ))
            if [ $resto -eq 0 ]; then
                echo "$num"
            fi
        done

        echo "Impares introducidos:"
        for num in "$@"; do
            (( resto = num % 2 ))
            if [ $resto -ne 0 ]; then
                echo "$num"
            fi
        done
        ;;
    p)
        echo "Pares introducidos:"
        for num in "$@"; do
            (( resto = num % 2 ))
            if [ $resto -eq 0 ]; then
                echo "$num"
            fi
        done
        ;;
    i)
        echo "Impares introducidos:"
        for num in "$@"; do
            (( resto = num % 2 ))
            if [ $resto -ne 0 ]; then
                echo "$num"
            fi
        done
        ;;
esac

unset modo
unset num
unset resto