def leArq(arquivo):
    dna=""
    f=open(arquivo,"r")
    linhas=f.readlines()
    for linha in linhas:
        linha=linha.strip()
        dna+=linha
    return dna
contA=0
contC=0
contT=0
contG=0
dna=leArq('content/rosalind_dna (2).txt')
for l in dna: 
    if(l=='A'):
        contA += 1
    elif(l=='T'):
        contT+=1
    elif(l=='C'):
        contC+=1
    elif(l=='G'):
        contG+=1
print("{} {} {} {}".format(contA,contC,contG,contT))