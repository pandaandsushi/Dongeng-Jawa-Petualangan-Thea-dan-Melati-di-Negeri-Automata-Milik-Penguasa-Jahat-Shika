import sys
import re
import os

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
                    if callable(token):
                        modified_token = token(flag)
                        list.extend(modified_token)
                    else:
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

    (r'<html', 'html' ),
    (r'/html>', '/html' ),
    (r'<head', 'head' ),
    (r'/head>', '/head' ),
    (r'<body', 'body' ),
    (r'/body>', '/body' ),
    (r'<title', 'title' ),
    (r'/title>', '/title' ),
    (r'<h1', 'h1' ),
    (r'/h1>', '/h1' ),
    (r'<h2', 'h2' ),
    (r'/h2>', '/h2' ),
    (r'<h3', 'h3' ),
    (r'/h3>', '/h3' ),
    (r'<h4', 'h4' ),
    (r'/h4>', '/h4' ),
    (r'<h5', 'h5' ),
    (r'/h5>', '/h5' ),
    (r'<h6', 'h6' ),
    (r'/h6>', '/h6' ),
    (r'<p', 'p' ),
    (r'/p>', '/p' ),
    (r'<div', 'div' ),
    (r'/div>', '/div' ),
    (r'<table', 'table' ),
    (r'/table>', '/table' ),
    (r'<tr', 'tr' ),
    (r'/tr>', '/tr' ),
    (r'<td', 'td' ),
    (r'/td>', '/td' ),
    (r'<th', 'th' ),
    (r'/th>', '/th' ),
    (r'<hr', 'hr' ),
    (r'<br', 'br' ),
    (r'<small', 'small' ),
    (r'<strong', 'strong' ),
    (r'<form', 'form' ),
    (r'/form>', '/form' ),
    (r'<button', 'button' ),
    (r'/button>', '/button' ),
    (r'<b', 'b' ),
    (r'<a', 'a' ),
    (r'<em', 'em' ),
    (r'<abbr', 'abbr' ),
    (r'<img', 'img' ),
    (r'<input', 'input' ),
    (r'<link', 'link' ),
    (r'<!-', '<!-'),
    (r'->', '->'),
    (r'/strong>', '/strong' ),
    (r'/small>', '/small' ),
    (r'/b>', '/b' ),
    (r'/a>', '/a' ),
    (r'/abbr>', '/abbr' ),
    (r'/em>', '/em' ),
    (r'id(?==)', 'id' ),
    (r'id(?= =)', 'id' ),
    (r'class(?==)', 'class'),
    (r'class(?= =)', 'class' ),
    (r'style(?==)', 'style' ),
    (r'style(?= =)', 'style' ),
    (r'src(?==)', 'src' ),
    (r'src(?= =)', 'src' ),
    (r'href(?==)', 'href' ),
    (r'href(?= =)', 'href' ),
    (r'alt(?==)', 'alt' ),
    (r'alt(?= =)=', 'alt' ),
    (r'action(?==)', 'action' ),
    (r'action(?= =)', 'action' ),
    (r'rel(?==)', 'rel' ),
    (r'rel(?= =)','rel' ),
    (r'"GET"', '"GET"' ),
    (r'\'GET\'', '\'GET\'' ),
    (r'"POST"', '"POST"' ),
    (r'\'POST\'', '\'POST\'' ),
    (r'"get"', '"get"' ),
    (r'\'get\'', '\'get\'' ),
    (r'"post"', '"post"' ),
    (r'\'post\'', '\'post\'' ),
    (r'method=', 'method1' ),
    (r'method =', 'method2' ),
    (r'type=', 'type1' ),
    (r'type =', 'type2' ),
    (r'"checkbox"', '"checkbox"' ),
    (r'\'checkbox\'', '\'checkbox\'' ),
    (r'"number"', '"number"' ),
    (r'\'number\'', '\'number\'' ),
    (r'"text"', '"text"' ),
    (r'\'text\'', '\'text\'' ),
    (r'"email"', '"email"' ),
    (r'\'email\'', '\'email\'' ),
    (r'"password"', '"password"' ),
    (r'\'password\'', '\'password\'' ),
    (r'"submit"', '"submit"' ),
    (r'\'submit\'', '\'submit\'' ),
    (r'"reset"', '"reset"' ),
    (r'\'reset\'', '\'reset\'' ),
    (r'"button"', '"button"' ),
    (r'\'button\'', '\'button\'' ),
    (r'="\S*(?=")', lambda m: ['=','petik2','e'] ),
    (r'<script', 'script' ),
    (r'/script>', '/script' ),
   
    (r'[\n]', 'nextLine'),
    (r'=', '='),
    (r'-', '-'),
    (r'"\S*"', 'e' ),
    (r'"' ,'petik2'),
    (r'\'', 'petik'),
    (r'<', '<'),
    (r'>', '>'),

    # Kata Random
    (r'\S*(?=</div)', 'e'),
    (r'\S*(?=</table)', 'e'),
    (r'\S*(?=</button)', 'e'),
    (r'\S*(?=</form)', 'e'),
    (r'\S*(?=</a)', 'e'),
    (r'\S*(?=<small)', 'e'),
    (r'\S*(?=</small)', 'e'),
    (r'\S*(?=<strong)', 'e'),
    (r'\S*(?=</strong)', 'e'),
    (r'\S*(?=<b)', 'e'),
    (r'\S*(?=</b)', 'e'),
    (r'\S*(?=<abbr)', 'e'),
    (r'\S*(?=</abbr)', 'e'),
    (r'\S*(?=<em)', 'e'),
    (r'\S*(?=</em)', 'e'),
    (r'\S*(?=</p)', 'e'),
    (r'\S*(?=</h1)', 'e'),
    (r'\S*(?=</h2)', 'e'),
    (r'\S*(?=</h3)', 'e'),
    (r'\S*(?=</h4)', 'e'),
    (r'\S*(?=</h5)', 'e'),
    (r'\S*(?=</h6)', 'e'),
    (r'\S*(?=\')', 'e'),
    (r'\S*(?=")', 'e'),
    (r'\S*(?=<)', 'e'),
    (r'\S*' , 'e')
    
]

def createToken(text):
    if(os.path.isfile(text)):
            try:
                file = open(text, encoding="utf8")
                chara = file.read()
                file.close()
            except IOError as e:
                print("File could not be opened.")
                exit(0)
    else:
        print('{} :File was not found in the specified path.'.format(text))
        exit(0)

    list = comparing(chara, operators)
    tokenResult = []

    for token in list:
        tokenResult.append(token)

    return tokenResult