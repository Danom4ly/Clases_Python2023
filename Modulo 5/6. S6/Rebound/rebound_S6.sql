CREATE TABLE empresa(
rut VARCHAR(12) PRIMARY KEY,
nombre VARCHAR(30),
direccion VARCHAR(255),
telefono VARCHAR(11),
correo VARCHAR(255),
web VARCHAR(40)
);

CREATE TABLE cliente(
rut VARCHAR(9) PRIMARY KEY,
nombre VARCHAR(30),
correo VARCHAR(255),
direccion VARCHAR(255),
celular VARCHAR(11),
alta BOOLEAN
);

CREATE TABLE tipo_vehiculo(
tipo_vehiculo_id SERIAL PRIMARY KEY,
nombre VARCHAR(255)
);

CREATE TABLE marca(
marca_id SERIAL PRIMARY KEY,
nombre VARCHAR(255)
);

CREATE TABLE vehiculo(
vehiculo_id SERIAL PRIMARY KEY,
patente VARCHAR(6),
modelo VARCHAR(255),
color VARCHAR(255),
PRECIO MONEY,
frecuencia_mantencion INT,
marca_id INT,
tipo_vehiculo_id INT
);

CREATE TABLE venta(
folio SERIAL PRIMARY KEY,
fecha DATE,
monto INT,
rut_cliente VARCHAR(9),
vehiculo_id INT
);

CREATE TABLE mantencion(
mantencion_id SERIAL PRIMARY KEY,
fecha DATE,
trabajos_realizados VARCHAR(255),
folio INT
);

ALTER TABLE mantencion ADD CONSTRAINT fk_folio
FOREIGN KEY(folio) REFERENCES venta(folio);

ALTER TABLE vehiculo ADD CONSTRAINT fk_marca_id
FOREIGN KEY(marca_id) REFERENCES marca(marca_id);

ALTER TABLE vehiculo ADD CONSTRAINT fk_tipo_vehiculo_id
FOREIGN KEY(tipo_vehiculo_id) REFERENCES tipo_vehiculo(tipo_vehiculo_id);

ALTER TABLE venta ADD CONSTRAINT fk_rut_cliente 
FOREIGN KEY(rut_cliente) REFERENCES cliente(rut);

ALTER TABLE venta ADD CONSTRAINT fk_vehiculo_id
FOREIGN KEY(vehiculo_id) REFERENCES vehiculo(vehiculo_id);

--Inserte los datos de una empresa.
INSERT INTO empresa VALUES ('99999999-9','Promenade','Santiago','912345678','promenade@promenade.cl','promenade.cl');

--Inserte 2 tipos de vehículo
INSERT INTO tipo_vehiculo(nombre) VALUES ('Carga');
INSERT INTO tipo_vehiculo(nombre) VALUES ('Transporte');

--Inserte 3 clientes.
INSERT INTO cliente VALUES ('111111111','Hugo','hugo@correo.cl','norte','911111111',true);
INSERT INTO cliente VALUES ('222222222','Paco','paco@correo.cl','sur','922222222',true);
INSERT INTO cliente VALUES ('333333333','Luis','luis@correo.cl','oeste','933333333',true);

--Inserte 2 marcas.
INSERT INTO marca(nombre) VALUES ('TOYOTA');
INSERT INTO marca(nombre) VALUES ('MAZDA');

--Inserte 5 vehículos.
INSERT INTO vehiculo(patente, modelo, color, precio, frecuencia_mantencion, marca_id, tipo_vehiculo_id) VALUES
	('AAAA11','M1','Negro','10000000',1,1,1),
	('BBBB22','M2','Blanco','20000000',2,2,1),
	('CCCC33','M3','Rojo','30000000',3,2,2),
	('DDDD44','M4','Verde','40000000',4,1,1),
	('EEEE55','M5','Azul','50000000',5,2,2);

--Elimina el último cliente.
--DELETE FROM cliente WHERE rut = '333333333'

--Inserte 1 venta para cada cliente.
INSERT INTO venta(fecha, monto, rut_cliente, vehiculo_id) VALUES
	('2023-01-01', 10000000, '111111111', 1),
	('2023-02-02', 20000000, '222222222', 2),
    ('2020-02-02', 30000000, '333333333', 3),
	('2020-02-03', 40000000, '333333333', 4);

INSERT INTO venta(fecha, monto, rut_cliente, vehiculo_id) VALUES ('2020-02-03', 40000000, '333333333', 4);
INSERT INTO venta(fecha, monto, rut_cliente, vehiculo_id) VALUES ('2020-02-04', 40000000, '333333333', 3);
INSERT INTO venta(fecha, monto, rut_cliente, vehiculo_id) VALUES ('2020-03-04', 40000000, '333333333', 3);
INSERT INTO venta(fecha, monto, rut_cliente, vehiculo_id) VALUES ('2020-03-04', 40000000, '333333333', 3);
	
--Modifique el nombre del segundo cliente.
--UPDATE cliente SET nombre = 'Pacoo' WHERE rut = '222222222';

--Liste todas las ventas.
--SELECT * FROM venta;

--Liste las ventas del primer cliente.
--SELECT * FROM venta WHERE rut_cliente = '111111111';

--Obtenga la patente de todos los vehículos.
--SELECT patente FROM vehiculo;

--CONSULTAS REBOUND
-- 1. Listar todos los vehículos que no han sido vendidos.
SELECT v.* FROM vehiculo v
LEFT JOIN venta ven
ON v.vehiculo_id = ven.vehiculo_id
WHERE ven.vehiculo_id is NULL;

-- 2. Listar todas las ventas de "febrero" del 2020 con las columnas: Folio, FechaVenta, MontoVenta, NombreCliente, RutCliente, Patente, NombreMarca, y Modelo.
SELECT ven.folio,ven.fecha,ven.monto,c.nombre,c.rut,v.patente,m.nombre,v.modelo 
FROM venta AS ven
JOIN cliente AS c
ON ven.rut_cliente = c.rut
JOIN vehiculo AS v
ON ven.vehiculo_id = v.vehiculo_id
JOIN marca AS m
ON v.marca_id = m.marca_id
WHERE EXTRACT(MONTH FROM ven.fecha) = '2' AND EXTRACT(YEAR FROM ven.fecha) = '2020';
--WHERE ven.fecha BETWEEN ('2020-01-01') AND ('2020-12-31'); -- Segunda opción

-- 3. Sumar las ventas por mes y marca del año 2020.
SELECT * FROM venta WHERE fecha BETWEEN ('2020-01-01') AND ('2020-12-31');

SELECT EXTRACT(MONTH FROM ven.fecha) AS mes_venta,m.nombre AS marca, SUM(ven.monto) AS venta_total 
FROM venta AS ven
JOIN vehiculo AS v
ON ven.vehiculo_id = v.vehiculo_id
JOIN marca AS m
ON v.marca_id = m.marca_id
WHERE EXTRACT(YEAR FROM ven.fecha) = '2020'
GROUP BY mes_venta, marca;

-- 4. Listar Rut y Nombre de las tablas cliente y empresa.
--Opcion A
SELECT c.rut,c.nombre,e.rut,e.nombre
FROM cliente AS c
CROSS JOIN empresa AS e
--Opcion B
SELECT rut, nombre FROM cliente
UNION
SELECT rut, nombre FROM empresa;

--OTRAS CONSULTAS
SELECT * FROM vehiculo;
SELECT * FROM marca;
SELECT * FROM empresa;
SELECT * FROM cliente;
SELECT * FROM tipo_vehiculo;