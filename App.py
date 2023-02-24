from PySimpleGUI import PySimpleGUI as sg
import script as spt

tema_app = 'Material1'
cor_sec = 'LightBlue'
cor_pri = 'DarkBlue'
title_font = 'Helvetica 18 bold'
sub_title_font = 'Helvetica 14'
font = 'Helvetica 12'
arquivo_save = 'saves/mainsave.txt'
arquivo_cont = 'saves/contentsave.txt'

# variáveis globais
MAX_MATERIAS = 4
save = spt.get_save()                                       # arquivo turno atual
dia = spt.dia
if save != '':
    turno = int(save[:3].rstrip("&"))                           # turno atual
    dia_semana, ciclo = spt.get_dia_semana()[0], spt.get_dia_semana()[1]      # info do dia atual



# ==================== FUNÇÕES AUXILIARES ==================== #
# QUEBRA DE LINHA PARA TABELAS
def quebra_linhas_str(str, larg):
    if len(str) < larg:
        return str
    list_str = str.split(' ')
    str = '$' + list_str[0]
    for i in range(1, len(list_str)):
        br = str.find('$')
        if len(str[br:])+len(list_str[i]) > larg:
            str = str.replace('$', '\n')
            str += '$'+list_str[i]
        else:
            str += ' '+list_str[i]
    str = str.replace('$', '\n')
    return str

# REDEFINE VARIÁVEIS GLOBAIS
def set_vars():
    global save, turno, dia_semana, ciclo
    save = spt.get_save()
    spt.save = save
    turno = int(save[:3].rstrip("&"))
    dia_semana, ciclo = spt.get_dia_semana()[0], spt.get_dia_semana()[1]



# ==================== TELA PRINCIPAL - SETTERS ==================== #
# adiciona checkboxes das matérias ~layout[3]
def set_ckboxes(layout):
    global ciclo
    row = layout[3]
    row.append(sg.Push())
    if len(ciclo) > 0:
        for i in range(len(ciclo)):
            row.append(sg.Checkbox(ciclo[i], default=False, key='-ckbox'+str(i+1)+'-', font=font+' italic'))
        row.append(sg.Push())
    else:
        row = [sg.Text('Não há matérias a serem estudadas hoje', font=font, expand_x=True, justification='center', text_color='Yellow')]

# adiciona inputs do conteúdo estudado ~layout[-3]
def set_inputs(layout):
    global ciclo
    row = layout[-3]
    row.append(sg.Push())
    if len(ciclo) > 0:
        largura = 60 - (len(ciclo) * 10)
        for i in range(len(ciclo)):
            row.append(sg.Column([[sg.Text(ciclo[i], font=font)], [sg.Multiline(size=(largura, 5), font=font, expand_x=True, expand_y=True, key='-in'+str(i+1)+'-', no_scrollbar=True, border_width=3)]]))
        row.append(sg.Push())
    else:
        row = [sg.Text('Nenhuma matéria foi estudada hoje', font=font, expand_x=True, justification='center', text_color='Yellow')]
        
# adiciona tabelas de revisão ~layout[5...]
def set_table(layout):
    turnos_rev = spt.get_turnos_rev(turno)
    cont_rev = spt.get_cont_rev(turnos_rev)
    if turnos_rev != 0:
        larg_col = len(turnos_rev) * 12
        layout.insert(5, 
        [sg.Text('Revisão:', font=sub_title_font, expand_x=True, justification='center')],)
        tabelas = []
        # cont_rev = [ (cont_rev)
        #     [ (turno)
        #         (bloco), (bloco), [(bloco[0]), bloco[1]]
        #     ], [
        #         ['H', 'Turno 14 HIstória'], ['G', 'Turno 14 Geografia'], ['S', 'Turno 14 Socio/Filo']
        #     ]
        # ]
        
        for ind_turno in range(len(turnos_rev)):  # quantos turnos serão revisados no cont_rev
            headings_tabela = ['Turno']
            val_tab = [[str(turnos_rev[ind_turno])]]
            for bloco in cont_rev[ind_turno]:
                headings_tabela.append(bloco[0])
                val_tab[0].append(quebra_linhas_str(bloco[1], int(larg_col-4)))
            tabelas.append([sg.Table(values=val_tab, headings=headings_tabela, key='-table'+str(turno+1)+'-', justification='center', num_rows=1, row_height=70, col_widths=larg_col, hide_vertical_scroll=True, background_color=cor_sec)])
        layout.insert(6, [sg.Push(), sg.Column(tabelas, scrollable=True, vertical_scroll_only=True, expand_y=True), sg.Push()])


# ==================== TELA PRINCIPAL - VALIDAÇÕES ==================== #
def valida_salvar():
    save = spt.get_save()
    turno_save = int(save[:3].rstrip('&'))
    if turno_save == turno + 1:
        return False
    else:
        return True

def valida_ckboxes(valores):
    for i in range(len(ciclo)):
        ind = '-ckbox'+str(i+1)+'-'
        if valores[ind] == False:
            return False
    return True

def valida_inputs(valores):
    for i in range(len(ciclo)):
        valor = valores['-in'+str(i+1)+'-']
        if valor == None or valor.strip() == '':
            return False
    return True

# lê inputs e formata os dados para salvamento
def get_inputs_cont(valores):
    lista_final = []
    for i in range(len(ciclo)):
        materia = ciclo[i]
        cont = valores['-in'+str(i+1)+'-'].strip()
        lista_final.append([materia, cont])
    return lista_final

def salvar(valores):
    conteudo = get_inputs_cont(valores)
    spt.salvar_turno(turno, dia, conteudo)



# ==================== TELA CONFIGURAR - SET e GET ==================== #
def set_config_ciclos(lista_configs, lista_mat):
    row = [sg.Push()]
    for i in range(5):
        col = sg.Column([[sg.Text('Ciclo '+str(i+1)+':', background_color=cor_sec)], [sg.Combo(lista_mat, font=font, readonly=True, key='-in_config'+str(i+1)+'-')], [sg.Text(text='', font='Arial 12 italic', size=(12, 5), key='-list_config'+str(i+1)+'-', expand_x=True)], [sg.Button('Adicionar', key='-adc_config'+str(i+1)+'-', expand_x=True)], [sg.Button('Limpar', key='-limp_config'+str(i+1)+'-', expand_x=True)]], 'LightBlue')
        row.append(col)
    row.append(sg.Push())
    return row

def get_buttons():
    save = spt.get_save()
    if save == '':
        btns = [sg.Button('Ver Plano', key='-ver_plano-', size=(16, 1), border_width=4), sg.Push(), sg.Button('Salvar', key='-salvar-', size=(8, 1), border_width=4)]
    else:
        btns = [sg.Button('Voltar', key='-voltar-', border_width=4), sg.Push(), sg.Button('Salvar Novo', key='-salvar-', border_width=4)]
    return btns


# ==================== TELA CONFIGURAR - FUNÇÕES ==================== #
def salvar_config(lista_config):
    str = '1&&00'
    for i in range(5):
        ciclo = lista_config[i]
        for c in ciclo:
            if c != '':
                str += c+'$'
        while str.count('$') % MAX_MATERIAS != 0:
            str += '_$'
    with open(arquivo_save, 'w', encoding='utf-8') as save:
        save.write(str)
        save.close()
    with open(arquivo_cont, 'w', encoding='utf-8') as cont_save:
        cont_save.write('')
        cont_save.close()
    set_vars()



# ==================== MENU PRINCIPAL ==================== #
def menu_principal():
    sg.theme(tema_app)
    save = spt.get_save()
    if int(save[3:5]) != int(dia):
        set_vars()
        layout = [
            [sg.Text('Turno: '+str(turno), expand_x=True, justification='right', font=sub_title_font), sg.Push(), sg.Text('Cronograma', expand_x=True, justification='center', font='helvetica 24 bold', background_color=cor_pri, text_color='White'), sg.Push(), sg.Text(str(dia_semana+'-feira'), expand_x=True, justification='left', font=sub_title_font)],
            [sg.Text('', size=(6,2))],
            [sg.Text('Matérias de hoje:', expand_x=True, justification='center', font=sub_title_font)],
            [], # checkboxes ~layout[3]
            [sg.Text('', size=(1, 1))], # pular linha
            [sg.Text('Anote aqui o conteúdo estudado para uma revisão futura', font=sub_title_font, justification='center', expand_x=True)],
            [], # inputs ~layout[-3]
            [sg.Text('', size=(1, 1))], # pular linha
            [sg.Button('Voltar', key='-voltar-', border_width=4), sg.Button('Alterar Cronograma', key='-alterar-', border_width=4), sg.Text('', expand_x=True), sg.Button('Salvar', key='-salvar-', border_width=4), sg.Button('Salvar e Sair', key='-salvarsair-', border_width=4)]
        ]
        set_ckboxes(layout)
        set_inputs(layout)
        set_table(layout)
    else:
        turno = turno = int(save[:3].rstrip("&"))
        dia_semana = spt.get_dia_semana(dia_atual=False)[0]
        layout = [
            [sg.Text('Turno: '+str(turno-1), expand_x=True, justification='right', font=sub_title_font), sg.Push(), sg.Text('Cronograma', expand_x=True, justification='center', font='helvetica 24 bold', background_color=cor_pri, text_color='White'), sg.Push(), sg.Text(str(dia_semana+'-feira'), expand_x=True, justification='left', font=sub_title_font)],
            [sg.Text('Você já estudou o turno de hoje, parabéns!!!\nVá descansar um pouco e volte amanhã para mais estudos :)', font=title_font)],
            [sg.Button('Voltar', key='-voltar-', border_width=4), sg.Push(), sg.Button('Alterar Cronograma', key='-alterar-', border_width=4)]
            ]
    
    janela = sg.Window('App de Estudos by Gustavo', layout)
    
    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            janela.close()
            return 'fechar'
        elif eventos == '-salvarsair-':
            if valida_ckboxes(valores) and valida_inputs(valores):
                if valida_salvar():
                    salvar(valores)
                    janela.close()
                    sg.popup_notify("Seu turno foi salvo")
                    return 'fechar'
                else:
                    janela.close()
                    return 'fechar'
            else:
                sg.popup_quick_message("Você ainda não completou o ciclo de hoje ou ainda não anotou o conteúdo estudado", background_color='Yellow', font=font)
        elif eventos == '-salvar-':
            if valida_ckboxes(valores) and valida_inputs(valores):
                if valida_salvar():
                    salvar(valores)
                else:
                    sg.popup_quick_message('Você já salvou esse turno', background_color=cor_pri, text_color='White')
            else:
                sg.popup_quick_message("Você ainda não completou o ciclo de hoje ou ainda não anotou o conteúdo estudado", background_color=cor_sec, font=font)
        elif eventos == '-alterar-':
            janela.close()
            return 'configurar'
        elif eventos == '-voltar-':
            janela.close()
            return 'inicial'

# ==================== MENU INICIAL ==================== #
def menu_inicial():
    sg.theme(tema_app)
    layout = [
        [sg.Text('', size=(1, 1))],
        [sg.Text('Bem vindo ao Guia de Estudos!!!', font=title_font, expand_x=True, justification='center', size=(40, 3))],
        [sg.Text("Aqui nós dividimos as semanas, de segunda a sexta, em ciclos de estudo.\nCada ciclo possui até 5 'Turnos', que são basicamente os dias de estudo, de forma que as matérias estudadas naquele dia são chamadas de 'bloco'.", font=font, size=(50, 6), expand_x=True, justification='center')],
    ]
    
    if save == '':
        layout.append([sg.Text('Parece que você ainda não configurou seu cronograma de estudos, deseja fazer isso agora?', font=font, justification='center', expand_x=True, size=(50, 3))])
        layout.append([sg.Push(), sg.Button('Criar cronograma', key='-criar_cronograma-', font=font, expand_x=True, size=(20, 2), border_width=4), sg.Push()])
    else:
        layout.append([sg.Push(), sg.Button('Ver cronograma', key='-ver_cronograma-', font=font, expand_x=True, size=(30, 3), border_width=4), sg.Push()])
    
    janela = sg.Window('Bem vindo!', layout)
    
    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            janela.close()
            return 'fechar'
        elif eventos == '-ver_cronograma-':
            janela.close()
            return 'principal'
        elif eventos == '-criar_cronograma-':
            janela.close()
            return 'configurar'

# ==================== MENU CONFIGURAR ==================== #
def menu_configurar():
    sg.theme(tema_app)
    
    lista_mat = ['Biologia', 'Física', 'Geografia', 'História', 'Literatura', 'Matemática', 'Química', 'Redação', 'Socio/Filo']
    cnfg_cl1, cnfg_cl2, cnfg_cl3, cnfg_cl4, cnfg_cl5 = [], [], [], [], []
    lista_configs = [cnfg_cl1, cnfg_cl2, cnfg_cl3, cnfg_cl4, cnfg_cl5]
    btns = get_buttons()
    
    layout = [
        [sg.Text('Altere seu cronograma da forma mais adequada para você', background_color=cor_pri, text_color='white', font=title_font, expand_x=True, justification='center')],
        [sg.Text('', size=(1, 1))],
        [sg.Text("(Lembre-se, cada semana pode ter até 5 'ciclos', para cada 'turno'/dia de estudo será atribuído um ciclo de acordo com o cronograma, contendo até no máximo 4 'blocos'/matérias por dia)", font=font+' italic', expand_x=True, justification='center', size=(60, 3))],
        [sg.Text('', size=(1, 1))],
        [sg.Push(), sg.Text('Personalize quais matérias serão\nestudadas ou adicione outras:', font=font, justification='center'), sg.Push(), sg.InputCombo(lista_mat, font=font, key='-in_mat-'), sg.Button('Adicionar', key='-adicionar_mat-', border_width=3), sg.Button('Remover', key='-remover_mat-', border_width=3), sg.Push()],
        [sg.Text('', size=(1, 1))],
        [], # layout[5] set ciclos
        [sg.Text('', size=(1, 1))],
        [sg.Column([btns], key='-col_btns-', expand_x=True)] # layout[8]
    ]
    
    layout[6] = set_config_ciclos(lista_configs, lista_mat)
    
    janela = sg.Window('Configurar cronograma', layout)
    
    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            janela.close()
            return 'fechar'
        elif eventos == '-adicionar_mat-':
            string = valores['-in_mat-'].strip()
            if string not in lista_mat:
                lista_mat.append(string)
                lista_mat.sort()
                janela['-in_mat-'].update(values=lista_mat)
                for i in range(5):
                    janela['-in_config'+str(i+1)+'-'].update(values=lista_mat)
                sg.popup_quick_message('Matéria adicionada', background_color=cor_pri, text_color='White')
            else:
                sg.popup_quick_message('Essa matéria já está na lista', background_color=cor_pri, text_color='White')
        elif eventos == '-remover_mat-':
            string = valores['-in_mat-']
            if string in lista_mat:
                lista_mat.remove(string)
                lista_mat.sort()
                janela['-in_mat-'].update(values=lista_mat)
                lista_configs
                for i in range(5):
                    janela['-in_config'+str(i+1)+'-'].update(values=lista_mat)
                sg.popup_quick_message('Matéria removida', background_color=cor_pri, text_color='White')
            else:
                sg.popup_quick_message('Essa matéria não está na lista', background_color=cor_pri, text_color='White')
        elif eventos == '-salvar-':
            if save == '':
                salvar_config(lista_configs)
                btns = get_buttons()
                janela['-col_btns-'].update([btns])
            else:
                opcao = sg.popup_ok_cancel('Isso apagará seus dados do plano anterior\nTem certeza disso?')
                if opcao == 'OK':
                    salvar_config(lista_configs)
                    btns = get_buttons()
                    janela['-col_btns-'].update([btns])
        elif eventos == '-ver_plano-':
            salvar_config(lista_configs)
            janela.close()
            return 'principal'
        elif eventos == '-voltar-':
            janela.close()
            return 'principal'
        for b in range(5):
            ind = str(b+1)
            if eventos == '-limp_config'+ind+'-':
                lista_configs[b].clear()
                janela['-list_config'+ind+'-'].update('\n'.join(lista_configs[b]))
                sg.popup_quick_message('Limpou o ciclo '+ind, background_color=cor_pri, text_color='White')
            elif eventos == '-adc_config'+ind+'-':
                if len(lista_configs[b]) >= 4:
                    sg.popup_quick_message('Você já possui 4 blocos nesse ciclo', background_color=cor_pri, text_color='White')
                else:
                    lista_configs[b].append(valores['-in_config'+ind+'-'])
                    janela['-list_config'+ind+'-'].update('\n'.join(lista_configs[b]))



def main():
    tela = menu_inicial()
    while True:
        if tela == 'principal':
            tela = menu_principal()
        elif tela == 'configurar':
            tela = menu_configurar()
        elif tela == 'inicial':
            tela = menu_inicial()
        elif tela == 'fechar':
            break

if __name__ == '__main__':
    main()