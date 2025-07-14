# ************************************** Random DNA Sequence *****************************************************

DNA_Seq = "ATCGATCACACATAGACAGTACAGATACGATACAGATCAGATNNNNNACAGATACAGTACAGATCAGATACNNNNNGATCAGCAGATCACGAGTACAGTACACAGTACAGTAGCACGA"
print(DNA_Seq)
print("DNA length : ", len(DNA_Seq))

# ************************************** Output below*************************************************************
"""
    ATCGATCACACATAGACAGTACAGATACGATACAGATCAGATACAGATACAGTACAGATCAGATACGATCAGCAGATCACGAGTACAGTACACAGTACAGTAGCACGA
    
"""
# **************************************** For Loop ****************************************************************
Adenine = []
Thymine = []
Cytosine = []
Guanine = []
NAN = []
for nucleotide in DNA_Seq:
    if nucleotide == "A":
        Adenine.append(nucleotide)
    elif nucleotide == "T":
        Thymine.append(nucleotide)
    elif nucleotide == "C":
        Cytosine.append(nucleotide)
    elif nucleotide == "G":
        Guanine.append(nucleotide)
    else:
        NAN.append(nucleotide)

# ********************************** Length of all nucleotide and NAN *****************************************
print("Length of Adenine : ", len(Adenine))
print("Length of Thymine : ", len(Thymine))
print("Length of Cytosine : ", len(Cytosine))
print("Length of Guanine : ", len(Guanine))
print("Length of NAN : ", len(NAN))

# ****************************** To Calculate Adenine_percentage *************************************************

Adenine_percentage = (len(Adenine)/len(DNA_Seq))*100
print("Adenine Percenatage : ", round((Adenine_percentage),2))

# ****************************** To Calculate Thymine_percentage *************************************************

Thymine_percentage = (len(Thymine)/len(DNA_Seq))*100
print("Thymine Percenatage : ", round((Thymine_percentage),2))

# ****************************** To Calculate Cytosine_percentage *************************************************

Cytosine_percentage = (len(Cytosine)/len(DNA_Seq))*100
print("Cytosine Percenatage : ", round((Cytosine_percentage),2))

# ****************************** To Calculate Guanine_percentage *************************************************

Guanine_percentage = (len(Guanine)/len(DNA_Seq))*100
print("Guanine Percenatage : ", round((Guanine_percentage),2))

# ****************************** To Calculate NAN_percentage *************************************************
NAN_percentage = (len(NAN)/len(DNA_Seq))*100
print("NAN Percenatage : ", round((NAN_percentage),2))

# ****************************** To Calculate Total_percentage of Nucleotide *************************************************
Total_Percentge = (Adenine_percentage+Thymine_percentage+Cytosine_percentage+Guanine_percentage+NAN_percentage)
print("Total percentage of A, T, C, G and NAN : ", Total_Percentge) 


"""

Q: Find the percentage of GC, AT, GT, CT, AG and AC etc?

"""