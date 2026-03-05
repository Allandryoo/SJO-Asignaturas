#!/bin/bash
if [ -z $1 ]
then
echo "Formato de uso: $0 parametro1 parametro2"
else
if [ -z $2 ]
then
echo "Formato de uso: $0 $1 parametro2"
fi
fi

if [[ "$1" < "$2" ]]
then
echo "$2 es mayor"
else
if [[ "$1" > "$2" ]]
then
echo "$1 es mayor"
else
if [[ "$1" == "$2" ]]
then
echo "Son iguales"
fi
fi
fi