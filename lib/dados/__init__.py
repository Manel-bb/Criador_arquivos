from lib.texto import *
from lib.arquivo import *


def ler_valor(inicial, final, v="Opção"):
    while True:
        try:
            valor = int(input(f"{v}: "))
        except Exception as e:
            print(f"\033[31mErro: {e}...\033[m")
        else:
            if valor < inicial or valor > final:
                print(f"\033[31mNúmero inválido. Digite um valor entre {inicial} e {final}.\033[m")
            else:
                break
    return valor


def data_e_hora():
    from datetime import datetime
    agora = datetime.now()
    d_h = agora.strftime("%d/%m/%y (%H:%M:%S)")
    return d_h


def operacao():
    menu3 = " [1] SOMA\n" \
    " [2] SUBTRAÇÃO\n" \
    " [3] MULTIPLICAÇÃO\n" \
    " [4] DIVISÃO\n" \
    " [5] POTENCIAÇÃO\n" \
    " [6] RAIZ\n" \
    " [7] SAIR"
    cor('roxo')
    tabela_opcoes(menu3, titulo="OPERAÇÕES")
    cor()
    c = 2
    operacao_completa = []
    while True:
        operacao = ler_valor(1, 7, "Operação")
        print()
        if operacao == 7:
            limpar()
            return
        if c == 2:
            primeiro_valor = float(input(f"{c-1}° valor: "))
            total = primeiro_valor
        #soma
        if operacao == 1:
            while True:
                try:
                    n = float(input(f"{c}° valor: "))
                except Exception as e:
                    print(f"\033[31mErro na leitura: {e}\033[m")
                else:
                    print(total, end='')
                    total1 = total + n
                    expr = (total, " + ", n, " = ", total1)
                    total = total1
                    print("  + ", n, " = ", total)
                    c += 1
                    break
        #subtração
        if operacao == 2:
            while True:
                try:
                    n = float(input(f"{c}° valor: "))
                except Exception as e:
                    print(f"\033[31mErro na leitura: {e}\033[m")
                else:
                    print(total, end='')
                    total1 = total - n
                    expr = (total, " - ", n, " = ", total1)
                    total = total1
                    print("  - ", n, " = ", total)
                    c += 1
                    break
        #multiplicação
        if operacao == 3:
            while True:
                try:
                    n = float(input(f"{c}° valor: "))
                except Exception as e:
                    print(f"\033[31mErro na leitura: {e}\033[m")
                else:
                    print(total, end='')
                    total1 = total * n
                    expr = (total, " x ", n, " = ", total1)
                    total = total1
                    print("  x ", n, " = ", total)
                    c += 1
                    break
        #divisão
        if operacao == 4:
            while True:
                try:
                    n = float(input(f"{c}° valor: "))
                except Exception as e:
                    print(f"\033[31mErro na leitura: {e}\033[m")
                else:
                    print(total, end='')
                    total1 = total / n
                    expr = (total, " / ", n, " = ", total1)
                    total = total1
                    print("  / ", n, " = ", total)
                    c += 1
                    break
        #potenciação
        if operacao == 5:
            while True:
                try:
                    n = float(input(f"{c}° valor: "))
                except Exception as e:
                    print(f"\033[31mErro na leitura: {e}\033[m")
                else:
                    print(total, end='')
                    total1 = total ** n
                    expr = (total, " ^ ", n, " = ", total1)
                    total = total1
                    print(" ^", n, " = ", total)
                    c += 1
                    break
        #rais quadrada
        if operacao == 6:
            while True:
                try:
                    n = float(input(f"{c}° valor: "))
                except Exception as e:
                    print(f"\033[31mErro na leitura: {e}\033[m")
                else:
                    print(total, end='')
                    total1 = total ** (1/n)
                    expr = (total, " ^ (1/", n, ") = ", total1)
                    total = total1
                    print("  ^ (1/", n, ") = ", total)
                    c += 1
                    break
        conta = ("".join(str(x) for x in expr))
        operacao_completa.append(conta)
        cont = continuar("Adicionar operação")
        if not cont:
            return total, operacao_completa
        limpar()
        cor('roxo')
        tabela_opcoes(menu3, titulo="OPERAÇÔES")
        cor()
        print(conta)

