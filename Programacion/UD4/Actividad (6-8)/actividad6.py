salir = False


class productos:

    def __init__(self, nombre, precio, descripcion, stock):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.stock = stock

    def getNombre(self):
        return self.nombre

    def getPrecio(self):
        return self.precio

    def getDescripcion(self):
        return self.descripcion

    def getStock(self):
        return f"{self.stock} unidades"

    def setNombre(self, newnom):
        self.nombre = newnom

    def setPrecio(self, newpri):
        self.precio = newpri

    def setDescripcion(self, newdes):
        self.descripcion = newdes

    def set_stock(self, newstk):
        self.stock = newstk

    def incrementar_stock(self):
        self.stock += 1

    def decrementar_stock(self):
        self.stock -= 1


producto1 = productos("RAM", 600.99, "la mas rapida de tota italia", 5)


print(producto1.getNombre())
producto1.setNombre("SSD")

print(producto1.getStock())
producto1.decrementar_stock()

print(producto1.getStock())
