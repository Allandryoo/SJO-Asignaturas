CREATE DATABASE repaso_dam;
USE repaso_dam;

CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    ciudad VARCHAR(40) DEFAULT 'Palma'
);

CREATE TABLE pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NOT NULL,
    total DECIMAL(6,2) CHECK (total >= 0),
    estado VARCHAR(20) NOT NULL DEFAULT 'pendiente',
    id_cliente INT,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

ALTER TABLE clientes ADD telefono VARCHAR(15); ALTER TABLE clientes RENAME COLUMN telefono TO movil;

INSERT INTO clientes (nombre, email, ciudad) VALUES
('Marta Ruiz','marta@correo.com','Palma'),
('Leo Serra','leo@correo.com',DEFAULT),
('Aina Torres',NULL,'Inca'),
('Joan Pérez','joan@correo.com','Manacor');

-- Fallara por email que ya existe y es campo unico
INSERT INTO clientes (nombre, email, ciudad) VALUES
('Miquel Roca','leo@correo.com','Llucmajor');

-- Fallara por no tener nombre ya que es campo no nulo
INSERT INTO clientes (nombre, email, ciudad) VALUES
(NULL,'nuria@correo.com','Palma');

INSERT INTO pedidos (fecha, total, estado, id_cliente)VALUES
('2026-04-14',39.95,'pendiente',1),
('2026-04-14',120.00,'pendiente',2),
('2026-04-15',75.50,'enviado',2),
('2026-04-16',15.00,DEFAULT,3);

-- Fallara porque el total es un numero negativo
INSERT INTO pedidos (fecha, total, estado, id_cliente) VALUES
('2026-04-17',-10.00,'pendiente',1);

-- Fallara porque el cliente no existe ya que el id es 99 y no hay ningun cliente con ese id
INSERT INTO pedidos (fecha, total, estado, id_cliente) VALUES
('2026-04-17',22.00,'pendiente',99);

-- 1. Mostrar todos los clientes.
SELECT * FROM clientes;

-- 2. Mostrar solo nombre y ciudad de los clientes.
SELECT nombre, ciudad FROM clientes;

-- 3. Mostrar los clientes cuya ciudad sea Palma.
SELECT * FROM clientes WHERE ciudad = 'Palma';

-- 4. Mostrar los pedidos con total >= 50.
SELECT * FROM pedidos WHERE total >= 50;

-- 5. Mostrar los clientes cuyo email sea NULL.
SELECT * FROM clientes WHERE email IS NULL;

-- 6. Mostrar los pedidos cuyo estado sea "pendiente".
SELECT * FROM pedidos WHERE estado = 'pendiente';

-- 7. Cambiar el estado del pedido 1 a "enviado".
UPDATE pedidos SET estado = 'enviado' WHERE id_pedido = 1;

-- 8. Cambiar la ciudad del cliente 4 a "Palma".
UPDATE clientes SET ciudad = 'Palma' WHERE id_cliente = 4;

-- 9. Eliminar el pedido 4.
DELETE FROM pedidos WHERE id_pedido = 4;

-- 10. Intentar eliminar el cliente 2. Explica qué ocurre.
-- Dara un error de integridad referencial.
-- Porque el cliente 2 tiene pedidos registrados en la tabla 'pedidos'. 
-- Borrar al cliente dejaría sus pedidos huérfanos, lo cual está prohibido por la clave foránea.
-- DELETE FROM clientes WHERE id_cliente = 2;

-- 11. Escribe una secuencia correcta para poder borrar al cliente 2 sin romper la integridad referencial.
-- Primero hay que borrar los registros dependientes:
DELETE FROM pedidos WHERE id_cliente = 2;
-- Cuando no tiene pedidos, si se puede borrar el cliente:
DELETE FROM clientes WHERE id_cliente = 2;

-- =======
-- Parte A
-- =======
START TRANSACTION;

UPDATE pedidos
SET total=999.99
WHERE id_pedido=1;

-- OBSERVACIÓN: 
-- Lo que enseña es que el cambio se ha hecho pero aún no se ha confirmado.
SELECT * FROM pedidos WHERE id_pedido=1;

ROLLBACK;

-- OBSERVACIÓN DESPUÉS DEL ROLLBACK:
-- Veremos que el total ha vuelto al valor anterior porque no guardamos el cambio.
SELECT * FROM pedidos WHERE id_pedido=1;

-- =======
-- Parte B
-- =======
START TRANSACTION;

UPDATE pedidos
SET estado='entregado'
WHERE id_pedido=3;

COMMIT;

-- 1. ¿Qué diferencia hay con el caso anterior?
-- La diferencia es que el comando COMMIT confirma y guarda los cambios 
-- de manera definitiva en la base de datos. En el caso de ROLLBACK, 
-- la operación se abortaba y se dejaba todo como estaba.

-- 2. ¿Podrías deshacer ahora ese cambio con ROLLBACK?
-- No. Una vez que se ejecuta COMMIT, la transacción se cierra y 
-- los datos se escriben permanentemente en la base de datos. Un ROLLBACK 
-- ejecutado después no tendrá ningún efecto sobre esos datos confirmados.

-- =======
-- Parte C
-- =======

-- 1. DDL
CREATE TABLE prueba (
    id INT PRIMARY KEY
);

-- 2. DDL
ALTER TABLE clientes ADD edad INT;

-- 3. DML
INSERT INTO clientes (nombre, email, ciudad)
VALUES ('Laura','laura@correo.com','Palma');

-- 4. DML
DELETE FROM pedidos WHERE id_pedido=2;
