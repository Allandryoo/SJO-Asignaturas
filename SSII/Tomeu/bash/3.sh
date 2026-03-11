#!/bin/bash

if [ -z $1 ]
then
    echo "Formato de uso: $0 [-C] [-P] [-G] [-S] [-A] numero1 numero2 ..."
    echo ""
    echo "C  Muestra cuantos numeros se han introducido"
    echo "P  Muestra el numero menor"
    echo "G  Muestra el numero mayor"
    echo "S  Muestra la suma de todos"
    echo "A  Muestra todo lo anterior"
fi

mostrar_contador=0
mostrar_menor=0
mostrar_mayor=0
mostrar_suma=0

while [ $# -gt 0 ]; do
    case $1 in
        C) mostrar_contador=1 ; shift ;;
        P) mostrar_menor=1    ; shift ;;
        G) mostrar_mayor=1    ; shift ;;
        S) mostrar_suma=1     ; shift ;;
        A)
            mostrar_contador=1
            mostrar_menor=1
            mostrar_mayor=1
            mostrar_suma=1
            shift
            ;;
        *)
            break
            ;;
    esac
done

if [ $mostrar_contador -eq 0 ] && [ $mostrar_menor -eq 0 ] && [ $mostrar_mayor -eq 0 ] && [ $mostrar_suma -eq 0 ]
then

    mostrar_contador=1
    mostrar_menor=1
    mostrar_mayor=1
    mostrar_suma=1
fi

if [ -z $1 ]; then
    echo "Error: no has introducido ningun numero"
fi

contador=0
suma=0
mayor=$1
menor=$1

for num in "$@"; do
    (( contador = contador + 1 ))
    (( suma = suma + num ))

    if [ $num -gt $mayor ]; then
        mayor=$num
    fi

    if [ $num -lt $menor ]; then
        menor=$num
    fi
done

if [ $mostrar_contador -eq 1 ]; then
    echo "Se han introducido: $contador numeros"
fi

if [ $mostrar_menor -eq 1 ]; then
    echo "El numero menor es: $menor"
fi

if [ $mostrar_mayor -eq 1 ]; then
    echo "El numero mayor es: $mayor"
fi

if [ $mostrar_suma -eq 1 ]; then
    echo "La suma de todos los numeros es: $suma"
fi

unset mostrar_contador
unset mostrar_mayor
unset mostrar_menor
unset mostrar_suma
unset mostrar_mayor
unset contador
unset mayor
unset menor
unset suma