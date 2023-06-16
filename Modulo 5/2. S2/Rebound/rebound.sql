CREATE TABLE clientes(
	cliente_id SERIAL PRIMARY KEY,
	nombre_cliente VARCHAR(50),
	ciudad VARCHAR(50)
);

CREATE TABLE articulos(
	codigo VARCHAR(10) PRIMARY KEY,
	nombre_articulo VARCHAR(50),
	precio DECIMAL(10,2)
);

CREATE TABLE ordenes(
	orden_id INT,
	fecha DATE,
	cantidad INT,
	codigo VARCHAR(10),
	cliente_id INT,
	CONSTRAINT fk_cliente_id FOREIGN KEY(cliente_id) REFERENCES clientes(cliente_id),
	CONSTRAINT fk_codigo FOREIGN KEY(codigo) REFERENCES articulos(codigo)
);

INSERT INTO clientes (nombre_cliente, ciudad) VALUES 
	('Martin', 'Santiago'),
	('Herman', 'Valparaíso'),
	('Pedro', 'Concepción');
	
INSERT INTO articulos (codigo, nombre_articulo, precio) VALUES
('3786','Red','35.00'),
('4011','Raqueta','65.00'),
('9132','Paq-3','4.75'),
('5794','Paq-4','5.00'),
('3141','Funda','10.00');

INSERT INTO ordenes (orden_id, fecha, cantidad, codigo, cliente_id) VALUES
(2301, '2020-02-23', 3, '3786', 1),
(2301, '2020-02-23', 6, '4011', 1),
(2301, '2020-02-23', 8, '9132', 1),
(2302, '2020-02-25', 4, '5794', 2),
(2303, '2020-02-27', 2, '4011', 3),
(2303, '2020-02-27', 2, '3141', 3);

DROP TABLE ordenes;

select * from clientes;
select * from articulos;
select * from ordenes;

select nombre_cliente from clientes;
select nombre_cliente, ciudad from clientes;

select * from clientes where ciudad = 'Santiago'; --where: donde el campo ciudad sea igual a "Santiago"

select count(*) from clientes; --Contar cantidad de clientes
select count(*) as total_clientes from clientes; -- as para cambiar el encabezado de la columna

select * from clientes order by nombre_cliente; --Ordena alfabeticamente (Posible Error)
select * from clientes order by nombre_cliente desc; -- Ordena alfabeticamente drescendiente
select * from clientes order by nombre_cliente asc; -- Ordena alfabeticamente ascendente

select count(*) from clientes where ciudad = 'Santiago'; --Contar clientes de Santiago

select * from clientes where nombre_cliente like 'P%';--Buscar todas las coincidencias que comienzan con la letra P
select * from clientes where nombre_cliente like '%o';--Buscar todas las coincidencias que Terminan con la letra O
select * from clientes where nombre_cliente like '%o%';--Buscar todas las coincidencias con la letra O
select * from clientes where nombre_cliente like upper('p%');--Buscar todas las coincidencias que comienzan con la letra P aunque sea minuscula
select * from clientes where nombre_cliente like lower('p%');--Buscar todas las coincidencias que comienzan con la letra P aunque sea mayuscula

select * from clientes where lower (nombre_cliente) like('p%');
select * from clientes where upper (nombre_cliente) like('P%');

select * from clientes where ciudad ='Valparaíso' and nombre_cliente='Herman';
select * from clientes where ciudad ='Valparaíso' and nombre_cliente like '%Herman%';

--BETWEEN: Obtener las órdenes realizadas en un rango de fechas especifíco
select * from ordenes where fecha between '2020-02-23' and '2020-02-25'
select * from ordenes where cantidad >=6;

--sum
select sum(cantidad) as cantidad_total from ordenes; --Sumar la cantidad total de articulos Vendidos

--avg
select avg(cantidad) as cantidad_avg from ordenes; --Promedio de la cantidad total de articulos Vendidos

--max
select max(fecha) from ordenes;

--min
select min(fecha) from ordenes;