import pandas as pd
import os

from pandas.core.frame import DataFrame


#AV2-PCA, CADASTRO DE ALUNOS

#Codigo feito por: Renan Rezende Rolão 


def menu() :
    option = int(input('''
 
MENU  

[1] - INSERIR
[2] - EXIBIR
[3] - REMOVER
[4] - SAIR

Escolha uma opção
'''))

    return option

def cadastra_aluno(alunos) :
    aluno_matricula = 0
    for aluno_matricula in range(len(alunos)):
        print("")
    aluno_nome = input('Digite o nome do aluno: ')
    aluno_rua = input('Digite a rua do aluno: ')
    aluno_numero = input('Digite o numero do aluno: ')
    aluno_bairro = input('Digite o bairro do aluno: ')
    aluno_cidade = input('Digite a cidade do aluno: ')
    aluno_UF = input('Digite a UF do aluno: ')
    aluno_telefone = input('Digite o telefone do aluno: ')
    aluno_email = input('Digite o email do aluno: ')
    aluno=aluno_matricula, aluno_nome, aluno_rua, aluno_numero, aluno_bairro, aluno_cidade, aluno_UF, aluno_telefone, aluno_email 
    alunos.append(aluno)
    meu_dicionario = {aluno_matricula: {'Nome': aluno_nome,'rua': aluno_rua, 'num':aluno_numero,'bairro': aluno_bairro,'cid': aluno_cidade, 'uf': aluno_UF, 'tel': aluno_telefone, 'email': aluno_email}}
    print("Cadastrado com sucesso")
    
    rn = pd.DataFrame(meu_dicionario)


    diretorio = os.path.dirname("./Trabalho-PCA") 
    rn.to_csv(str(os.path.join(diretorio, "cadastro_renan.csv" )), index=False)
    print("\nSalvando...")



def mostrar_aluno(alunos) :  
        for aluno in alunos:
            aluno_matricula, aluno_nome, aluno_rua, aluno_numero, aluno_bairro, aluno_cidade, aluno_UF, aluno_telefone, aluno_email= aluno
            print(f'Matrícula: {aluno_matricula}\nNome: {aluno_nome}\nRua: {aluno_rua}\nNúmero: {aluno_numero}\nBairro: {aluno_bairro}')
            print(f'Cidade: {aluno_cidade}\nUF: {aluno_UF}\nTelefone: {aluno_telefone}\nE-mail: {aluno_email}\n')
            

def remover(alunos):
    for aluno in alunos:
        aluno_matricula = aluno
        aluno_matricula=str(input("Digite o número da matrícula do aluno que deseja remover:"))
        if aluno in alunos:
            alunos.remove(aluno)
        print("Aluno removido com sucesso!")

    else:
        print("Aluno não encontrado. Tente novamente!")


def limpa_tela():
  import os
  os.system('clear')
 
def programa() :
    
    alunos = []


    while True:
        option = menu()

        limpa_tela()

        if option == 1 :
            cadastra_aluno(alunos)
        if option == 2 :
            mostrar_aluno(alunos)
        if option == 3 :
            remover(alunos)
        if option == 4 :
          print("Fim do Programa")
          break
          

programa()