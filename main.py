from FileHandler import FileHandler
import regex as reg
import error as er
import argparse
import time
from colorama import Fore, Style
from pyfiglet import Figlet

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

# buat run tulis ini xnya ganti nama file apa aja bebas
#  python main.py pda.txt x.html

class PDA:
    def compute(self, inputString, parsedLines):
        line = 1
        initStackSymbol = parsedLines['initial_stack']
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
        print('{}\t {}\t {}\t ({}, {})'.format(currentState, '_', 'Z', currentStackSymbol, currentStackSymbol))
        for i in range(len(inputString)):
            ada = False
            if inputString[i]=='nextLine':
                line+=1
                prevchar = inputString[i]
            else:
                for production in productions:
                    if ((production[0] == currentState) and (production[1] == inputString[i]) and (production[2] == currentStackSymbol)):
                        currentState = production[3]
                        nextstack = production[4]
                        ada=True
                if(ada==True):
                    prevchar = inputString[i]
                    previousStackSymbol = currentStackSymbol
                    currentStackSymbol = nextstack
                    print('{}\t {}\t {}\t ({}, {})'.format(currentState, inputString[i], previousStackSymbol, previousStackSymbol, nextstack))
                    #time.sleep(2)
                else:
                    currentchar = inputString[i]
                    if(prevchar == currentchar):
                        currentchar = prevchar
                    if(prevchar=='nextLine' ):
                        line = line-1
                        inputString[i] = 'e'
                    break

            if i==(len(inputString)-1):
                end = True

        if end:
            if(currentStackSymbol.upper() in finalStates):
                accepted = True
        
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
    print(lexer)

    fh = FileHandler()
    pda = PDA()
    
    lines = fh.readFile(txt_filename)
    print('Reading Automata File')
    print('Automata File Successfully Read')
  
    print('Loading Details from Automata File: ')
    
    parsedLines = fh.parseFile(lines)
    print('States: ', parsedLines['states'])
    print('Input Symbols: ', parsedLines['input_symbols'])
    print('Stack Symbols: ', parsedLines['stack_symbols'])
    print('Initial State: ', parsedLines['initial_state'])
    print('Initial Stack Symbol: ', parsedLines['initial_stack'])
    print('Final States: ', parsedLines['final_states'])

    print('Details loaded')
    print('Computing the Transition Table:')

    accepted, line, currentchar = pda.compute(lexer, parsedLines)
    if not accepted:
        printfalse()
        position = er.searchposition(html_filename,currentchar,line)
        er.printerror(html_filename,position,line)
    else:
        printtrue()

if __name__ == '__main__':
    main()