
class CuentaBancaria:
    def __init__(self, nombre, saldo, iban):
        self.nombre = nombre
        self.saldo = saldo
        self.iban = iban

    def obtener_saldo(self):
        print(f"{self.nombre} tu saldo actual: {self.saldo}€")

    def depositar(self, cantidaddeposito):
        if cantidaddeposito < 0:
            print("No puede ingresar una cantidad negativa")
        else:
            self.saldo = self.saldo + cantidaddeposito
            print(
                f"{self.nombre} has ingresado {cantidaddeposito}, Tu saldo ahora es de: {self.saldo}€")

    def retirar(self, cantidadretirada):
        if cantidadretirada <= self.saldo:
            self.saldo = self.saldo - cantidadretirada
            print(
                f"{self.nombre} has retirado {cantidadretirada}, Tu saldo ahora es de: {self.saldo}€")
        elif cantidadretirada < 0:
            print("No puede retirar una cantidad negativa")
        else:
            print("No dispone de tanta cantidad")

    def transferencia(self, cantidatransferir, cuentadestino):
        if cantidatransferir <= self.saldo and cantidatransferir > 0:
            cuentadestino.saldo = cuentadestino.saldo + cantidatransferir
            self.saldo = self.saldo - cantidatransferir
            print(
                f"{self.nombre} has enviado {cantidatransferir}€ a {cuentadestino.nombre} con IBAN:{cuentadestino.iban}")
        else:
            print("Cantidad erronea")


class CuentaRecompensa(CuentaBancaria):
    def __init__(self, nombre, saldo, iban):
        super().__init__(nombre, saldo, iban)

    def obtener_saldo(self):
        print(f"{self.nombre} tu saldo actual: {self.saldo}€")

    def transferencia(self, cantidatransferir, cuentadestino):
        if cantidatransferir <= self.saldo and cantidatransferir > 0:
            cuentadestino.saldo = cuentadestino.saldo + cantidatransferir
            self.saldo = self.saldo - cantidatransferir
            print(
                f"{self.nombre} has enviado {cantidatransferir}€ a {cuentadestino.nombre} con IBAN:{cuentadestino.iban}")
        else:
            print("Cantidad erronea")

    def depositar(self, cantidaddeposito):
        if cantidaddeposito < 0:
            print("No puede ingresar una cantidad negativa")
        else:
            self.saldo = self.saldo + (cantidaddeposito * 1.05)
            print(
                f"{self.nombre} has ingresado {cantidaddeposito}€ y se te ha añadido una bonificacion del 5%, Total:{cantidaddeposito*1.05}")

    def retirar(self, cantidadretirada):
        if cantidadretirada <= self.saldo:
            self.saldo = self.saldo - cantidadretirada
            print(
                f"{self.nombre} has retirado: {cantidadretirada}€, Saldo actual:{self.saldo}€")
        elif cantidadretirada < 0:
            print("No puede retirar una cantidad negativa")
        else:
            print("No dispone de tanta cantidad")


class CuentaAhorros(CuentaBancaria):
    def __init__(self, nombre, saldo, iban):
        super().__init__(nombre, saldo, iban)

    def obtener_saldo(self):
        print(f"{self.nombre} tu saldo actual: {self.saldo}€")

    def transferencia(self, cantidatransferir, cuentadestino):
        if cantidatransferir <= self.saldo and cantidatransferir > 0:
            cuentadestino.saldo = cuentadestino.saldo + cantidatransferir
            self.saldo = self.saldo - cantidatransferir
            print(
                f"{self.nombre} has enviado {cantidatransferir}€ a {cuentadestino.nombre} con IBAN:{cuentadestino.iban}")
        else:
            print("Cantidad erronea")

    def depositar(self, cantidaddeposito):
        if cantidaddeposito < 0:
            print("No puede ingresar una cantidad negativa")
        else:
            self.saldo = self.saldo + cantidaddeposito
            print(
                f"{self.nombre} has ingresado {cantidaddeposito}, Tu saldo ahora es de: {self.saldo}€")

    def retirar(self, cantidadretirada):
        if (cantidadretirada + 5) <= self.saldo and cantidadretirada > 0:
            self.saldo = self.saldo - cantidadretirada - 5
            print(
                f"{self.nombre} has retirado: {cantidadretirada} - 5€ de comision de retiro, Saldo actual:{self.saldo}.")
        elif cantidadretirada < 0:
            print("No puede retirar una cantidad negativa")
        else:
            print("No dispone de la cantidad suficiente")


cuenta1 = CuentaBancaria("Alan", 3000, 12345)
cuenta2 = CuentaBancaria("Carlos", 100, 23456)

cuentainteres = CuentaRecompensa("Daniel", 1000, 34567)

cuentahorros = CuentaAhorros("Juan", 1000, 45678)

print(f"{cuenta1.nombre}, saldo {cuenta1.saldo}€ con IBAN: {cuenta1.iban}")
print(f"{cuenta2.nombre}, saldo {cuenta2.saldo}€ con IBAN: {cuenta2.iban}")

cuenta1.depositar(-100)
cuenta1.obtener_saldo()
cuenta1.retirar(15000)
cuenta1.obtener_saldo()
cuenta2.obtener_saldo()
cuenta1.transferencia(10700, cuenta2)
cuenta2.obtener_saldo()

cuentainteres.obtener_saldo()
cuentainteres.depositar(-12)
cuentainteres.obtener_saldo()

cuentahorros.obtener_saldo()
cuentahorros.retirar(200000)
cuentahorros.obtener_saldo()
