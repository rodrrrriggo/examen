const preguntas = document.querySelectorAll(".encabezado");

preguntas.forEach(pregunta => {
    pregunta.addEventListener("click", () => {
        removerClaseActivo()
        pregunta.nextElementSibling.classList.add("activo")
    })
});

function removerClaseActivo() {
    preguntas.forEach((pregunta) => {
        pregunta.nextElementSibling.classList.remove("activo")
    });
}