import random
print("Lets Play a game to identify the number!!")
a=input("So are you ready? "
        "Type Yes or No")
if a=='no' or a=='No':
    quit()
elif a=='yes' or a=='Yes':
    print("So lets Play!!!")
else:
    print("Wrong Input")

r1=random.randint(0,15)
chances=10
while chances>0:
    answer = int(input("Start Guessing"))
    if r1==answer :
        print("Correct!")
    elif answer>r1:
        print("Your answer is greater")
    elif answer<r1:
        print("Your answer is less")
    chances-=1
    print("Chances Left= ",chances)


