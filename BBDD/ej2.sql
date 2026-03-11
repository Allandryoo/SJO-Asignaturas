CREATE DATABASE practica_2;
USE practica_2;

CREATE TABLE Libros (
	ISBN INT PRIMARY KEY NOT NULL,
    Titulo VARCHAR(50) NOT NULL,
    Descripcion VARCHAR(300),
    Num_Paginas INT NOT NULL,
    Precio DECIMAL (5,2) NOT NULL,
    IdEditorial INT,
    FOREIGN KEY (IdEditorial) REFERENCES Editoriales(IdEditorial)
);

CREATE TABLE Autores (
	IdAutor INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(30) NOT NULL,
    Fecha_Nacimiento DATE,
    Nacionalidad VARCHAR(20),
    Precio DECIMAL (5,2) NOT NULL
);

CREATE TABLE Clientes (
	DNI INT,
    Nombre VARCHAR(30),
    Fecha_Nacimiento ,
    Direccion,
);

CREATE TABLE Categorias (
	IdCategoria INT PRIMARY KEY AUTO_INCREMENT,
    Categoria
);

CREATE TABLE Editoriales (
	IdEditorial INT PRIMARY KEY AUTO_INCREMENT,
    Editorial
);

CREATE TABLE Prestamos (
	IdPrestamo INT PRIMARY KEY AUTO_INCREMENT,
    Libro,
    Cliente,
    Fecha_Prestamo,
    Fecha_Devolucion
);