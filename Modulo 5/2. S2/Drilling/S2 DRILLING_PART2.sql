SELECT * FROM articulos;
SELECT * FROM ordenes;
SELECT * FROM clientes;

--Obtener los artículos con un precio mayor a $50
SELECT * FROM articulos WHERE precio > 50;

--Obtener los artículos ordenados por nombre de forma descendente
SELECT * FROM articulos ORDER BY nombre_articulo desc;
SELECT * FROM articulos ORDER BY nombre_articulo asc;

--Obtener el artículo más barato
SELECT * FROM articulos WHERE precio = (SELECT MIN(precio) FROM articulos);

--Obtener la orden más reciente
SELECT * FROM ordenes WHERE orden_id = (SELECT max(orden_id) FROM ordenes);
SELECT * FROM ordenes WHERE fecha = (SELECT max(fecha) FROM ordenes);

--Obtener las órdenes con la cantidad superior a la media de la cantidad de órdenes
SELECT orden_id FROM ordenes WHERE cantidad > (SELECT AVG(cantidad) FROM ordenes);

--Obtener el número total de órdenes por cliente
SELECT cliente_id, COUNT(orden_id) FROM ordenes GROUP BY cliente_id ORDER BY cliente_id asc;

--Obtener el cliente con el ID más bajo
SELECT nombre_cliente,cliente_id FROM clientes WHERE cliente_id = (SELECT min(cliente_id) FROM clientes);