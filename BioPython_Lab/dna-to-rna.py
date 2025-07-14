# ************************import Seq Class from Bio.Seq module in the Biopython Library**********************************
from Bio.Seq import Seq

# Create Random DNA completely Divided by 3
DNA = Seq("ATGGTCAGTACAGTA")
print("DNA : ", DNA)
print("Length of DNA : ", len(DNA))                    # Length of DNA

# Transcribe DNA to RNA 
RNA = DNA.transcribe()
print("RNA : ", RNA)
print("Length of RNA : ", len(RNA))                    # Length of DNA

# Translate RNA to Protein / Amino Acids
Protein = RNA.translate()
print("Protein (Amino Acids) : ", Protein)
