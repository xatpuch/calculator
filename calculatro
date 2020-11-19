class Calculator():
    def pr(x):
        if x == "*" or x == "/":
            return 2
        if x == "-" or x == "+":
            return 1
        elif x == "(":
            return 0

    def parse(s):
        delims = ["+", "-", "*", "/", "(", ")"]
        lex = []
        tmp = ""
        for a in s:
            if a != " ":
                if a in delims:
                    if tmp != "":
                        lex += [tmp]
                    lex += [a]
                    tmp = ""
                else:
                    tmp += a
        if tmp != "":
            lex += [tmp]
        return lex
    def evaluate(self,string):
        x = Calculator.parse(string)
        stek = []
        oper = ["+","-","/","*"]
        stroka = []
        for i in x:
            if i.replace(".","").isdigit():
                stroka.append(i)
            elif i in oper:
                if stek == []:
                    stek.append(i)
                elif Calculator.pr(stek[-1]) < Calculator.pr(i):
                    stek.append(i)
                elif Calculator.pr(stek[-1]) >= Calculator.pr(i):
                    while stek != [] and Calculator.pr(stek[-1]) >= Calculator.pr(i):
                        stroka.append(stek.pop(-1))
                    stek.append(i)
            elif i == "(":
                stek.append(i)
            elif i == ")":
                for i in stek[::-1]:
                    if i != "(":
                        stroka.append(stek.pop())
                    else:
                        stek.pop(-1)
                        break
        #print(stroka,stek)
        pol = stroka+stek[::-1]
        #return pol
        stek2 = []
        for i in pol:
            if i.replace(".","").isdigit():
                stek2.append(i)
            elif i == "+" or i == "-" or i == "/" or i == "*":
                if i == "+" and stek2 != []:
                    stek2.append(float(stek2.pop())+float(stek2.pop()))
                elif i == "*" and stek2 != []:
                    stek2.append(float(stek2.pop())*float(stek2.pop()))
                elif i == "-" and stek2 != []:
                    stek2.append(float(stek2.pop(-2))-float(stek2.pop()))
                elif i == "/" and stek2 != []:
                    stek2.append(float(stek2.pop(-2))/float(stek2.pop()))
        if int(stek2[0]) == stek2[0]:
            return stek2[0]
        elif type(stek2[0]) == float:
            return stek2[0]
        else:
            return int(stek2[0])
