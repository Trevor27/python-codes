# this program cocsists of functions that perform/solve a problem known as sequence alignment
# SickleCellDisease


aminoAcids = {          # Dictionary to hold mapping of DNA codons and their corresponding Amino acids (DNA codon: SLC)
    "ATT": "I",     
    "ATC": "I",
    "ATA": "I",

    "CTT": "L",
    "CTC": "L",
    "CTA": "L",
    "CTG": "L",
    "TTA": "L",
    "TTG": "L",

    "GTT": "V",
    "GTC": "V",
    "GTA": "V",
    "GTG": "V",

    "TTI": "P",
    "TTC": "P",

    "ATG": "M",
    }


# This function takes a DNA sequence from user input and outputs the amino acid sequence
def translate(DNA):
    DNA = DNA.upper()
    slc = ""
    if (len(DNA) == 0):
        
        return ""
    if (len(DNA) % 3 != 0):
        noOfchars = 3 - (len(DNA) % 3)      # If DNA isn't divisible by 3, add extra characters ("X")
        count = 0
        for i in range (0, noOfchars):
            DNA += "X"
       
    for i in range(0,len(DNA),3):       # DNA will be split into groups of 3 characters
        listDna = [DNA[i:i+3]]
            
        for j in listDna:
            slc += aminoAcids.get(j,"X")

    return slc

          
DNA = input("Enter DNA: ")
print(translate(DNA))


#************************** Task 2 ******************************


# this function reads the contents of text files then identifies the first occurence of lowercase letter 'a'
# then corrects sequences according to normal DNA and mutated DNA
def mutate():    
    lines = open('DNA.txt','r')
    normal = ""
    mutated = ""
    for word in lines.readlines():
        myword = ""
        for char in word:            
            if char == 'a':
                normal += "A"
                mutated += "T"
            else:
                normal += char
                mutated += char              

    file1 = open("normalDNA.txt","w")
    file1.write(normal)
    file1.close
    file1 = open("mutatedDNA.txt","w")
    file1.write(mutated)
    file1.close
            
                       
mutate()

print("\n")


# this function calls on the translate function to take text files input
# calling the translate function on both (normalDNA.txt and mutatedDNA), and output both amino acids to the user
def txtTranslate():
    
    file2 = open ('normalDNA.txt', 'r')
    if file2.mode == 'r':
        lines = file2.read()
        operation1 = translate(lines)
        print('Normal DNA: Amino acid sequence'+ '\n' + operation1)
        
    print("\n")        

    file3 = open('mutatedDNA.txt', 'r')
    if file2.mode == 'r':
        lines = file3.read()
        operation2 = translate(lines)
        print('Mutated DNA: Amino acid sequence'+ '\n' + operation2)

txtTranslate()




