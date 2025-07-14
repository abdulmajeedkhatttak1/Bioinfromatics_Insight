#**************************************Take a rnadom RNA sequence****************************** 

rna_sequence = "AUCGAUCAGAUCAGAUACAGAU"

U_to_T = rna_sequence.replace("U","T")

print(U_to_T)

# ***************************Output of the above Code is given Below**************************
"""
ATCGATCAGATCAGATACAGAT

"""
# ********************************************************************************************

rna_sequence = "AUCGAUCAGAUCAGAUACAGAU" 

dna_sequence = ""

for necleotide in rna_sequence:
    if necleotide=="U":
        necleotide.replace("U","T")
        dna_sequence+="T"
        
    else:
        dna_sequence += necleotide
        
print(dna_sequence)

# ***************************Output of the above Code is given Below**************************
"""

ATCGATCAGATCAGATACAGAT

"""


"""

Q: I would like to hear your suggestions — how can we perform this type of U-to-T nucleotide replacement 
using a while loop or any alternative method or logic you recommend?

"""