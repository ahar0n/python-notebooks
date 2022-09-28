INSERT INTO Libreria.Editorial VALUES(1, 'Wiley');
INSERT INTO Libreria.Editorial VALUES(2, 'Penguin');
INSERT INTO Libreria.Editorial VALUES(3, 'Springer');
INSERT INTO Libreria.Editorial VALUES(4, 'CRC');
INSERT INTO Libreria.Editorial VALUES(5, 'MIT Press');
INSERT INTO Libreria.Editorial VALUES(6, 'HarperCollins');

INSERT INTO Libreria.Genero VALUES(1, 'Mathematics');
INSERT INTO Libreria.Genero VALUES(2, 'Data Science');
INSERT INTO Libreria.Genero VALUES(3, 'Economics');
INSERT INTO Libreria.Genero VALUES(4, 'History');
INSERT INTO Libreria.Genero VALUES(5, 'Science');

INSERT INTO Libreria.Libro VALUES(1, 'Data Smart', 'Foreman, John', 1, 2);
INSERT INTO Libreria.Libro VALUES(2, 'God Created the Integers', 'Hawking, Stephen', 2, 1);
INSERT INTO Libreria.Libro VALUES(3, 'Superfreakonomics',	'Dubner, Stephen',	6, 3);
INSERT INTO Libreria.Libro VALUES(4, 'Orientalism',	'Said, Edward', 2, 4);
INSERT INTO Libreria.Libro VALUES(6, 'The Nature of Statistical Learning Theory', 'Vapnik, Vladimir', 3, 2);
INSERT INTO Libreria.Libro VALUES(7, 'The Drunkards Walk', 'Mlodinow, Leonard', 2, 2);

INSERT INTO Libreria.Comuna VALUES(1, 'Santiago');
INSERT INTO Libreria.Comuna VALUES(2, 'Concepción');
INSERT INTO Libreria.Comuna VALUES(3, 'Rancagua');
INSERT INTO Libreria.Comuna VALUES(4, 'Iquique');
INSERT INTO Libreria.Comuna VALUES(5, 'La Serena');
INSERT INTO Libreria.Comuna VALUES(6, 'Temuco');
INSERT INTO Libreria.Comuna VALUES(7, 'Valdivia');

INSERT INTO Libreria.Cliente VALUES ('17171171K','Jossica','Jones', 'Franklin 123', 1);
INSERT INTO Libreria.Cliente VALUES ('181234321','Javier','Rosales', 'Sebastopol 554', 1);
INSERT INTO Libreria.Cliente VALUES ('161231232','Rosa','Saez', 'Campo Lindo 221', 1);
INSERT INTO Libreria.Cliente VALUES ('19287123K','Juan','Tapia', 'Colon 23', 2);
INSERT INTO Libreria.Cliente VALUES ('15287123K','Eric','Lara', 'Ohiggins 661', 4);

INSERT INTO Libreria.Pedido (ClienteID, LibroID, Cantidad, Fecha) VALUES('17171171K',1,3,'2008-11-11 13:00:00');
INSERT INTO Libreria.Pedido (ClienteID, LibroID, Cantidad, Fecha) VALUES('181234321',3,1,'2008-10-09 18:20:00');
INSERT INTO Libreria.Pedido (ClienteID, LibroID, Cantidad, Fecha) VALUES('181234321',2,1,'2010-01-03 15:00:00');
INSERT INTO Libreria.Pedido (ClienteID, LibroID, Cantidad, Fecha) VALUES('19287123K',2,1,'2011-02-03 12:00:00');
INSERT INTO Libreria.Pedido (ClienteID, LibroID, Cantidad, Fecha) VALUES('15287123K',2,1,'2010-04-04 11:00:00');
INSERT INTO Libreria.Pedido (ClienteID, LibroID, Cantidad, Fecha) VALUES('15287123K',6,1,'2011-01-11 13:00:00');
INSERT INTO Libreria.Pedido (ClienteID, LibroID, Cantidad, Fecha) VALUES('19287123K',3,2,'2012-08-03 11:00:00');