import express from 'express';
import { join } from 'path';
import { fileURLToPath } from 'url';
import mysql from 'mysql2/promise';
import crypt from 'crypto-js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = join(__filename, '..');

class DataSource {

    // ¡¡¡ INGRESAR PASS PARA EL USUARIO ROOT !!!
    constructor() {
        this.config = {
            host: '127.0.0.1',
            user: 'root',
            password: 'F3rr4r1.1',
            database: 'programweb'
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
async function crearUsuario(userData) {
    try {
        console.log('[info]: Conectando a la base de datos...');
        await dataSource.connect();
        const connection = await dataSource.getConnection();
        const keyCrypt = 'Yvouubhtay4Qfj3x';
        const passCrypt = crypt.AES.encrypt(userData.passwd, keyCrypt).toString();
        const query = `INSERT INTO users (userName, userEmail, userPass) 
                       VALUES (?, ?, ?)`;
        await connection.execute(query, [
            userData.name,
            userData.email,
            passCrypt,
        ]);
        console.log('[info]: Usuario creado exitosamente.');
        return true;
    } catch (error) {
        console.error(`[error]: Error al crear el usuario: ${error}`);
        return false;
    } finally {
        if (dataSource.pool) {
            await dataSource.disconnect();
        }
    }
}
async function obtenerUsuario(userName){
    try {
        console.log('[info]: Conectando a la base de datos...');
        await dataSource.connect();
        const connection = await dataSource.getConnection();
        const query = `SELECT userName FROM users WHERE userName = '${userName}'`;
        const [rows, fields] = await connection.execute(query);
        console.log(`[info]: Usuario ${userName} obtenido correctamente.`);
        return rows;
    } catch (error) {
        console.error('[error]: Error al obtener el usuario:', error);
        return false;
    } finally {
        if (dataSource.pool) {
            await dataSource.disconnect();
        }
    }
}
async function obtenerCorreo(userEmail){
    try {
        console.log('[info]: Conectando a la base de datos...');
        await dataSource.connect();
        const connection = await dataSource.getConnection();
        const query = `SELECT userEmail FROM users WHERE userEmail = '${userEmail}'`;
        const [rows, fields] = await connection.execute(query);
        console.log(`[info]: Correo ${userEmail} obtenido correctamente.`);
        return rows;
    } catch (error) {
        console.error('[error]: Error al obtener el correo:', error);
        return false;
    } finally {
        if (dataSource.pool) {
            await dataSource.disconnect();
        }
    }
}

const app = express();
app.use(express.urlencoded({ extended: false }));
app.use(express.json());

app.use(express.static(join(__dirname, '../public')));
app.get('/', (req, res) => {
    res.sendFile(join(__dirname, '../public/index.html'));
});

app.post('/api/crearUsuario', async (req, res) => {
    try {
        const dataUser = req.body;
        const create = await crearUsuario({ ...dataUser });
        if(create){
            res.redirect('/index.html');
        } else {
            res.redirect('https://google.com');
        }
    } catch (error) {
        console.log(`[error]: ${error}`);
        res.json({ status: false, message: 'Ha ocurrido un error.' });
    };
});

app.get('/api/users', async (req, res) => {
    try {
        const { userName } = req.query;
        const { userEmail } = req.query;
        if(userName){
            const getUser = await obtenerUsuario(userName);
            res.json(getUser);
        } else if (userEmail) {
            const getEmail = await obtenerCorreo(userEmail);
            res.json(getEmail);
        } else {
            res.json(false);
        };
    } catch (error) {
        console.log(`[error]: ${error}`);
        res.json({ status: false, message: 'Ha ocurrido un error.' });
    };
});

const port = 8080;
app.listen(port);
console.log(`[info]: Servicio URL http://127.0.0.1:${port}`);
