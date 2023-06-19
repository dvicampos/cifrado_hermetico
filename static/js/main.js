function adivinarPalabra(event) {
  enviado()
    event.preventDefault();  // Evita el envío del formulario normalmente

    var palabra = document.getElementById('palabra').value;
    var respuesta = document.getElementById('respuesta').value;

    // Realiza una solicitud AJAX utilizando fetch
    fetch('/adivinar', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ respuesta: respuesta, palabra: palabra }),
    })
      .then(function (response) {
        return response.json();  // Parsea la respuesta JSON
      })
      .then(function (data) {
        mostrarMensaje(data.mensaje);  // Llama a la función para mostrar el mensaje
      })
      .catch(function (error) {
        console.log('Error:', error);
      });
  }

  function mostrarMensaje(mensaje) {
    var mensajeContainer = document.getElementById('mensaje-container');
    mensajeContainer.innerHTML = '<div class="alert">' + mensaje + '</div>';
  }

  function enviado(){
    setTimeout(scrollToBottom, 100)
  }
  function scrollToBottom() {
    window.scrollTo({
      top: window.pageYOffset + 100,
      behavior: "smooth"
    });
  }

  
  