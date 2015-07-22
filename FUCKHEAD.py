syntax=""
decvar=""
running=True
print("FUCKHEAD v0.3.1-alpha")

def inputSyntax():
    global syntax
    syntax=input("> ")

def checkSyntax():
    global syntax
    global decvar
    global running
    if syntax.startswith('LISTEN SHITFACE "') and syntax.endswith('"') or syntax.startswith("LISTEN SHITFACE '") and syntax.endswith("'"):
        to_print=syntax[17:-1]
        print(to_print)
    elif syntax.startswith('LISTEN SHITFACE '):
        to_print=decvar[0:]
        print(to_print)
    elif syntax.startswith('PAY THE FUCK ATTENTION '):
        decvar = syntax[24:]
        decvar = decvar.split("=")
        decvar=decvar[1]
    elif syntax.startswith('SHUT THE FUCK UP'):
        running=False
    elif syntax.startswith("GIMME SOME DAMN HELP"):
        commands=['LISTEN SHITFACE', 'PAY THE FUCK ATTENTION', 'SHUT THE FUCK UP', 'GIMME SOME DAMN HELP']
        commandsDesc=['Prints input', 'Defines a variable', 'Exits FUCKHEAD', 'Prints help information']
        for i in range(0, len(commands)):
            print("%s - %s" % (commands[i], commandsDesc[i]))
    else:
        print("HEY ASSHOLE, '%s' ISN'T A COMMAND" % syntax)

while running:
    inputSyntax()
    checkSyntax()
