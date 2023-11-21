import argparse
import sys
import re

# python tes.py test/x.html

def comparing(text, operators):
    pos = 0
    line = 1
    list = []

    while (pos < len(text)):
        if text[pos] == '\n':
            line += 1

        flag = None
        for current_token in operators:
            pattern, tag = current_token

            regex = re.compile(pattern)
            flag = regex.match(text,pos)

            if flag:
                if tag:
                    token = tag
                    list.append(token)
                break

        if not flag:
            print("SYNTAX ERROR !!!")
            print(f'Error Expression at line {line}: {text[pos:].splitlines()[0]}')
            sys.exit(1)
        else:
            pos = flag.end(0)

    return list

operators = [

    (r'[ \t]+', None),
    (r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',  None),
    (r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',  None),
   
    (r'[\n]', 'nextLine'),
    (r'h1', 'h1'),
    (r'h2', 'h2'),
    (r'h3', 'h3'),
    (r'h4', 'h4'),
    (r'h5', 'h5'),
    (r'h6', 'h6'),
    (r'p', 'p'),
    (r'script', 'script'),
    (r'title', 'title'),
    (r'body', 'body'),
    (r'head', 'head'),
    (r'html', 'html'),
    (r'<', '<'),
    (r'>', '>'),
    (r'/', '/'),

    # Kata Random
    (r'\S*(?=<)', 'e'),
    (r'\S*', 'e'),
]

def createToken(text):
    file = open(text, encoding="utf8")
    chara = file.read()
    file.close()

    list = comparing(chara, operators)
    tokenResult = []

    for token in list:
        tokenResult.append(token)

    return tokenResult

def verdict():
    arg = argparse.ArgumentParser()
    arg.add_argument('file', type = argparse.FileType('r'))
    args = arg.parse_args()

    print("File name: " + str(args.file.name))
    print()

    token = createToken(args.file.name)
    token = [x.lower() for x in token]
    print(token)

if __name__ == "__main__":
    verdict()