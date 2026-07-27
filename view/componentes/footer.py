from tkinter import * 

class Footer(Frame):
    def __init__(self, master, controller=None):
        super().__init__(master, bg="#d9d9d9")
        self.controller = controller

        self.label_nome = Label(self, text="PAINT 1.0", bg="#d9d9d9")
        self.label_nome.pack(side=LEFT, padx=10, pady=2)

        self.label_posicao = Label(self, text="X: 0, Y: 0", bg="#d9d9d9")
        self.label_posicao.pack(side=RIGHT, padx=10, pady=2)

    def atualizar_coordenadas(self, x, y):
        if x is None or y is None:
            self.label_posicao.config(text="X: --, Y: --")
        else:
            self.label_posicao.config(text=f"X: {x}, Y: {y}")