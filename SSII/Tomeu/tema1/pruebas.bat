if "%1"=="" goto aiuda

set NumOriginal=%1

set /a calculo=NumOriginal/2
set /a calculo=calculo*2

if %calculo% equ %NumOriginal% (
    echo El numero %NumOriginal% es PAR.
) else (
    echo El numero %NumOriginal% es IMPAR.
)

goto final

:aiuda
echo.
echo La forma correcta de usar el programa es:
echo parimpar.bat "numero"
echo.

:final