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
        stack = []
        oper = ["+","-","/","*"]
        line = []
        for i in x:
            if i.replace(".","").isdigit():
                line.append(i)
            elif i in oper:
                if stack == []:
                    stack.append(i)
                elif Calculator.pr(stack[-1]) < Calculator.pr(i):
                    stack.append(i)
                elif Calculator.pr(stack[-1]) >= Calculator.pr(i):
                    while stack != [] and Calculator.pr(stack[-1]) >= Calculator.pr(i):
                        line.append(stack.pop(-1))
                    stack.append(i)
            elif i == "(":
                stack.append(i)
            elif i == ")":
                for i in stack[::-1]:
                    if i != "(":
                        line.append(stack.pop())
                    else:
                        stack.pop(-1)
                        break
        pol = line+stack[::-1]
        stack2 = []
        for i in pol:
            if i.replace(".","").isdigit():
                stack2.append(i)
            elif i == "+" or i == "-" or i == "/" or i == "*":
                if i == "+" and stack2 != []:
                    stack2.append(float(stack2.pop())+float(stack2.pop()))
                elif i == "*" and stack2 != []:
                    stack2.append(float(stack2.pop())*float(stack2.pop()))
                elif i == "-" and stack2 != []:
                    stack2.append(float(stack2.pop(-2))-float(stack2.pop()))
                elif i == "/" and stack2 != []:
                    stack2.append(float(stack2.pop(-2))/float(stack2.pop()))
        if int(stack2[0]) == stack2[0]:
            return stack2[0]
        elif type(stack2[0]) == float:
            return stack2[0]
        else:
            return int(stack2[0])
