# Module for Basic DNA analysis
## Notes:
### seq_filename = file containing a DNA sequence, nothing else
### seq = a str sequence of DNA
### nuc = str nucleotide of interest, e.g., 'A'

def read_seq_from_file(seq_filename):
    seq_file = open(seq_filename)
    dna_seq = ''.join(seq_file.read().split()).upper()
    seq_file.close()
    return dna_seq


## Manipulate the Sequence
def reverse(seq):
    return ''.join(reversed(seq))

def complement(seq):
    d = {'A':'T','C':'G','G':'C','T':'A'}
    return ''.join(map(d.get,seq))

def reverseComplement(seq):
    return ''.join(reversed(complement(seq)))


## Get info from Sequence
def length(seq):
    return len(seq)

def freq(seq,nuc):
    return seq.count(nuc)

def percentGC(seq):
    gccount = freq(seq,'C') + freq(seq, 'G')
    return 100*float(gccount)/length(seq)

def palindrome(seq):
    halfn = length(seq) // 2
    first_half = seq[:halfn]
    second_half = seq[-halfn:]
    rcpal = False
    if first_half == reverse(second_half):
        rcpal = True
    return rcpal

def rc_palindrome(seq):
    halfn = length(seq)//2
    first_half = seq[:halfn]
    second_half = seq[-halfn:]
    rcpal = False
    if first_half == reverseComplement(second_half):
        rcpal = True
    return rcpal
