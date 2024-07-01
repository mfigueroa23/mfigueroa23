// Datos
const nombre = document.getElementById("name");
const email = document.getElementById("email");
const passwd = document.getElementById("passwd");
const confirmPasswd = document.getElementById("confirmPasswd");

// Mensajes
const nameStatus = document.getElementById("nameStatus");
const emailStatus = document.getElementById("emailStatus");
const passwdStatus = document.getElementById("passwdStatus");
const confirmPasswdStatus = document.getElementById("confirmPasswdStatus");

// Boton
const btn = document.getElementById("btn");

// Funciones
function verifyName(min) {
    if(nombre.value.length >= min && nombre.value.match(/^[a-zA-Z0-9\s]+$/)){
        fetch(`/api/users?userName=${nombre.value}`)
        .then(res => res.json())
        .then(data => {
            if(data.length >= 1){
                nameStatus.textContent = 'El nombre ya esta siendo usado';
                nombre.style.border = "4px solid red"
                btn.disabled = true;
            } else {
                nameStatus.textContent = 'El nombre esta disponible';
                nombre.style.border = "4px solid green"
                btn.disabled = false;
            };
        });
    } else {
        nameStatus.textContent = 'El nombre es invalido';
        nombre.style.border = "4px solid red"
        btn.disabled = true;
    };
};

function verifyEmail(){
    if(email.value.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)){
        fetch(`/api/users?userEmail=${email.value}`)
        .then(res => res.json())
        .then(data => {
            if(data.length >= 1){
                emailStatus.textContent = 'El correo esta siendo ocupado';
                email.style.border = "4px solid red";
                btn.disabled = true;
            } else {
                emailStatus.textContent = 'El correo es valido';
                email.style.border = "4px solid green";
                btn.disabled = false;
            };
        });
    } else {
        emailStatus.textContent = 'El correo es requerido';
        email.style.border = "4px solid red";
        btn.disabled = true;
    };
};

function verifyPasswd(){
    if(passwd.value.match(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#.,-_])[A-Za-z\d@$!%*?&#.,-_]{8,}$/)){
        passwdStatus.textContent = 'La contraseña es segura';
        passwd.style.border = "4px solid green";
        btn.disabled = false;
    } else {
        passwdStatus.textContent = 'La contraseña no cumple con estadares de seguridad';
        passwd.style.border = "4px solid red";
        btn.disabled = true;
    };
};

function verifyConfirmPasswd(){
    if(confirmPasswd.value.match(passwd.value) && confirmPasswd.value != ''){
        confirmPasswdStatus.textContent = 'La constraseña coindice';
        confirmPasswd.style.border = '4px solid green';
        btn.disabled = false;
    } else {
        confirmPasswdStatus.textContent = 'La constraseña no coindice';
        confirmPasswd.style.border = '4px solid red';
        btn.disabled = true;
    };
};

function sendConfirmationForm(){
    alert("¡Gracias por suscribirte! Tu usuario se ha creado correctamente");
};
