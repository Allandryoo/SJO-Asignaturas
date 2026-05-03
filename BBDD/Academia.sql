CREATE DATABASE academia_allandryo_santos;
USE academia_allandryo_santos;

CREATE TABLE Estudiantes (
    IdEstudiante INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    FechaNacimiento DATE NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Direccion VARCHAR(150),
    Telefono VARCHAR(20),
    FechaRegistro DATETIME DEFAULT NOW()
);

CREATE TABLE Profesores (
    IdProfesor INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Especialidad VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Salario DECIMAL(10, 2) NOT NULL,
    CHECK (Salario > 0)
);

CREATE TABLE Cursos (
    IdCurso INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL,
    Descripcion TEXT,
    DuracionHoras INT NOT NULL,
    IdProfesor INT NOT NULL,
    FechaInicio DATE NOT NULL,
    FechaFin DATE NOT NULL,
    CHECK (DuracionHoras > 0),
    CHECK (FechaFin > FechaInicio),
    FOREIGN KEY (IdProfesor) REFERENCES Profesores(IdProfesor)
);

CREATE TABLE Matriculas (
    IdMatricula INT PRIMARY KEY AUTO_INCREMENT,
    IdEstudiante INT NOT NULL,
    IdCurso INT NOT NULL,
    FechaInscripcion DATETIME DEFAULT NOW(),
    Estado ENUM('Activo', 'Finalizado', 'Cancelado') DEFAULT 'Activo',
    FOREIGN KEY (IdEstudiante) REFERENCES Estudiantes(IdEstudiante),
    FOREIGN KEY (IdCurso) REFERENCES Cursos(IdCurso)
);

CREATE TABLE Pagos (
    IdPago INT PRIMARY KEY AUTO_INCREMENT,
    IdMatricula INT NOT NULL,
    Monto DECIMAL(10, 2) NOT NULL,
    FechaPago DATETIME DEFAULT NOW(),
    MetodoPago ENUM('Efectivo', 'Tarjeta', 'Transferencia') NOT NULL,
    CHECK (Monto > 0),
    FOREIGN KEY (IdMatricula) REFERENCES Matriculas(IdMatricula)
);

INSERT INTO Estudiantes (Nombre, Apellido, FechaNacimiento, Email, Direccion, Telefono) VALUES
('Carlos', 'García', '2000-03-15', 'carlos.garcia@email.com', 'Calle Mayor 10, Madrid', '612345678'),
('María', 'López', '1999-07-22', 'maria.lopez@email.com', 'Av. Libertad 5, Barcelona', '623456789'),
('Juan', 'Martínez', '2001-01-10', 'juan.martinez@email.com', 'Plaza España 3, Valencia', '634567890'),
('Ana', 'Fernández', '1998-11-05', 'ana.fernandez@email.com', 'Calle Sol 8, Sevilla', '645678901'),
('Pedro', 'Sánchez', '2002-06-18', 'pedro.sanchez@email.com', 'Calle Luna 12, Málaga', '656789012'),
('Laura', 'Ramírez', '2000-09-30', 'laura.ramirez@email.com', 'Av. Constitución 7, Zaragoza', '667890123'),
('Diego', 'Torres', '1997-04-25', 'diego.torres@email.com', 'Calle Real 20, Bilbao', '678901234'),
('Sofía', 'Moreno', '2001-12-03', 'sofia.moreno@email.com', 'Paseo del Prado 15, Madrid', '689012345'),
('Andrés', 'Jiménez', '1999-02-14', 'andres.jimenez@email.com', 'Calle Olmo 9, Granada', '690123456'),
('Lucía', 'Ruiz', '2003-08-08', 'lucia.ruiz@email.com', 'Av. Andalucía 22, Córdoba', '601234567'),
('Miguel', 'Hernández', '2000-05-19', 'miguel.hernandez@email.com', 'Calle Norte 4, Valladolid', '612345679'),
('Elena', 'Díaz', '1998-10-27', 'elena.diaz@email.com', 'Calle Sur 6, Alicante', '623456780'),
('Pablo', 'Álvarez', '2002-03-11', 'pablo.alvarez@email.com', 'Plaza Mayor 1, Salamanca', '634567891'),
('Carmen', 'Romero', '2001-07-07', 'carmen.romero@email.com', 'Calle Ancha 14, Toledo', '645678902'),
('Jorge', 'Navarro', '1999-09-16', 'jorge.navarro@email.com', 'Av. Portugal 30, Badajoz', '656789013'),
('Isabel', 'Domínguez', '2000-01-28', 'isabel.dominguez@email.com', 'Calle Flores 11, Murcia', '667890124'),
('Raúl', 'Vega', '1997-06-04', 'raul.vega@email.com', 'Paseo Marítimo 8, Cádiz', '678901235'),
('Patricia', 'Castro', '2003-11-21', 'patricia.castro@email.com', 'Calle Nueva 5, Huelva', '689012346'),
('Fernando', 'Ortega', '1998-04-09', 'fernando.ortega@email.com', 'Av. América 17, Vigo', '690123457'),
('Claudia', 'Guerrero', '2001-08-13', 'claudia.guerrero@email.com', 'Calle Vieja 2, Gijón', '601234568'),
('Adrián', 'Santos', '2000-12-25', 'adrian.santos@email.com', 'Plaza del Carmen 9, Pamplona', '612345670'),
('Natalia', 'Iglesias', '1999-05-31', 'natalia.iglesias@email.com', 'Calle Río 16, Logroño', '623456781'),
('Sergio', 'Medina', '2002-10-02', 'sergio.medina@email.com', 'Av. Europa 25, Santander', '634567892'),
('Marta', 'Garrido', '2001-02-17', 'marta.garrido@email.com', 'Calle Parque 13, Oviedo', '645678903'),
('Alejandro', 'Cortés', '1998-07-20', 'alejandro.cortes@email.com', 'Calle Monte 7, San Sebastián', '656789014');

INSERT INTO Profesores (Nombre, Apellido, Especialidad, Email, Salario) VALUES
('Roberto', 'Méndez', 'Programación', 'roberto.mendez@academia.com', 2800.00),
('Silvia', 'Peña', 'Bases de Datos', 'silvia.pena@academia.com', 2650.00),
('Francisco', 'Lara', 'Redes', 'francisco.lara@academia.com', 2500.00),
('Teresa', 'Blanco', 'Diseño Web', 'teresa.blanco@academia.com', 2700.00),
('Alberto', 'Crespo', 'Inteligencia Artificial', 'alberto.crespo@academia.com', 3200.00),
('Beatriz', 'Serrano', 'Ciberseguridad', 'beatriz.serrano@academia.com', 3000.00),
('Manuel', 'Molina', 'Sistemas Operativos', 'manuel.molina@academia.com', 2550.00),
('Cristina', 'Suárez', 'Matemáticas', 'cristina.suarez@academia.com', 2400.00),
('Javier', 'Marín', 'Marketing Digital', 'javier.marin@academia.com', 2600.00),
('Rosa', 'Gil', 'Desarrollo Móvil', 'rosa.gil@academia.com', 2750.00),
('Enrique', 'Pascual', 'Cloud Computing', 'enrique.pascual@academia.com', 3100.00),
('Dolores', 'Herrera', 'DevOps', 'dolores.herrera@academia.com', 2900.00),
('Óscar', 'Fuentes', 'Machine Learning', 'oscar.fuentes@academia.com', 3300.00),
('Pilar', 'Cabrera', 'Análisis de Datos', 'pilar.cabrera@academia.com', 2850.00),
('Tomás', 'Vargas', 'Programación Web', 'tomas.vargas@academia.com', 2700.00),
('Inés', 'Campos', 'UX/UI', 'ines.campos@academia.com', 2650.00),
('Luis', 'Reyes', 'Blockchain', 'luis.reyes@academia.com', 3150.00),
('Gloria', 'León', 'Testing QA', 'gloria.leon@academia.com', 2500.00),
('Ramón', 'Aguilar', 'Big Data', 'ramon.aguilar@academia.com', 3050.00),
('Alicia', 'Prieto', 'IoT', 'alicia.prieto@academia.com', 2800.00),
('Víctor', 'Nieto', 'Robótica', 'victor.nieto@academia.com', 2950.00),
('Esperanza', 'Giménez', 'Inglés Técnico', 'esperanza.gimenez@academia.com', 2300.00),
('Daniel', 'Esteban', 'Gestión de Proyectos', 'daniel.esteban@academia.com', 2750.00),
('Marina', 'Vera', 'Contabilidad', 'marina.vera@academia.com', 2450.00),
('Gonzalo', 'Soto', 'Estadística', 'gonzalo.soto@academia.com', 2600.00);

INSERT INTO Cursos (Nombre, Descripcion, DuracionHoras, IdProfesor, FechaInicio, FechaFin) VALUES
('Java Avanzado', 'Programación orientada a objetos con Java', 120, 1, '2025-09-01', '2025-12-20'),
('SQL y MySQL', 'Gestión de bases de datos relacionales', 80, 2, '2025-09-15', '2025-11-30'),
('Redes Cisco CCNA', 'Certificación CCNA de Cisco', 100, 3, '2025-10-01', '2026-01-15'),
('HTML5, CSS3 y JS', 'Desarrollo frontend moderno', 90, 4, '2025-09-01', '2025-11-30'),
('Python para IA', 'Introducción a la IA con Python', 150, 5, '2025-10-15', '2026-03-15'),
('Hacking Ético', 'Fundamentos de ciberseguridad ofensiva', 110, 6, '2025-11-01', '2026-02-28'),
('Linux Administración', 'Administración de sistemas Linux', 70, 7, '2025-09-01', '2025-11-15'),
('Cálculo y Álgebra', 'Matemáticas para ingeniería', 60, 8, '2025-09-15', '2025-11-30'),
('SEO y SEM', 'Posicionamiento en buscadores', 50, 9, '2025-10-01', '2025-12-01'),
('Flutter y Dart', 'Desarrollo de apps móviles multiplataforma', 100, 10, '2025-09-15', '2026-01-15'),
('AWS Cloud Practitioner', 'Fundamentos de Amazon Web Services', 80, 11, '2025-10-01', '2025-12-20'),
('Docker y Kubernetes', 'Contenerización y orquestación', 90, 12, '2025-11-01', '2026-02-15'),
('Deep Learning', 'Redes neuronales profundas con TensorFlow', 130, 13, '2025-10-15', '2026-03-01'),
('Power BI', 'Visualización de datos empresariales', 60, 14, '2025-09-01', '2025-11-01'),
('React.js', 'Desarrollo de SPAs con React', 100, 15, '2025-09-15', '2026-01-15'),
('Figma Profesional', 'Diseño de interfaces con Figma', 50, 16, '2025-10-01', '2025-12-01'),
('Solidity y Web3', 'Desarrollo de smart contracts', 110, 17, '2025-11-01', '2026-02-28'),
('Selenium y Testing', 'Automatización de pruebas de software', 70, 18, '2025-09-01', '2025-11-15'),
('Hadoop y Spark', 'Procesamiento de datos masivos', 120, 19, '2025-10-15', '2026-02-15'),
('Arduino y Sensores', 'Proyectos IoT con Arduino', 80, 20, '2025-09-15', '2025-12-20'),
('ROS y Drones', 'Programación de robots y drones', 100, 21, '2025-10-01', '2026-01-15'),
('Business English', 'Inglés para el entorno profesional', 60, 22, '2025-09-01', '2025-11-30'),
('Scrum Master', 'Metodologías ágiles y Scrum', 40, 23, '2025-10-01', '2025-11-15'),
('Excel Financiero', 'Excel aplicado a contabilidad', 50, 24, '2025-09-15', '2025-11-30'),
('R para Estadística', 'Análisis estadístico con R', 70, 25, '2025-10-01', '2025-12-20');

INSERT INTO Matriculas (IdEstudiante, IdCurso, FechaInscripcion, Estado) VALUES
(1, 1, '2025-08-20 10:00:00', 'Activo'),
(2, 2, '2025-08-22 11:30:00', 'Activo'),
(3, 3, '2025-09-01 09:00:00', 'Activo'),
(4, 4, '2025-08-25 14:00:00', 'Finalizado'),
(5, 5, '2025-09-10 16:00:00', 'Activo'),
(6, 6, '2025-10-05 10:30:00', 'Cancelado'),
(7, 7, '2025-08-18 08:45:00', 'Finalizado'),
(8, 8, '2025-08-30 12:00:00', 'Activo'),
(9, 9, '2025-09-05 15:15:00', 'Activo'),
(10, 10, '2025-08-28 09:30:00', 'Finalizado'),
(11, 11, '2025-09-12 11:00:00', 'Activo'),
(12, 12, '2025-10-01 13:00:00', 'Cancelado'),
(13, 13, '2025-09-08 10:00:00', 'Activo'),
(14, 14, '2025-08-20 14:30:00', 'Finalizado'),
(15, 15, '2025-08-26 16:45:00', 'Activo'),
(16, 16, '2025-09-03 08:00:00', 'Activo'),
(17, 17, '2025-10-10 09:15:00', 'Cancelado'),
(18, 18, '2025-08-19 11:30:00', 'Finalizado'),
(19, 19, '2025-09-15 10:00:00', 'Activo'),
(20, 20, '2025-08-29 13:45:00', 'Activo'),
(21, 21, '2025-09-07 15:00:00', 'Activo'),
(22, 22, '2025-08-21 09:00:00', 'Finalizado'),
(23, 23, '2025-09-02 12:30:00', 'Activo'),
(24, 24, '2025-08-27 14:00:00', 'Activo'),
(25, 25, '2025-09-11 10:30:00', 'Activo');

INSERT INTO Pagos (IdMatricula, Monto, FechaPago, MetodoPago) VALUES
(1, 450.00, '2025-08-20 10:15:00', 'Tarjeta'),
(2, 320.00, '2025-08-22 11:45:00', 'Transferencia'),
(3, 500.00, '2025-09-01 09:30:00', 'Efectivo'),
(4, 380.00, '2025-08-25 14:20:00', 'Tarjeta'),
(5, 600.00, '2025-09-10 16:30:00', 'Transferencia'),
(6, 420.00, '2025-10-05 10:50:00', 'Efectivo'),
(7, 280.00, '2025-08-18 09:00:00', 'Tarjeta'),
(8, 250.00, '2025-08-30 12:15:00', 'Transferencia'),
(9, 200.00, '2025-09-05 15:30:00', 'Efectivo'),
(10, 400.00, '2025-08-28 09:45:00', 'Tarjeta'),
(11, 350.00, '2025-09-12 11:20:00', 'Transferencia'),
(12, 380.00, '2025-10-01 13:15:00', 'Efectivo'),
(13, 550.00, '2025-09-08 10:30:00', 'Tarjeta'),
(14, 240.00, '2025-08-20 14:45:00', 'Transferencia'),
(15, 420.00, '2025-08-26 17:00:00', 'Efectivo'),
(16, 200.00, '2025-09-03 08:30:00', 'Tarjeta'),
(17, 460.00, '2025-10-10 09:30:00', 'Transferencia'),
(18, 280.00, '2025-08-19 11:45:00', 'Efectivo'),
(19, 500.00, '2025-09-15 10:20:00', 'Tarjeta'),
(20, 330.00, '2025-08-29 14:00:00', 'Transferencia'),
(21, 400.00, '2025-09-07 15:15:00', 'Efectivo'),
(22, 250.00, '2025-08-21 09:20:00', 'Tarjeta'),
(23, 180.00, '2025-09-02 12:45:00', 'Transferencia'),
(24, 220.00, '2025-08-27 14:30:00', 'Efectivo'),
(25, 300.00, '2025-09-11 10:45:00', 'Tarjeta');

-- 1.INNER JOIN

-- Consulta 1: Listar cada estudiante con el curso en el que está matriculado y su estado
SELECT e.Nombre, e.Apellido, c.Nombre AS Curso, m.Estado
FROM Estudiantes e
INNER JOIN Matriculas m ON e.IdEstudiante = m.IdEstudiante
INNER JOIN Cursos c ON m.IdCurso = c.IdCurso;

-- Consulta 2: Mostrar cada curso con el nombre completo del profesor que lo imparte
SELECT c.Nombre AS Curso, CONCAT(p.Nombre, ' ', p.Apellido) AS Profesor, p.Especialidad
FROM Cursos c
INNER JOIN Profesores p ON c.IdProfesor = p.IdProfesor;

-- Consulta 3: Detalle completo de pagos con datos del estudiante, curso y método de pago
SELECT CONCAT(e.Nombre, ' ', e.Apellido) AS Estudiante, c.Nombre AS Curso,
       pa.Monto, pa.MetodoPago, pa.FechaPago
FROM Pagos pa
INNER JOIN Matriculas m ON pa.IdMatricula = m.IdMatricula
INNER JOIN Estudiantes e ON m.IdEstudiante = e.IdEstudiante
INNER JOIN Cursos c ON m.IdCurso = c.IdCurso;

-- 2. LEFT JOIN

-- Consulta 4: Listar todos los profesores y sus cursos (incluyendo los que no tienen curso asignado)
SELECT CONCAT(p.Nombre, ' ', p.Apellido) AS Profesor, p.Especialidad,
       IFNULL(c.Nombre, 'Sin curso asignado') AS Curso
FROM Profesores p
LEFT JOIN Cursos c ON p.IdProfesor = c.IdProfesor;

-- Consulta 5: Listar todos los estudiantes y su pago (incluyendo los que aún no han pagado)
SELECT CONCAT(e.Nombre, ' ', e.Apellido) AS Estudiante,
       IFNULL(pa.Monto, 0) AS MontoPagado, IFNULL(pa.MetodoPago, 'Sin pago') AS Metodo
FROM Estudiantes e
LEFT JOIN Matriculas m ON e.IdEstudiante = m.IdEstudiante
LEFT JOIN Pagos pa ON m.IdMatricula = pa.IdMatricula;

-- 3. RIGHT JOIN 

-- Consulta 6: Listar todos los cursos y las matrículas asociadas (incluyendo cursos sin matrículas)
SELECT c.Nombre AS Curso, c.DuracionHoras,
       IFNULL(CONCAT(e.Nombre, ' ', e.Apellido), 'Sin estudiantes') AS Estudiante
FROM Estudiantes e
RIGHT JOIN Matriculas m ON e.IdEstudiante = m.IdEstudiante
RIGHT JOIN Cursos c ON m.IdCurso = c.IdCurso;

-- 4. SELF JOIN

-- Consulta 7: Listar pares de profesores que tienen el mismo salario
SELECT CONCAT(p1.Nombre, ' ', p1.Apellido) AS Profesor1,
       CONCAT(p2.Nombre, ' ', p2.Apellido) AS Profesor2,
       p1.Salario
FROM Profesores p1
INNER JOIN Profesores p2 ON p1.Salario = p2.Salario AND p1.IdProfesor < p2.IdProfesor;

-- 5. FUNCIONES DE CADENAS

-- Consulta 8: Nombre completo en mayúsculas, email en minúsculas y longitud del email
SELECT UPPER(CONCAT(e.Nombre, ' ', e.Apellido)) AS NombreCompleto,
       LOWER(e.Email) AS EmailMinusculas,
       LENGTH(e.Email) AS LongitudEmail
FROM Estudiantes e;

-- Consulta 9: Extraer el dominio del email de cada profesor y mostrar las 3 primeras letras del nombre
SELECT SUBSTRING(p.Nombre, 1, 3) AS Iniciales,
       p.Apellido,
       SUBSTRING(p.Email, LOCATE('@', p.Email) + 1) AS Dominio
FROM Profesores p;

-- 6. FUNCIONES DE AGREGACIÓN

-- Consulta 10: Número total de estudiantes matriculados por curso, con suma y media de pagos
SELECT c.Nombre AS Curso,
       COUNT(m.IdMatricula) AS TotalMatriculas,
       SUM(pa.Monto) AS TotalRecaudado,
       ROUND(AVG(pa.Monto), 2) AS PagoPromedio
FROM Cursos c
INNER JOIN Matriculas m ON c.IdCurso = m.IdCurso
INNER JOIN Pagos pa ON m.IdMatricula = pa.IdMatricula
GROUP BY c.Nombre;

-- Consulta 11: Salario máximo, mínimo y promedio de los profesores
SELECT COUNT(*) AS TotalProfesores,
       MAX(Salario) AS SalarioMaximo,
       MIN(Salario) AS SalarioMinimo,
       ROUND(AVG(Salario), 2) AS SalarioPromedio,
       SUM(Salario) AS NominaTotal
FROM Profesores;

-- Consulta 12: Número de matrículas por estado
SELECT Estado, COUNT(*) AS Cantidad
FROM Matriculas
GROUP BY Estado
ORDER BY Cantidad DESC;

-- 7. FUNCIONES DE FECHA Y HORA

-- Consulta 13: Edad actual de cada estudiante y días desde su registro
SELECT CONCAT(Nombre, ' ', Apellido) AS Estudiante,
       FechaNacimiento,
       TIMESTAMPDIFF(YEAR, FechaNacimiento, NOW()) AS Edad,
       DATEDIFF(NOW(), FechaRegistro) AS DiasRegistrado
FROM Estudiantes;

-- Consulta 14: Duración real de cada curso en días, y mes/año de inicio
SELECT Nombre AS Curso,
       YEAR(FechaInicio) AS AnioInicio,
       MONTH(FechaInicio) AS MesInicio,
       DAY(FechaInicio) AS DiaInicio,
       DATEDIFF(FechaFin, FechaInicio) AS DuracionDias
FROM Cursos;

-- Consulta 15: Pagos realizados en el año 2025, agrupados por mes
SELECT MONTH(FechaPago) AS Mes,
       COUNT(*) AS NumeroPagos,
       SUM(Monto) AS TotalRecaudado
FROM Pagos
WHERE YEAR(FechaPago) = 2025
GROUP BY MONTH(FechaPago)
ORDER BY Mes;

-- 8. OPERADORES LÓGICOS Y WILDCARDS

-- Consulta 16: Cursos que contengan la palabra "Web" en el nombre o descripción y duren más de 40 horas
SELECT Nombre, Descripcion, DuracionHoras
FROM Cursos
WHERE (Nombre LIKE '%Web%' OR Descripcion LIKE '%Web%')
  AND DuracionHoras > 40;

-- Consulta 17: Estudiantes cuyo nombre empiece por "A" o cuyo apellido tenga exactamente 5 letras
SELECT Nombre, Apellido, Email
FROM Estudiantes
WHERE Nombre LIKE 'A%' OR Apellido LIKE '_____';

-- 9. ORDER BY CON MÚLTIPLES COLUMNAS

-- Consulta 18: Estudiantes ordenados por fecha de inscripción (desc) y nombre (asc)
SELECT e.Nombre, e.Apellido, m.FechaInscripcion, c.Nombre AS Curso
FROM Estudiantes e
INNER JOIN Matriculas m ON e.IdEstudiante = m.IdEstudiante
INNER JOIN Cursos c ON m.IdCurso = c.IdCurso
ORDER BY m.FechaInscripcion DESC, e.Nombre ASC;

-- 10. PAGINACIÓN CON LIMIT Y OFFSET

-- Consulta 19a: Mostrar los primeros 10 cursos disponibles (página 1)
SELECT IdCurso, Nombre, DuracionHoras, FechaInicio
FROM Cursos
ORDER BY FechaInicio
LIMIT 10 OFFSET 0;

-- Consulta 19b: Mostrar los siguientes 10 cursos (página 2)
SELECT IdCurso, Nombre, DuracionHoras, FechaInicio
FROM Cursos
ORDER BY FechaInicio
LIMIT 10 OFFSET 10;

-- 11. UNION Y UNION ALL

-- Consulta 20a: Lista unificada de nombres de estudiantes y profesores (sin duplicados)
SELECT Nombre, Apellido, 'Estudiante' AS Rol FROM Estudiantes
UNION
SELECT Nombre, Apellido, 'Profesor' AS Rol FROM Profesores
ORDER BY Rol, Apellido;

-- Consulta 20b: Lista unificada incluyendo duplicados (UNION ALL)
SELECT Nombre, Apellido, 'Estudiante' AS Rol FROM Estudiantes
UNION ALL
SELECT Nombre, Apellido, 'Profesor' AS Rol FROM Profesores
ORDER BY Rol, Apellido;