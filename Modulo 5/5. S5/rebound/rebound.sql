BEGIN;

CREATE TABLE editoriales (
    codigo SERIAL PRIMARY KEY,
    nombre VARCHAR(255)
);

CREATE TABLE libros(
    codigo SERIAL PRIMARY KEY,
    titulo VARCHAR(255),
    codigo_editorial INT,
    FOREIGN KEY(codigo_editorial) REFERENCES editoriales(codigo)
);

SAVEPOINT save_1;

INSERT INTO editoriales(nombre) VALUES
    ('Anaya'),
    ('Andina'),
    ('S.M');

SAVEPOINT save_2;

INSERT INTO libros(titulo, codigo_editorial) VALUES
    ('Don Quijote de La Mancha I', 1),
    ('El principito', 2),
    ('El principe', 3),
    ('Diplomacia', 3),
    ('Don Quijote de La Mancha II', 1);

SAVEPOINT save_3;

ALTER TABLE libros ADD autor VARCHAR(255), ADD precio MONEY;

SAVEPOINT save_4;

UPDATE libros SET autor = CASE
    WHEN codigo = 1 THEN 'Miguel de Cervantes'
    WHEN codigo = 2 THEN 'Antoine SaintExupery'
    WHEN codigo = 3 THEN 'Maquiavelo'
    WHEN codigo = 4 THEN 'Henry kissinger'
    WHEN codigo = 5 THEN 'Miguel de Cervantes'
    END
Where codigo IN (1,2,3,4,5);

SAVEPOINT save_5;

UPDATE libros SET precio = CASE
    WHEN codigo = 1 THEN 150
    WHEN codigo = 2 THEN 120
    WHEN codigo = 3 THEN 180
    WHEN codigo = 4 THEN 170
    WHEN codigo = 5 THEN 140
    END
Where codigo IN (1,2,3,4,5);

SAVEPOINT save_6;

INSERT INTO libros(titulo,codigo_editorial,autor,precio) VALUES
    ('El Mundo de luna', 1, 'Francisco Puelma', 120),
    ('Bluey', 2, 'Pepa Pig', 150);

SAVEPOINT save_7;

DELETE FROM libros WHERE codigo_editorial = 1;

ROLLBACK TO SAVEPOINT save_7;

COMMIT;

BEGIN;

UPDATE editoriales SET nombre = 'Iberlibro' WHERE nombre = 'Andina';
UPDATE editoriales SET nombre = 'Mountain' WHERE nombre = 'S.M';

SAVEPOINT ocho;

ROLLBACK;

--CONSULTAS
SELECT * FROM editoriales;
SELECT * FROM libros;