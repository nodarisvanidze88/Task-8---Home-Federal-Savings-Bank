import random as rd

def textToMoney(txt):
    a = txt.lower().strip()
    a1 = a.split()
    b = txt.lower().strip()
    b1 = list(b)
    if a1[0] == "hello":
        return 0
    elif b1[0] == "h":
        return 20
    elif a1[0] != "hello" and b1[0] != "h" and a1[0] != "stop":
        return 100
    elif a1[0] == "stop":
        return "stop"

input("Hi ")
money = 0
answers = [
        "What did you say? ",
        "I think you told hello, but you always can stop it. ",
        "Do you need money? ",
        "Congratulation you got a money, just say stop. ",
        "Are you OK? I don't think so, do you whant stop it? just say stop. ",
        "How can I help you? "
        ]
x = len(answers)-1
while True:
    randNumber = rd.randint(0, x)
    text = input(answers[randNumber])
    value = textToMoney(text)
    if value != "stop":
        money = money + value
        print("$ " + str(money))
    elif value == "stop":
        print("You are good guy")
        break
