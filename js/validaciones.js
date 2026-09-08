// 1ra parte
// EJERCICIO 1: Validar Fecha de nacimiento

function validarFechaNacimiento() {
    // Buscamos TODOS los inputs que tengan la clase "input-fecha"
    const inputsFecha = document.querySelectorAll(".input-fecha");

    // Recorremos cada uno con un bucle clásico
    for (let i = 0; i < inputsFecha.length; i++) {
        let valorFecha = inputsFecha[i].value;

        if (valorFecha === "") {
            alert(`Participante ${i + 1}: Debe seleccionar una fecha de nacimiento`);
            inputsFecha[i].focus();
            return false;
        }

        let fechaNacimiento = new Date(valorFecha + "T00:00:00");
        let fechaActual = new Date();
        fechaActual.setHours(0, 0, 0, 0);

        if (fechaNacimiento > fechaActual) {
            alert(`Participante ${i + 1}: La fecha de nacimiento no puede ser posterior a la fecha actual`);
            inputsFecha[i].focus();
            return false;
        }
    }
    return true; // Si todas las fechas pasaron, devuelve true
}

// EJERCICIO 2: Validar DNI
function validarDNI() {
    // Buscamos TODOS los inputs que tengan la clase "input-dni"
    const inputsDni = document.querySelectorAll(".input-dni");

    for (let i = 0; i < inputsDni.length; i++) {
        let valorDni = inputsDni[i].value.trim();

        if (valorDni === "") {
            alert(`Participante ${i + 1}: Debe ingresar un DNI`);
            inputsDni[i].focus();
            return false;
        }

        if (valorDni.length !== 8 || isNaN(valorDni)) {
            alert(`Participante ${i + 1}: El DNI debe contener exactamente 8 dígitos`);
            inputsDni[i].focus();
            return false;
        }
    }
    return true; // Si todos los DNI pasaron, devuelve true
}
// EJERCICIO 3.1: Función constructora

function Actividad (nombre, lugar, dia, horario, cupo, estado){
    this.nombre = nombre;
    this.lugar=lugar;
    this.dia=dia;
    this.horario=horario;
    this.cupo=cupo;
    this.estado=estado; // "disponible" o "completo"
}

// EJERCICIO 3.2: Clase SistemaDeportes
class SistemaDeportes{
    constructor(){
        this.actividades=[];
    }

    //agrega uno o más elementos al final de un array
    agregarActividad(actividad){
        this.actividades.push(actividad);
    }

    //dar acceso a la lista completa de actividade
    listarActividades() {
        return this.actividades;
    }
}

// EJERCICIO 3.3: instanciar clase

// 1. Instanciamos el sistema general
const sistema = new SistemaDeportes();

// 2. Creamos los 4 objetos individuales con la función constructora
const actFutbol = new Actividad ("Futbol", "Cancha de la UNCA", "Lunes y Viernes", "18:00-20:00", 20, "disponible");
const actBasquet = new Actividad ("Básquet", "Gimnasio cubierto de la UNCA", "Martes y jueves", "17:00-19:00", 15, "disponible");
const actVoley = new Actividad ("Vóley", "Gimnasio cubierto de la UNCA", "Lunes y Viernes", "16:00-18:00", 10, "completo");
const actAtletismo = new Actividad ("Atletismo", "Gimnasio cubierto de la UNCA", "Lunes y Viernes", "18:00-20:00", 25, "disponible");

sistema.agregarActividad(actFutbol);
sistema.agregarActividad(actBasquet);
sistema.agregarActividad(actVoley);
sistema.agregarActividad(actAtletismo);
console.log(sistema.listarActividades());

// 2da parte
// EJERCICIO 4:

function cargarTablaActividades() {

    // Obtener la referencia al cuerpo de la tabla
    const cuerpoTabla = document.getElementById("cuerpoTabla");

    if (!cuerpoTabla) {
        return;
    }

    // Limpiamos el contenido previo
    cuerpoTabla.innerHTML = "";

    //Obtenemos el array de actividades para obtener los datos necesarios
    const actividades = sistema.listarActividades();

    //Recorremos cada actividad cargada en el array
    actividades.forEach(function (actividad){

        //Fabricamos esqueleto de la tabla
        const fila = document.createElement("tr");

        //
        const celdaNombre = document.createElement("td");
        celdaNombre.textContent = actividad.nombre;
        fila.appendChild(celdaNombre);

        const celdaLugar = document.createElement("td");
        celdaLugar.textContent = actividad.lugar;
        fila.appendChild(celdaLugar);

        const celdaDia = document.createElement("td");
        celdaDia.textContent = actividad.dia;
        fila.appendChild(celdaDia);

        const celdaHorario = document.createElement("td");
        celdaHorario.textContent= actividad.horario;
        fila.appendChild(celdaHorario);

        const celdaCupos = document.createElement("td");
        celdaCupos.textContent= actividad.cupo;
        fila.appendChild(celdaCupos);

        const celdaEstado = document.createElement("td");
        celdaEstado.textContent = actividad.estado;
        // Aplicamos estilos según el valor del estado
        if (actividad.estado === "disponible") {
            celdaEstado.className = "text-success fw-bold text-capitalize";
        } else if (actividad.estado === "completo") {
            celdaEstado.className = "text-danger fw-bold text-capitalize";
        }
        fila.appendChild(celdaEstado);

        cuerpoTabla.appendChild(fila);
    });
}

// EJERCICIO 5:

function generarBloquesParticipantes() {
    const inputCantidad = document.getElementById("cantidadParticipantes");
    const contenedor = document.getElementById("contenedorParticipantes");

    if (!inputCantidad || !contenedor) {
        return;
    }

    const cantidad = parseInt(inputCantidad.value, 10);

    // Validación del rango exigido (1 a 10)
    if (isNaN(cantidad) || cantidad < 1 || cantidad > 10) {
        alert("Por favor, ingrese una cantidad de participantes entre 1 y 10.");
        return;
    }

    // Limpiamos los bloques previos si los hubiera
    contenedor.innerHTML = "";

    // Bucle para crear el bloque de cada participante
    for (let i = 1; i <= cantidad; i++) {
        // 1. Creamos una tarjeta contenedora
        const card = document.createElement("div");
        card.className = "card mb-4 shadow-sm bg-white border";

        // 2. Encabezado del bloque (Participante 1, Participante 2, etc.)
        const cardHeader = document.createElement("div");
        cardHeader.className = "card-header card-header-unca";
        cardHeader.textContent = `Participante ${i}`;

        // 3. Cuerpo de la tarjeta
        const cardBody = document.createElement("div");
        cardBody.className = "card-body";

        // 4. Inyectamos la estructura de los campos requeridos
        cardBody.innerHTML = `
            <div class="mb-3">
                <label for="nombre_${i}" class="form-label fw-bold">Apellido y Nombre:</label>
                <input type="text" id="nombre_${i}" name="nombre_${i}" class="form-control" required>
            </div>
            <div class="mb-3">
                <label for="dni_${i}" class="form-label fw-bold">DNI:</label>
                <input type="text" id="dni_${i}" name="dni_${i}" class="form-control input-dni" required>
            </div>
            <div class="mb-3">
                <label for="fecha_${i}" class="form-label fw-bold">Fecha de Nacimiento:</label>
                <input type="date" id="fecha_${i}" name="fecha_${i}" class="form-control input-fecha" required>
            </div>
            <div class="mb-3">
                <label class="form-label fw-bold d-block">Sexo:</label>
                <div class="form-check form-check-inline">
                    <input class="form-check-input" type="radio" name="sexo_${i}" id="sexo_m_${i}" value="Masculino" required>
                    <label class="form-check-label" for="sexo_m_${i}">Masculino</label>
                </div>
                <div class="form-check form-check-inline">
                    <input class="form-check-input" type="radio" name="sexo_${i}" id="sexo_f_${i}" value="Femenino">
                    <label class="form-check-label" for="sexo_f_${i}">Femenino</label>
                </div>
                <div class="form-check form-check-inline">
                    <input class="form-check-input" type="radio" name="sexo_${i}" id="sexo_nb_${i}" value="No binario">
                    <label class="form-check-label" for="sexo_nb_${i}">No binario</label>
                </div>
            </div>
            <div class="mb-3">
                <label for="nivel_${i}" class="form-label fw-bold">Nivel:</label>
                <select id="nivel_${i}" name="nivel_${i}" class="form-select">
                    <option value="inicial">Inicial</option>
                    <option value="intermedio">Intermedio</option>
                    <option value="avanzado">Avanzado</option>
                </select>
            </div>
        `;

        // Ensamblamos la tarjeta
        card.appendChild(cardHeader);
        card.appendChild(cardBody);

        // Agregamos la tarjeta terminada al contenedor general en el DOM
        contenedor.appendChild(card);
    }
}


//agregar un escuchador de eventos --> Aclaro que se ejecute luego de cargar toda la pag y armar el DOM
document.addEventListener("DOMContentLoaded", function () {

    //Parte 1
    //Buscamos el formulario dentro del DOM
    let formulario = document.querySelector("form");

    if (formulario) {

        // Dejamos escuchando el momento en que se intente enviar el formulario
        // El navegador nos pasa el objeto "event" como parámetro
        formulario.addEventListener("submit", function (event) {

            //Ejercicio 1
            let dniValido = validarDNI();
            if(!dniValido){
               event.preventDefault();
               return;
            }

            //Ejercicio 2
            let fechaValida = validarFechaNacimiento();
            //Le prohíbe al formulario enviarse, manteniéndote en la misma pantalla para que el usuario pueda corregir el campo.
            if (!fechaValida) {
                event.preventDefault();
            }

        });

        const btnGenerar = document.getElementById("btnGenerar");
        if (btnGenerar) {
            btnGenerar.addEventListener("click", generarBloquesParticipantes);

            generarBloquesParticipantes();
        }
    }

    //Parte 2
    cargarTablaActividades();

});
