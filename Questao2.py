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
listaux=[]
cont=0
contaux=0
contaux2=0
#cria uma lista auxiliar sem o \n 
for i in lista:
    while (contaux2<len(i)):
        if i[contaux2]!='\n':
            listaux.append(i[contaux2])
        contaux2=contaux2+1
#cria uma lista com os codons(trincas)
while (contaux<len(listaux)):
    cont=cont+1
    contaux=contaux+1
    if cont==3:
         listtemp=[]
         listtemp.append(listaux[contaux-3])
         listtemp.extend(listaux[contaux-2])
         listtemp.extend(listaux[contaux-1])
         listaaux.append(listtemp)
         listtemp=[]
         cont=0
#correr os codons e decodificar em proteinas
contador=0
listaproteina=[]
while (contador<len(listaaux)):
    if(listaaux[0]=='ATG'):
        listaproteina.append('Met')
        contador=contador+1
    else:
        print("sem codon de inicio")
    

print(listaaux)

