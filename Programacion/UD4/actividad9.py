class tablet:

    def __init__(self, creador, tamano_pantalla, num_cores, apps, status):
        self.creador = creador
        self.tamano_pantalla = tamano_pantalla
        self.num_cores = num_cores
        self.apps = apps
        self.status = status

    def power_on(self):
        self.status = True

    def power_off(self):
        self.status = False

    def install_app(self, app_anadida):

        if app_anadida in self.apps:
            print("Esta app ya existe")
        else:
            self.apps.append(app_anadida)

    def uninstall_app(self, app_elimiada):

        if app_elimiada in self.apps:
            self.apps.remove(app_elimiada)
        else:
            print("Esta app no esta instalada")

    def getapps(self):
        return self.apps

    def getstatus(self):
        return self.status


apps = ["python", "java"]

tablet1 = tablet("alan", 14, 6, apps, False)
print(tablet1.getstatus())
print(tablet1.getapps())
tablet1.install_app("javascript")
print(tablet1.getapps())
tablet1.uninstall_app("jºgava")
print(tablet1.getapps())
tablet1.power_on()
print(tablet1.getstatus())
