-- Cantidad de estudiantes, separados por genero, que postularon a una carrera técnica (nivel de carrera) por cada ciudad de origen (colegio) y por cada año.
-- Libro, Genero, Ciudad, fecha, Cantidad
USE Libreria;
SELECT date_format(Pedido.fecha, '%d-%m-%Y') AS 'fecha',
    Libro.Titulo AS 'Libro',
    Genero.Nombre AS 'Genero',
    Ciudad.Nombre AS 'Ciudad',
    sum(Pedido.Cantidad) AS 'cantidad'
FROM Pedido, Libro, Genero, Ciudad, Cliente
WHERE Pedido.LibroID = Libro.LibroID
    AND Libro.GeneroID = Genero.GeneroID
    AND Pedido.ClienteID = Cliente.ClienteID
    AND Cliente.CiudadID = Ciudad.CiudadID
GROUP BY date_format(Pedido.fecha, '%d-%m-%Y'), Libro.Titulo, Genero.Nombre, Ciudad.Nombre;