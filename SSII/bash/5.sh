#!/bin/bash

if [ -z $1 ]; then
    echo "Formato de uso: $0 numero"
    echo "Indica si el numero es par o impar"
fi

(( resto = $1 % 2 ))

if [ $resto -eq 0 ]; then
    echo "El numero $1 es un numero par"
else
    echo "El numero $1 es un numero impar"
fi

unset resto