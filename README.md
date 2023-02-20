Cronograma de Estudos - Python

Esse aplicativo tem o intuito de mostrar ao usuário o turno atual de estudos, com as respectivas matérias a serem estudadas, bem como as revisões a serem feitas naquele dia, de forma a revisar todos os dias os conteúdos estudados no dia, semana, e mês diretamente antecessores ao atual, garantindo assim melhor eficiência na retenção de informações em situações de longo prazo.
Os conteúdos estudados em cada dia são inseridos pelo usuário ao final de cada turno e armazenados em um .txt para resgate posterior.

Funcionalidades do usuário:
- Criação de cronogramas que dividem os dias da semana em até 5 ciclos, contendo cada um até 4 matérias diferentes e personalizáveis;
- Alteração do cronograma atual a qualquer momento, tendo em vista que o histórico será apagado para criação de um novo cronograma de estudos;
- Inserção dos dados estudados em cada turno para consulta posterior nos dias determinados;

Requisitos:
- Existência de arquivos 'tempsave.txt' e 'contentsave.txt' vazios(caso seja a primeira vez que o app foi aberto) no mesmo diretório do Aplicativo;



O programa está dividido em dois arquivos:

- Script.py  ==> é reservado para funções independentes, que terão como objetivo ler dados, tratar códigos de salvamento e definir variáveis que serão utilizadas posteriormente, parte majoritariamente Back-End do projeto e reutilizável caso o aplicativo migre para uma página desenvolvida em Django por exemplo
- App.py     ==> Na prática, o executável do aplicativo, arquivo reservado para a criação e funcionalidades da interface desenvolvida com a biblioteca Python 'PySimpleGUI'. Suas funções são especialmente direcionadas para a interface do app que tem como objetivo a praticidade e facilidade de uso, abandonando critérios de Design ou boa aparência.

* ERROS a serem corrigidos:
- Problema: Trocar de tela após salvar o turno do dia atual avança para o próximo turno;
- Solução: Utilizar uma API de calendário designar cada turno a um dia, limitando o avanço de turnos;
status de progresso: EM ANDAMENTO

* PROPOSTAS a serem implementadas(Requisitos Não-Funcionais):
- Dificuldade: Deve-se estudar todas matérias do turno obrigatoriamente;
- Proposta: Retirar as checkboxes de conclusão e possibilitar a negligência de algumas matérias(MAS NUNCA DE TODAS);
status de progressão: EM AGUARDO

- Dificuldade: Tela de criação de cronogramas pouco intuitiva;
- Proposta: Eliminação de botões desnecessários, talvez reorganização de layout de tela;
status de progressão: EM AGUARDO

Proposta de projeto pessoal: Migração do app para página web Django