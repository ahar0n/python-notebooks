select * from Localizacion;

USE VentasDM;
SELECT sum(Ventas.Cantidad) AS 'cant',
    Tiempo.Anio AS 'año',
    Localizacion.Region AS 'region'
FROM Ventas, Tiempo, Localizacion
WHERE Ventas.TiempoID = Tiempo.TiempoID
    AND Ventas.LocalizacionID = Localizacion.LocalizacionID
GROUP BY año, region;