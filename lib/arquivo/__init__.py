from lib.dados import *
from lib.texto import *
import os
# padrão:
#os.chdir(os.path.dirname(os.path.abspath(__file__)))

# local:
os.chdir(r"/home/Manel/Documents/textos_from_pythoncodes")



def abrir_arquivo(nome):
    try:
        with open(nome, 'rt', encoding='utf-8') as arq:
            print(f'\033[32mAbrindo arquivo "{nome}" já existente...\033[m')
    except FileNotFoundError:
        try:
            with open(nome, 'wt', encoding='utf-8') as arq:
                pass
        except Exception as e:
            print(f'\033[31mErro em abrir arquivo: {e}\033[m')
        else:
            print(f'\033[32mArquivo "{nome}" criado com sucesso!\033[m')


def cadastrar_valores(nome, campo_a="<desconhecido>", b='', data_hora=0):
    try:
        with open(nome, 'at', encoding='utf-8') as arq:
            if data_hora == 1:
                dh = data_e_hora()
                if isinstance(campo_a, (int, float)):
                    arq.write(f'{dh}\n{b}\n\n')
                else: 
                    arq.write(f'{dh}\n{campo_a}\n\n')
            else:
                if isinstance(campo_a, (int, float)):
                    arq.write(f'{b}\n\n')
                else:
                    arq.write(f'{campo_a}\n\n')
    except Exception as e:
        print(f'\033[31mErro no cadastramento: {e}\033[m')
    else:
        print(f'\033[32mNovo registro de "{nome}" adicionado.\033[m')


def ler_lista(nome):
    try:
        with open(nome, 'rt', encoding='utf-8') as arq:
            for linha in arq:
                print(f'{linha}', end='')
    except Exception as e:
        print(f'\033[31mErro ao ler arquivo: {e}.\033[m')
