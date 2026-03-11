CREATE DATABASE empresa_db;
USE empresa_db;

CREATE TABLE empleados (
	empleado_id INT,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    salario DECIMAL(7, 2),
    fecha_contratacion DATE
);

CREATE TABLE departamentos (
	departamento_id INT,
    nombre VARCHAR(50)
);

CREATE TABLE proyectos (
	proyecto_id INT,
    nombre VARCHAR(50)
);

INSERT INTO empleados VALUES
(1, 'Carlos', 'Gómez', 2500.50, '2018-01-15'),
(2, 'María', 'López', 2700.00, '2019-03-22'), 
(3, 'Juan', 'Pérez', 2300.75, '2020-07-10'), 
(4, 'Ana', 'Martínez', 2600.20, '2017-11-05'), 
(5, 'Luis', 'Hernández', 2450.00, '2016-09-18'), 
(6, 'Sofía', 'Ramírez', 2800.90, '2021-02-14'), 
(7, 'Miguel', 'Torres', 2550.30, '2015-06-01'), 
(8, 'Lucía', 'Flores', 2400.10, '2018-12-09'), 
(9, 'Javier', 'Vargas', 2650.00, '2019-08-27'), 
(10, 'Elena', 'Castro', 2750.80, '2020-10-03'), 
(11, 'Andrés', 'Santos', 2350.40, '2017-04-12'), 
(12, 'Paula', 'Reyes', 2900.00, '2021-05-20'), 
(13, 'Diego', 'Cruz', 2500.00, '2016-03-30'), 
(14, 'Valeria', 'Mendoza', 2600.60, '2018-07-19'), 
(15, 'Hugo', 'Silva', 2450.90, '2019-01-25'), 
(16, 'Camila', 'Rojas', 2550.00, '2020-11-11'), 
(17, 'Adrián', 'Navarro', 2700.40, '2015-10-07'), 
(18, 'Isabel', 'Peña', 2300.20, '2017-02-28'), 
(19, 'Fernando', 'Iglesias', 2750.00, '2018-05-16'), 
(20, 'Natalia', 'Cortés', 2850.70, '2021-03-09'), 
(21, 'Ricardo', 'Vega', 2600.00, '2016-08-14'), 
(22, 'Gabriela', 'Acosta', 2500.50, '2019-09-21'), 
(23, 'Tomás', 'Salazar', 2400.00, '2020-04-17'), 
(24, 'Daniela', 'Campos', 2650.80, '2017-12-01'), 
(25, 'Sebastián', 'Fuentes', 2550.10, '2018-06-23'), 
(26, 'Alejandra', 'Carrillo', 2700.00, '2019-11-30'), 
(27, 'Manuel', 'Paredes', 2450.60, '2020-08-05'), 
(28, 'Rocío', 'Miranda', 2800.00, '2016-01-19'), 
(29, 'Pablo', 'Serrano', 2350.90, '2017-09-03'), 
(30, 'Claudia', 'Delgado', 2900.20, '2021-06-14'), 
(31, 'Esteban', 'Bravo', 2500.00, '2015-04-27'), 
(32, 'Irene', 'Solís', 2600.40, '2018-10-22'), 
(33, 'Óscar', 'Valdez', 2750.00, '2019-12-18'), 
(34, 'Marta', 'Benítez', 2400.70, '2020-02-29'), 
(35, 'Raúl', 'Arias', 2550.30, '2017-07-08'), 
(36, 'Patricia', 'Esquivel', 2650.00, '2016-11-12'), 
(37, 'Jorge', 'Montoya', 2450.10, '2018-03-05'), 
(38, 'Verónica', 'Lara', 2800.50, '2019-05-28'), 
(39, 'César', 'Aguilar', 2300.00, '2020-09-14'), 
(40, 'Lorena', 'Palacios', 2900.80, '2021-01-07'), 
(41, 'Alberto', 'Rivas', 2600.00, '2017-05-19'), 
(42, 'Noelia', 'Zamora', 2500.40, '2018-08-11'), 
(43, 'Gustavo', 'Calderón', 2750.00, '2019-02-26'), 
(44, 'Rebeca', 'Soto', 2400.20, '2020-12-03'), 
(45, 'Iván', 'Bermúdez', 2550.90, '2016-04-15'), 
(46, 'Teresa', 'Aranda', 2650.00, '2017-10-29'), 
(47, 'Fabián', 'Molina', 2450.30, '2018-02-17'), 
(48, 'Silvia', 'Guerrero', 2800.10, '2019-06-06'), 
(49, 'Emilio', 'Ponce', 2350.00, '2020-03-13'), 
(50, 'Alicia', 'Rosales', 2900.50, '2021-07-21');

INSERT INTO departamentos VALUES
(1, 'Recursos Humanos'), 
(2, 'Finanzas'),
(3, 'Marketing'), 
(4, 'Ventas'), 
(5, 'Tecnología'), 
(6, 'Logística'), 
(7, 'Atención al Cliente'), 
(8, 'Producción'), 
(9, 'Investigación y Desarrollo'), 
(10, 'Compras');

INSERT INTO proyectos VALUES
(1, 'Sistema de Inventarios'), 
(2, 'Aplicación Móvil Corporativa'), 
(3, 'Migración a la Nube'), 
(4, 'Campaña Publicitaria 2024'), 
(5, 'Optimización de Logística'),
(6, 'Implementación ERP'), 
(7, 'Desarrollo de E‑commerce'), 
(8, 'Mejora de Atención al Cliente'), 
(9, 'Automatización de Procesos'), 
(10, 'Análisis de Datos'), 
(11, 'Expansión Internacional'), 
(12, 'Rediseño de Marca'), 
(13, 'Seguridad Informática'), 
(14, 'Integración de Sistemas'), 
(15, 'Proyecto de Innovación I+D');

-- Este comando muestra la indformacion de todas las columnas de la tabla empleados
SELECT * FROM empleados;

-- Este comando muestra la indformacion de todas las personas con el salario igual o mayor a 2700 de la tabla empleados
SELECT nombre, apellido, salario FROM empleados WHERE salario >= 2700;

-- Para este ejercicio primero compruebo los empleados con mas de 8 años en total son 15
SELECT * FROM empleados WHERE fecha_contratacion < '2018-01-01';

-- Con este comando actualizo el salario de los empleados a 3000 con mas de 8 años
UPDATE empleados SET salario = 3000.00 WHERE fecha_contratacion < '2018-01-01';

-- Si quisiera cambiar el salario de los 10 primeros
UPDATE empleados SET salario = 3000.00 WHERE empleado_id <= 10;

-- En este comando se borran los registros de las persona con ID del 11 al 15
DELETE FROM empleados WHERE empleado_id > 10 AND empleado_id <= 15;

SET AUTOCOMMIT = OFF;
-- Al desactivar el autocommit al hacer este update si hacemos SELECT antes de hacer commit la informacion de la tabla seguira igual como si no hubiesemos hecho nada
UPDATE empleados SET salario = 1000.00 WHERE empleado_id >= 45;
-- Comprobando si efectuo la sentencia
SELECT * FROM empleados;
-- Una vez ejecutada una sentencia SQL hacemos commit y los cambios se guardaran
COMMIT;
SET AUTOCOMMIT = ON;

-- Cambiando el nombre de la tabla
RENAME TABLE empleados TO personal;
-- El comando de SELECT * FROM empleados; ya no funciona ahora tenemos que usar
SELECT * FROM personal;

-- Añadiendo una nueva columna de gmail con maximo 30 caracteres
ALTER TABLE personal ADD gmail VARCHAR(30);

-- Eliminando la columna de la tabla
ALTER TABLE personal DROP COLUMN gmail;

-- Cambiando la columan fecha-contratacion de DATE a DATETIME
ALTER TABLE personal MODIFY COLUMN fecha_contratacion DATETIME;