#lendo arquivo .fasta
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

seq_usuario = list(input("Entre com a sequencia de nucleotideos:"))

for i in seq_usuario:
    if i != 'A' and i != 'C' and i != 'T' and i != 'G':
        print("Sequencia incorreta. Submeta apenas caracteres A, C, T e G.")

