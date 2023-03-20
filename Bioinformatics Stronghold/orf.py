fast= open('fasta.txt','r') #Open the fasta file with the DNA strings
d={} #Create a dictionary to order the DNA strings with the ID as the key
content={} #Create a dictionary to load the GC content of each DNA string

#Create the dictionary with the ID and the string#
for line in fast:
    line=line.strip() #To eliminate the '\n' of the string.
    if '>' in line:
        id=str(line[10:]) #If the line is the ID of the fast, we save the ID to a variable
    else:
        try:
            d[id]=d[id]+line #Using the ID previously saved, we use it to create a new key in the dictionary, adding the line or lines with the sequences
        except:
            d[id]=line

#Add to the dictionary the reverse complement of the DNA string
dna=d[id]
nt=list(dna[::-1]) #Make a list with the reverse dna
rdna='' #Create a empty variable string to add the result
for i in nt:
    if i == 'A':
        rdna=rdna+'T'
    elif i == 'T':
        rdna=rdna+'A'
    elif i == 'G':
        rdna=rdna+'C'
    elif i == 'C':
        rdna=rdna+ 'G' #Change each nt into his pair (C<->G and A<->T)
rid='r'+id;d[rid]=rdna

#Transcribe DNA to RNA#
for key in d:
    nucleotide=list(d[key])
    rna= '' #Create an empty string variable to create the RNA sequence
    for i in nucleotide:
        if i == 'T': #Each 'T' of the string will be changed into U
            rna=rna +'U'
        elif i in ['A','G','C']: #The other ones will remain the same
            rna=rna + i
    d[key]=rna
#Search the Open Reading Frames in both directions#
orf=1
rnaprot={}
for key in d:
    string=d[key]
    for num in range(0,len(string)):
        codon=str(string[num:num+3])
        if codon == 'AUG':
            substr=''
            for i in range(num,len(string),3):
                aa=str(string[i:i+3])
                substr=substr+aa
                if aa in ['UAG','UGA','UAA']:
                    rnaprot[orf]=substr
                    orf=orf+1
                    break

 #Translate the ORFs into protein#
codontab ={"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
       "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
       "UAU":"Y", "UAC":"Y", "UAA":"", "UAG":"",
       "UGU":"C", "UGC":"C", "UGA":"", "UGG":"W",
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
protein={}
search=list()
for key in rnaprot:
    peptide=''
    rna=rnaprot[key]
    for i in range(0,len(rna),3): 
        codon=str(rna[i:i+3]) #Code a for loop with a step of three nts and save in a variable the codon
        peptide= peptide+codontab[codon] #Search in the codon tab the codon saved and add the aa in the prptide string
    if peptide not in search:
        protein[key]=peptide
        search.append(peptide)

#Create the output to obtain the protein strings#  
for key in protein:
    print(protein[key])
