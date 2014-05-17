#! /usr/bin/python

# DAH should be three DOTs.
# Space between DOTs and DAHs should be one DOT.
# Space between two letters should be one DAH.
# Space between two words should be DOT DAH DAH.

import time
import RPi.GPIO as GPIO

DOT = 0.1 #.5 seconds 
DASH = 3 * DOT
SENTINAL = 6 * DOT

morsetab = {
        'A': '.-',              'a': '.-',
        'B': '-...',            'b': '-...',
        'C': '-.-.',            'c': '-.-.',
        'D': '-..',             'd': '-..',
        'E': '.',               'e': '.',
        'F': '..-.',            'f': '..-.',
        'G': '--.',             'g': '--.',
        'H': '....',            'h': '....',
        'I': '..',              'i': '..',
        'J': '.---',            'j': '.---',
        'K': '-.-',             'k': '-.-',
        'L': '.-..',            'l': '.-..',
        'M': '--',              'm': '--',
        'N': '-.',              'n': '-.',
        'O': '---',             'o': '---',
        'P': '.--.',            'p': '.--.',
        'Q': '--.-',            'q': '--.-',
        'R': '.-.',             'r': '.-.',
        'S': '...',             's': '...',
        'T': '-',               't': '-',
        'U': '..-',             'u': '..-',
        'V': '...-',            'v': '...-',
        'W': '.--',             'w': '.--',
        'X': '-..-',            'x': '-..-',
        'Y': '-.--',            'y': '-.--',
        'Z': '--..',            'z': '--..',
        '0': '-----',           ',': '--..--',
        '1': '.----',           '.': '.-.-.-',
        '2': '..---',           '?': '..--..',
        '3': '...--',           ';': '-.-.-.',
        '4': '....-',           ':': '---...',
        '5': '.....',           "'": '.----.',
        '6': '-....',           '-': '-....-',
        '7': '--...',           '/': '-..-.',
        '8': '---..',           '(': '-.--.-',
        '9': '----.',           ')': '-.--.-',
        ' ': ' ',               '_': '..--.-'
}

def main():
    print "Main"
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    code = morse("Hello")
    showSentinal()
    blink(code)
    showSentinal()
    GPIO.cleanup()

# Convert a string to morse code with \001 between the characters in
# the string.
def morse(line):
    print "morse "
    res = ''
    for c in line:
        try:
            res += morsetab[c] + '\001'
        except KeyError:
            pass
    return res

# Blink a line of morse code.
def blink(line):
    print "blink "
    for c in line:
        if c == '.':
            print "dot "
            GPIO.output(7,True)
            time.sleep(DOT)
        elif c == '-':
            print "dash "
            GPIO.output(7,True)
            time.sleep(DASH)
        else:                   # space
            print "space "
            GPIO.output(7,False)
            time.sleep(DOT*4)
        GPIO.output(7,False)
        time.sleep(DOT*3) #space between characters

# Display the sentinal value
def showSentinal():
    print "sentinal "
    GPIO.output(7,True)
    time.sleep(SENTINAL)    
    GPIO.output(7,False)


if __name__ == '__main__':
    main()
