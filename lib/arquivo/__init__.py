from lib.interface import *


def arquivoExiste(nome):#verificar se o arquivo de txt existe
    try:
        a = open(nome, 'rt')#tentando abri o arquivo, txt parametro da funçoa e  'rt'
        a.close()
    except FileNotFoundError:# "FileNotFoundError" trauçao  "Aquivo Não Existe"
        return False #se o arquivo nao existir o retorno e falso
    else:
        return True

def criarArquivo(nome):#funçao para criar o arquivo caso ele nao exista 
    try:
        a = open(nome, 'wt+')# o "wt" siguinifica gravar o arquivo  o "+" e o parametro que ira criar o arquivo propriamente dito,caso ele nao exista ainda.
        a.close()#fechar o arquivo ! 
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} Criado com Sucesso !' ) 


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')#primeiro abrimo o arquivo
    except:
        print('Erro -> Ao abri O arquivo ! ')
    else:
        # print('PESSOAS CADASTRADAS')
        cabeçalho("PESSOAS CADASTRADAS ")
        print(a.readlines())#ler tudo de dentro do arquivo txt
    

