@echo off

if "%1" == "" (
    echo Manera correcta de uso: %0 numero1 numero2 
    goto final_programa
)

if "%2" == "" (
    echo Manera correcta de uso: %0 %1 numero2
    goto final_programa
)

set numero1=%1
set numero2=%2

if %numero1% LSS %numero2% (
    echo %numero2% es mayor que %numero1%
    goto final_programa
) else if %numero1% GTR %numero2% (
    echo %numero1% es mayor que %numero2%
    goto final_programa
) else (
    echo %numero1% es igual a %numero2%
    goto final_programa
)

:final_programa

