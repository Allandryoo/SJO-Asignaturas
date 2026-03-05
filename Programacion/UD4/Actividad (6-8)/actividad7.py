class libros:
    
    def __init__(self, titulo, autor, genero, paginas):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.paginas = paginas

    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor

    def get_genero(self):
        return self.genero
    
    def get_paginas(self):
        return self.paginas
    
    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_autor(self, autor):
        self.autor = autor

    def set_genero(self, genero):
        self.genero = genero

    def set_paginas(self, paginas):
        self.paginas = paginas

