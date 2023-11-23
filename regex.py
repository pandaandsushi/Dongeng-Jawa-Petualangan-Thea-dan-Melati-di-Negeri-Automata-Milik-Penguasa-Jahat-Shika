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

    (r'h1(?=>)' , 'h1'),
    (r'h1\S*(?=<)' , 'e'),
    (r'h1\S*(?=")' , 'e'),
    (r'h2(?=>)' , 'h2'),
    (r'h2\S*(?=<)' , 'e'),
    (r'h2\S*(?=")' , 'e'),
    (r'h3(?=>)' , 'h3'),
    (r'h3\S*(?=<)' , 'e'),
    (r'h3\S*(?=")' , 'e'),
    (r'h4(?=>)' , 'h4'),
    (r'h4\S*(?=<)' , 'e'),
    (r'h4\S*(?=")' , 'e'),
    (r'h5(?=>)' , 'h5'),
    (r'h5\S*(?=<)' , 'e'),
    (r'h5\S*(?=")' , 'e'),
    (r'h6(?=>)' , 'h6'),
    (r'h6\S*(?=<)' , 'e'),
    (r'h6\S*(?=")' , 'e'),
    (r'em(?=>)' , 'em'),
    (r'em\S*(?=<)' , 'e'),
    (r'em\S*(?=")' , 'e'),
    (r'p(?=>)' , 'p'),
    (r'p\S*(?=<)' , 'e'),
    (r'p\S*(?=")' , 'e'),
    (r'img' , 'img'),
    (r'img(?=>)' , 'img'),
    (r'img\S*(?=<)' , 'e'),
    (r'img\S*(?=")' , 'e'),
    (r'src(?==)' , 'src'),
    (r'src\S*(?=<)' , 'e'),
    (r'src\S*(?=")' , 'e'),
    (r'script' , 'script'),
    (r'script(?=>)' , 'script'),
    (r'script\S*(?=<)' , 'e'),
    (r'script\S*(?=")' , 'e'),
    (r'title(?=>)' , 'title'),
    (r'title\S*(?=<)' , 'e'),
    (r'title\S*(?=")' , 'e'),
    (r'body(?=>)' , 'body'),
    (r'body\S*(?=<)' , 'e'),
    (r'body\S*(?=")' , 'e'),
    (r'head(?=>)' , 'head'),
    (r'head\S*(?=<)' , 'e'),
    (r'head\S*(?=")' , 'e'),
    (r'html(?=>)' , 'html'),
    (r'html\S*(?=<)' , 'e'),
    (r'html\S*(?=")' , 'e'),
    (r'div(?=>)' , 'div'),
    (r'div\S*(?=<)' , 'e'),
    (r'div\S*(?=")' , 'e'),
    (r'alt(?==)' , 'alt'),
    (r'alt\S*(?=<)' , 'e'),
    (r'alt\S*(?=")' , 'e'),
    (r'type(?==)' , 'type'),
    (r'type\S*(?=<)' , 'e'),
    (r'type\S*(?=")' , 'e'),
    (r'button' , 'button'),
    (r'button(?=")' , 'button'),
    (r'button(?=\')' , 'button'),
    (r'button\S*(?=<)' , 'e'),
    (r'button\S*(?=")' , 'e'),
    (r'submit(?=")' , 'submit'),
    (r'submit(?=\')' , 'submit'),
    (r'submit\S*(?=<)' , 'e'),
    (r'submit\S*(?=")' , 'e'),
    (r'reset(?=")' , 'reset'),
    (r'reset(?=\')' , 'reset'),
    (r'reset\S*(?=<)' , 'e'),
    (r'reset\S*(?=")' , 'e'),
    (r'input' , 'input'),
    (r'(?=")input(?=")' , 'input'),
    (r'input\S*(?=<)' , 'e'),
    (r'input\S*(?=")' , 'e'),
    (r'text(?=")' , 'text'),
    (r'text(?=\')' , 'text'),
    (r'text\S*(?=<)' , 'e'),
    (r'text\S*(?=")' , 'e'),
    (r'password(?=")' , 'password'),
    (r'password(?=\')' , 'password'),
    (r'password\S*(?=<)' , 'e'),
    (r'password\S*(?=")' , 'e'),
    (r'number(?=")' , 'number'),
    (r'number(?=\')' , 'number'),
    (r'number\S*(?=<)' , 'e'),
    (r'number\S*(?=")' , 'e'),
    (r'checkbox(?=")' , 'checkbox'),
    (r'checkbox(?=\')' , 'checkbox'),
    (r'checkbox\S*(?=<)' , 'e'),
    (r'checkbox\S*(?=")' , 'e'),
    (r'email(?=")' , 'email'),
    (r'email(?=\')' , 'email'),
    (r'email\S*(?=<)' , 'e'),
    (r'email\S*(?=")' , 'e'),
   
    (r'[\n]', 'nextLine'),
    (r'=', '='),
    (r'"' ,'petik2'),
    (r'\'', 'petik'),
    (r'<', '<'),
    (r'>', '>'),
    (r'/', '/'),

    # Kata Random
    (r'\S*(?=")', 'e'),
    (r'\S*(?=<)', 'e'),
    (r'\S*' , 'e')
    
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