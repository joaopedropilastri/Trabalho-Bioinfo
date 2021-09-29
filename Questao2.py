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
listaaux=[]
cont=0
contaux=0
for i in lista:     
    while (contaux<len(i)):
        cont=cont+1
        contaux=contaux+1
        if cont==3:
            listtemp=[]
            listtemp.append(i[contaux-3])
            listtemp.extend(i[contaux-2])
            listtemp.extend(i[contaux-1])
            listaaux.append(listtemp)
            listtemp=[]
            cont=0
        
print(listaaux)

