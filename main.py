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
#  python main.py test/x.html

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
                    if(prevchar=='nextLine'):
                        line = line-1
                        inputString[i] = 'e'
                    break

                if i==len(inputString)-1:
                    end = True

        if(currentStackSymbol in finalStates and end):
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
    parser.add_argument('file', type=argparse.FileType('r'))
    args = parser.parse_args()
    filename = args.file.name

    lexer = reg.createToken(filename)
    print(lexer)
    fh = FileHandler()
    pda = PDA()
    lines = fh.readFile('pda.txt')
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
    print('Productions List:')
    for production in parsedLines['productions']:
        print('\t', production)

    print('Details loaded')
    print('Computing the Transition Table:')

    accepted, line, currentchar = pda.compute(lexer, parsedLines)
    if not accepted:
        printfalse()
        position = er.searchposition(filename,currentchar,line)
        er.printerror(filename,position,line)
    else:
        printtrue()

if __name__ == '__main__':
    main()