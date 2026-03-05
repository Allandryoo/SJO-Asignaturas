@echo off

if "%1" == "" (
    echo Forma de uso correcto: %0 numero numero ...
)

:loop
if "%1" == "" (
    goto fin
)
set numero=%1

set /a div=numero / 2
set /a div=div * 2 

if %div% EQU %numero% (
    echo %1 es par
    shift
    goto loop
) else (
    echo %1 es impar
    shift
    goto loop
)

:fin 
echo Adios ;/