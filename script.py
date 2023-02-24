import requests

# FUNÇÕES AUXILIARES: 
def gerar_cod_save(turno, dia, lista_ciclos):
    c1 = str(turno+1)
    while len(c1) < 3:
        c1 += '&'
    c2 = ''
    for ciclo in lista_ciclos:
        c2 += '$'.join(ciclo)
        c2 += '$'
        while c2.count('$') % MAX_MATERIAS != 0:
            c2 += '_$'
    return c1 + dia + c2

def gerar_cod_cont(turno, lista_cont):
    cod_cont = str(turno)
    cont_final = ''
    while len(cod_cont) < 3:
        cod_cont += '&'
    for item in lista_cont:
        cont_final += '$'.join(item) + '$'
    text = cod_cont+cont_final+'\n'
    return text

# SEMANA
class Semana:
    def __init__(self, tipo_semana, n_ciclos):
        self.dia1, self.dia2, self.dia3, self.dia4, self.dia5 = Dia(), Dia(), Dia(), Dia(), Dia()
        self.lista_dias = [self.dia1, self.dia2, self.dia3, self.dia4, self.dia5]
        if tipo_semana == 1 or tipo_semana == 5:
            self.adiciona_ciclos(0)
        elif n_ciclos != 3:
            self.adiciona_ciclos(tipo_semana-1)
        else:
            if tipo_semana == 2:
                self.adiciona_ciclos(2)
            elif tipo_semana == 3:
                self.adiciona_ciclos(1)
            else:
                self.adiciona_ciclos(0)
    
    ##### ADICIONA ATÉ 5 CICLOS DIFERENTES EM 5 DIAS DA SEMANA #####
    def adiciona_ciclos(self, comeco):
        lista_ciclos = get_ciclos()
        ind_C = comeco
        ind_D = 0
        while ind_D < len(self.lista_dias):
            if ind_C == len(lista_ciclos):
                ind_C = 0
            self.lista_dias[ind_D].ciclo = lista_ciclos[ind_C]
            ind_C += 1
            ind_D += 1

# DIA
class Dia:
    def __init__(self):
        self.ciclo = 0

# ==================== FUNÇÃO SALVAR ==================== #
def salvar_turno(turno, dia, conteudo=''):
    lista_ciclos = get_ciclos()
    with open(arquivo_save, 'w', encoding='utf-8') as f1:
        f1.write(gerar_cod_save(turno, dia, lista_ciclos))
    f1.close()
    if conteudo != '':
        with open(arquivo_cont, 'a', encoding='utf-8') as f2:
            f2.write(gerar_cod_cont(turno, conteudo))
        f2.close()

# ==================== FUNÇÃO REVISÃO ==================== #
def get_turnos_rev(turno):      # devolve uma lista com os turno a revisar
    revisoes = []
    dias_rev = [1, 7, 30]
    for tempo in dias_rev:
        if turno > tempo:
            revisoes.append(turno - tempo)
    if len(revisoes) > 0:
        revisoes.sort()
        return revisoes
    else:
        return 0

def get_cont_rev(turnos_rev):     # devolve os conteúdos de revisão
    with open(arquivo_cont, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        f.close()
    rev = []
    lines_ex = lines[:]
    for line in lines_ex:
        num_l = int(line[:3].rstrip('&'))
        if num_l not in turnos_rev:
           lines.remove(line)
    for l in lines:             # Física$AERODINÂMICAA 1$Matemática$GEOMETRIA ESPACIALL Turno 1$
        line = l.rstrip("$\n").lstrip(l[:3]).split('$')
        temp_list, i = [], 0
        while i < len(line):
            temp_list.append([line[i], line[i+1]])
            i += 2
        rev.append(temp_list)
    return rev

# ==================== DEFINIÇÃO DE VARIÁVEIS ==================== #
def get_ciclos():    # devolve a lista de ciclos do cronograma atual
    lista_ciclos = []
    lista_mat_save = save[5:].split('$')
    n_ciclos = int(save.count('$') / MAX_MATERIAS)
    for i in range(n_ciclos):
        temp_ciclo = lista_mat_save[i*MAX_MATERIAS:4+i*MAX_MATERIAS]
        while '_' in temp_ciclo:
            temp_ciclo.remove('_')
        lista_ciclos.append(temp_ciclo)
    return lista_ciclos

def get_semana():    # devolve o tipo da semana atual
    turno = int(save[:3].rstrip('&'))
    n_ciclos = int(save.count('$') / MAX_MATERIAS)
    i = turno / (n_ciclos * 5) % 1
    if n_ciclos == 1 or n_ciclos == 5 or n_ciclos == 4 and i > 0.025 and i < 0.275 or n_ciclos == 3 and i > 0.033 and i < 0.366 or n_ciclos == 2 and i > 0.050 and i < 0.550:
        tipo_semana = 1
    elif n_ciclos == 4 and i > 0.275 and i < 0.525 or n_ciclos == 3 and i > 0.366 and i < 0.700 or n_ciclos == 2 and (i > 0.550 or i < 0.050):
        tipo_semana = 2
    elif n_ciclos == 4 and i > 0.525 and i < 0.775 or n_ciclos == 3 and (i > 0.700 or i < 0.033):
        tipo_semana = 3
    else:
        tipo_semana = 4
    return tipo_semana

def get_dia_semana(dia_atual=True):       # devolve o dia da semana e seu respectivo ciclo em uma lista
    turno = int(save[:3].rstrip('&'))
    n_ciclos = int(save.count('$') / MAX_MATERIAS)
    tipo_semana = get_semana()
    semana = Semana(tipo_semana, n_ciclos)
    d = turno % 5
    if not dia_atual:
        d -= 1
    if d == 1:
        dia_semana = 'Segunda'
        ciclo_atual = semana.dia1.ciclo
    elif d == 2:
        dia_semana = 'Terça'
        ciclo_atual = semana.dia2.ciclo
    elif d == 3:
        dia_semana = 'Quarta'
        ciclo_atual = semana.dia3.ciclo
    elif d == 4:
        dia_semana = 'Quinta'
        ciclo_atual = semana.dia4.ciclo
    elif d == 0:
        dia_semana = 'Sexta'
        ciclo_atual = semana.dia5.ciclo
    return [dia_semana, ciclo_atual]

def get_dia():
    url = 'http://worldtimeapi.org/api/timezone/America/Sao_Paulo'
    resposta = requests.get(url)
    resposta = resposta.json()['datetime']
    dia = resposta[8:10]
    return dia

def get_save():   # devolve a leitura do aquivo de salvamento
    with open(arquivo_save, 'r', encoding='utf=8') as f:
        save = f.read()
        f.close()
    return save

# variáveis
MAX_MATERIAS = 4

arquivo_save = 'saves/mainsave.txt'
arquivo_cont = 'saves/contentsave.txt'
save = get_save()
dia = get_dia()