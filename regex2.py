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
    (r'/small>', '/small' ),
    (r'<strong', 'strong' ),
    (r'/strong>', '/strong' ),
    (r'<form', 'form' ),
    (r'/form>', '/form' ),
     (r'<button', 'button' ),
    (r'/button>', '/button' ),
    (r'<b', 'b' ),
    (r'/b>', '/b' ),
    (r'<a', 'a' ),
    (r'/a>', '/a' ),
    (r'<abbr', 'abbr' ),
    (r'/abbr>', '/abbr' ),
    (r'<em', 'em' ),
    (r'/em>', '/em' ),
    (r'<img', 'img' ),
    (r'<input', 'input' ),
    (r'<link', 'link' ),
    (r'id =', lambda m: ['id','='] ),
    (r'id=', lambda m: ['id','='] ),
    (r'class =', lambda m: ['class','='] ),
    (r'class=', lambda m: ['class','='] ),
    (r'style =', lambda m: ['style','='] ),
    (r'style=', lambda m: ['style','='] ),
    (r'src =', lambda m: ['src','='] ),
    (r'src=', lambda m: ['src','='] ),
    (r'href =', lambda m: ['href','='] ),
    (r'href=', lambda m: ['href','='] ),
    (r'alt =', lambda m: ['alt','='] ),
    (r'alt=', lambda m: ['alt','='] ),
    (r'type =', lambda m: ['type','='] ),
    (r'type=', lambda m: ['type','='] ),
    (r'action =', lambda m: ['action','='] ),
    (r'action=', lambda m: ['action','='] ),
    (r'method =', lambda m: ['method','='] ),
    (r'method=', lambda m: ['method','='] ),
    (r'rel =', lambda m: ['rel','='] ),
    (r'rel=', lambda m: ['rel','='] ),
    (r'"submit', '"submit' ),
    (r'\'submit', '\'submit' ),
    (r'"button', '"button' ),
    (r'\'button', '\'button' ),
    (r'"reset', '"reset' ),
    (r'\'reset', '\'reset' ),
    # (r'<h2', lambda m: ['<', 'h2'] ),
    # (r'</h2', lambda m: ['<', '/' ,'h2'] ),
    # (r'<h3', lambda m: ['<', 'h3'] ),
    # (r'</h3', lambda m: ['<', '/' ,'h3'] ),
    # (r'<h4', lambda m: ['<', 'h4'] ),
    # (r'</h4', lambda m: ['<', '/' ,'h4'] ),
    # (r'<h5', lambda m: ['<', 'h5'] ),
    # (r'</h5', lambda m: ['<', '/' ,'h5'] ),
    # (r'<h6', lambda m: ['<', 'h6'] ),
    # (r'</h6', lambda m: ['<', '/' ,'h6'] ),
    # (r'<em', lambda m: ['<', 'em'] ),
    # (r'</em', lambda m: ['<', '/' ,'em'] ),
    # (r'<p', lambda m: ['<', 'p'] ),
    # (r'</p', lambda m: ['<', '/' ,'p'] ),
    # (r'<abbr', lambda m: ['<', 'abbr'] ),
    # (r'</abbr', lambda m: ['<', '/' ,'abbr'] ),
    # (r'<img', lambda m: ['<', 'img'] ),
    # (r'<link', lambda m: ['<', 'link'] ),
    # (r'<a', lambda m: ['<', 'a'] ),
    # (r'</a', lambda m: ['<', '/' ,'a'] ),
    # (r'rel =', lambda m: ['rel','='] ),
    # (r'rel=', lambda m: ['rel','='] ),
    # (r'href =', lambda m: ['href','='] ),
    # (r'href=', lambda m: ['href','='] ),
    # (r'src =', lambda m: ['src','='] ),
    # (r'src=', lambda m: ['src','='] ),
    # (r'src\S*(?=<)' , 'e'),
    # (r'src\S*(?=")' , 'e'),
    # (r'<script', lambda m: ['<', 'script'] ),
    # (r'</script', lambda m: ['<', '/' ,'script'] ),
    # (r'<title', lambda m: ['<', 'title'] ),
    # (r'</title', lambda m: ['<', '/' ,'title'] ),
    # (r'<body', lambda m: ['<', 'body'] ),
    # (r'</body', lambda m: ['<', '/' ,'body'] ),
    # (r'<head', lambda m: ['<', 'head'] ),
    # (r'</head', lambda m: ['<', '/' ,'head'] ),
    # (r'<html', lambda m: ['<', 'html'] ),
    # (r'</html', lambda m: ['<', '/' ,'html'] ),
    # (r'<div', lambda m: ['<', 'div'] ),
    # (r'</div', lambda m: ['<', '/' ,'div'] ),
    # (r'<table', lambda m: ['<', 'table'] ),
    # (r'</table', lambda m: ['<', '/' ,'table'] ),
    # (r'<tr', lambda m: ['<', 'tr'] ),
    # (r'</tr', lambda m: ['<', '/' ,'tr'] ),
    # (r'<td', lambda m: ['<', 'td'] ),
    # (r'</td', lambda m: ['<', '/' ,'td'] ),
    # (r'<th', lambda m: ['<', 'th'] ),
    # (r'</th', lambda m: ['<', '/' ,'th'] ),
    # (r'<form', lambda m: ['<', 'form'] ),
    # (r'</form', lambda m: ['<', '/' ,'form'] ),
    # (r'<!', lambda m: ['<', '!'] ),
    # (r'alt(?==)' , 'alt'),
    # (r'alt\S*(?=<)' , 'e'),
    # (r'alt\S*(?=")' , 'e'),
    # (r'type(?==)' , 'type'),
    # (r'type\S*(?=<)' , 'e'),
    # (r'type\S*(?=")' , 'e'),
    # (r'action(?==)' , 'action'),
    # (r'action\S*(?=<)' , 'e'),
    # (r'action\S*(?=")' , 'e'),
    # (r'method(?==)' , 'method'),
    # (r'method\S*(?=<)' , 'e'),
    # (r'method\S*(?=")' , 'e'),
    # (r'<button', lambda m: ['<', 'button'] ),
    # (r'"button"', lambda m: ['petik2', 'button', 'petik2'] ),
    # (r'button\S*(?=<)' , 'e'),
    # (r'button\S*(?=")' , 'e'),
    # (r'submit(?=")' , 'submit'),
    # (r'submit(?=\')' , 'submit'),
    # (r'submit\S*(?=<)' , 'e'),
    # (r'submit\S*(?=")' , 'e'),
    # (r'reset(?=")' , 'reset'),
    # (r'reset(?=\')' , 'reset'),
    # (r'reset\S*(?=<)' , 'e'),
    # (r'reset\S*(?=")' , 'e'),
    # (r'<input', lambda m: ['<', 'input'] ),
    # (r'input\S*(?=<)' , 'e'),
    # (r'input\S*(?=")' , 'e'),
    # (r'text(?=")' , 'text'),
    # (r'text(?=\')' , 'text'),
    # (r'text\S*(?=<)' , 'e'),
    # (r'text\S*(?=")' , 'e'),
    # (r'password(?=")' , 'password'),
    # (r'password(?=\')' , 'password'),
    # (r'password\S*(?=<)' , 'e'),
    # (r'password\S*(?=")' , 'e'),
    # (r'number(?=")' , 'number'),
    # (r'number(?=\')' , 'number'),
    # (r'number\S*(?=<)' , 'e'),
    # (r'number\S*(?=")' , 'e'),
    # (r'checkbox(?=")' , 'checkbox'),
    # (r'checkbox(?=\')' , 'checkbox'),
    # (r'checkbox\S*(?=<)' , 'e'),
    # (r'checkbox\S*(?=")' , 'e'),
    # (r'email(?=")' , 'email'),
    # (r'email(?=\')' , 'email'),
    # (r'email\S*(?=<)' , 'e'),
    # (r'email\S*(?=")' , 'e'),
    # (r'get(?=")' , 'get'),
    # (r'get(?=\')' , 'get'),
    # (r'get\S*(?=<)' , 'e'),
    # (r'get\S*(?=")' , 'e'),
    # (r'post(?=")' , 'post'),
    # (r'post(?=\')' , 'post'),
    # (r'post\S*(?=<)' , 'e'),
    # (r'post\S*(?=")' , 'e'),
   
    (r'[\n]', 'nextLine'),
    (r'=', '='),
    (r'-', '-'),
    (r'"' ,'petik2'),
    (r'\'', 'petik'),
    (r'<', '<'),
    (r'>', '>'),
    (r'/', '/'),

    # Kata Random
    (r'\S*(?=\')', 'e'),
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