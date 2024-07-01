// index.js
const express = require('express');
const http = require('http');
const { Server } = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = new Server(server);

app.use(express.static('public'));

io.on('connection', (socket) => {
  socket.on('set username', (username) => {
    socket.username = username;
  });

  socket.on('join room', (room) => {
    socket.join(room);
    socket.room = room;
    io.to(room).emit('user connected', `${socket.username} se ha unido a ${room}`);
  });

  socket.on('chat message', (msg) => {
    if (socket.username && socket.room) {
      io.to(socket.room).emit('chat message', { user: socket.username, text: msg });
    }
  });

  socket.on('file upload', (file) => {
    if (socket.username && socket.room) {
      io.to(socket.room).emit('file upload', { user: socket.username, name: file.name, data: file.data });
    }
  });

  socket.on('disconnect', () => {
    if (socket.username && socket.room) {
      io.to(socket.room).emit('user disconnected', `${socket.username} se ha desconectado`);
    }
  });
});

const port = 80;
server.listen(port, () => {
  console.log(`server en: http://127.0.0.1:${port}`);
});
