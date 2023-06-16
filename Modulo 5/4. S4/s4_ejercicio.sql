--Actualizar el nombre del cliente con ID 1 en la tabla "clientes"
UPDATE clientes SET nombre_cliente = 'Fulanito' WHERE cliente_id = 1;

--Incrementar en 10 el precio de todos los artículos en la tabla "articulos"
UPDATE articulos SET precio = precio + 10;

--Actualizar la cantidad de una orden específica en la tabla "ordenes"
UPDATE ordenes SET cantidad = 8 WHERE orden_id = 2301 AND codigo = '4011';

--Cambiar el código de un artículo en la tabla "articulos" basado en su nombre
INSERT INTO articulos VALUES ('2020', 'Poste', 50.00);
UPDATE articulos SET codigo = 3030 WHERE nombre_articulo = 'Poste';

--Actualizar la ciudad de todos los clientes que pertenecen a una determinada ciudad en la tabla "clientes"
UPDATE clientes SET ciudad = 'Chiloe' WHERE ciudad = 'Valparaíso';

--Clientes que con ordenes
SELECT c.*, o.orden_id FROM clientes c
LEFT JOIN ordenes o
ON c.cliente_id = o.cliente_id;

--Clientes que no tienen ordenes asociadas
SELECT c.* FROM clientes c
LEFT JOIN ordenes o
ON c.cliente_id = o.cliente_id
WHERE o.cliente_id is NULL;

--Clientes que tienen ordenes asociadas
SELECT c.* FROM clientes c
LEFT JOIN ordenes o
ON c.cliente_id = o.cliente_id
WHERE o.cliente_id is not NULL;

--Obtener articulos que no han sido incluidos en ordenes
--INSERT INTO articulos VALUES('2020','Poste',50.00)
SELECT a.* FROM articulos a
LEFT JOIN ordenes o
ON a.codigo = o.codigo
WHERE o.codigo is null;

--Obtener las ordenes realizadas por clientes de una ciudad especifica
SELECT o.*, c.nombre_cliente FROM ordenes o
INNER JOIN clientes c
ON o.cliente_id = c.cliente_id
WHERE c.ciudad = 'Concepción';

--Obtener todas las ordenes junto con la info del cliente y el articulo correspondiente
SELECT o.*, c.nombre_cliente, c.ciudad , a.nombre_articulo FROM ordenes o
JOIN clientes c
ON o.cliente_id = c.cliente_id
JOIN articulos a
ON o.codigo = a.codigo;



SELECT * FROM clientes;
SELECT * FROM articulos;
SELECT * FROM ordenes;