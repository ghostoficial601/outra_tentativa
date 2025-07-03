# aqui vai ser a interface:
from funcoes import soma, subtracao, divisao, multiplicacao
while True:
    quest = str(input("O que vc gostaria de usar:\n0.sair \n1.+\n2.-\n3.%\n4.x\n--> "))
    x_ = int(input("escreva um numero: "))
    y_ = int(input("escreva um numero: "))
    if quest in ["0", "sair"]:
        break
    elif quest in ["1", "+"]:
        print(soma(x=x_, y=y_))
    elif quest in ["2", "-"]:
        print(subtracao(x=x_, y=y_))
    elif quest in ["3", "%"]:
        print(divisao(x=x_, y=y_))
    elif quest in ["4", "x", "*"]:
        print(multiplicacao(x=x_, y=y_))

    