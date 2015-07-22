from sys import *

tokens = []
num_stack=[]
print("FUCKHEAD v1.0.0-alpha")

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
            elif expr != ""and isexpr == 0:
                tokens.append("NUM:" + expr)
                expr = ""
            tok = ""
        elif tok =="LISTEN SHITFACE":
            tokens.append("PRINT")
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
    return tokens
    #print(tokens)

def evalExpression(expr):
    expr = "," + expr

    i = len(expr)-1
    num = ""
    while i >= 0:
        if expr[i] == "+" or expr[i] == "-" or expr[i] == "/" or expr[i] == "*" or expr[i] == "%":
            num = num[::-1]
            num_stack.append(num)
            num_stack.append(expr[i])
            num = ""
        elif expr[i] == ",":
            num = num[::-1]
            num_stack.append(num)
            num = ""
        else:
            num += expr[i]
        i-=1
    print(num_stack)




def doPrint(toPrint):
    if(toPrint[0:6] == "STRING"):
        toPrint = toPrint[8:-1]
    if(toPrint[0:3] == "NUM"):
        toPrint = toPrint[4:]
    if(toPrint[0:4] == "EXPR"):
        toPrint = evalExpression(toPrint[5:])
    print(toPrint)

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

def run():
    data = open_file(argv[1])
    toks = lex(data)
    parse(toks)

run()
