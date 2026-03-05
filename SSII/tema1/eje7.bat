@echo off

if "%1" == "" (
    echo Forma de uso correcto: %0 numero numero ...
    goto F
)

:inicio
cls

echo E: Mostrar en orden si son pares e impares.
echo C: Agrupar numeros en pares e impares.
echo P: Mostrar solo los pares.
echo I: Mostrar solo los impares.
echo F: Finalizar programa.

set /p opcion=Escoge una opcion
goto %opcion%

:E 
for %%i in (%*) do (
    set /a div=%%i %% 2
    if %div% == 0 (
        echo %%i es par
    ) else (
        echo %%i es impar
    )
)
pause
goto inicio

:C
:loop
if "%1" == "" (
    goto F
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
pause
goto inicio

:p
echo Pares
for %%i in (%*) do (
    set /a div=%%i %% 2
    if %div% == 0 (
        echo %%i 
    )
)
pause
goto inicio

:I
echo Impares
for %%i in (%*) do (
    set /a div=%%i %% 2
    if not %div% == 0 (
        echo %%i 
    )
)
pause
goto inicio

:F
echo Adios ;/