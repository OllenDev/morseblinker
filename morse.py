#! /usr/bin/python

# DAH should be three DOTs.
# Space between DOTs and DAHs should be one DOT.
# Space between two letters should be one DAH.
# Space between two words should be DOT DAH DAH.

import time
import RPi.GPIO as GPIO

DOT = 0.5 #.5 seconds 
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
    res = ''
    for c in line:
        try:
            res += morsetab[c] + '\001'
        except KeyError:
            pass
    return res

# Blink a line of morse code.
def blink(line):
    for c in line:
        if c == '.':
            GPIO.output(7,True)
            time(DOT)
        elif c == '-':
            GPIO.output(7,True)
            time(DASH)
        else:                   # space
            GPIO.output(7,False)
            time(DOT*4)
        GPIO.output(7,False)
        time(DOT*3) #space between characters

# Display the sentinal value
def showSentinal()
    GPIO.output(7,True)
    time(SENTINAL)    
    GPIO.output(7,True)


if __name__ == '__main__':
    main()