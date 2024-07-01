const socket = io();
const notificationSound = document.getElementById('notification-sound');
const messageInput = document.getElementById('message');
const fileInput = document.getElementById('fileInput');
const uploadFileButton = document.getElementById('uploadFile');
const emojiPicker = document.querySelector('emoji-picker');
const messagesList = document.getElementById('messages');
let messages = [];
let currentRoom = 'general';

document.getElementById('join').addEventListener('click', () => {
  const username = document.getElementById('username').value;
  const room = document.getElementById('room').value;

  if (username.trim()) {
    socket.emit('set username', username);
    socket.username = username;
    joinRoom(room);
    document.getElementById('login').style.display = 'none';
    document.getElementById('chat').style.display = 'flex';
  } else {
    alert('Please enter a username');
  }
});

document.getElementById('send').addEventListener('click', () => {
  const message = messageInput.value;

  if (message.trim()) {
    socket.emit('chat message', { room: currentRoom, message });
    messageInput.value = '';
  }
});

document.getElementById('leave').addEventListener('click', () => {
  const room = document.getElementById('room').value;
  socket.emit('join room', 'general');
  document.getElementById('login').style.display = 'flex';
  document.getElementById('chat').style.display = 'none';
  messages = [];
  renderMessages();
});

emojiPicker.addEventListener('emoji-click', event => {
  messageInput.value += event.detail.unicode;
});

uploadFileButton.addEventListener('click', () => {
  fileInput.click();
});

fileInput.addEventListener('change', () => {
  const file = fileInput.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = () => {
      socket.emit('file upload', { room: currentRoom, name: file.name, data: reader.result });
    };
    reader.readAsDataURL(file);
  }
});

socket.on('user connected', (message) => {
  messages.push({ system: true, message });
  renderMessages();
  notificationSound.play();
});

socket.on('user disconnected', (message) => {
  messages.push({ system: true, message });
  renderMessages();
  notificationSound.play();
});

socket.on('chat message', (msg) => {
  messages.push({ user: msg.user, text: msg.text });
  renderMessages();
  notificationSound.play();
});

socket.on('file upload', (file) => {
  messages.push({ user: file.user, file: file });
  renderMessages();
  notificationSound.play();
});

function joinRoom(room) {
  currentRoom = room;
  socket.emit('join room', room);
  messages = [];
  messagesList.innerHTML = '';
  socket.emit('load messages', room);
}

socket.on('load messages', (msgs) => {
  messages = msgs;
  renderMessages();
});

function renderMessages() {
  messagesList.innerHTML = '';
  messages.forEach(msg => {
    const item = document.createElement('li');
    if (msg.system) {
      item.textContent = msg.message;
    } else if (msg.file) {
      item.innerHTML = `<strong>${msg.user}:</strong> <a href="${msg.file.data}" download="${msg.file.name}">${msg.file.name}</a>`;
    } else {
      item.innerHTML = `<strong>${msg.user}:</strong> ${msg.text}`;
    }
    messagesList.appendChild(item);
  });
}


