DROP DATABASE IF EXISTS empresa_joins;
CREATE DATABASE empresa_joins;
USE empresa_joins;

-- ==========================================
-- TABLAS
-- ==========================================

CREATE TABLE departamentos (
    id_departamento INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    ciudad VARCHAR(100) NOT NULL
);

CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    ciudad VARCHAR(100) NOT NULL,
    sector VARCHAR(100) NOT NULL
);

CREATE TABLE empleados (
    id_empleado INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    puesto VARCHAR(100) NOT NULL,
    salario DECIMAL(10,2) NOT NULL,
    fecha_contratacion DATE NOT NULL,
    id_departamento INT NULL,
    manager_id INT NULL,
    CONSTRAINT fk_empleado_departamento
        FOREIGN KEY (id_departamento) REFERENCES departamentos(id_departamento),
    CONSTRAINT fk_empleado_manager
        FOREIGN KEY (manager_id) REFERENCES empleados(id_empleado)
);

CREATE TABLE proyectos (
    id_proyecto INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NULL,
    presupuesto DECIMAL(12,2) NOT NULL,
    id_departamento INT NOT NULL,
    id_cliente INT NULL,
    CONSTRAINT fk_proyecto_departamento
        FOREIGN KEY (id_departamento) REFERENCES departamentos(id_departamento),
    CONSTRAINT fk_proyecto_cliente
        FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

CREATE TABLE asignaciones (
    id_empleado INT NOT NULL,
    id_proyecto INT NOT NULL,
    rol VARCHAR(100) NOT NULL,
    horas_semana INT NOT NULL,
    PRIMARY KEY (id_empleado, id_proyecto),
    CONSTRAINT fk_asignacion_empleado
        FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado),
    CONSTRAINT fk_asignacion_proyecto
        FOREIGN KEY (id_proyecto) REFERENCES proyectos(id_proyecto)
);

INSERT INTO departamentos (id_departamento, nombre, ciudad) VALUES
(1, 'Desarrollo Web', 'Palma'),
(2, 'Marketing', 'Palma'),
(3, 'Recursos Humanos', 'Inca'),
(4, 'Soporte', 'Manacor'),
(5, 'I+D', 'Palma'),
(6, 'Administración', 'Llucmajor');   -- este departamento no tendrá empleados

INSERT INTO clientes (id_cliente, nombre, ciudad, sector) VALUES
(1, 'TechNova', 'Madrid', 'Tecnología'),
(2, 'GreenFoods', 'Valencia', 'Alimentación'),
(3, 'EduSmart', 'Palma', 'Educación'),
(4, 'BlueTravel', 'Barcelona', 'Turismo'),
(5, 'HealthPlus', 'Sevilla', 'Salud'),
(6, 'UrbanMove', 'Bilbao', 'Logística');  -- este cliente no tendrá proyectos

-- Primero insertamos empleados sin depender de otros empleados no creados todavía
INSERT INTO empleados (id_empleado, nombre, apellido, puesto, salario, fecha_contratacion, id_departamento, manager_id) VALUES
(1, 'Ana', 'Torres', 'Directora General', 42000.00, '2018-03-10', 1, NULL),
(2, 'Luis', 'Pérez', 'Jefe de Desarrollo', 36000.00, '2019-06-15', 1, 1),
(5, 'Laura', 'Martín', 'Jefa de Marketing', 34000.00, '2020-02-01', 2, 1),
(7, 'Carlos', 'Navarro', 'Responsable RRHH', 30000.00, '2021-01-11', 3, 1),
(10, 'Nuria', 'Vidal', 'Jefa de Soporte', 32000.00, '2020-09-01', 4, 1),
(12, 'Rosa', 'Ferrer', 'Investigadora', 31000.00, '2022-03-15', 5, 1);

INSERT INTO empleados (id_empleado, nombre, apellido, puesto, salario, fecha_contratacion, id_departamento, manager_id) VALUES
(3, 'Marta', 'Gómez', 'Desarrolladora Senior', 29000.00, '2021-04-20', 1, 2),
(4, 'Sergio', 'Ruiz', 'Desarrollador Junior', 24000.00, '2023-01-10', 1, 2),
(6, 'Paula', 'Díaz', 'Técnica de Marketing', 23000.00, '2023-05-02', 2, 5),
(8, 'Elena', 'Castro', 'Técnica de Soporte', 22000.00, '2024-02-12', 4, 10),
(9, 'Iván', 'López', 'Consultor Externo', 27000.00, '2024-09-01', NULL, 2), -- sin departamento
(11, 'Diego', 'Serra', 'Becario Desarrollo', 18000.00, '2025-01-20', 1, 2);

INSERT INTO proyectos (id_proyecto, nombre, fecha_inicio, fecha_fin, presupuesto, id_departamento, id_cliente) VALUES
(1, 'Web corporativa TechNova', '2025-01-15', NULL, 18000.00, 1, 1),
(2, 'App pedidos GreenFoods', '2025-02-01', NULL, 25000.00, 1, 2),
(3, 'Campaña EduSmart 2025', '2025-03-10', '2025-06-30', 12000.00, 2, 3),
(4, 'Migración de servidores', '2025-01-20', NULL, 15000.00, 4, NULL), -- proyecto interno, sin cliente
(5, 'Portal reservas BlueTravel', '2025-04-01', NULL, 30000.00, 1, 4),
(6, 'Selección talento 2026', '2025-05-01', NULL, 8000.00, 3, NULL), -- sin asignaciones
(7, 'IA educativa', '2025-03-15', NULL, 40000.00, 5, 3),
(8, 'ERP HealthPlus', '2025-06-01', NULL, 27000.00, 6, 5); -- departamento sin empleados

INSERT INTO asignaciones (id_empleado, id_proyecto, rol, horas_semana) VALUES
(2, 1, 'Jefe de proyecto', 10),
(3, 1, 'Backend', 20),
(4, 1, 'Frontend', 18),
(11, 1, 'Apoyo desarrollo', 12),

(2, 2, 'Arquitecto', 8),
(3, 2, 'Backend', 15),
(11, 2, 'Testing', 10),

(5, 3, 'Coordinación campaña', 12),
(6, 3, 'Redes sociales', 20),

(10, 4, 'Responsable técnico', 10),
(8, 4, 'Soporte sistemas', 22),

(2, 5, 'Supervisor técnico', 6),
(4, 5, 'Frontend', 16),
(9, 5, 'Consultoría UX', 14),

(12, 7, 'Investigación', 25);

-- ========================
-- INNER JOIN
-- ========================

-- 1. Consulta: nombre y apellido de cada empleado junto con el nombre de su departamento
SELECT e.nombre, e.apellido, d.nombre AS nombre_departamento
FROM empleados e
INNER JOIN departamentos d 
ON e.id_departamento = d.id_departamento;

-- 2. Muestra el nombre de cada proyecto junto con el nombre del cliente al que pertenece.
SELECT p.nombre AS nombre_proyecto, c.nombre AS nombre_cliente
FROM proyectos p
INNER JOIN clientes c 
ON p.id_cliente = c.id_cliente;

-- 3. Lista los empleados asignados a proyectos, mostrando nombre del empleado, nombre del proyecto y rol.
SELECT e.nombre AS nombre_empleado, p.nombre AS nombre_proyecto, a.rol
FROM empleados e
INNER JOIN asignaciones a 
ON e.id_empleado = a.id_empleado
INNER JOIN proyectos p 
ON a.id_proyecto = p.id_proyecto;

-- 4. Muestra todos los proyectos junto con el departamento responsable.
SELECT p.nombre AS nombre_proyecto, d.nombre AS nombre_departamento
FROM proyectos p
INNER JOIN departamentos d 
ON p.id_departamento = d.id_departamento;

-- 5. Obtén el nombre del empleado, su puesto y las horas semanales que dedica a cada proyecto.
SELECT e.nombre AS nombre_empleado, e.puesto, p.nombre AS nombre_proyecto, a.horas_semana
FROM empleados e
INNER JOIN asignaciones a 
ON e.id_empleado = a.id_empleado
INNER JOIN proyectos p 
ON a.id_proyecto = p.id_proyecto;

-- 6. Lista los proyectos con cliente y departamento, mostrando: proyecto, cliente y departamento.
SELECT p.nombre AS nombre_proyecto, c.nombre AS nombre_cliente, d.nombre AS nombre_departamento
FROM proyectos p
INNER JOIN clientes c 
ON p.id_cliente = c.id_cliente
INNER JOIN departamentos d 
ON p.id_departamento = d.id_departamento;

-- ========================
-- LEFT JOIN
-- ========================

-- 1. Muestra todos los empleados, aunque no tengan departamento, indicando su departamento si existe.
SELECT e.nombre, e.apellido, d.nombre AS nombre_departamento
FROM empleados e
LEFT JOIN departamentos d 
ON e.id_departamento = d.id_departamento;

-- 2. Muestra todos los clientes, aunque no tengan proyectos, indicando el nombre del proyecto si existe.
SELECT c.nombre AS nombre_cliente, p.nombre AS nombre_proyecto
FROM clientes c
LEFT JOIN proyectos p 
ON c.id_cliente = p.id_cliente;

-- 3. Muestra todos los proyectos, aunque no tengan cliente, indicando el cliente si existe.
SELECT p.nombre AS nombre_proyecto, c.nombre AS nombre_cliente
FROM proyectos p
LEFT JOIN clientes c 
ON p.id_cliente = c.id_cliente;

-- 4. Muestra todos los empleados, aunque no estén asignados a ningún proyecto, indicando el proyecto si existe.
SELECT e.nombre AS nombre_empleado, p.nombre AS nombre_proyecto
FROM empleados e
LEFT JOIN asignaciones a 
ON e.id_empleado = a.id_empleado
LEFT JOIN proyectos p 
ON a.id_proyecto = p.id_proyecto;

-- 5. Saca un listado de departamentos y los empleados que pertenecen a ellos, pero incluyendo también departamentos sin empleados.
SELECT d.nombre AS nombre_departamento, e.nombre AS nombre_empleado
FROM departamentos d
LEFT JOIN empleados e 
ON d.id_departamento = e.id_departamento;

-- 6. Muestra todos los proyectos y las asignaciones asociadas, incluyendo los proyectos que todavía no tienen empleados asignados.
SELECT p.nombre AS nombre_proyecto, a.id_empleado, a.rol
FROM proyectos p
LEFT JOIN asignaciones a 
ON p.id_proyecto = a.id_proyecto;

-- ========================
-- RIGHT JOIN
-- ========================

-- 1. Usando RIGHT JOIN, muestra todos los departamentos y los empleados que pertenecen a ellos, incluyendo los departamentos sin empleados.
SELECT d.nombre AS nombre_departamento, e.nombre AS nombre_empleado
FROM empleados e
RIGHT JOIN departamentos d 
ON e.id_departamento = d.id_departamento;

-- 2. Usando RIGHT JOIN, muestra todos los proyectos y sus asignaciones, incluyendo los proyectos sin asignaciones.
SELECT p.nombre AS nombre_proyecto, a.rol
FROM asignaciones a
RIGHT JOIN proyectos p 
ON a.id_proyecto = p.id_proyecto;

-- 3. Usando RIGHT JOIN, muestra todos los clientes y sus proyectos, incluyendo clientes sin proyectos.
SELECT c.nombre AS nombre_cliente, p.nombre AS nombre_proyecto
FROM proyectos p
RIGHT JOIN clientes c 
ON p.id_cliente = c.id_cliente;

-- 4. Usando RIGHT JOIN, muestra todos los departamentos y los proyectos asociados, incluyendo departamentos que no tengan proyectos.
SELECT d.nombre AS nombre_departamento, p.nombre AS nombre_proyecto
FROM proyectos p
RIGHT JOIN departamentos d 
ON p.id_departamento = d.id_departamento;

-- ========================
-- SELF JOIN
-- ========================

-- 1. Muestra cada empleado junto con el nombre y apellido de su jefe.
SELECT e.nombre AS empleado, e.apellido AS apellido_empleado, m.nombre AS jefe, m.apellido AS apellido_jefe
FROM empleados e
LEFT JOIN empleados m 
ON e.manager_id = m.id_empleado;

-- 2. Muestra solo los empleados que sí tienen jefe, indicando empleado y jefe.
SELECT e.nombre AS empleado, m.nombre AS jefe
FROM empleados e
INNER JOIN empleados m 
ON e.manager_id = m.id_empleado;

-- 3. Muestra los jefes y cuántos empleados tienen a su cargo.
SELECT m.nombre AS jefe, m.apellido AS apellido_jefe, COUNT(e.id_empleado) AS num_empleados
FROM empleados e
INNER JOIN empleados m 
ON e.manager_id = m.id_empleado
GROUP BY m.id_empleado, m.nombre, m.apellido;

-- 4. Muestra parejas de empleados que pertenecen al mismo departamento, evitando que un empleado salga emparejado consigo mismo.
SELECT e1.nombre AS empleado_1, e2.nombre AS empleado_2, d.nombre AS departamento
FROM empleados e1
JOIN empleados e2 
ON e1.id_departamento = e2.id_departamento
JOIN departamentos d 
ON e1.id_departamento = d.id_departamento
WHERE e1.id_empleado < e2.id_empleado;

-- ========================
-- EXTRAS
-- ========================

-- 1. Muestra los empleados que no tienen departamento.
SELECT nombre, apellido 
FROM empleados 
WHERE id_departamento IS NULL;

-- 2. Muestra los clientes que no tienen proyectos.
SELECT c.nombre AS cliente_sin_proyectos
FROM clientes c
LEFT JOIN proyectos p 
ON c.id_cliente = p.id_cliente
WHERE p.id_proyecto IS NULL;

-- 3. Muestra los proyectos que no tienen empleados asignados.
SELECT p.nombre AS proyecto_sin_empleados
FROM proyectos p
LEFT JOIN asignaciones a 
ON p.id_proyecto = a.id_proyecto
WHERE a.id_empleado IS NULL;

-- 4. Muestra los empleados que no participan en ningún proyecto.
SELECT e.nombre, e.apellido
FROM empleados e
LEFT JOIN asignaciones a 
ON e.id_empleado = a.id_empleado
WHERE a.id_proyecto IS NULL;

-- 5. Muestra los empleados y la suma total de horas semanales que tienen asignadas en proyectos.
SELECT e.nombre, e.apellido, COALESCE(SUM(a.horas_semana), 0) AS total_horas_semanales
FROM empleados e
LEFT JOIN asignaciones a 
ON e.id_empleado = a.id_empleado
GROUP BY e.id_empleado, e.nombre, e.apellido;
