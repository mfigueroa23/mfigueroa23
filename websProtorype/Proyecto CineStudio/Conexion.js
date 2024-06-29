
const express = require('express');
const path = require('path');
const mysql = require('mysql');
const { constants } = require('buffer');

const app = express();

const MySQL = mysql.createConnection({
    host: '10.0.6.39',
    user: 'estudiante',
    password: 'Info-2023',
    database: 'cinestudio'

});

app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.set('views', path.join(__dirname, 'views'));
app.use(express.static(path.join(__dirname, 'views')));

app.get('/', function (req, res) {

    res.sendFile(path.join(__dirname, './views/Index.html'));
});
app.post('/Guardar_pelicula', (req, res) => {

    console.log(req)

    const { nombre, descripcion, fecha, categoria, entrada } = req.body;

    const query = 'INSERT INTO Peliculas (Nombre, Descripcion, Fecha, Categoria, Precio) VALUES (?, ?, ?, ?, ?)';
    const values = [nombre, descripcion, fecha, categoria, entrada];

    MySQL.query(query, values, (err, results) => {
        if (err) {
            console.error('Error al insertar los datos en la DB: ' + err.stack);
            return res.status(500).send({
                message: 'Error al insertar los datos en la base de datos'
            });
        }
        res.status(200).sendFile(path.join(__dirname, './views/index.html'));
    });

});

app.get('/GuardarPeliculas', (req, res) => {
    const query = 'SELECT * FROM Peliculas';
    MySQL.query(query, (err, results) => {
        if (err) {
            console.error('Error al obtener los datos de la DB: ' + err.stack);
            return res.status(500).send({
                message: 'Error al obtener los datos de la Base de Datos'
            });
        }
        res.status(200).send({
            message: 'Datos obtenidos exitosamente',
            data: results
        });
    });
});

app.listen(3006, function () {

    console.log("Conexión exitosa a la base de datos MySQL http://localhost:3006");
});
