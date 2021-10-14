#Discentes:
#Clauber Junior Machado Fonseca - 11837442
#Graciella dos Santos Favoreto - 11812542
#João Pedro Pilastri Terruel - 11812584
#Victor Pereira Moura - 11836160

#lendo arquivo .fasta
from io import UnsupportedOperation


def ler_fasta(arquivo):
    sequencia = ''
    lista = []
    with open(arquivo, 'r') as fasta:
            sequencia = ''
            for linha in fasta:
                if not linha.startswith('>'):
                    sequencia += linha
            lista.append(sequencia)

    return lista

lista = ler_fasta("gene_S_Whuhan.fasta")
lista_str = str(lista)

def entrada():
    seq_entrada = input("Entre com a sequencia de nucleotideos:")
    seq_entrada = seq_entrada.upper()
    verificacao(seq_entrada)

def normalizacao(seq_entrada):
    for i in seq_entrada:
        if i != 'A' and i != 'C' and i != 'T' and i != 'G':
            print("Sequencia incorreta. Submeta apenas caracteres A, C, T e G.")
            entrada()
        else:
            verificacao(seq_entrada, lista_str)

def verificacao(seq_entrada):
    try:
        lista_str.index(seq_entrada)
    except ValueError:
        print("Sequencia nao encontrada;")
        entrada()
    else:
        indice = lista_str.index(seq_entrada)
        print("Sequencia encontrada a partir do nucleotideo de numero ", indice-1)

entrada()