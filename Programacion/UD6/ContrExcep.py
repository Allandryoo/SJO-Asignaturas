class ErrorCantidadMinima(Exception):
    pass
class ErrorCantidadMaxima(Exception):
    pass
class ErrorNegativo(Exception):
    pass

def validar_negativo(numero):
    if numero < 0:
        raise ErrorNegativo("No puedes ingresar un cantidad negativa")

def validar_maximo(numero):
    if numero < 0:
        raise ErrorCantidadMaxima("Cantidad maxima a ingresar 50.000€")

def validar_minimo(numero):
    if numero < 0:
        raise ErrorCantidadMinima("Cantidad minima a ingresar 5€")
    
class cliente:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

    def ingresar_dinero(self, cantidad):
        self.saldo = self.saldo + cantidad
        print("Saldo actualizado")

    def retirar_dinero(self, cantidad):
        self.saldo = self.saldo - cantidad

c1 = cliente("A", 1000)

while True:
    try:
        print(f"Saldo: {c1.saldo}")
        cantidad = int(input("Indica la cantidad a ingresar\n"))
        validar_maximo(cantidad)
        validar_minimo(cantidad)
        validar_negativo(cantidad)
        c1.ingresar_dinero(cantidad)
    except ErrorCantidadMaxima as max:
        print(max)
    except ErrorCantidadMinima as min:
        print(min)
    except ErrorNegativo as neg:
        print(neg)
        
