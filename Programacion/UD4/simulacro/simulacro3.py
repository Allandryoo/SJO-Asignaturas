from hmac import new


class Curso:
    def __init__(self, codigo, titulo, horas, precio):
        self.codigo = codigo
        self.titulo = titulo
        if horas <= 0:
            self.horas =0
        else:
            self.horas = horas
        self.precio = precio

    def mostrar_info(self):
        return f"Codigo:{self.codigo} | Titulo:{self.titulo} |Horas:{self.horas} | Precio:{self.precio}"

    def precio_final(self):
        preciofinal = self.horas * self.precio
        return preciofinal


class CursoOnline(Curso):
    def __init__(self, codigo, titulo, horas, precio, plataforma):
        super().__init__(codigo, titulo, horas, precio)
        self.plataforma = plataforma

    def mostrar_info(self):
        return f"Codigo:{self.codigo} | Titulo:{self.titulo} | Horas:{self.horas} | Precio:{self.precio} | Plataforma:{self.plataforma}"

    def precio_final(self):
        preciofinal = self.horas * self.precio
        return preciofinal


class CursoPresencial(Curso):
    def __init__(self, codigo, titulo, horas, precio, aula):
        super().__init__(codigo, titulo, horas, precio)
        self.aula = aula

    def mostrar_info(self):
        return f"Codigo:{self.codigo} | Titulo:{self.titulo} | Horas:{self.horas} | Precio:{self.precio} | Aula:{self.aula}"

    def precio_final(self):
        if self.horas > 40:
            preciofinal = self.horas * (self.precio * 1.15)
            return preciofinal
        else:
            preciofinal = self.horas * self.precio
            return preciofinal


def crear_curso(tipo):
    codigocurso = int(input("Indica el codigo del curso: "))
    titulocurso = input("Indica el Titulo del curso: ")
    horascurso = input("Indica las horas del curso: ")
    preciocurso = input("Incdica el precio del curso: ")

    match tipo.upper():
        case "O":
            plataformacurso = input(
                "Indica la plataforma en la que se hara el curso:\n")
            return CursoOnline(codigocurso, titulocurso, horascurso, preciocurso, plataformacurso)
        case "P":
            aulacurso = input("Indica el aula del curso:\n")
            return CursoPresencial(codigocurso, titulocurso, horascurso, preciocurso, aulacurso)


def agregar_curso(tipo, curso_creado):
    match tipo.upper():
        case "O":
            cursos.update({curso_creado.codigo: {"titulo": curso_creado.titulo, "horas": curso_creado.horas,
                          "precio": curso_creado.precio, "plataforma": curso_creado.plataforma}})
        case "P":
            cursos.update({curso_creado.codigo: {"titulo": curso_creado.titulo,
                          "horas": curso_creado.horas, "precio": curso_creado.precio, "aula": curso_creado.aula}})


def menu():
    for key, value in opciones.items():
        print(f"Presiona {key} para: {value}.")


def mostrar_cursos():
    for key, value in cursos.items():
        print(
            f"Codigo:{key} | {value}")


salir = True
opciones = {
    "A": "Añadir curso",
    "M": "Mostrar informacion cursos",
    "P": "Calcular precio curso",
    "S": "Salir"
}
c1 = CursoPresencial(1, "DAW", 51, 12, "4A")
c2 = CursoPresencial(2, "DAM", 38, 12, "4A")
c3 = CursoOnline(3, "ASIX", 45, 11, "Netflix")

listacursos = [c1, c2, c3]

cursos = {}
for i in listacursos:
    cursos.update(
        {i.codigo: {"titulo": i.titulo, "horas": i.horas, "precio": i.precio}})

while salir:

    menu()
    opcion = input("")
    match opcion.upper():

        case "A":
            tipocurso = input("El curso es (O)online o (P)presencial\n")
            newcourse = crear_curso(tipocurso)
            agregar_curso(tipocurso, newcourse)

        case "M":
            mostrar_cursos()
