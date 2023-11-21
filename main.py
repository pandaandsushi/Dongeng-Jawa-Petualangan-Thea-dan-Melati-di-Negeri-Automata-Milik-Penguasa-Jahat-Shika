from FileHandler import FileHandler
import regex as reg
import error as er
import argparse
import time
from colorama import Fore, Style

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

        print('State\tInput\tStack\tMove')
        print('{}\t {}\t {}\t ({}, {})'.format(currentState, '_', 'Z', currentStackSymbol, currentStackSymbol))
        for char in inputString:
            ada = False
            if char=='nextLine':
                line+=1
                prevchar = char
            else:
                for production in productions:
                    if ((production[0] == currentState) and (production[1] == char) and (production[2] == currentStackSymbol)):
                        currentState = production[3]
                        nextstack = production[4]
                        ada=True
                if(ada==True):
                    prevchar = char
                    previousStackSymbol = currentStackSymbol
                    currentStackSymbol = nextstack
                    print('{}\t {}\t {}\t ({}, {})'.format(currentState, char, previousStackSymbol, previousStackSymbol, nextstack))
                    #time.sleep(2)
                else:
                    currentchar = char
                    if(prevchar == currentchar):
                        currentchar = prevchar
                    if(prevchar=='nextLine'):
                        line = line-1
                        char = 'e'
                    break
                
        if(currentStackSymbol in finalStates):
            accepted = True
        
        return accepted, line, currentchar

def main():
    # argparse
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
    #time.sleep(3)
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
        position = er.searchposition(filename,currentchar,line)
        er.printerror(filename,position,line)
    else:
        print("yeyy selamat udah bener")

if __name__ == '__main__':
    main()