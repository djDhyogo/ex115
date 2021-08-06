1
from lib.interface import *
from time import sleep
from lib.arquivo import * #este sinal de * siguinifica importar tudo

# cabeçalho('SISTEMA AQUIVO v1.0')

arq = "cursoemvideo.txt"#variavel global como o nome do arquivo 


if not arquivoExiste(arq):#verificando se existe o arquivo .txt 
    criarArquivo(arq)#se nao encontra ele ira criar o arquivo 


while True:
    #chamando a funçao menu e pasando uma 'lista' com parametro "as opção de escolhas"
    resposta = menu(['Ver Pessoas Cadastradas','Cadastra Nova Pessoa','Sair do Sistema'])
    if  resposta == 1:
        #opçao de listar o conteudo de uma arquivo !
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('Opçao 2')
    elif resposta == 3:
        cabeçalho('\033[31m Saindo do Program... Ate logo !!\033[m'.center(42))
        break
    else:
        print('\033[31mErro: Opçao Invalida ! Tente novamente\033[m')
    sleep(1)

