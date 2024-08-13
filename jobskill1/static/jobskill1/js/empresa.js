document.addEventListener("DOMContentLoaded", function() {
    // VALIDACIÓN DE LOS CAMPOS NOMBRE Y CONTRASEÑA

    const form = document.querySelector("form");
    const nombre = document.getElementById("nombre");
    const direccion = document.getElementById("direccion");
    const telefono = document.getElementById("telefono");
    const email = document.getElementById("email");
    const password = document.getElementById("password");
    const Confirmar_password = document.getElementById("Confirmar_password");

    form.addEventListener("submit", function(event) {
        // Array para almacenar los errores
        let errors = [];

        if (nombre.value.trim() === "") {
            errors.push("El nombre de usuario no puede estar vacío.");
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

        if (password.value.trim() === "") {
            errors.push("El campo contraseña está vacío.");
        }

        if (password.value.trim() !== Confirmar_password.value.trim()) {
            errors.push("Las contraseñas no coinciden.");
        }

        //Alertas si hay errores
        if (errors.length > 0) {
            alert(errors.join("\n"));
            event.preventDefault();
            return;
        }

        // Éxito
        alert("Los datos se guardaron correctamente.");
    });
});
