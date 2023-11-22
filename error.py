import argparse
import os
import sys
import re

def searchposition(filename, string,errorline):
        file = open(filename, encoding="utf8")
        text = file.read()
        file.close()

        pos = 0
        line = 1

        while (pos < len(text)):
            if text[pos] == '\n':
                line += 1
            if string == 'e' and line == errorline:
                return pos+1
            if text[pos] == string and line == errorline :
                break

            pos +=1

        return pos

def printerror(filename, position, errorline):
    file = open(filename, encoding="utf8")
    text = file.read()
    file.close()

    pos = 0
    line = 1
    tokens = []

    while (pos < len(text)):
        if text[pos] == '\n':
            line += 1
        flag = None
        if line == errorline and pos == position:
            print(f'Error Expression at line {line}: {text[pos:].splitlines()[0]}')

        pos+=1