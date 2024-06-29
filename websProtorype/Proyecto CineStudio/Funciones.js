
function agregaDolar(Entrada) {
    // Obtener el valor ingresado por el usuario
    let valor = Entrada.value;
    valor = valor.replace(/[^\d]/g, '');
    valor = "$" + valor;
    Entrada.value = valor;
}
function agregaFecha(fecha) {
    // Obtener el valor ingresado por el usuario
    let dates = fecha.value;
    fecha.value = dates;
}
function agregaCategoria(categoria) {
    // Obtener el valor ingresado por el usuario
    let genero = categoria.value;
    categoria.value = genero;
}

