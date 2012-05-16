#!/usr/bin/python
#
# visual_arithmatic.py
# Written by Andrew Lin (dragoncoil@gmail.com), May 2012
#
# This work is licensed under the Creative Commons Attribution-ShareAlike 3.0
# Unported License. To view a copy of this license, visit
#   http://creativecommons.org/licenses/by-sa/3.0/
# or send a letter to
#   Creative Commons
#   444 Castro Street, Suite 900,
#   Mountain View, California, 94041, USA.
#
"""
Addition and subtraction with 'avocado' cheats on a command line interface (because
either I am doing a retro, old school thing, or I am too lazy to write a GUI).

For those that don't get the avocado reference, visit
   http://www.khanacademy.org/math/arithmetic/addition-subtraction/v/basic-addition
"""
import argparse
import random

def visualize( value ):
    """Number and avocados"""
    s = "%2d" % value # Only works well with 1- and 2-digit numbers right now.
    s += '\t'
    for i in range( value ):
        s += 'o '
        if ( i + 1 ) % 10 == 0:
            # Group sets of 10
            s += ' '
    return s

def addition( max ):
    """Addition with avocados."""
    x = random.randint( 0, max )
    y = random.randint( 0, max )
    while( True ):
        print( '  %s' % visualize( x ) )
        print( '+ %s' % visualize( y ) )
        print( '====' )
        sum = raw_input( '? ' )

        try:
            sum = int( sum )
        except ValueError:
            print( 'Try again.\n' )
            continue

        if x + y == sum:
            print( 'Correct!\n' )
            break
        else:
            print( 'Try again.\n' )

def subtraction( max ):
    """Subtraction with avocados."""
    x = random.randint( 0, max )
    y = random.randint( 0, x ) # No negative differences!
    while( True ):
        print( '  %s' % visualize( x ) )
        print( '- %s' % visualize( y ) )
        print( '====' )
        difference = raw_input( '? ' )

        try:
            difference = int( difference )
        except ValueError:
            print( 'Try again.\n' )
            continue

        if x - y == difference:
            print( 'Correct!\n' )
            break
        else:
            print( 'Try again.\n' )


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument( '--max', dest='max', default=10, type=int )
    parser.add_argument( '--count', dest='count', default=127, type=int )
    parser.add_argument( '--subtraction', dest='subtraction', action='store_true' )
    parser.add_argument( '--both', dest='both', action='store_true' )
    args = parser.parse_args()

    random.seed()

    for x in range( args.count ):
        if ( args.both and random.randint( 0, 1 ) ) or args.subtraction:
            subtraction( args.max )
        else:
            addition( args.max )
