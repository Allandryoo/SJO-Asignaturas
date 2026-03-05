class Material:
    def __init__(self, titulo, autor, fecha_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.fecha_publicacion = fecha_publicacion
        self.prestado = False

    def getTitulo(self):
        return self.titulo
    
    def getAutor(self):
        return self.autor
    
    def getFecha_publicacion(self):
        return self.fecha_publicacion
    
    def getPrestado(self):
        return self.prestado
    
    def setTitulo(self, newtit):
        self.titulo = newtit

    def setAutor(self, newaut):
        self.autor = newaut

    def setFecha_publicacion(self, newfec):
        self.fecha_publicacion = newfec

    def setPrestado(self, newpre):
        self.prestado = newpre

    def prestar(self):
        if self.prestado == True:
            print("Prestado")
        else:
            self.setPrestado(True)

    def devolver(self):
        self.setPrestado(False)

    def mostrar_info(self):
        if self.prestado == True:
            return f"Titulo: {self.titulo} | Autor: {self.autor} | Año: {self.fecha_publicacion} | Estado: No disponible"
        else:
            return f"Titulo: {self.titulo} | Autor: {self.autor} | Año: {self.fecha_publicacion} | Estado: Disponible"
        
class Libro(Material):
    def __init__(self, titulo, autor, fecha_publicacion, num_paginas):
        super().__init__(titulo, autor, fecha_publicacion)
        self.num_paginas = num_paginas

def mostrar_info(self):
    if self.prestado == True:
        return f"Titulo: {self.titulo} | Autor: {self.autor} | Año: {self.fecha_publicacion} | Numero de paginas: {self.num_paginas} | Estado: No disponible"
    else:
        return f"Titulo: {self.titulo} | Autor: {self.autor} | Año: {self.fecha_publicacion} | Numero de paginas: {self.num_paginas} | Estado: Disponible"

class Revista(Material):
    def __init__(self, titulo, autor, fecha_publicacion, num_edicion):
        super().__init__(titulo, autor, fecha_publicacion)
        self.num_edicion = num_edicion

    def mostrar_info(self):
        if self.prestado == True:
            return f"Titulo: {self.titulo} | Autor: {self.autor} | Año: {self.fecha_publicacion} | Numero de edicion: {self.num_edicion} | Estado: No disponible"
        else:
            return f"Titulo: {self.titulo} | Autor: {self.autor} | Año: {self.fecha_publicacion} | Numero de edicion: {self.num_edicion} | Estado: Disponible"
        
class Biblioteca:
    def __init__(self):
        self.lista_materiales=[]

    def agregar_material(self, material):
        self.lista_materiales.append(material)

    def mostrar_materiales(self):
        lista_mostrar=[]
        for i in self.lista_materiales:
            lista_mostrar.append(i.mostrar_info())
        
        return lista_mostrar

    def buscar_por_titulo(self, titulo):
        for i in self.lista_materiales:
            if i.titulo == titulo:
                i.mostrar_info()

biblio = Biblioteca()

libro1 = Libro("Python desde cero", "Alan edgar poe", 2023, 350)
revista1 = Revista("Programacion Hoy", "Alan walker", 2021, 42)

biblio.agregar_material(libro1)
biblio.agregar_material(revista1)

print(biblio.mostrar_materiales())