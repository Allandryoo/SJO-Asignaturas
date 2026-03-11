#!/bin/bash

echo "CONVERSOR DE BASES"
echo "---------------------"
echo "En que base esta ese numero?"
echo "1) Decimal"
echo "2) Binario"
echo "3) Octal"
echo "4) Hexadecimal"
read base_origen

echo ""
echo "Introduce el numero a convertir:"
read numero

echo ""
echo "A que base quieres convertirlo?"
echo "1) Decimal"
echo "2) Binario"
echo "3) Octal"
echo "4) Hexadecimal"
read base_destino

case $base_origen in
    1) base_in=10 ;;
    2) base_in=2  ;;
    3) base_in=8  ;;
    4) base_in=16 ;;
    *)
        echo "Opcion de origen no valida"
        ;;
esac

case $base_destino in
    1) base_out=10 ;;
    2) base_out=2  ;;
    3) base_out=8  ;;
    4) base_out=16 ;;
    *)
        echo "Opcion de destino no valida"
        ;;
esac

numero=$(echo $numero | tr 'a-f' 'A-F')

resultado=$(echo "ibase=$base_in; obase=$base_out; $numero" | bc)

echo ""
echo "Resultado: $numero (base $base_in) = $resultado (base $base_out)"

unset base_origen
unset base_destino
unset numero
unset base_in
unset base_out