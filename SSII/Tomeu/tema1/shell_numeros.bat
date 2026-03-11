@echo off

set contador=0
set sumador=0
set mayor=%1
set menor=%1

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
echo Hay %contador% numeros
echo La suma total: %sumador%
echo El numero mayor es: %mayor%
echo El numero menor es: %menor%