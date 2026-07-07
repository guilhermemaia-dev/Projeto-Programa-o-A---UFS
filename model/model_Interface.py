class ModelInterface:
    def __init__(self):
        self.lista_cores = ["#00a8ff", "#c01414", "#10eb09", "#000000", "#ffffff", "#d9ff00", "#a200ff", "#ff5e00", "#858585", "#E7E7E7"]
        self.cor_selecionada_borda = "#000000"
        self.cor_selecionada_preenchimento = ''
        self.ferramenta_atual = "Mao_Livre"
        self.figuras = []
        #self.ferramentas_traduzidas = {"Mao_Livre": Mao_Livre, "Reta": Reta, "Retangulo": Retangulo, "Oval": Oval, "Circulo": Circulo}