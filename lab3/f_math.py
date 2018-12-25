from random import randint , choice
from calc import evaluate
#  1 . generate equation
x = randint(0,9)
y = randint(0,9)
op = choice(["+","-","*","/"])
error = randint(-1,1)

r = evaluate(x,y,op) + error



print(f"{x} + {y} = {r}")
equation_is_valid = error == 0
user_answer = input("(y/n) ? ").upper()
# user_answer_yes = (user_answer == "Y")
# if equation_is_valid == user_answer_yes:
#     print("yay")
# else:
#     print("nay")

if user_answer == "Y":
    if error == 0:
       print("yay")
    else:
        print("nay")
else:
    if error == 0:
        print("nay")
    else:
        print("yay")


