# criar arquivo para diferentes situações dependendo do contexto aplicado
from lib.arquivo import *
from lib.dados import *
from lib.texto import *

menu1 = " [1] ADICIONAR ELEMENTO\n" \
" [2] ABRIR OUTRA LISTA\n" \
" [3] LER LISTA\n" \
" [4] SAIR"

menu2 = " [1] TEXTO\n" \
" [2] OPERAÇÕES MATEMÁTICAS" \

bs()
arq = input("Nome do arquivo: ")
limpar()
abrir_arquivo(arq)
while True:
    tabela_opcoes(menu1)
    atividade = ler_valor(1, 4, "Opção")

    #possibilidades do menu:
    #cadastro
    if atividade == 1:
        limpar()

        #opções dentro de cadastro:
        tabela_opcoes(menu2, titulo="NOVO CADASTRO")
        atividade2 = ler_valor(1, 2, "Opção")
        limpar()
        if atividade2 == 1:
            bs()
            texto = str(input("Texto: ")).strip().capitalize()
            limpar()
            cadastrar_valores(arq, texto, data_hora=1)
        if atividade2 == 2:
            resultado, conta = operacao()
            limpar()
            cadastrar_valores(arq, resultado, " -> ".join(conta), data_hora=1)     

    #abrir outra lista
    elif atividade == 2:
        limpar()
        bs()
        arq = input("Nome do arquivo: ")
        limpar()
        bs()
        abrir_arquivo(arq)
        continue
    #ler lista
    elif atividade == 3:
        limpar()
        bs()
        ler_lista(arq)
    #sair
    elif atividade == 4:
        finalizando()
        break

