BEGIN;

SAVEPOINT uno;

CREATE TABLE peliculas(
    id INT PRIMARY KEY,
    pelicula VARCHAR(255),
    estreno INT,
    director VARCHAR(255)
);

CREATE TABLE reparto(
    id_pelicula INT,
    actor VARCHAR(255),
    FOREIGN KEY(id_pelicula) REFERENCES peliculas(id)
);

COMMIT;

--3. Cargar ambos archivos a su tabla correspondiente.
--\COPY "peliculas" FROM 'C:\Users\miran\ApoyoCSV\peliculas.csv' WITH CSV;
--\COPY "reparto" FROM 'C:\Users\miran\ApoyoCSV\reparto.csv' WITH CSV;

-- 7. Listar todos los actores que aparecen en la película "Titanic", indicando el título de la película, año de estreno, director y todo el reparto
--Forma A
SELECT pelicula, estreno, director, actor FROM peliculas 
JOIN reparto 
ON peliculas.id = reparto.id_pelicula
WHERE pelicula = 'Titanic';
--Forma B 
SELECT p.pelicula, p.estreno, p.director, r.actor FROM peliculas AS p 
JOIN reparto AS r
ON p.id = r.id_pelicula
WHERE pelicula = 'Titanic';

-- 8. Listar los 10 directores más populares, indicando su nombre y cuántas películas aparecen en el top 100.
SELECT director, COUNT(director) AS Top_100 FROM peliculas GROUP BY director ORDER BY Top_100 DESC LIMIT 10;

-- 9. Indicar cuántos actores distintos hay.
SELECT COUNT(DISTINCT actor) AS Total_Distintos FROM reparto;

-- 10. Indicar las películas estrenadas entre los años 1990 y 1999 (ambos incluidos), ordenadas por título de manera ascendente.
SELECT pelicula, estreno FROM peliculas WHERE estreno BETWEEN 1990 AND 1999;

-- 11. Listar los actores de la película más nueva.
SELECT r.actor, p.pelicula, p.estreno FROM peliculas AS p 
JOIN reparto AS r
ON p.id = r.id_pelicula
WHERE estreno = (SELECT MAX(estreno) FROM peliculas);

-- 12. Inserte los datos de una nueva película solo en memoria, y otra película en el disco duro.
--TEMPORAL
BEGIN;
SAVEPOINT save_1;
INSERT INTO peliculas VALUES(101, 'Avatar', 2009, 'James Cameron');
--ROLLBACK TO SAVEPOINT save_1 --(Opcional)
COMMIT;
ROLLBACK;
--DIRECTO al Disco
INSERT INTO peliculas VALUES(102, 'Avatar 2', 2022, 'James Cameron');
--DELETE FROM peliculas WHERE id_pelicula = 102;

-- 13. Actualice 5 directores utilizando ROLLBACK.
BEGIN;
UPDATE peliculas SET director = CASE director
	WHEN 'Robert Zemeckis' THEN 'Bob esponja'
	WHEN 'James Cameron' THEN 'Patricio'
	WHEN 'Francis Ford Coppola' THEN 'Calamardo'
	WHEN 'Ridley Scott' THEN 'Don Cangrejo'
	WHEN 'Peter Jackson' THEN 'Arenita'
	ELSE director
	END;
ROLLBACK;

-- 14. Inserte 3 actores a la película “Rambo” utilizando SAVEPOINT
--IDENTIFICANDO id RAMBO
SELECT id, pelicula FROM peliculas WHERE pelicula = 'Rambo';

BEGIN;
SAVEPOINT save_1;
INSERT INTO reparto VALUES (72, 'Hugo');
SAVEPOINT save_2;
INSERT INTO reparto VALUES (72, 'Paco');
SAVEPOINT save_3;
INSERT INTO reparto VALUES (72, 'Luis');

--ROLLBACK
ROLLBACK TO SAVEPOINT save_1;
ROLLBACK TO SAVEPOINT save_2;
ROLLBACK TO SAVEPOINT save_3;

COMMIT;
--14 END


-- 15. Elimina las películas estrenadas el año 2008 solo en memoria.
BEGIN;
ALTER TABLE reparto DISABLE TRIGGER ALL;
ALTER TABLE peliculas DISABLE TRIGGER ALL;
DELETE FROM peliculas WHERE estreno = 2008;

ROLLBACK;

-- 16. Inserte 2 actores para cada película estrenada el 2001.


BEGIN;
INSERT INTO reparto VALUES
	(13, 'Juan Carlos Bodoque'),
	(13, 'Tulio Tribiño'),
	(16, 'Juan Carlos Bodoque'),
	(16, 'Tulio Tribiño'),	
	(55, 'Juan Carlos Bodoque'),
	(55, 'Tulio Tribiño'),	
	(78, 'Juan Carlos Bodoque'),
	(78, 'Tulio Tribiño'),
	(94, 'Juan Carlos Bodoque'),
	(94, 'Tulio Tribiño'),
	(99, 'Juan Carlos Bodoque'),
	(99, 'Tulio Tribiño');

ROLLBACK;
	
-- 17. Actualice la película “King Kong” por el nombre de “Donkey Kong”, sin efectuar cambios en disco duro.
BEGIN;
UPDATE peliculas SET pelicula = 'Donkey Kong' WHERE pelicula = 'King Kong';

ROLLBACK;

--CONSULTAS
SELECT * FROM peliculas WHERE estreno = 2001;
SELECT * FROM peliculas WHERE estreno = 2008;
SELECT * FROM peliculas;
SELECT * FROM reparto;