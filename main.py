import turtle
import pandas as pd

# Configurar pantalla y mostrar imagen
screen = turtle.Screen()
screen.title("Mexico y sus estados")
image = r"C:\Users\sergi_zr88xxb\Desktop\Python_Portfolio\Project 20- Detector de coordenadas\Mexico_sin_nombres.gif"
screen.addshape(image)
turtle.shape(image)

# Desactivar animaciones para evitar movimientos visibles
screen.tracer(0)

# Lista para almacenar los estados y sus coordenadas
estados_coordenadas = []

# Función para capturar clics en el mapa
def get_mouse_click_coor(x, y):
    # Si el clic está dentro del botón, no pedir estado
    if -100 <= x <= 100 and -275 <= y <= -225:
        guardar_coordenadas()
        return
    
    estado = screen.textinput("Estado", "Ingresa el nombre del estado:")
    if estado:
        estados_coordenadas.append({"estado": estado, "x": x, "y": y})
        print(f"Guardado: {estado} - Coordenadas: ({x}, {y})")

# Guardar la información en un archivo CSV con Pandas
def guardar_coordenadas():
    if estados_coordenadas:  # Solo guarda si hay datos
        df = pd.DataFrame(estados_coordenadas)  # Convertir lista en DataFrame
        df.to_csv("estados_coordenadas.csv", index=False, encoding="utf-8")  # Guardar CSV
        print("Coordenadas guardadas en estados_coordenadas.csv")
    screen.bye()  # Cierra la ventana de Turtle

# Función para dibujar un botón con texto
def crear_boton(x, y, ancho, alto, texto):
    boton = turtle.Turtle()
    boton.penup()
    boton.hideturtle()
    boton.goto(x - ancho // 2, y - alto // 2)  # Mover a la esquina inferior izquierda
    boton.pendown()
    boton.fillcolor("lightgray")
    boton.begin_fill()
    for _ in range(2):  # Dibujar rectángulo
        boton.forward(ancho)
        boton.left(90)
        boton.forward(alto)
        boton.left(90)
    boton.end_fill()
    
    # Escribir texto encima del botón
    boton.penup()
    boton.goto(x, y - 10)  # Ajuste fino para centrar el texto
    boton.write(texto, align="center", font=("Arial", 10, "bold"))

# Crear botón en la parte inferior
crear_boton(0, -250, 100, 50, "Cerrar y Guardar")

# Reactivar animaciones antes de mostrar cambios en pantalla
screen.update()

# Usar un solo evento de clic para manejar mapa y botón
turtle.onscreenclick(get_mouse_click_coor)

# Vincular evento de teclado
screen.onkey(guardar_coordenadas, "s")  # Presiona 's' para guardar y salir
screen.listen()  # Asegura que detecte las teclas

turtle.mainloop()
