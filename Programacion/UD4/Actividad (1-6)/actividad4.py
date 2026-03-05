salir = False


class coche:

    def __init__(self, marca, modelo, potencia, color, matriculacion, siguiente_revision):
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
        self.color = color
        self.matriculacion = matriculacion
        self.siguiente_revision = siguiente_revision

    def mostrar(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Potencia: {self.potencia}, Color: {self.color}, Año matriculacion: {self.matriculacion}, Revision: {self.siguiente_revision}.")

    def acelerar(self):
        self.potencia = self.potencia + 10
        return self.potencia

    def frenar(self):
        self.potencia = self.potencia - 10
        return self.potencia

    def itv(self):
        self.matriculacion = 2025-self.matriculacion
        match self.matriculacion:

            case 1:
                print("Pasa la itv en 3 años")
            case 2:
                print("Pasa la itv en 2 años")
            case 3:
                print("Pasa la itv en 1 año")
            case 4:
                print("Tienes que pasar la itv")
            case 5:
                print("Pasa la itv en 1 año")
            case 6:
                print("Tienes que pasar la itv")
            case 7:
                print("Pasa la itv en 1 año")
            case 8:
                print("Tienes que pasar la itv")
            case _:
                print("Tienes que pasar la itv")


coche1 = coche("honda", "civic", 100, "rojo", 2024, 2023)


while not salir:

    opcion = input(
        "Escoge una opcion: a(acelerar), f(frenar), m(mostrar informacion), i(comprobar itv), s(salir)")

    match opcion:

        case "a":
            coche1.acelerar()
        case "f":
            coche1.frenar()
        case "m":
            coche1.mostrar()
        case "i":
            coche1.itv()
        case "s":
            salir = True
