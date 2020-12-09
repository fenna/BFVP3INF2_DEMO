#!/usr/bin/env python3

"""
    This demonstrates some error handling. Most appropiate way is to
    demonstrate in pycharm and run the code so that you can see the exit status
    usage: uncomment in main a call to a function to demonstrate the function
"""

__author__ = 'Fenna Feenstra'
__version__ = '0.1'


#imports
import sys

#functions
def fire_error():
    """
    This function uses each element of the list as a divider
    and uses exception handling to catch type and zero division errors
    """
    l = [2,1,3,2,4,"foo",3,4,0,5]
    errors = 0
    for n in l:
        try:
            print('{}'.format(1/n))
        except (ZeroDivisionError, TypeError) as e:
            print("{} ({}): cannot divide 1 by '{}'".format(type(e).__name__, e.args[0], n))
            errors += 1
        finally:
            print('result of: 1/{}'.format(n))

    print('\n', '# error\'s: {}'.format(errors))


def demo_file_error(filename):
    """
        this function demonstrates different ways of error handling 
        in case of an file not found error. uncomment to see the effect
        
    """
    try:
        f = open(filename, 'r')
        f.read()
        f.close()
    except FileNotFoundError as e:
        print("{} ({}): cannot find file '{}'".format(type(e).__name__, e.args[0], filename))
        #sys.exit("cannot find file: " + filename)
        #raise Exception("cannot find file: " + filename)
    finally:
        print("this was the demo file error for {}".format(filename))


def demo_with():
    """
    this function demonstrates how to read a file 
    using with statement
    """
    poem = 'Piet die kon niet dichten daarom dicht de file zichzelf'
    with open('SintNiclaas.txt', 'w') as f_out:
        f_out.write(poem)
    try:
        with open('SintNicaas.txt', 'r') as f:
            print(f.readlines())
    except:
        print('oops')


def input2output(input, output):
    """
    this function demonstrates with as input and output handling
    """
    try:
        with open(input, "r") as inp, open(output, "w") as out:
            out.write(inp.read())
    except IOError as e:
        print('{} ({})'.format(type(e).__name__, e.args[0]))
    finally:
        print('process ended')



def main():
    pass
    #fire_error()
    demo_file_error("wtf.txt")
    #demo_with()
    #input2output('inputfile', 'outputfile')

if __name__ == "__main__":
    sys.exit(main())
