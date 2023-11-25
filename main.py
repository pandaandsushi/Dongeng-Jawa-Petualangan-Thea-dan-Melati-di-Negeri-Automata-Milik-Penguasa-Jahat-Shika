from openfile import FileHandler
import regex as reg
import error as er
import argparse
import time
from colorama import Fore, Style
from pyfiglet import Figlet
import os

def printopening():
    custom_fig = Figlet(font='starwars') 
    logo_text = custom_fig.renderText('SUGENG RAWUH')

    print(Fore.YELLOW)
    print(logo_text)
    print(Style.RESET_ALL)

def printtrue():
    custom_fig = Figlet(font='starwars') 
    logo_text = custom_fig.renderText('SELAMET WES BENER')

    print(Fore.GREEN)
    print(logo_text)
    print(Style.RESET_ALL)

def printfalse():
    custom_fig = Figlet(font='starwars') 
    logo_text = custom_fig.renderText('WADUH SALAH')

    print(Fore.RED)
    print(logo_text)
    print(Style.RESET_ALL)
    print("Syntax Error")


class PDA:
    def __init__(self):
        self.stack = []

    def compute(self, inputString, parsedLines):
        line = 1
        initStackSymbol = parsedLines['initial_stack']
        self.stack.append(initStackSymbol)
        finalStates = parsedLines['final_states']
        initialState = parsedLines['initial_state']
        productions = parsedLines['productions']

        accepted = False
        
        currentchar = ''
        prevchar = ''
        currentStackSymbol = initStackSymbol
        currentState = initialState
        nextstack=initStackSymbol
        end = False

        print('State\tInput\tStack\tMove')
        print('{}\t {}\t {}\t ({}, {})'.format(currentState, '_', 'Z', currentStackSymbol, self.stack))
        for i in range(len(inputString)):
            ada = False
            if inputString[i]=='nextLine':
                line+=1
                prevchar = inputString[i]
            else:
                for production in productions:
                    if ((production[0] == currentState) and (production[1] == inputString[i]) and (production[2] == currentStackSymbol)):
                        currentState = production[3]
                        ada = True
                        if(len(production[4]) > 1):
                            self.stack.append(inputString[i])
                        elif ((production[4] == 'e') and (len(self.stack) != 1)):
                            self.stack.pop()
                            break
                        break
                if(ada==True):
                    previousStackSymbol = currentStackSymbol
                    currentStackSymbol = self.stack[len(self.stack)-1]
                    print('{}\t {}\t {}\t ({}, {})'.format(currentState, inputString[i], previousStackSymbol, currentStackSymbol, self.stack))
                else:
                    currentchar = inputString[i]
                    if(prevchar == currentchar):
                        currentchar = prevchar
                    if(prevchar=='nextLine'):
                        inputString[i] = 'e'
                
                    term_size = os.get_terminal_size()
                    print('=' * term_size.columns)
                    break

            if i==(len(inputString)-1):
                end = True

        if end:
            if(currentState in finalStates):
                accepted = True
            print("\n")
            term_size = os.get_terminal_size()
            print('=' * term_size.columns)
        
        return accepted, line, currentchar

def main():
    print('Pada suatu hari....')
    time.sleep(1)
    print('Thea dan Melati membuat sebuah program HTML untuk mengalahkan sang penguasa jahat Shika')
    time.sleep(1)
    print('Akankah mereka akan menang??')
    printopening()

    parser = argparse.ArgumentParser()
    parser.add_argument('txt_file', type=str)
    parser.add_argument('html_file', type=str)
    args = parser.parse_args()

    html_filename = 'test/' + args.html_file
    txt_filename = args.txt_file

    lexer = reg.createToken(html_filename)

    fh = FileHandler()
    pda = PDA()
    
    lines = fh.readFile(txt_filename)
  
    parsedLines = fh.parseFile(lines)
    term_size = os.get_terminal_size()
    print('=' * term_size.columns)

    print('PUSH DOWN AUTOMATA PROCESSES\n')
    
    print('States: ', parsedLines['states'])
    print('Input Symbols: ', parsedLines['input_symbols'])
    print('Stack Symbols: ', parsedLines['stack_symbols'])
    print('Initial State: ', parsedLines['initial_state'])
    print('Initial Stack Symbol: ', parsedLines['initial_stack'])
    print('Final States: ', parsedLines['final_states'])

    print('Push Down Automata Processes:')

    accepted, line, currentchar = pda.compute(lexer, parsedLines)
    if not accepted:
        printfalse()
        position = er.searchposition(html_filename,currentchar,line)
        er.printerror(html_filename,position,line)
    else:
        printtrue()
        print("Accepted")

if __name__ == '__main__':
    main()