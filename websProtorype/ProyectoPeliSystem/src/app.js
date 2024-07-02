import express from 'express';
import { join } from 'path';
import { fileURLToPath } from 'url';
import mysql from 'mysql2/promise';

const __filename = fileURLToPath(import.meta.url);
const __dirname = join(__filename, '..');

const app = express();
app.use(express.urlencoded({ extended: false }));
app.use(express.json());

class DataSource {

    // ¡¡¡ INGRESAR PASS PARA EL USUARIO ROOT !!!
    constructor() {
        this.config = {
            host: 'localhost',
            user: 'root',
            password: 'F3rr4r1.1',
            database: 'PeliSystem'
        };
        this.pool = null;
    }

    async connect() {
        try {
            this.pool = await mysql.createPool(this.config);
            console.log('[info]: Conexión establecida.');
        } catch (error) {
            console.error('[error]: Error al conectar con la base de datos:', error);
            throw error;
        }
    }

    async disconnect() {
        try {
            if (this.pool) {
                await this.pool.end();
                console.log('[info]: Desconexión exitosa.');
            }
        } catch (error) {
            console.error('[error]: Error al desconectar de la base de datos:', error);
            throw error;
        }
    }

    async getConnection() {
        try {
            if (!this.pool) {
                await this.connect();
            }
            return await this.pool.getConnection();
        } catch (error) {
            console.error('[error]: Error al obtener la conexión de la base de datos:', error);
            throw error;
        }
    }
}

const dataSource = new DataSource();
async function crearPelicula(movieData) {
    try {
        console.log('[info]: Conectando a la base de datos...');
        await dataSource.connect();
        const connection = await dataSource.getConnection();
        const query = `INSERT INTO movies (movieName, movieDescription, movieCategory, movieRelease, moviePrice) 
                       VALUES (?, ?, ?, ?, ?)`;
        await connection.execute(query, [
            movieData.movieName,
            movieData.movieDescription,
            movieData.movieCategory,
            movieData.movieRelease,
            movieData.moviePrice
        ]);
        console.log('[info]: Película creada exitosamente.');
        return true;
    } catch (error) {
        console.error(`[error]: Error al crear la película: ${error}`);
        return false;
    } finally {
        if (dataSource.pool) {
            await dataSource.disconnect();
        }
    }
}

async function obtenerTodasLasPeliculas() {
    try {
        console.log('[info]: Conectando a la base de datos...');
        await dataSource.connect();
        const connection = await dataSource.getConnection();
        const query = 'SELECT id, movieName, movieDescription, movieCategory, movieRelease, moviePrice FROM movies';
        const [rows, fields] = await connection.execute(query);
        console.log('[info]: Películas obtenidas correctamente.');
        return rows;
    } catch (error) {
        console.error('[error]: Error al obtener las películas:', error);
        return false;
    } finally {
        if (dataSource.pool) {
            await dataSource.disconnect();
        }
    }
}

async function eliminarPelicula(id){
    try {
        console.log('[info]: Conectando a la base de datos...');
        await dataSource.connect();
        const connection = await dataSource.getConnection();
        const query = 'DELETE FROM movies WHERE id = ?';
        await connection.execute(query, [id]);
        console.log('[info]: Película eliminada correctamente.');
        return true;
    } catch (error) {
        console.error('[error]: Error al eliminar la película:', error);
        return false;
    } finally {
        if (dataSource.pool) {
            await dataSource.disconnect();
        }
    }
}

app.use(express.static(join(__dirname, '../client')));
app.get('/', (req, res) => {
    res.sendFile(join(__dirname, '../client/index.html'));
});

app.post('/api/crearPelicula', async (req, res) => {
    try {
        const dataPelicula = req.body;
        const create = await crearPelicula({ ...dataPelicula });
        if(create){
            res.redirect('/listar.html');
        } else {
            res.redirect('/');
        }
    } catch (error) {
        console.log(`[error]: ${error}`);
        res.json({ status: false, message: 'Ha ocurrido un error.' });
    };
});

app.get('/api/listarPeliculas', async (req, res) => {
    try {
        const peliculas = await obtenerTodasLasPeliculas();
        res.json(peliculas);
    } catch (error) {
        console.error('[error]:', error.message);
        res.status(500).json({ status: false, message: 'Ha ocurrido un error al obtener las películas.' });
    }
});

app.delete('/api/eliminarPelicula', async (req, res) => {
    try {
        const { id } = req.query;
        const deletePeli = await eliminarPelicula(id);
        if (deletePeli) {
            res.json({ status: true, message: 'Película eliminada correctamente.' });
        } else {
            res.json({ status: false, message: 'Ha ocurrido un error al eliminar la película.' });
        }
    } catch (error) {
        console.error('[error]:', error.message);
        res.status(500).json({ status: false, message: 'Ha ocurrido un error al eliminar la película.' });
    }
});

const port = 8080;
app.listen(port);
console.log(`[info]: Servicio URL http://127.0.0.1:${port}`);
