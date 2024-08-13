document.addEventListener("DOMContentLoaded", function() {

    // VALIDACION DE LOS CAMPOS NOMBRE Y CONTRASEÑA


    const form = document.querySelector("form");
    const nombre = document.getElementById("nombre");
    const password = document.getElementById("password");

    form.addEventListener("submit", function(event) {
        
        if (nombre.value.trim() === "") {

            alert("El nombre de usuario no puede estar vacío.");
            event.preventDefault();
            return;
        }

        if (password.value.trim() === "") {
            alert("La contraseña no puede estar vacía.");
            event.preventDefault();
            return;
            // ENVIO DE ALERTAS EN CASO DE DEJARLOS EN BLANCO
        }
 
        // ESPACIO PARA COLOCAR MAS VALIDACIONES
    });
});
