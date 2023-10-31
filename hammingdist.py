# collects user input for DNA sequences & converts them to lists for analysis
dna1 = input("Enter a DNA seq: ")
dna2 = input("Enter another DNA seq: ")
dna1 = list(dna1)
dna2 = list(dna2)

# counter vars: i = iterates through base pairs; muts = counter for point mutations
i = 0
muts = 0

"""
For any genome that has 10 million Gbp or less, iterates through the genomes, comparing them element-by-element, and checks for mutations
"""
for i in range(10000000000000000):
  try:
    if dna1[i] != dna2[i]:
      muts += 1
      i += 1
    else:
      i += 1
  except Exception:
    pass

print(muts)
