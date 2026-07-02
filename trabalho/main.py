import tkinter as tk
from abc import ABC, abstractmethod

# --- 1. Estrutura de Classes das Figuras ---

class Figura(ABC):
    def __init__(self, x1, y1, x2, y2, cor="black"):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.cor = cor

    @abstractmethod
    def desenhar(self, canvas):
        pass

class Reta(Figura):
    def desenhar(self, canvas):
        # Retorna o ID do objeto criado para podermos manipulá-lo se necessário
        return canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.cor, width=2)

class Retangulo(Figura):
    def desenhar(self, canvas):
        return canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline=self.cor, width=2)

# --- 2. Classe Principal do Aplicativo (Gerencia o Mouse) ---

class AppDesenho:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint POO - Reta e Retângulo")
        
        # Configuração da Interface
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack(expand=True, fill="both")
        
        # Barra de ferramentas simples
        self.frame_tools = tk.Frame(root)
        self.frame_tools.pack(fill="x")
        
        self.tipo_figura = tk.StringVar(value="Reta")
        tk.Radiobutton(self.frame_tools, text="Reta", variable=self.tipo_figura, value="Reta").pack(side="left")
        tk.Radiobutton(self.frame_tools, text="Retângulo", variable=self.tipo_figura, value="Retangulo").pack(side="left")
        
        # Variáveis de estado do mouse
        self.x_inicial = 0
        self.y_inicial = 0
        self.id_rascunho = None  # Guarda o ID da figura que está sendo "esticada"

        # Bindings (Eventos do Mouse)
        self.canvas.bind("<Button-1>", self.ao_clicar)
        self.canvas.bind("<B1-Motion>", self.ao_arrastar)
        self.canvas.bind("<ButtonRelease-1>", self.ao_soltar)

    def ao_clicar(self, event):
        # Salva a posição onde o usuário clicou
        self.x_inicial = event.x
        self.y_inicial = event.y

    def ao_arrastar(self, event):
        # 1. Se já houver um rascunho sendo desenhado, apaga ele
        if self.id_rascunho:
            self.canvas.delete(self.id_rascunho)

        # 2. Cria uma nova instância da classe selecionada
        if self.tipo_figura.get() == "Reta":
            figura = Reta(self.x_inicial, self.y_inicial, event.x, event.y, "blue")
        else:
            figura = Retangulo(self.x_inicial, self.y_inicial, event.x, event.y, "red")

        # 3. Desenha e guarda o ID para apagar no próximo movimento (efeito de arrasto)
        self.id_rascunho = figura.desenhar(self.canvas)

    def ao_soltar(self, event):
        # Quando solta o botão, o rascunho vira a figura definitiva
        self.id_rascunho = None 

# --- 3. Execução ---

if __name__ == "__main__":
    root = tk.Tk()
    app = AppDesenho(root)
    root.mainloop()