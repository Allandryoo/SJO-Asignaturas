import tkinter as tk
from tkinter import messagebox

TAM = 60
BLANCO = "white"
NEGRO = "black"


class Pieza:
    def __init__(self, tipo, color):
        self.tipo = tipo
        self.color = color


class Ajedrez:
    def __init__(self, root):
        self.root = root
        self.root.title("Ajedrez - 2 Jugadores")

        self.turno = BLANCO
        self.seleccion = None
        self.movimientos_posibles = []
        self.tablero = [[None for _ in range(8)] for _ in range(8)]

        self.canvas = tk.Canvas(root, width=640, height=640)
        self.canvas.pack()

        self.inicializar_tablero()
        self.dibujar_tablero()

        self.canvas.bind("<Button-1>", self.click)

    def inicializar_tablero(self):
        orden = ["torre", "caballo", "alfil", "reina", "rey", "alfil", "caballo", "torre"]
        for i in range(8):
            self.tablero[0][i] = Pieza(orden[i], NEGRO)
            self.tablero[1][i] = Pieza("peon", NEGRO)
            self.tablero[6][i] = Pieza("peon", BLANCO)
            self.tablero[7][i] = Pieza(orden[i], BLANCO)

    def simbolo(self, pieza):
        simbolos = {
            ("rey", BLANCO): "♔", ("reina", BLANCO): "♕",
            ("torre", BLANCO): "♖", ("alfil", BLANCO): "♗",
            ("caballo", BLANCO): "♘", ("peon", BLANCO): "♙",
            ("rey", NEGRO): "♚", ("reina", NEGRO): "♛",
            ("torre", NEGRO): "♜", ("alfil", NEGRO): "♝",
            ("caballo", NEGRO): "♞", ("peon", NEGRO): "♟",
        }
        return simbolos[(pieza.tipo, pieza.color)]

    def dibujar_tablero(self):
        self.canvas.delete("all")

        for f in range(8):
            for c in range(8):
                color = "#EEEED2" if (f + c) % 2 == 0 else "#769656"
                self.canvas.create_rectangle(
                    c * TAM, f * TAM, (c + 1) * TAM, (f + 1) * TAM, fill=color
                )

        for (f, c) in self.movimientos_posibles:
            self.canvas.create_rectangle(
                c * TAM, f * TAM, (c + 1) * TAM, (f + 1) * TAM,
                outline="blue", width=4
            )

        for f in range(8):
            for c in range(8):
                pieza = self.tablero[f][c]
                if pieza:
                    self.canvas.create_text(
                        c * TAM + TAM // 2,
                        f * TAM + TAM // 2,
                        text=self.simbolo(pieza),
                        font=("Arial", 32)
                    )

    def click(self, event):
        f, c = event.y // TAM, event.x // TAM

        if self.seleccion:
            if (f, c) in self.movimientos_posibles:
                self.mover(*self.seleccion, f, c)
                self.turno = NEGRO if self.turno == BLANCO else BLANCO
            self.seleccion = None
            self.movimientos_posibles = []
        else:
            pieza = self.tablero[f][c]
            if pieza and pieza.color == self.turno:
                self.seleccion = (f, c)
                self.movimientos_posibles = self.obtener_movimientos_validos(f, c)

        self.dibujar_tablero()

    def mover(self, f0, c0, f1, c1):
        pieza = self.tablero[f0][c0]
        destino = self.tablero[f1][c1]

        if destino and destino.tipo == "rey":
            messagebox.showinfo(
                "Fin del juego",
                f"¡Has ganado!\nPiezas {pieza.color.upper()}"
            )
            self.root.quit()

        self.tablero[f1][c1] = pieza
        self.tablero[f0][c0] = None

        if pieza.tipo == "peon" and (f1 == 0 or f1 == 7):
            self.promocionar_peon(f1, c1, pieza.color)

    def promocionar_peon(self, f, c, color):
        opciones = ["reina", "torre", "alfil", "caballo"]
        ventana = tk.Toplevel(self.root)
        ventana.title("Promoción de peón")

        def elegir(tipo):
            self.tablero[f][c] = Pieza(tipo, color)
            ventana.destroy()
            self.dibujar_tablero()

        for o in opciones:
            tk.Button(
                ventana,
                text=o.capitalize(),
                width=10,
                command=lambda t=o: elegir(t)
            ).pack(padx=10, pady=5)

    def obtener_movimientos_validos(self, f, c):
        return [(f1, c1) for f1 in range(8) for c1 in range(8)
                if self.movimiento_valido(f, c, f1, c1)]

    def movimiento_valido(self, f0, c0, f1, c1):
        pieza = self.tablero[f0][c0]
        destino = self.tablero[f1][c1]

        if destino and destino.color == pieza.color:
            return False

        df, dc = f1 - f0, c1 - c0

        if pieza.tipo == "peon":
            d = -1 if pieza.color == BLANCO else 1
            fila_inicio = 6 if pieza.color == BLANCO else 1

            # Movimiento simple
            if dc == 0 and df == d and destino is None:
                return True

            # Movimiento doble (NUEVO)
            if (f0 == fila_inicio and dc == 0 and df == 2 * d and
                    destino is None and self.tablero[f0 + d][c0] is None):
                return True

            # Captura
            if abs(dc) == 1 and df == d and destino:
                return True

        if pieza.tipo == "torre":
            return (df == 0 or dc == 0) and self.camino_libre(f0, c0, f1, c1)

        if pieza.tipo == "alfil":
            return abs(df) == abs(dc) and self.camino_libre(f0, c0, f1, c1)

        if pieza.tipo == "reina":
            return (df == 0 or dc == 0 or abs(df) == abs(dc)) and self.camino_libre(f0, c0, f1, c1)

        if pieza.tipo == "caballo":
            return (abs(df), abs(dc)) in [(1, 2), (2, 1)]

        if pieza.tipo == "rey":
            return max(abs(df), abs(dc)) == 1

        return False

    def camino_libre(self, f0, c0, f1, c1):
        df = f1 - f0
        dc = c1 - c0
        pasos = max(abs(df), abs(dc))
        df //= pasos if pasos else 1
        dc //= pasos if pasos else 1

        for i in range(1, pasos):
            if self.tablero[f0 + df * i][c0 + dc * i]:
                return False
        return True


if __name__ == "__main__":
    root = tk.Tk()
    Ajedrez(root)
    root.mainloop()
