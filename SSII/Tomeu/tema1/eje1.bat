@echo off

:Inicio

cls

echo CALCULADORA
echo S:Suma
echo R:Resta
echo D:Divison
echo M:Multiplicacion
echo E:Exit

Set /p opcion=Elige una opcion (S/R/D/M/E):

goto %opcion%

:S
set /p x=Introduce el primer numero:
set /a x<0 goto %opcion%
set /p y=Introduce el segundo numero:
set /a z=x+y
echo El resultado de la Suma de %x% y %y% es %z%
pause
goto inicio

:R
set /p x=Introduce el primer numero:
set /p y=Introduce el segundo numero:
set /a z=x-y
echo El resultado de la Resta de %x% menos %y% es %z%
pause
goto Inicio

:M
set /p x=Introduce el primer numero:
set /p y=Introduce el segundo numero:
set /a z=x*y
echo El resultado de la Multiplicacion de %x% y %y% es %z%
pause
goto inicio

:D
set /p x=Introduce el primer numero:
set /p y=Introduce el segundo numero:
set /a z=x/y
echo El resultado de la Divison de %x% y %y% es %z%
pause
goto inicio

:E
pause
exit