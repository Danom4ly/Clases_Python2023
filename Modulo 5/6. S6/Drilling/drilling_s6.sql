CREATE TABLE empresa(
	rut VARCHAR(10) PRIMARY KEY,
	nombre VARCHAR(120),
	direccion VARCHAR(120),
	telefono VARCHAR(15),
	correo VARCHAR(80),
	web VARCHAR(50)
);

CREATE TABLE herramienta(
	id_herramienta INT PRIMARY KEY,
	nombre VARCHAR(120),
	precio_dia MONEY
);

CREATE TABLE cliente(
	rut VARCHAR(10) PRIMARY KEY,
	nombre VARCHAR(120),
	correo VARCHAR(80),
	direccion VARCHAR(120),
	celular VARCHAR(15)
);

CREATE TABLE arriendo(
	folio INT PRIMARY KEY,
	fecha DATE,
	dias INT,
	valor_dia INT,
	garantia VARCHAR(30),
	id_herramienta INT,
	rut_cliente VARCHAR(10)
);

ALTER TABLE arriendo ADD CONSTRAINT fk_id_herramienta FOREIGN KEY(id_herramienta) REFERENCES herramienta(id_herramienta);
ALTER TABLE arriendo ADD CONSTRAINT fk_rut_cliente FOREIGN KEY(rut_cliente) REFERENCES cliente(rut);

--Datos de una empresa.
INSERT INTO empresa VALUES ('99999999-9','Promenade','Santiago','912345678','promenade@promenade.cl','promenade.cl');

--5 herramientas.
INSERT INTO herramienta VALUES(1,'Taladro Electrico',10000),
                              (2,'Cierra Electrica',20000),
                              (3,'Pistola de Clavos',30000),
                              (4,'Lijadora',40000),
                              (5,'Serrucho Electrico',50000);

--3 clientes.
INSERT INTO cliente VALUES('22222222-2','Juan Perez','j.perez@mail.com','1 Calle Uno',2222222222),
                          ('33333333-3','Juanita Sánches','j.sanches@mail.com','2 Calle Dos',3333333333),
                          ('44444444-4','Marcelo Ugarte','m.ugarte@mail.com','3 Calle Tres',4444444444);

--arriendos
INSERT INTO arriendo VALUES
	(1,'15/01/20',5,20000,'Eficacia en 5 dias o menos',2,'22222222-2'),
   	(2,'12/11/22',2,30000,'Eficacia en 2 dias o menos',3,'22222222-2'),
   	(3,'15/01/20',1,40000,'Eficacia en 1 dia',4,'33333333-3'),
   	(4,'12/11/22',3,40000,'Eficacia en solo 3 dias',5,'33333333-3');


-- 1. Listar todos los arriendos con las siguientes columnas: Folio, Fecha, Días, ValorDia, NombreCliente, RutCliente.
SELECT a.folio,a.fecha,a.dias,a.valor_dia,c.nombre,c.rut
FROM arriendo AS a
JOIN cliente AS c
ON a.rut_cliente = c.rut

-- 2. Listar los clientes sin arriendos.
SELECT c.rut,c.nombre FROM cliente AS c
LEFT JOIN arriendo AS a
ON c.rut = a.rut_cliente
WHERE a.rut_cliente is NULL;

-- 3. Liste RUT y Nombre de las tablas empresa y cliente.
SELECT rut, nombre FROM cliente
UNION
SELECT rut, nombre FROM empresa;

-- 4. Liste la cantidad de arriendos por mes.
SELECT EXTRACT(YEAR FROM fecha) AS año,
EXTRACT(MONTH FROM fecha) AS mes,
COUNT(folio) AS cantidad_arriendos 
FROM arriendo 
GROUP BY año,mes; 

--CONSULTAS	
SELECT * FROM cliente;						  
SELECT * FROM herramienta;
SELECT * FROM empresa;
SELECT * FROM arriendo;