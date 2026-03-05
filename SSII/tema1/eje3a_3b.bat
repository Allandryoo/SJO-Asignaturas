@echo off

:inicio
cls

set contador=0
set sumador=0
set mayor=%1
set menor=%1

echo C: Contador de numeros introducidos.
echo P: Numero menor.
echo G: Numero mayor.
echo S: Suma de todos los numeros.
echo A: Todas las anteriores.
echo F: Finalizar programa.

set /p opcion=Escoge una opcion:

goto %opcion%

:C
for %%i in (%*) do (
    set /a contador=contador + 1
)
echo Hay %contador% numeros.
pause
goto inicio

:P
for %%i in (%*) do (
    if %%i LSS %menor% (
        set menor=%%i
    )
)
echo El numero menor es: %menor%.
pause
goto inicio

:G
for %%i in (%*) do (
    if %%i GTR %mayor% (
        set mayor=%%i
    )
)
echo El numero mayor es: %mayor%.
pause
goto inicio

:S
for %%i in (%*) do (
    set /a sumador=sumador + %%i
)
echo La suma total: %sumador%.
pause
goto inicio

:A
for %%i in (%*) do (

    if %%i GTR %mayor% (
        set mayor=%%i
    )
    if %%i LSS %menor% (
        set menor=%%i
    )
    set /a contador=contador + 1
    set /a sumador=sumador + %%i
)
echo Hay %contador% numeros.
echo La suma total: %sumador%.
echo El numero mayor es: %mayor%.
echo El numero menor es: %menor%.
pause
goto inicio

:F
echo Adios