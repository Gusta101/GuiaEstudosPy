# GuiaEstudosPy

Reimplementação do projeto inicial.

Agora utilizando técnicas mais sofisticadas, através do uso do framework de desenvolvimento web Flask, e utilização de API local .json (evitando utilização de banco de dados SQL devido à baixa potência da minha máquina atual), esse projeto visa auxiliar o usuário nos estudos para quaisquer concursos, provas, ou carreiras que lhe convirem.

## Funcionalidade

Na aplicação o usuário deverá inserir inicialmente, a ordem de matérias ou assuntos - ciclo -  que desejará estudar em cada turno, que representa um dia de estudo, de forma a criar um padrão de ciclos que o programa organizará ao longo dos dias úteis da semana.

Ao final de cada turno (dia de estudo), o usuário insere o conteúdo que foi abordado - capítulo onde finalizou, quantas páginas foram lidas, e etc. - para que seja salvo num arquivo .json, a numeração do turno e o conteúdo inserido para cada matéria.

Após um dia, uma semana, e um mês daquele turno, o aplicativo mostrará também ao usuário o conteúdo abordado anteriormente para revisão, visando o maior aproveitamento dos estudos a longo prazo.

ex.: Turno 37 serão mostradas as matérias designadas àquele dia, bem como os conteúdos vistos no turno 36, 30 e 7 e suas respectivas matérias.

## Implementações futuras

Após a finalização da ideia inicial, pretendo adicionar:

- Personalização de planos, para que o usuário possa editar o plano após sua criação, podendo excluí-lo e criar outro, ou editá-lo livremente sem perder seu histórico;
- Função de cadastro, permitindo a utulização do app a vários usuários, bastando logar na aplicação e vizualizar seu plano de estudos;
- Múltiplos planos, permitindo que cada usuário possa criar mais de um plano de estudos, cada um com seu histórico, sua ordem de ciclos e turno atual.
