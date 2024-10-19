import keyboard
import os

# Variable para almacenar las teclas presionadas
buffer = ""

# Función que crea un archivo txt con el mensaje
def crear_txt():
    with open("texto.txt", "w") as file:
        file.write("Hola, cómo estás chico")
    print("Archivo creado: texto.txt")

# Función que se llama cada vez que se presiona una tecla
def detectar_teclas(event):
    global buffer
    # Agregar la tecla presionada al buffer
    buffer += event.name
    
    # Comprobar si el buffer contiene la palabra "call"
    if "call" in buffer:
        crear_txt()
        # Vaciar el buffer después de crear el archivo
        buffer = ""

# Escuchar eventos de teclado
keyboard.on_press(detectar_teclas)

# Mantener el script corriendo indefinidamente
keyboard.wait()
