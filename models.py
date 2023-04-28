from datetime import date

class Estudo:
    def __init__(self, save_dict):
        self.turno = self.define_turno(save_dict)
        self.ciclo = self.define_ciclo(save_dict)
        self.dia = date.today().day

    @staticmethod
    def define_turno(save_dict):
        turno = max(save_dict["historico"])
        return int(turno) + 1

    @staticmethod
    def define_ciclo(save_dict):
        ciclo = save_dict["ciclos"]
        ind = (self.turno if self.turno <= len(ciclo) else self.turno % len(ciclo)) - 1
        return ciclo[ind]

    def __repr__(self):
        return f"O turno é: {self.turno}\nO ciclo é:\n{self.ciclo}"