@echo off
echo Factorizacion

set /p usuario=Indica un numero a Factorizar: 
set resultado=1
set numero=%usuario%

:loop
if %numero% GTR 1 (
    set /a resultado=resultado*numero
    set /a numero=numero-1
    goto loop
) else (
    echo Resultado: %resultado%
    goto fin
)
:fin
echo adios