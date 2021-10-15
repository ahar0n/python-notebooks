use universidad;

-- Tabla Departamento ------------------------------------------- 
insert into departamento (idDep, nombre, presupuestoAnual, rutProf) values (1, 'ingenieria', 100000000, '11111111-1');
insert into departamento (idDep, nombre, presupuestoAnual, rutProf) values (2, 'sistemas', 50000000, '10354869-7');
insert into departamento (idDep, nombre, presupuestoAnual, rutProf) values (3, 'matematica', 150000000, '167458852-9');

-- Tabla Título -------------------------------------------------
insert into titulo (cod, nombre) values ('12345', 'ingeniero informatico'); 
insert into titulo (cod, nombre) values ('67890', 'mecanico');
insert into titulo (cod, nombre) values ('78678', 'cartógrafo');

-- Tabla Profesor -----------------------------------------------
insert into profesor (rutProf, nombre, cod, IdDep) values ('11111111-1', 'juan perez', '78678', 1);
insert into profesor (rutProf, nombre, cod, IdDep) values ('121914856-5', 'jose carrasco', '12345', 1);
insert into profesor (rutProf, nombre, cod, IdDep) values ('10354869-7', 'manuel osess', '67890', 1);
insert into profesor (rutProf, nombre, cod, IdDep) values ('15487956-8', 'marco lopez', '67890', 2);
insert into profesor (rutProf, nombre, cod, IdDep) values ('167458852-9', 'anita bustamante', '12345', 2);

-- Tabla Alumno -------------------------------------------------
insert into alumno (rutAlu, nombre) values ('15126954-8', 'margarita pinilla'); 
insert into alumno (rutAlu, nombre) values ('14852654-7', 'monica soto');
insert into alumno (rutAlu, nombre) values ('15785365-8', 'marco ferj'); 
insert into alumno (rutAlu, nombre) values ('14652985-4', 'manuel resto'); 

-- Tabla Asignatura ---------------------------------------------
insert into asignatura (codAsig, nombre, horas, rutProf) values ( '11111', 'logistica', 6, '11111111-1');
insert into asignatura (codAsig, nombre, horas, rutProf) values ( '22222', 'calculo I', 6, '121914856-5');
insert into asignatura (codAsig, nombre, horas, rutProf) values ( '33333', 'fisica I', 4, '10354869-7');

-- Tabla Cursa --------------------------------------------------
insert into cursa (rutAlu, codAsig, Anio, Semestre, Promedio) values ('15126954-8', '11111', 2010, 1, 4.5);
insert into cursa (rutAlu, codAsig, Anio, Semestre, Promedio) values ('15126954-8', '22222', 2010, 1, 3.6);
insert into cursa (rutAlu, codAsig, Anio, Semestre, Promedio) values ('15126954-8', '33333', 2010, 2, 3.7);
insert into cursa (rutAlu, codAsig, Anio, Semestre, Promedio) values ('14852654-7', '11111', 2010, 1, 5.8);
insert into cursa (rutAlu, codAsig, Anio, Semestre, Promedio) values ('14852654-7', '22222', 2010, 2, 5.2);
insert into cursa (rutAlu, codAsig, Anio, Semestre, Promedio) values ('14852654-7', '33333', 2010, 2, 3.8);
insert into cursa (rutAlu, codAsig, Anio, Semestre, Promedio) values ('14652985-4', '11111', 2010, 1, 3.4);