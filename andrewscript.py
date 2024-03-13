stack = []
lineCount = 1

PUSH_KEYWORD = "push"
PRINT_KEYWORD =  "print"
POPLASTEL_KEYWD = "pop"
EQU_KEYWD = "equ"
POS_KEYWD = "pos"
EXIT_KEYWD = "ret"
PRINTPOS_KEYWD= "out"
READ_KEYWD = "input"
SUM_KEYWD = "sum"
SUB_KEYWD = "sub"
SUMALL_KEYWD = "sumall"
SUBALL_KEYWD = "suball"

def ParseExpr(line):
    codeLine = line.split()

    #EQU
    if codeLine[0] == EQU_KEYWD:
        indexes = [int(codeLine[1]), int(codeLine[2])]
        if stack[indexes[0]] == stack[indexes[1]]:
            print("true")
        else:
            print("false")
        return

    #PUSH
    if codeLine[0] == PUSH_KEYWORD and not codeLine[1] == "":
        stack.append(codeLine[1])
        return
    
    #PRINT
    if codeLine[0] == PRINT_KEYWORD:
        print(stack)
        return

    #POP LAST EL
    if codeLine[0] == POPLASTEL_KEYWD:
        stack.remove(len(stack) - 1)
        return

    #GET POS OF VAL
    if codeLine[0] == POS_KEYWD:
        valToSeek = codeLine[1]
        i = 0
        valFound = False

        while i < len(stack):
            if stack[i] == valToSeek:
                valFound = True
                print("Value found at " + str(i))
                return

        print("Value not found")
        return
    
    #RET
    if codeLine[0] == EXIT_KEYWD:
        exit()
        return

    #PRINT FROM POS
    if codeLine[0] == PRINTPOS_KEYWD:
        index = int(codeLine[1])

        print(stack[index])
        return
    
    #READ INPUT
    if codeLine[0] == READ_KEYWD:
        val = int(input("input a value: "))
        stack.append(val)

    #SUM
    if codeLine[0] == SUM_KEYWD:
        arg1 = int(codeLine[1])
        arg2 = int(codeLine[2])
        res = stack[arg1] + stack[arg2]
        print(res)

    #SUB
    if codeLine[0] == SUB_KEYWD:
        arg1 = int(codeLine[1])
        arg2 = int(codeLine[2])
        res = stack[arg1] - stack[arg2]
        print(res)

    #SUMALL
    if codeLine[0] == SUMALL_KEYWD:
        i = 0
        acc = 0
        while i < len(stack):
            acc += int(stack[i])
            i += 1
        print(acc)

    #SUBALL
    if codeLine[0] == SUBALL_KEYWD:
        i = 0
        acc = 0
        while i < len(stack):
            acc -= int(stack[i])
            i += 1
        print(acc)

    #REMOVE EL
    #if codeLine[0] == :
        #return

while True:
    code = input(">")

    if len(code) > 0:
        try:
            if code.split()[0] == "exec":
                file = open(code.split()[1], "r")

                for line in file:
                    ParseExpr(line)
            else:
                ParseExpr(code)
        except:
            print("Unexpected error!")