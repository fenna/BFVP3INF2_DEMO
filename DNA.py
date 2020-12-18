#!/usr/bin/env python3

"""Module with regular dna modifications"""

__author__ = 'fennaf'

import sys

def transcribe(dna):
    """
    return the dna string as rna string
    """
    return dna.replace('T', 'U')


def reverse(s):
    """
    reverse the sequence string in reverse order
    """
    letters = list(s)
    letters.reverse()
    return ''.join(letters)


def complement(s):
    """
    return the complementary sequence string
    """
    basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    letters = list(s)
    letters = [basecomplement[base] for base in letters]
    return ''.join(letters)


def codons(s):
    """
    returns codons from a list of dna string
    """
    end = len(s) - (len(s) % 3) - 1
    codons = [s[i:i+3] for i in range(0, end, 3)]
    return codons


def gc(s):
    """
    return the percentage of dna composed of G+C
    """
    gc = s.count('G') + s.count('C')
    return gc *100 / len(s)

def main(args):
    return 0


if __name__ == "__main__":
    exitcode = main(sys.argv)
    sys.exit(exitcode)
