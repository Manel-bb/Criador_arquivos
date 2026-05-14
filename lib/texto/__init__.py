def bs(lin=40, carac='='):
    print(carac * lin)


def cor(cor=''):
    if cor == "":
        print('\033[m', end='')
    elif cor == "azul":
        print('\033[36m', end='')
    elif cor == "verde":
        print('\033[32m', end='')
    elif cor == "vermelho":
        print('\033[31m', end='')
    elif cor == "amarelo":
        print('\033[33m', end='')
    elif cor == "roxo":
        print('\033[35m', end='')
    

def limpar():
    print('\033[2J\033[H')


def heading(a=40, texto="...", b='='):
    bs(a, b)
    print(f'{texto:^40}')
    bs(a, b)


def tabela_opcoes(texto, a=40, b='=', titulo="MENU"):
    bs(a, b)
    print(f'{titulo:^40}')
    bs(a, b)
    print(texto)
    bs(a, b)


def finalizando():
    from time import sleep
    sleep(1)
    print(f'\033[36m{f'\nFINALIZANDO PROGRAMA'}', end='')
    for c in range(0, 3):
        sleep(0.5)
        print('.', end='', flush=True)
    print('\033[31m')
    sleep(0.5)
    bs()
    print(f'{'<<<PROGRAMA FINALIZADO>>>':^40}')
    bs()
    print('\033[m')


def reticencias(frase=""):
    from time import sleep
    print(f'\033[32m{frase}', end='')
    for c in range(0, 3):
        sleep(0.5)
        print('.', end='', flush=True)
    print('\033[m')
    sleep(0.5)


def continuar(texto="Deseja continuar"):
    while True:
        cont = str(input(f"\033[33m{texto}? [S/N]: \033[m")).strip().upper()
        if cont not in ["S", "N"]:
            print('\033[31mResposta inválida.\033[m')
        if cont == "N":
            return False
        else:
            return True