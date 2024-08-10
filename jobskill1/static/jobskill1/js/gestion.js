document.addEventListener("DOMContentLoaded", function() {

    // VALIDACIÓN DE LOS CAMPOS NOMBRE Y CONTRASEÑA

    const form = document.querySelector("form");
    const nombre = document.getElementById("nombre");
    const direccion = document.getElementById("direccion");
    const telefono = document.getElementById("telefono");
    const email = document.getElementById("email");
    const apellido = document.getElementById("apellido");
    const genero = document.getElementById("genero");
    const password1 = document.getElementById("password1");
    const password2 = document.getElementById("password2");

    form.addEventListener("submit", function(event) {
        // Array para almacenar los errores
        let errors = [];

        if (nombre.value.trim() === "") {
            errors.push("El nombre de usuario no puede estar vacío.");
        }

        if (apellido.value.trim() === "") {
            errors.push("El campo apellido está vacío.");
        }

        if (direccion.value.trim() === "") {
            errors.push("El campo dirección está vacío.");
        }

        if (telefono.value.trim() === "") {
            errors.push("El campo teléfono está vacío.");
        }

        if (email.value.trim() === "") {
            errors.push("El campo email está vacío.");
        }

        if (genero.value.trim() === "") {
            errors.push("El campo género está vacío.");
        }

        if (password1.value.trim() === "") {
            errors.push("El campo contraseña está vacío.");
        }

        if (password1.value.trim() !== password2.value.trim()) {
            errors.push("Las contraseñas no coinciden.");
        }

        // Mostrar alertas si hay errores
        if (errors.length > 0) {
            alert(errors.join("\n"));
            event.preventDefault();
            return;
        }

        // Si no hay errores, mostrar mensaje de éxito
        alert("Los datos se guardaron correctamente.");
    });
});
