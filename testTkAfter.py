import tkinter as tk
import random

class LogWindow():

    def update_log(self):
        text_random = random.randint(1, 100)
        self.label1.config(text=f"Número aleatorio: {text_random}")
        self.master.after(2000,self.update_log)

    def __init__(self):
        self.master = tk.Tk()
        self.master.title('test')
        self.master.config(width=400, height=300)

        self.label1 = tk.Label(text="¡Hola mundo!")
        self.label1.place(x=100, y=70)
        self.run()

    def run(self):
        self.master.after(2000,self.update_log)
        self.master.mainloop()


# def actualizar_etiqueta():
#     numero_aleatorio = random.randint(1, 100)
#     etiqueta1.config(text=f"Número aleatorio: {numero_aleatorio}")
#     ventana.after(1000, actualizar_etiqueta)

# ventana = tk.Tk()
# ventana.title("Ejemplo after() en Tk")
# ventana.config(width=400, height=300)
# etiqueta1 = tk.Label(text="¡Hola mundo!")
# etiqueta1.place(x=100, y=70)
# ventana.after(1000, actualizar_etiqueta)
# ventana.mainloop()

l = LogWindow()