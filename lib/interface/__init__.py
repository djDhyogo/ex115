# aqui sera  criado a interface começando

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TabError):#se apresentar um desses dois tipos de erro
            print('\033[0;31mErro ! Digite um numero inteiro Valido \033[m')
            continue#esse comando reinicia o laço while
        except KeyboardInterrupt:
            #caso não seja digitado crt + c 
            print(f'Programa finalizado pelo usuario !')
            #nesse caso valor de n sera 0.
            return 0 
        else:
            return n


def linha(tam=42):#esse codigo cria linhas. 
    return '-' * tam


def cabeçalho(txt):
    """
    :param txt: PARAMETRO RECEBE UMA STR "FRASE "
    :return: IMPRIME NA TELA O CABEÇARIO COM
    A DETERMINADA FRASE, QUE SERA PASSADA COMO
    PARAMETRO
    """
    print(linha())
    print(f'{txt}'.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:#imprimindo a lista 
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc





