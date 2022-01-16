class Solution:
    def calculate(s):
        currentNumber = lastNumber = answer = 0
        operator = "+"
        if(s == "" or s == "0"):
            print("Answer is 0")
        else:
            for char in s + "+":
                if(char.isdigit()):
                    currentNumber = (currentNumber * 10) + int(char)
                    print("Current number is " + str(currentNumber))
                elif(char.isspace()):
                    continue
                else:
                    if(operator == "+"):
                        lastNumber += currentNumber
                    elif(operator == "-"):
                        lastNumber -= currentNumber
                    elif(operator == "*"):
                        lastNumber = lastNumber * currentNumber
                    elif(operator == "/"):
                        lastNumber = int(lastNumber / currentNumber)

                    if(char in {"+", "-"}):
                        answer += lastNumber
                        lastNumber = 0
                    operator = char
                    currentNumber = 0
        print("Answer is --> " + str(answer))
    str = "14-3/2"
    calculate(str)
