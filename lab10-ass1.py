#program for implementation of gates
s = (int)(input("Enter the gate"))
if(s == 1):
    print("()")
elif(s == 2):
    print("()")
elif(s == 3):
    print("()()()")
elif(s == 4):
    print("()()()()")
elif(s == 5):
    print("()()()()()")
else:
    print("Invalid gate")
s1 = ["()","()()","()()()","()()()()","()()()()()"]
print(s1)
