#!/usr/bin/env python3

"""
Draw a sierpinski triangle using turtle graphics
"""

__author__ = "Tsjerk A. Wassenaar"


import sys
import turtle


def l_system(depth, axiom, **rules):
    """Generate L-system from axiom using rules, up to given depth"""

    if not depth:
        return axiom
    
    # Basic, most straight-forward implementation
    # Note 1: it doesn't matter if axiom is a string or a list
    # Note 2: consider the difference between .extend() and .append()
    out = []
    for char in axiom:
        if char in rules:
            out.extend(rules[char])
        else:
            out.append(char)
    
    return l_system(depth - 1, out, **rules)


def plant1(depth):
    #return l_system(depth, 'X', X='F-[[X]+X]+F[+|FX]-X', F='FF')
    return l_system(depth, 'X', X='F[-X][X]F[-X]+FX', F='FF')


def actions(step=5, angle=90):
    """Return dictionary with control functions for L-system"""

    stack = []

    def forward(turt):
        turt.forward(step)

    def right(turt):
        turt.right(angle)

    def left(turt):
        turt.left(angle)

    def push(turt):
        stack.append((turt.pos(), turt.heading()))

    def pop(turt):
        pos, heading = stack.pop()
        turt.penup()
        turt.setheading(heading)
        turt.goto(pos)
        turt.pendown()

    def turn(turt):
        turt.right(180)

    return {'F': forward, 'f': forward, 
            '+': right, '-': left, 
            '[': push, ']': pop, '|': turn}


def main(args):
    """Main function"""
    
    # Preparation
    don = turtle.Turtle(shape="turtle")
    don.speed(0)
    don.penup()
    don.goto((0,-250))
    don.left(90)
    don.pendown()
    actdict = actions(step=5, angle=25)

    # Work
    for char in plant1(6):
        if char in actdict:
            actdict[char](don)

    # Finish
    input('Press any key to continue')

    return 0


if __name__ == "__main__":
    excode = main(sys.argv)
    sys.exit(excode)


