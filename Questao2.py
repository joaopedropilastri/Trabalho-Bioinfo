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

# testando...
#codon inicio ATG, codon parada TAA, TAG, TGA
lista = ler_fasta("gene_S_Whuhan.fasta")
cont=0
for i in lista:     
    print(i)  
