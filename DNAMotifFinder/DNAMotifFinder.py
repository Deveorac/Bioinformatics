"""
Rosalind Project
Find all instances of a given motif in a DNA sequence. 
Programmed by Deveorac in 2019. 
"""

f = open("DNA_seq.txt", "r")
dna = f.read()

motif = input("Please enter desired motif: ")

positions = []

for i in range(len(dna)):
    if dna.startswith(motif, i):
        positions.append(i+1)
        
    
print(positions)