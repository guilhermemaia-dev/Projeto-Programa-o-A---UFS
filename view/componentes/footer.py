from tkinter import * 

class Footer(Frame):
    def __init__(self, master, controller=None):
        super().__init__(master, bg="#11111B", highlightbackground="#313244", highlightthickness=1)
        self.controller = controller



        self.label_posicao = Label(self, text="X: 0, Y: 0", bg="#11111B", fg="#CDD6F4", font=("Segoe UI", 9, "bold"))
        self.label_posicao.pack(side=LEFT, padx=12, pady=3)


        self.label_separador = Label(self, text="|", bg="#11111B", fg="#45475A", font=("Segoe UI", 9))
        self.label_separador.pack(side=LEFT, padx=0, pady=3)


        self.label_nome = Label(self, text="PAINT 1.0", bg="#11111B", fg="#89B4FA", font=("Segoe UI", 9, "bold"))
        self.label_nome.pack(side=RIGHT, padx=12, pady=3)



    def atualizar_coordenadas(self, x, y):
        if x is None or y is None:
            self.label_posicao.config(text="X: --, Y: --")
        else:
            self.label_posicao.config(text=f"X: {x}, Y: {y}")