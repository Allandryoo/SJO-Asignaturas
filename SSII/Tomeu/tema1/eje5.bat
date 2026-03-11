@echo off 

if "%1" == "" (
    echo Formato de uso correcto: %0 numero
    goto F
)

set numero=%1

set /a div=numero / 2
set /a div=div * 2 

if %div% EQU %numero% (
    echo %1 es par
    goto F
) else (
    echo %1 es impar
    goto F
)

:F
