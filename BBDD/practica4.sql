CREATE DATABASE biblioteca;
USE biblioteca;

CREATE TABLE Usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    tipo_usuario ENUM('estudiante', 'profesor') NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE Libros (
    id_libro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    anio_publicacion YEAR NOT NULL,
    disponibles INT DEFAULT 1,
    CHECK (disponibles >= 0)
);

CREATE TABLE Copia_Libros (
    id_copia INT AUTO_INCREMENT PRIMARY KEY,
    id_libro INT,
    estado ENUM('disponible', 'prestado', 'perdido') DEFAULT 'disponible',
    FOREIGN KEY (id_libro) REFERENCES Libros(id_libro)
);

CREATE TABLE Prestamos (
    id_prestamo INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_copia INT,
    fecha_prestamo DATE NOT NULL,
    fecha_devolucion DATE DEFAULT NULL,
    devuelto BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
    FOREIGN KEY (id_copia) REFERENCES Copia_Libros(id_copia)
);

INSERT INTO Usuarios (nombre, tipo_usuario, email) VALUES
('Ana López', 'estudiante', 'ana@mail.com'),
('Carlos Ruiz', 'estudiante', 'carlos@mail.com'),
('Lucía Gómez', 'estudiante', 'lucia@mail.com'),
('Dr. Pérez', 'profesor', 'perez@mail.com'),
('Dra. Sánchez', 'profesor', 'sanchez@mail.com');

INSERT INTO Libros (titulo, autor, anio_publicacion, disponibles) VALUES
('SQL Básico', 'Autor A', 2010, 3),
('Bases de Datos', 'Autor B', 2015, 2),
('Programación Web', 'Autor C', 2020, 4),
('Algoritmos', 'Autor D', 2005, 2),
('Redes', 'Autor E', 2012, 1),
('IA Moderna', 'Autor F', 2022, 2),
('Sistemas Operativos', 'Autor G', 2008, 1);

INSERT INTO Copia_Libros (id_libro) VALUES
(1),(1),(1),
(2),(2),
(3),(3),(3),(3),
(4),(4),
(5),
(6),(6),
(7);

DELIMITER //

CREATE TRIGGER before_insert_prestamo
BEFORE INSERT ON Prestamos
FOR EACH ROW
BEGIN
    DECLARE prestamos_actuales INT;
    DECLARE tipo VARCHAR(20);

    SELECT tipo_usuario INTO tipo
    FROM Usuarios
    WHERE id_usuario = NEW.id_usuario;

    SELECT COUNT(*) INTO prestamos_actuales
    FROM Prestamos
    WHERE id_usuario = NEW.id_usuario AND devuelto = FALSE;

    IF tipo = 'estudiante' AND prestamos_actuales >= 3 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Límite de préstamos alcanzado (estudiante)';
    END IF;

    IF tipo = 'profesor' AND prestamos_actuales >= 5 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Límite de préstamos alcanzado (profesor)';
    END IF;

END //

DELIMITER ;


DELIMITER //

CREATE TRIGGER before_insert_fecha
BEFORE INSERT ON Prestamos
FOR EACH ROW
BEGIN
    DECLARE dias INT;
    DECLARE tipo VARCHAR(20);

    SELECT tipo_usuario INTO tipo
    FROM Usuarios
    WHERE id_usuario = NEW.id_usuario;

    IF tipo = 'estudiante' THEN
        SET dias = 15;
    ELSE
        SET dias = 30;
    END IF;

    SET NEW.fecha_devolucion = DATE_ADD(NEW.fecha_prestamo, INTERVAL dias DAY);
END //

DELIMITER ;

INSERT INTO Prestamos (id_usuario, id_copia, fecha_prestamo)
VALUES
(1,1,'2026-01-01'),
(1,2,'2026-01-05'),
(2,3,'2026-02-01'),
(3,4,'2026-02-10'),
(4,5,'2026-03-01'),
(5,6,'2026-03-05'),
(4,7,'2026-03-10'),
(5,8,'2026-03-15'),
(2,9,'2026-04-01'),
(3,10,'2026-04-05');

SET GLOBAL event_scheduler = ON;

DELIMITER //

CREATE EVENT marcar_perdidos
ON SCHEDULE EVERY 1 DAY
DO
BEGIN
    UPDATE Copia_Libros c
    JOIN Prestamos p ON c.id_copia = p.id_copia
    SET c.estado = 'perdido'
    WHERE p.devuelto = FALSE
    AND p.fecha_prestamo < DATE_SUB(CURDATE(), INTERVAL 6 MONTH);
END //

DELIMITER ;


-- 1 Usuarios con nº préstamos
SELECT u.id_usuario, u.nombre, COUNT(p.id_prestamo) AS prestamos
FROM Usuarios u
LEFT JOIN Prestamos p ON u.id_usuario = p.id_usuario AND p.devuelto = FALSE
GROUP BY u.id_usuario;

-- 2 Libros más prestados
SELECT l.id_libro, l.titulo, COUNT(p.id_prestamo) AS total
FROM Libros l
JOIN Copia_Libros c ON l.id_libro = c.id_libro
JOIN Prestamos p ON c.id_copia = p.id_copia
GROUP BY l.id_libro
HAVING total > 2;

-- 3 Usuarios con retrasos
SELECT u.id_usuario, u.nombre, l.id_libro, l.titulo,
DATEDIFF(CURDATE(), p.fecha_devolucion) AS dias_retraso
FROM Prestamos p
JOIN Usuarios u ON p.id_usuario = u.id_usuario
JOIN Copia_Libros c ON p.id_copia = c.id_copia
JOIN Libros l ON c.id_libro = l.id_libro
WHERE p.devuelto = FALSE
AND CURDATE() > p.fecha_devolucion;

-- 4 Últimos 10 préstamos
SELECT u.id_usuario, u.nombre, u.tipo_usuario, p.fecha_prestamo
FROM Prestamos p
JOIN Usuarios u ON p.id_usuario = u.id_usuario
ORDER BY p.fecha_prestamo DESC
LIMIT 10;

-- 5 Libro más popular
SELECT l.id_libro, l.titulo, COUNT(*) AS total
FROM Libros l
JOIN Copia_Libros c ON l.id_libro = c.id_libro
JOIN Prestamos p ON c.id_copia = p.id_copia
GROUP BY l.id_libro
ORDER BY total DESC
LIMIT 1;

-- 6 Libro más antiguo disponible
SELECT l.id_libro, l.titulo, l.anio_publicacion, COUNT(c.id_copia) AS copias
FROM Libros l
JOIN Copia_Libros c ON l.id_libro = c.id_libro
WHERE c.estado = 'disponible'
GROUP BY l.id_libro
ORDER BY l.anio_publicacion ASC
LIMIT 1;