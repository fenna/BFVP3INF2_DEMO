#!/usr/bin/env python3

"""
module to demonstrate sys.argv
        usage: demo_sys.py arg1 arg2 ...argn
"""

__author__ = "fennaf"

## CODE
# Imports.
import sys

def arg_info(args):
  print("This is the name of the script: ", args[0])
  print("These are the arguments", args[1:])
  print("Number of arguments: ", len(args))
  print("The arguments are: " , str(args))
  return 0

def main(args):
    if len(args) < 2:
        print("please enter an argument")
    else:
      arg_info(args)
    return 0

if __name__ == "__main__":
    exitcode = main(sys.argv)
    sys.exit(exitcode)
