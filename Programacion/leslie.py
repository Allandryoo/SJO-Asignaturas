from abc import ABC, abstractmethod
class Empleado:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    @abstractmethod
    def calcular_salario(self):
        pass

class EmpleadoMensual(Empleado):
    def __init__(self, id, nombre, salario, irpf):
        super().__init__(id, nombre)
        self.salario = salario
        self.irpf = irpf

    def calcular_salario(self):
        salarioneto = self.salario-(self.salario*self.irpf)
        return salarioneto

class EmpleadoHoras(Empleado):
    def __init__(self, id, nombre, numhoras, preciohoras):
        super().__init__(id, nombre)
        self.numhoras = numhoras
        self.preciohoras = preciohoras

    def calcular_salario(self):
        salarioneto = self.numhoras * self.preciohoras
        return salarioneto
    
class EmpleadoTrabajo(Empleado):
    def __init__(self, id, nombre, numt, preciot):
        super().__init__(id, nombre)
        self.numt = numt
        self.preciot = preciot

    def calcular_salario(self):
        salarioneto = self.numt * self.preciot
        return salarioneto


empleado1=EmpleadoMensual(1,"Alan",2200,0.10)
empleado2=EmpleadoHoras(2,"Duki",140,12)
empleado4=EmpleadoTrabajo(4,"jasl",5,200)
print(empleado1.calcular_salario())
print(empleado2.calcular_salario())

empleado3=Empleado(1,"jota")

print(empleado1.nombre)
print(empleado4.calcular_salario())