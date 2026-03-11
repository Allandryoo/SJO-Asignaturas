#!/bin/bash

if [ -z $1 ]; then
    echo "Formato de uso: $0 n1 n2 n3 ... nn"
    echo "Indica para cada numero si es par o impar"
fi

for num in "$@"; do
    (( resto = num % 2 ))

    if [ $resto -eq 0 ]; then
        echo "El numero $num es un numero par"
    else
        echo "El numero $num es un numero impar"
    fi
done

unset num
unset resto