import sys
import DNAstuff as dna

file = sys.argv[1] # file containing a DNA sequence, nothing else

# Read and print sequence from file
seq = dna.read_seq_from_file(file)
print('DNA Sequence read from file:', seq)


# Manipulate the Sequence
print('\n\nSEQUENCE MANIPULATION\n')
## print reverse of the sequence
print('Reverse Sequence:', dna.reverse(seq))

## print complement of sequence
print('Complement Sequence:', dna.complement(seq))

## print reverse complement of sequence
print('Reverse Complement of Sequence:', dna.reverseComplement(seq))


# Get info from Sequence
print('\n\nSEQUENCE INFORMATION\n')
## print length of sequence
print('Sequence length:', dna.length(seq))

## count number of specific nucleotides (e.g., 'A')
print("Number of A's:", dna.freq(seq,'A'))

## get the GC percentage of a sequence
print('GC percentage:', dna.percentGC(seq))

## is it a palindrome? (True or False) (e.g., ATGCCGTA is a palindrome)
print('Is a palindrome:', dna.palindrome(seq))

## is it a reverse palidrome? (True or False) (e.g., ATGCGCAT is a reverse palindrome)
print('Is a reverse palindrome:', dna.rc_palindrome(seq))
