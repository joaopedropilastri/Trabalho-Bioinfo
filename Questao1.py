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

# finalizada
lista = ler_fasta("gene_S_Whuhan.fasta")

def contacg(lista):
    QCG=0
    for i in lista:   
        print(i)  
    QG=i.count('G')
    QC=i.count('C')
    PC=(QC*100)/len(i)
    PG=(QG*100)/len(i)
    print('Porcentagem de G: ', PG,'%')
    print('Porcentagem de C: ', PC,'%')
    
contacg(lista)