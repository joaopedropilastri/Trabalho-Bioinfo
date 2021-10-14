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

def gerar_proteina(lista):
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
             palavra=''
             palavra=listaux[contaux-3]+ listaux[contaux-2]+ listaux[contaux-1]
             listaaux.append(palavra)
             listtemp=[]
             cont=0
             
    #correr os codons e decodificar em proteinas
    contador=0
    listaproteina=[]
    while (contador<=len(listaaux)):
        if(listaaux[contador]=='ATG'):
            listaproteina.append('Met')
        elif(listaaux[contador]=='TTA' or listaaux[contador]=='TTG' or listaaux[contador]=='CTT' or listaaux[contador]=='CTC' or listaaux[contador]=='CTA' or listaaux[contador]=='CTG'):
            listaproteina.append('Leu')
        elif(listaaux[contador]=='TTT' or listaaux[contador]=='TTC'):
            listaproteina.append('Phe')
        elif(listaaux[contador]=='ATT' or listaaux[contador]=='ATC' or listaaux[contador]=='ATA'):
            listaproteina.append('Ile')
        elif(listaaux[contador]=='GTT' or listaaux[contador]=='GTC' or listaaux[contador]=='GTA' or listaaux[contador]=='GTG'):
            listaproteina.append('Val')
        elif(listaaux[contador]=='TCT' or listaaux[contador]=='AGT' or listaaux[contador]=='AGC' or listaaux[contador]=='TCC' or listaaux[contador]=='TCA' or listaaux[contador]=='TCG'):
            listaproteina.append('Ser')
        elif(listaaux[contador]=='CCT' or listaaux[contador]=='CCC' or listaaux[contador]=='CCA' or listaaux[contador]=='CCG'):
            listaproteina.append('Pro')
        elif(listaaux[contador]=='ACT' or listaaux[contador]=='ACC' or listaaux[contador]=='ACA' or listaaux[contador]=='ACG'):
            listaproteina.append('Thr')
        elif(listaaux[contador]=='GCT' or listaaux[contador]=='GCC' or listaaux[contador]=='GCA' or listaaux[contador]=='GCG'):
            listaproteina.append('Ala')
        elif(listaaux[contador]=='TAT' or listaaux[contador]=='TAC'):
            listaproteina.append('Tyr')
        elif(listaaux[contador]=='CAT' or listaaux[contador]=='CAC'):
            listaproteina.append('His')
        elif(listaaux[contador]=='CAA' or listaaux[contador]=='CAG'):
            listaproteina.append('Gln')
        elif(listaaux[contador]=='AAT' or listaaux[contador]=='AAC'):
            listaproteina.append('Asn')
        elif(listaaux[contador]=='AAA' or listaaux[contador]=='AAG'):
            listaproteina.append('Lys')
        elif(listaaux[contador]=='GAT' or listaaux[contador]=='GAC'):
            listaproteina.append('Asp')
        elif(listaaux[contador]=='GAA' or listaaux[contador]=='GAG'):
            listaproteina.append('Glu')
        elif(listaaux[contador]=='TGT' or listaaux[contador]=='TGC'):
            listaproteina.append('Cys')
        elif(listaaux[contador]=='TGG'):
            listaproteina.append('Trp')
        elif(listaaux[contador]=='CGT' or listaaux[contador]=='CGC' or listaaux[contador]=='CGA' or listaaux[contador]=='CGG' or listaaux[contador]=='AGA' or listaaux[contador]=='AGG'):
            listaproteina.append('Arg')
        elif(listaaux[contador]=='GGT' or listaaux[contador]=='GGC' or listaaux[contador]=='GGA' or listaaux[contador]=='GGG'):
            listaproteina.append('Gly')
        elif(listaaux[contador]=='TAA' or listaaux[contador]=='TAG' or listaaux[contador]=='TGA'):
            break
        contador=contador+1

    return listaproteina

#1. Comparar a sequência de nucleotídeos com a sequência de Wuhan;
#2. Comparar a sequenciado proteica com a sequência de Wuhan;
#3. Mostrar as principais alterações (qual nucleotídeo / aminoácido foi substituído e qual a posição / index da substituição)

gene_wuhan = ler_fasta("gene_S_Whuhan.fasta")
gene_brazil = ler_fasta("gene_S_Brazil.fasta")

proteina_brazil = gerar_proteina(gene_brazil)
proteina_wuhan = gerar_proteina(gene_wuhan)

gene_brazil = str(gene_brazil)
gene_wuhan = str(gene_wuhan)

nucleotideos = min(len(gene_wuhan), len(gene_brazil))

print("COMPARAÇÃO DE SEQUÊNCIA DE NUCLEOTÍDEOS")

for nucleotideo in range (nucleotideos):
    if (gene_brazil[nucleotideo] != gene_wuhan[nucleotideo]):
            print("Diferença na posição de nucleotídeo ", nucleotideo, ": Troca de ", gene_wuhan[nucleotideo] , " por " , gene_brazil[nucleotideo])

aminoacidos = min(len(proteina_brazil), len(proteina_wuhan))

print("COMPARAÇÃO DE SEQUÊNCIA PROTEICA")

for aminoacido in range (aminoacidos):
    if (proteina_brazil[aminoacido] != proteina_wuhan[aminoacido]):
            print("Diferença na posição de aminoácido ", aminoacido, ": Troca de ", proteina_wuhan[aminoacido] , " por " , proteina_brazil[aminoacido])
