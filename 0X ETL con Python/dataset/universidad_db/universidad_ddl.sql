CREATE DATABASE universidad;
USE universidad;

CREATE TABLE alumno ( 
rutAlu Char(12) NOT NULL, 
Nombre Char(30) NOT NULL 
);

ALTER TABLE alumno ADD PRIMARY KEY (rutAlu);

CREATE TABLE asignatura( 
codAsig Char(5) NOT NULL, 
Nombre Char(30), 
Horas Int, 
rutProf Char(12)
);

ALTER TABLE asignatura ADD PRIMARY KEY (codAsig);

CREATE TABLE profesor( 
rutProf Char(12) NOT NULL, 
Nombre Varchar(50) NOT NULL, 
cod Char(5), 
IdDep int
);

ALTER TABLE profesor ADD PRIMARY KEY (rutProf);

CREATE TABLE cursa( 
rutAlu Char(12) NOT NULL, 
codAsig Char(5) NOT NULL, 
Anio Int, 
Semestre Int, 
Promedio Double
);

ALTER TABLE cursa ADD PRIMARY KEY (rutAlu,codAsig);

CREATE TABLE titulo( 
cod Char(5) NOT NULL, 
nombre Varchar(30)
);

ALTER TABLE titulo ADD PRIMARY KEY (cod);

CREATE TABLE departamento( 
IdDep int NOT NULL, 
nombre Char(20), 
PresupuestoAnual Double, 
rutProf Char(12)
);

ALTER TABLE departamento ADD PRIMARY KEY (IdDep);

ALTER TABLE cursa ADD CONSTRAINT alumnocursa FOREIGN KEY (rutAlu) 
REFERENCES alumno (rutAlu) 
ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE cursa ADD CONSTRAINT Impartidas FOREIGN KEY (codAsig) 
REFERENCES asignatura (codAsig) 
ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE asignatura ADD CONSTRAINT Imparte FOREIGN KEY (rutProf) 
REFERENCES profesor (rutProf) 
ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE profesor ADD CONSTRAINT tituloProf FOREIGN KEY (cod) 
REFERENCES titulo (cod) 
ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE profesor ADD CONSTRAINT Pertenece FOREIGN KEY (IdDep) 
REFERENCES departamento (IdDep) 
ON DELETE NO ACTION ON UPDATE NO ACTION;