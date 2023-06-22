--tabla categorias
--PK categoria_id, nombre

CREATE TABLE categorias(
	categoria_id SERIAL PRIMARY KEY,
	nombre VARCHAR(50)
);

--tabla productos
--PK producto_id, nombre, precio, FK categoria_id

CREATE TABLE productos(
	producto_id SERIAL PRIMARY KEY,
	nombre VARCHAR(50),
	precio INT,
	categoria_id INT,
	FOREIGN KEY (categoria_id) REFERENCES categorias(categoria_id)
);

-- insertar valores "categorias"

INSERT INTO categorias(nombre) VALUES('Electronica');
INSERT INTO categorias(nombre) VALUES('Ropa');
INSERT INTO categorias(nombre) VALUES('Hogar');


-- Consulta tabla categorias
SELECT * FROM categorias;


-- insertar valores "productos"
INSERT INTO productos(nombre,precio,categoria_id) VALUES 
	('Telefono',12000,1),
	('Televisor',500000,1),
	('Pantalon',1000,2),
	('Polera',500,2),
	('Tetera',2500,3),
	('Mesa',40000,3);
	
-- Consulta tabla productos
SELECT * FROM productos;