# FUCKHEAD v1.1.0-alpha

from sys import *

tokens = []
num_stack=[]
symbols = {}
print("FUCKHEAD v1.1.0-alpha")

def open_file(filename):
    data = open(filename, "r").read()
    data += "<EOF>"
    return data

def lex(filecontents):
    tok = ""
    state = 0
    string = ""
    isexpr=0
    expr = ""
    n = ""
    var_started = 0
    var = ""
    filecontents = list(filecontents)
    for char in filecontents:
        tok += char
        if tok == " ":
            if state == 0:
                tok = ""
            else:
                tok = " "
        elif tok == "\n" or tok == "<EOF>":
            if expr != "" and isexpr == 1:
                tokens.append("EXPR:" + expr)
                expr = ""
            elif expr != "" and isexpr == 0:
                tokens.append("NUM:" + expr)
                expr = ""
            elif var != "":
                var = var[:-1]
                tokens.append("VAR:" + var)
                var = ""
                var_started = 0
            tok = ""
        elif tok == "LISTEN SHITFACE":
            tokens.append("PRINT")
            tok = ""
        elif tok == "FUCKING" and state == 0:
            tok = ""
            var_started = 1
            var += tok
        elif tok == "IS" and state == 0:
            if var != "":
                var = var[:-1]
                tokens.append("VAR:" + var)
                var = ""
                var_started = 0
            tokens.append("EQUALS")
            tok = ""
        elif var_started == 1 and tok is not char in "IS FUCKING":
            var += tok
            tok = ""
        elif tok == "0" or tok == "1" or tok =="2" or tok =="3" or tok =="4" or tok =="5" or tok =="6" or tok =="7" or tok =="8" or tok =="9":
            expr += tok
            tok = ""
        elif tok == "+" or tok == "-" or tok == "*" or tok == "/" or tok == "(" or tok == ")":
            isexpr=1
            expr += tok
            tok = ""
        elif tok == "\"":
            if state == 0:
                state = 1
            elif state == 1:
                tokens.append("STRING:" + string + "\"")
                string = ""
                state = 0
                tok = ""
        elif state == 1:
            string += tok
            tok = ""
    #print(tokens)
    return tokens

def evalExpression(expr):
    return eval(expr)

def doPrint(toPrint):
    if(toPrint[0:6] == "STRING"):
        toPrint = toPrint[8:-1]
    if(toPrint[0:3] == "NUM"):
        toPrint = toPrint[4:]
    if(toPrint[0:4] == "EXPR"):
        toPrint = evalExpression(toPrint[5:])
    print(toPrint)

def doAssign(varname, varvalue):
    symbols[varname[4:]] = varvalue

def parse(toks):
    i = 0
    while(i < len(toks)):
        if toks[i] + " " + toks[i+1][0:6] == "PRINT STRING" or toks[i] + " " + toks[i+1][0:3] == "PRINT NUM" or toks[i] + " " + toks[i+1][0:4] == "PRINT EXPR":
            if toks[i+1][0:6] == "STRING":
                doPrint(toks[i+1])
            elif toks[i+1][0:3] == "NUM":
                doPrint(toks[i+1])
            elif toks[i+1][0:4] == "EXPR":
                doPrint(toks[i+1])
            i+=2
        if toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:6] == "VAR EQUALS STRING":
            doAssign(toks[i], toks[i+2])
            i+=3
        print(symbols)

def run():
    data = open_file(argv[1])
    toks = lex(data)
    parse(toks)

run()
