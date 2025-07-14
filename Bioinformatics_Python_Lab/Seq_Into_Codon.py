"""
Bioinformatics Script: Sequence Input or Generation

This script allows the user to either input a custom DNA/RNA sequence for further analysis.
such as DNA/RNA sequence into codon 
lets Perform it.

"""

DNA_Seq = "ATCGATACAGTAAGGATCAGATCAGATA"
# first print the DNA_Seq
print(DNA_Seq)  # ATCGATACAGTAAGGATCAGATCAGATA

# find length of DNA_Seq
print("length of DNA_Seq : ", len(DNA_Seq))

# NOW python loop can help us to change sequence into codon

# **********************************For Loop********************************************

for nucleotide in range(0, len(DNA_Seq), 3):
    codon = DNA_Seq[nucleotide:nucleotide+3]
    print(codon)

# **********************************output of For Loop********************************************
"""
ATCGATACAGTAAGGATCAGATCAGATA
length of DNA_Seq :  28
ATC
GAT
ACA
GTA
AGG
ATC
AGA
TCA
GAT
A
"""   
    
# **********************************While Loop******************************************************


nucleotide = 0
while nucleotide <= len(DNA_Seq):
    codon = DNA_Seq[nucleotide:nucleotide+3]
    print(codon)
    nucleotide+=3
    
# **********************************output of While Loop********************************************    
"""
ATC
GAT
ACA
GTA
AGG
ATC
AGA
TCA
GAT
A
"""

# *********************************** Answer Below Question ****************************************
"""
Q: In the current code, the output includes a remaining single nucleotide (e.g., 'A') at the end when the total length
isn't divisible by 3. How can you modify the code to ensure the output consists of only complete codons (triplets), 
with no leftover nucleotides?
"""