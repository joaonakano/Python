''' Treinar a Recursividade com um Projeto 

- Fazer um programa que (1) PEDE AO USUÁRIO um NÚMERO INTEIRO REAL e (2) exibe uma tabela de TABUADA (3) que seja compartimentalizada em uma ou demais funções
'''

numeroUser = int(input("Digite um número INTEIRO: "))
contagem = int(input("Insira até quantas vezes deseja calcular: "))

def tabuada(numero, contagem):  
    if contagem == 0:
        return
    print(f"{numero} * {contagem} =", (numero * contagem))
    tabuada(numeroUser, contagem-1)


tabuada(numeroUser, contagem)