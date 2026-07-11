import pickle

class Arquivo:
    def __init__(self, model):
        self.model = model

    def salvar_para_arquivo(self, caminho):
        with open(caminho, 'wb') as arquivo:
            #Salva a lista de figuras#
            pickle.dump(self.model.figuras, arquivo)

    def carregar_de_arquivo(self, caminho):
        with open(caminho, 'rb') as arquivo:
            #Substitui a lista atual pela lista carregada#
            self.model.figuras = pickle.load(arquivo)