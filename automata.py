import tkinter as tk
import numpy as np
import copy

class AutomataCelular:
    def __init__(self, root, filas, columnas):
        self.root = root
        self.filas = filas
        self.columnas = columnas
        self.celulas = np.zeros((filas, columnas), dtype=int)
        self.canvas = tk.Canvas(root, width=columnas * 20, height=filas * 20, borderwidth=0, highlightthickness=0)
        self.canvas.pack()
        self.iniciar_interfaz()

    def iniciar_interfaz(self):
        # Inicialización de la matriz con valores aleatorios
        self.celulas = np.random.choice([0, 1], size=(self.filas, self.columnas), p=[0.5, 0.5])

        # Primera generación
        self.actualizar_tablero()

        # Botón para cambiar de generación
        btn_siguiente = tk.Button(self.root, text="Siguiente Generación", command=self.siguiente_generacion)
        btn_siguiente.pack()

    def actualizar_tablero(self):
        self.canvas.delete("all")

        for i in range(self.filas):
            for j in range(self.columnas):
                color = "black" if self.celulas[i][j] == 1 else "white"
                self.canvas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill=color)

    def siguiente_generacion(self):
        nueva_generacion = copy.deepcopy(self.celulas)
 
        for i in range(self.filas):
            for j in range(self.columnas):
                izquierda = self.celulas[i][(j - 1) % self.columnas]
                actual = self.celulas[i][j]
                derecha = self.celulas[i][(j + 1) % self.columnas]

                # Aplicar la regla de selección
                if izquierda == 0 and actual == 0 and derecha == 0:
                    nueva_generacion[i][j] = 0
                elif izquierda == 0 and actual == 0 and derecha == 1:
                    nueva_generacion[i][j] = 1
                elif izquierda == 0 and actual == 1 and derecha == 0:
                    nueva_generacion[i][j] = 1
                elif izquierda == 0 and actual == 1 and derecha == 1:
                    nueva_generacion[i][j] = 1
                elif izquierda == 1 and actual == 0 and derecha == 0:
                    nueva_generacion[i][j] = 1
                elif izquierda == 1 and actual == 0 and derecha == 1:
                    nueva_generacion[i][j] = 0
                elif izquierda == 1 and actual == 1 and derecha == 0:
                    nueva_generacion[i][j] = 0
                elif izquierda == 1 and actual == 1 and derecha == 1:
                    nueva_generacion[i][j] = 0

        self.celulas = copy.deepcopy(nueva_generacion)
        self.actualizar_tablero()

# Cración de la Ventana principal
root = tk.Tk()
root.title("Automata Celular Simple")

# Creación de Automata celular
automata = AutomataCelular(root, filas=4, columnas=8)

root.mainloop()
