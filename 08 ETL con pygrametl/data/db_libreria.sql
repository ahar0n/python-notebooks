CREATE DATABASE Libreria;
USE Libreria;

CREATE TABLE Libro(
    LibroID INT PRIMARY KEY, 
    Titulo VARCHAR(500) NOT NULL, 
    Autor VARCHAR(500),
    EditorialID INT NOT NULL,
    GeneroID INT NOT NULL
);

CREATE TABLE Genero(
    GeneroID int PRIMARY KEY,
    Nombre varchar(200) NOT NULL
);

CREATE TABLE Editorial(
    EditorialID int PRIMARY KEY,
    Nombre varchar(200) NOT NULL
);

ALTER TABLE Libro ADD CONSTRAINT fk_Libro_Genero foreign key(GeneroID)
references Genero(GeneroID)
on delete no action on update no action;

ALTER TABLE Libro ADD CONSTRAINT fk_Libro_Editorial foreign key(EditorialID)
references Editorial(EditorialID)
on delete no action on update no action;

CREATE TABLE Cliente(
    ClienteID varchar(9) PRIMARY KEY,
    NombreCliente varchar(100),
    ApellidoCliente varchar(100) NOT NULL,
    Direccion varchar(500),
    ComunaID int NOT NULL
);

CREATE TABLE Comuna(
    ComunaID int PRIMARY KEY,
    Nombre varchar(200) NOT NULL
);

ALTER TABLE Cliente ADD CONSTRAINT fk_Cliente_Comuna foreign key(ComunaID)
references Comuna(ComunaID)
on delete no action on update no action;

CREATE TABLE Pedido(
    OrdenID int AUTO_INCREMENT PRIMARY KEY,
    ClienteID varchar(9) NOT NULL,
    LibroID int NOT NULL,
    Cantidad INT NOT NULL,
    Fecha datetime NOT NULL
);

ALTER TABLE Pedido ADD CONSTRAINT fk_Pedido_Cliente foreign key(ClienteID)
references Cliente(ClienteID)
on delete no action on update no action;

ALTER TABLE Pedido ADD CONSTRAINT fk_Pedido_Libro foreign key(LibroID)
references Libro(LibroID)
on delete no action on update no action;