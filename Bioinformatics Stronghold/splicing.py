fast=open('fasta.txt','r')
d={}
control=0
stringid=''

#Create a dictionary with the principal string and the substrings#
for line in fast:
    line=line.strip() #To eliminate the '\n' of the string.
    if '>' in line:
        id=str(line[10:14]) #If the line is the ID of the fast, we save the ID to a variable
        if stringid=='':
            stringid=id   
    else:
        try:
            d[id]=d[id]+line #Using the ID previously saved, we use it to create a new key in the dictionary, adding the line or lines with the sequences
        except:
            d[id]=line

#Delete the sequences of the substring in the principal string to obtain the DNA spliced#
splicing=d[stringid]
for substr in d:
    if substr !=stringid:
        search=splicing.find(d[substr])
        splicing=splicing.replace(d[substr],'')
print(splicing)

#Trancribe the DNA exons using a code similar in the exercise 2#
nucleotide=list(splicing)
rna= '' #Create an empty string variable to create the RNA sequence
for i in nucleotide:
    if i == 'T': #Each 'T' of the string will be changed into U
        rna=rna +'U'
    elif i in ['A','G','C']: #The other ones will remain the same
        rna=rna + i
print(rna)

#Translate the RNA using the codon table (exercise 5)
peptide=''
codontab ={"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
       "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
       "UAU":"Y", "UAC":"Y", "UAA":"*", "UAG":"*",
       "UGU":"C", "UGC":"C", "UGA":"*", "UGG":"W",
       "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
       "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
       "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
       "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
       "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
       "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
       "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
       "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
       "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
       "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
       "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
       "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",} #Add the codon table in a dictionary
for i in range(0,len(rna),3): 
    codon=str(rna[i:i+3]) #Code a for loop with a step of three nts and save in a variable the codon
    try:
         peptide= peptide+codontab[codon] #Search in the codon tab the codon saved and add the aa in the prptide string
    except:
         break #Incase the variable codon have less than three nts, then it doesn't exist an aa in the codon table.
print(peptide)