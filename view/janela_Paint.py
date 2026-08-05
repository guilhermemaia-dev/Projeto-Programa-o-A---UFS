from tkinter import *
from tkinter import filedialog
from view.componentes.header import Header
from view.componentes.footer import Footer
from view.componentes.canvas_desenho import CanvasDesenho

class JanelaPaint:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("PAINT 1.0")
        self.janela.geometry("1280x720")
        self.janela.minsize(1000,600)
        self.janela.state("zoomed")
        self.controller = None


    def iniciar(self, controller):
        self.controller = controller

        self.criar_binds()

        menu = Menu(self.janela)
        self.janela.config(menu=menu)
        menu_arquivo = Menu(menu, tearoff= 0)
        menu.add_cascade(label="Arquivo",menu=menu_arquivo)
        menu_arquivo.add_command(label="Salvar",command=self.controller.salvar_desenho)
        menu_arquivo.add_command(label="Abrir",command=self.controller.abrir_desenho)

        self.header = Header(self.janela, self.controller)
        self.header.pack(side=TOP, fill=X)

        self.footer = Footer(self.janela, self.controller)
        self.footer.pack(side=BOTTOM, fill=X)

        self.canvas_desenho = CanvasDesenho(self.janela, self.controller)
        self.canvas_desenho.pack(side=TOP, fill=BOTH, expand=True)

    def criar_binds(self):
        self.janela.bind("<Control-c>", self.controller.control_c)
        self.janela.bind("<Control-v>", self.controller.control_v)
        self.janela.bind("<Control-z>", self.controller.ctrl_z)
        self.janela.bind("<Control-y>", self.controller.ctrl_y)
        self.janela.bind("<Up>", self.controller.camada_frontal)
        self.janela.bind("<Down>", self.controller.camada_traseira)
        self.janela.bind("<Left>", self.controller.mover_uma_atras)
        self.janela.bind("<Right>", self.controller.mover_uma_frente)
        self.janela.bind("<Delete>", self.controller.remover)

        
    def desenhar_figuras(self, lista_figuras, figura_selecionada=None):
        self.canvas_desenho.desenhar_figuras(lista_figuras, figura_selecionada)

    def alterar_cor_preview(self, cor_borda, cor_preenchimento):
        self.header.alterar_cor_preview(cor_borda, cor_preenchimento)

    def alterar_ferramenta_preview(self, ferramenta_atual):
        self.header.alterar_ferramenta_preview(ferramenta_atual)

    def pedir_caminho_salvar(self):
        return filedialog.asksaveasfilename(
            title="Salvar Arquivo",
            defaultextension=".paint",
            filetypes=[("Arquivos Paint", "*.paint"), ("Todos os Arquivos", "*.*")])
    
    def pedir_caminho_abrir(self):
        return filedialog.askopenfilename(
            title="Abrir Arquivo",
            filetypes=[("Arquivos Paint", "*.paint"), ("Todos os Arquivos", "*.*")])

    def atualizar_label_posicao(self, x, y):
        self.footer.atualizar_coordenadas(x,y)


    def desenhar_mao_livre(self, figura, dash=None):
        self.canvas_desenho.desenhar_mao_livre(figura, dash=dash)

    def desenhar_reta(self, figura, dash=None):
        self.canvas_desenho.desenhar_reta(figura, dash=dash)

    def desenhar_retangulo(self, figura, dash=None):
        self.canvas_desenho.desenhar_retangulo(figura, dash=dash)

    def desenhar_oval(self, figura, dash=None):
        self.canvas_desenho.desenhar_oval(figura, dash=dash)

    def desenhar_circulo(self, figura, dash=None):
        self.canvas_desenho.desenhar_circulo(figura, dash=dash)

    def desenhar_quadrado(self, figura, dash=None):
        self.canvas_desenho.desenhar_quadrado(figura, dash=dash)

    def desenhar_pincel(self, figura, dash=None):
        self.canvas_desenho.desenhar_pincel(figura, dash=dash)