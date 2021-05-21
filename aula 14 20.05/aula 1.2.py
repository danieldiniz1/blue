from time import sleep
print('''
[1] Exibir lista de alunos
[2] Inserir aluno e nota
[3] Alterar nota do aluno
[4] Consultar nota do aluno
[5] Apagar o aluno da lista
[6] Exibir média da turma
[0] Sair
''')

turma = {}

while True:
  print()
  menu = input("Escolha uma opção: ")
  
  if menu in '0':
    break

  else:

    if menu in '1' and len(turma) != 0:

      print('Exibindo lista de alunos...')
      print()

      for key, value in turma.items():
        sleep(1)
        print(f'{key}: {value}')

        print()

    else:

      print('Dicionário de alunos vazio')
      print()

    if menu in '2':
      print()

      aluno = input('Qual o nome do aluno?: ').lower().capitalize()
      nota = float(input('Digite a nota do aluno: '))
      turma[aluno] = nota

    elif menu in '3':
      print()
      print('Essa é a lista de alunos...')

      for key, value in turma.items():
        print(f"{key}: {value}")
          
        print()

        aluno = input('Qual o nome do aluno que deseja alterar a nota?: ').lower().capitalize()
        nota = float(input('Digite a nota do aluno: '))
        turma[aluno] = nota 
        print('Nota alterada com sucesso!')

        print()

    elif menu in '4': 

      aluno = input('Deseja consultar a nota de qual aluno?: ').lower().capitalize()
      verifica = turma.get(aluno, 'O aluno não esta nessa turma')    
      print(f'{aluno}: {verifica}')
      
      print()

    elif menu in '5':

      aluno = input('Nome do aluno que saiu da turma: ').lower().capitalize()
      del turma[aluno]
      print('Aluno deletado...')
      
      print()
        
    elif menu in '6':

      soma = 0
      for value in turma.values():
        soma+=value

      media = soma / len(turma)
      print(f'Média da turma: {media}')

print('Lista final de alunos...')
for key, value in turma.items():
  print(f'{key}: {value}')