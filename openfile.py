import os

class FileHandler:

    def __init__(self):
        pass

    def readFile(self, filePath):
        lines=[]
        if(os.path.isfile(filePath)):
            try:
                with open(filePath) as file:
                    lines = [line.rstrip() for line in file]
            except IOError as e:
                print("File could not be opened.")
                exit(0)
        else:
            print('{} :File was not found in the specified path.'.format(filePath))
            exit(0)
        return lines

    def parseFile(self,lines):
        states = lines[0].rstrip().split()
        input_symbols = lines[1].rstrip().split()
        stack_symbols = lines[2].rstrip().split()
        initial_state = lines[3]
        initial_stack = lines[4]
        final_states = lines[5].rstrip().split()
        productions = lines[6:]
        for i in range(len(productions)):
            productions[i] = productions[i].rstrip().split()

        parsedLines = {'states':states,
                        'input_symbols':input_symbols,
                        'stack_symbols':stack_symbols,
                        'initial_state':initial_state,
                        'initial_stack':initial_stack,
                        'final_states':final_states,
                        'productions':productions}
        return parsedLines
    
