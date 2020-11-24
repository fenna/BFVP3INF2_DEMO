#!/usr/bin/env python3

"""
program shows turtle following sinuswave
"""

__author__ = "F.Feenstra"

## CODE

#IMPORTS
import numpy as np
import sys
import turtle

#CONSTANTS
MARGE = 10
SCREEN = turtle.Screen()
SAMPLE_RATE = int(SCREEN.window_width()/2 -MARGE) - int(MARGE - SCREEN.window_width()/2)
AMPLITUDE = SCREEN.window_height()/4
PHASE = 0
FREQUENCY = 2

#FUNCTIONS

def comp_y(t):
    """compute the y value of the sin wave at the for a specific sample"""
    y_t = AMPLITUDE * np.sin(2 * np.pi * FREQUENCY * (t/SAMPLE_RATE) + PHASE)
    return y_t


def comp_amplitude(x):
    """compute the y value of the sin wave at the for each sample"""
    y = []
    for t in x:
        y.append(comp_y(t))
    return y


def turtle_wave(start, y):
    """Draw a turtle and move it over the sinewave, starting at _start_"""
    dude = turtle.Turtle(shape="turtle", visible=False)
    dude.penup()
    i = start
    for j in range(0, SAMPLE_RATE):
        pos = dude.pos()
        dude.setheading(np.arctan2(y[j]-pos[1], i-pos[0]) * 180 / np.pi)
        dude.goto(i, y[j])
        if i == start:
            dude.pendown()
            dude.showturtle()
        i +=1
    dude.hideturtle()
    return

def turtle_wave_back(end, y):
    """Draw a turtle and move it backwards over the sinewave, from _end_ to _start_"""
    dude = turtle.Turtle(shape="turtle", visible=False)
    dude.penup()
    i = end
    for j in range(SAMPLE_RATE-1, 0, -1):
        pos = dude.pos()
        dude.setheading(np.arctan2(y[j]-pos[1], i-pos[0]) * 180 / np.pi)
        dude.goto(i, y[j])
        if i == end:
            dude.pendown()
            dude.showturtle()
        i -=1
    return


def main():
    """Main function to calculate sine wave and draw turtle"""
    start = int(MARGE - SCREEN.window_width()/2)
    end = int(SCREEN.window_width()/2 - MARGE)
    x = np.arange(start, end) # the points on the x axis for plotting
    y = comp_amplitude(x) # the points on the y axis for plotting
    turtle_wave(start, y)
    turtle_wave_back(end, y)
    return 0


if __name__ == '__main__':
    exitcode = main()
    sys.exit(exitcode)
