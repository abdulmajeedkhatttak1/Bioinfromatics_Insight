#**************************************Take a rnadom DNA sequence****************************** 

dna_sequence = "ATCGATCAGATCAGATACAGAT"

# T_to_U = dna_sequence.replace("T","U")

# print(T_to_U)

# ***************************Output of the above Code is given Below**************************
"""
AUCGAUCAGAUCAGAUACAGAU

"""

dna_sequence = "ATCGATCAGATCAGATACAGAT"

rna_sequence = ""

for necleotide in dna_sequence:
    if necleotide=="T":
        necleotide.replace("T","U")
        rna_sequence+="U"
        
    else:
        rna_sequence += necleotide
        
print(rna_sequence)

# ***************************Output of the above Code is given Below**************************
"""

AUCGAUCAGAUCAGAUACAGAU

"""
"""


Q: I would like to hear your suggestions — how can we perform this type of T-to-U nucleotide replacement 
using a while loop or any alternative method or logic you recommend?

"""