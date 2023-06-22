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


--Iniciando una transacción
BEGIN;

--Asegruando el primer estado creando un Save
SAVEPOINT primer_save;

--Inserte 5 herramientas.
INSERT INTO herramienta VALUES(1,'Taladro Electrico',10000),
                              (2,'Cierra Electrica',20000),
                              (3,'Pistola de Clavos',30000),
                              (4,'Lijadora',40000),
                              (5,'Serrucho Electrico',50000);
		

--Asegruando el segundo estado creando un Save							  
SAVEPOINT segundo_save;


--Inserte 3 clientes.
INSERT INTO cliente VALUES('22222222-2','Juan Perez','j.perez@mail.com','1 Calle Uno',2222222222),
                          ('33333333-3','Juanita Sánches','j.sanches@mail.com','2 Calle Dos',3333333333),
                          ('44444444-4','Marcelo Ugarte','m.ugarte@mail.com','3 Calle Tres',4444444444);


--Asegruando el tercer estado creando un Save							  
SAVEPOINT tercer_save;						  
						  
--Elimina el último cliente
DELETE FROM cliente WHERE rut = '44444444-4';						  

--Asegruando el tercer estado creando un Save							  
SAVEPOINT cuarto_save;

--Elimina la primera herramienta.
DELETE FROM herramienta WHERE id_herramienta = 1;

--Asegruando el quinto estado creando un Save							  
SAVEPOINT quinto_save;

--Inserte 2 arriendos para cada cliente
INSERT INTO arriendo VALUES
	(1,'15/01/20',5,20000,'Eficacia en 5 dias o menos',2,'22222222-2'),
   	(2,'12/11/22',2,30000,'Eficacia en 2 dias o menos',3,'22222222-2'),
   	(3,'15/01/20',1,40000,'Eficacia en 1 dia',4,'33333333-3'),
   	(4,'12/11/22',3,40000,'Eficacia en solo 3 dias',5,'33333333-3');

--Asegruando el sexto estado creando un Save							  
SAVEPOINT sexto;	

--Modifique el correo electrónico del primer cliente.
UPDATE cliente SET correo = 'j_perez@mail.com' WHERE rut = '22222222-2';
	
--Elimina el quinto SAVE
RELEASE SAVEPOINT quinto_save;

--si estoy contento y sucede todo bien, realizamos un commit
COMMIT;

--no estoy contento con el estado, se regresa completamente al ultimo estado valido
ROLLBACK;

--CONSULTAS	
SELECT * FROM cliente;						  
SELECT * FROM herramienta;
SELECT * FROM empresa;
SELECT * FROM arriendo;

ROLLBACK TO SAVEPOINT primer_save;
ROLLBACK TO SAVEPOINT segundo_save;
ROLLBACK TO SAVEPOINT tercer_save;
ROLLBACK TO SAVEPOINT cuarto_save;
ROLLBACK TO SAVEPOINT quinto_save;
