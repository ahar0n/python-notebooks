CREATE DATABASE VentasDM;
USE VentasDM;
        
CREATE TABLE Libro
(
  LibroID INT          NOT NULL,
  Titulo  VARCHAR(500) NOT NULL,
  Genero  VARCHAR(200) NULL    ,
  PRIMARY KEY (LibroID)
) COMMENT 'Dimension';

CREATE TABLE Localizacion
(
  LocalizacionID INT          NOT NULL,
  Comuna         VARCHAR(200) NOT NULL,
  Region         VARCHAR(200) NOT NULL,
  PRIMARY KEY (LocalizacionID)
) COMMENT 'Dimension';

CREATE TABLE Tiempo
(
  TiempoID  INT NOT NULL,
  Dia       INT NOT NULL,
  Mes       INT NOT NULL,
  Anio      INT NOT NULL,
  PRIMARY KEY (TiempoID)
) COMMENT 'Dimension';

CREATE TABLE Ventas
(
  LocalizacionID INT NOT NULL,
  TiempoID       INT NOT NULL,
  LibroID        INT NOT NULL,
  Cantidad       INT NOT NULL,
  PRIMARY KEY (LocalizacionID, TiempoID, LibroID)
) COMMENT 'FactTable';

ALTER TABLE Ventas
  ADD CONSTRAINT FK_Localizacion_TO_Ventas
    FOREIGN KEY (LocalizacionID)
    REFERENCES Localizacion (LocalizacionID);

ALTER TABLE Ventas
  ADD CONSTRAINT FK_Tiempo_TO_Ventas
    FOREIGN KEY (TiempoID)
    REFERENCES Tiempo (TiempoID);

ALTER TABLE Ventas
  ADD CONSTRAINT FK_Libro_TO_Ventas
    FOREIGN KEY (LibroID)
    REFERENCES Libro (LibroID);