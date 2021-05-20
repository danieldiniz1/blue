#exercício 4


menu = [(0, '0- Sair'),
(1, "1- Exibir lista de alunos com suas notas (cada aluno tem uma nota)"),
(2, "2- Inserir aluno e nota"),
(3, "3- Alterar a nota de um aluno"),
(4, "4- Consultar nota de um aluno específico "),
(5, "5- Apagar um aluno da lista"),
(6, "6- Exibir a média da turma"),
]
continuar = True

listaalunos={}


while continuar ==True:

    for opcao in menu:
        print(opcao[1])

    selecao = int(input("qual opção você quer selecionar? "))
    if selecao == 0:
        break
    elif selecao == 1:
        print(listaalunos)
    elif selecao == 2:
        nome = input("digite o nome do aluno: ")
        nota = float(input("digite a nota do aluno: "))
        listaalunos.update({nome:nota})
    elif selecao ==3:
        alterar = input("Digite o nome do aluno que você quer alterar a nota: ")
        notanova = float(input(f"digite a nova nota do aluno:{alterar} "))
        listaalunos.update({alterar:notanova})
    elif selecao ==4:
        print("Qual aluno você quer ver a nota? ")
        print(listaalunos.get(nome)
