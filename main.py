import json
from datetime import date

class Estudo:
    def __init__(self, save_dict):
        self.turno = self.define_turno(save_dict)
        self.ciclo = self.define_ciclo(save_dict)
        self.dia = date.today().day

    def define_turno(self, save_dict):
        turno = max(save_dict["historico"])
        return int(turno) + 1

    def define_ciclo(self, save_dict):
        ciclo = save_dict["ciclos"]
        ind = (self.turno if self.turno <= len(ciclo) else self.turno % len(ciclo)) - 1
        return ciclo[ind]

    def __repr__(self):
        return f"O turno é: {self.turno}\nO ciclo é:\n{self.ciclo}"

# Retorna um objeto Python do arquivo Json de dados
def le_arquivo():
    with open("datasave.json", "r") as file:
        read = json.load(file)
        file.close()
    return read

# Recebe um objeto Python e escreve seu conteúdo no arquivo Json de dados
def escreve_arquivo(dict_json):
    with open("datasave.json", "w") as file:
        json.dump(dict_json, file)
        file.close()

# Recebe o objeto Estudo, a lista de conteúdos estudados, e um objeto Python Json
# Retorna um ubjeto Python Json com o turno de estudos formatado e adicionado
def adiciona_conteudo(obj_estudo, list_cont, dict_json):
    ciclo = obj_estudo.ciclo
    if len(ciclo) != len(list_cont):
        raise ValueError("A lista de conteúdos não condiz com as matérias do dia")

    conteudo = {}
    for ind in range(len(ciclo)):
        conteudo[ciclo[ind]] = list_cont[ind]

    turno_str = "{:03d}".format(obj_estudo.turno)
    dict_json["historico"][turno_str] = conteudo
    return dict_json

def funcao_teste():
    # Inicialização
    save_dict = le_arquivo()
    estudo_atual = Estudo(save_dict)

    # Amostragem (site com Flask/HTML)
    print(estudo_atual)

    # Inserção de dados do usuário (Inputs de Texto)
    lista_conteudo = ["Geometria Analítica", "Revolução Francesa", "Oriente Médio"]

    # Salvamento de turno diário (Botão Salvar)
    json_novo = adiciona_conteudo(estudo_atual, lista_conteudo, save_dict)
    escreve_arquivo(json_novo)

    # Reinicialização e amostragem para DEBUG
    save_dict_novo = le_arquivo()
    estudo_novo = Estudo(save_dict_novo)
    print(estudo_novo)

def main():
    save_dict = le_arquivo()
    estudo_atual = Estudo(save_dict)

if __name__ == '__main__':
    main()