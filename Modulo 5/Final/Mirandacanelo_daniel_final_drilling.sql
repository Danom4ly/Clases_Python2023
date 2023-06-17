--CONSULTAS
SELECT * FROM category;
SELECT * FROM inventory;
SELECT * FROM customer;
SELECT * FROM film_category;
SELECT * FROM rental;
SELECT * FROM film;
SELECT * FROM payment;
SELECT * FROM address;
SELECT * FROM language;
SELECT * FROM staff;
SELECT * FROM city;
SELECT * FROM country;
SELECT * FROM store;
SELECT * FROM actor;
SELECT * FROM film_actor;

--Aquellas usadas para insertar, modificar y eliminar un Customer, Staff y Actor.
--Customer
--Ingresar
INSERT INTO customer(customer_id, store_id, first_name, last_name, email, address_id, activebool, create_date, last_update, active) 
VALUES (xx,xx,xx,xx,xx,xx,xx,xx,xx,xx);--valores
--Modificar
UPDATE customer SET parametro_a_cambiar = 'valor_nuevo' WHERE parametro_a_cambiar = 'valor_a_cambiar';
-- Eliminar
DELETE FROM customer WHERE parametro_unico = 'valor';

--Staff
--Ingresar
INSERT INTO staff(staff_id, first_name, last_name, address_id, email, store_id, active, username, password, last_update, picture) 
VALUES (xx,xx,xx,xx,xx,xx,xx,xx,xx,xx,xx);--valores
--Modificar
UPDATE staff SET parametro_a_cambiar = 'valor_nuevo' WHERE parametro_a_cambiar = 'valor_a_cambiar';
-- Eliminar
DELETE FROM staff WHERE parametro_unico = 'valor';

--Actor
--Ingresar
INSERT INTO actor(actor_id, first_name, last_name, last_update) 
VALUES (xx, xx, xx, xx);--valores
--Modificar
UPDATE actor SET parametro_a_cambiar = 'valor_nuevo' WHERE parametro_a_cambiar = 'valor_a_cambiar';
-- Eliminar
DELETE FROM actor WHERE parametro_unico = 'valor';


--Listar todas las “rental” con los datos del “customer” dado un año y mes.
SELECT 
c.customer_id, c.store_id, c.first_name, c.last_name, c.email, c.address_id, c.activebool, c.create_date, c.last_update, c.active, 
r.rental_date, r.inventory_id, r.customer_id, r.return_date, r.staff_id, r.last_update
FROM rental AS r
JOIN customer AS c
ON r.customer_id = c.customer_id
WHERE EXTRACT(MONTH FROM r.rental_date) = '05' AND EXTRACT(YEAR FROM r.rental_date) = '2005';

--Listar Número, Fecha (payment_date) y Total (amount) de todas las “payment”.
SELECT payment_id AS Número, payment_date AS Fecha, amount AS Total FROM payment ORDER BY Fecha asc;

--Listar todas las “film” del año 2006 que contengan un (rental_rate) mayor a 4.0.
SELECT * FROM film WHERE release_year = 2006 AND rental_rate > 4.0;

--Realiza un Diccionario de datos que contenga el nombre de las tablas y columnas, si
--éstas pueden ser nulas, y su tipo de dato correspondiente.

SELECT
    t1.TABLE_NAME AS tabla_nombre,
    t1.COLUMN_NAME AS columna_nombre,
    t1.COLUMN_DEFAULT AS columna_defecto,
    t1.IS_NULLABLE AS columna_nulo,
    t1.DATA_TYPE AS columna_tipo_dato,
    COALESCE(t1.NUMERIC_PRECISION,
    t1.CHARACTER_MAXIMUM_LENGTH) AS columna_longitud,
    PG_CATALOG.COL_DESCRIPTION(t2.OID,
    t1.DTD_IDENTIFIER::int) AS columna_descripcion,
    t1.DOMAIN_NAME AS columna_dominio
FROM 
    INFORMATION_SCHEMA.COLUMNS t1
    INNER JOIN PG_CLASS t2 ON (t2.RELNAME = t1.TABLE_NAME)
WHERE 
    t1.TABLE_SCHEMA = 'public'
ORDER BY
    t1.TABLE_NAME;
