def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if len(dna1) > len(dna2):
        return True
    else:
        return False

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    occur = 0
    for char in dna:
        if nucleotide in char:
            occur = occur + 1
    return occur
            

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    for char in dna1:
        if dna2 in dna1:
            return True
        else:
            return False
def is_valid_sequence(dna):
    ''' (str) -> bool
    return true if it dna contains only as chars A,T,C,G
    '''
    protein = 'A,T,C,G'
    count = 0
    for v in dna:
        for char in protein:
            if char in v:
                count = count + 1
    sequence = len(dna)-count
    if sequence > 0 :
        return False
    else:
        return True
def insert_sequence(dna1,dna2,index):
    ''' (str,str,int)--> int
    return the
    '''
    return dna1[:index] + dna2 + dna1[index:]
def get_complement(dna):
    '''(str)-->str
    '''
    if dna == 'A':
        return 'T'
    elif dna == 'G':
        return 'C'
    elif dna == 'T':
        return 'A'
    elif dna == 'C':
        return 'G'
def get_complementary_sequence(dna):
    """(str) -> str
    The parameter is a DNA sequence. Return the DNA sequence that is
    complementary to the given DNA sequence.
    For example, if you call this function with 'AT' as the argument,
    it should return 'TA'.
    get_complementary_sequence("AT")
    'TA'
    get_complementary_sequence("CG")
    'GC'
    get_complementary_sequence("ACGT")
    'TGCA'
    """
    SEQ = ''
    for char in dna:
        if 'A' in char:
            SEQ = SEQ +'T'
        elif 'G' in char:
            SEQ = SEQ + 'C'
        elif 'T' in char:
            SEQ = SEQ + 'A'
        elif 'C' in char:
            SEQ = SEQ + 'G'
        return SEQ
    

        


