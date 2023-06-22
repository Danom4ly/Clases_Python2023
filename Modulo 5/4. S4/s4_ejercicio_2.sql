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

SELECT * FROM clientes;
SELECT * FROM articulos;
SELECT * FROM ordenes;