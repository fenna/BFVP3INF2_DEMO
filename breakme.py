#!usr/bin/#!/usr/bin/env python3

__author__ = 'fennaf'

''' Program that generate errors '''
#There should be 12 other errors in the list from assignment 1 that
#you should be able to understand. Select 10 errors and write a program
#or small programs in which your code causes those. If you can isolate
#the code in a function (like ZeroDivisionError) do that and don't call
#the function. Otherwise write and test the code and then make it a comment block.
#You are allowed to discuss (calmly) and you can browse the internet to
#find more background and maybe examples of error raising code.
import sys
import math


def index_error():
    l = ["there", "are", "four", "elements"]
    return (l[4])


def zero_division_error():
    return 2/0


def type_error():
    return 1 + "2"


def file_not_found_error(file):
    f = open(file)
    f.close()
    return 0


def attribute_error():
    f = open('data/BRCA1.pdb')
    f.next()
    f.close()
    return 0


def key_error():
    dict = {'C': 'cake', 'T': 'thee'}
    return dict['K']


def name_error():
    return b


def module_error():
    import nonsense
    return 0


def math_error():
    return math.sqrt(-4)


def recursion_error(**a):
    return recursion_error()


def main(args):
    err = index_error()
    #err = zero_division_error()
    #err = type_error()
    #file_not_found_error('RTFM')
    #err = attribute_error()
    #err = module_error()
    #err = key_error()
    #err = name_error()
    #err = math_error()
    #err = recursion_error(a='what',b='duh')
    return 0


if __name__ == '__main__':
    exitcode=(main(sys.argv))
    sys.exit(exitcode)
