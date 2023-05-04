from datetime import date

class Estudo:
    def __init__(self, save_dict):
        self.turno = self.define_turno(save_dict)
        self.ciclo = self.define_ciclo(save_dict)
        self.revisao = self.define_revisao(save_dict)
        self.dia = date.today().day

    def define_turno(self, save_dict):
        turno = max(save_dict["historico"])
        return int(turno) + 1

    def define_ciclo(self, save_dict):
        ciclo = save_dict["ciclos"]
        ind = (self.turno if self.turno <= len(ciclo) else self.turno % len(ciclo)) - 1
        return ciclo[ind]

    def define_revisao(self, save_dict):
        revisoes = []
        for tempo in [1, 7, 30]:
            turno_revisao = self.turno - tempo
            if turno_revisao > 0:
                key_revisao = "{:03d}".format(turno_revisao)
                revisoes.append((turno_revisao, save_dict["historico"][key_revisao]))
        return revisoes

    def __repr__(self):
        return f"O turno é: {self.turno}\nO ciclo é:\n{self.ciclo}"