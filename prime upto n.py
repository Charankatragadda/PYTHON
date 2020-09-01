#prime numbers from 1 to n
n=int(input("enter the number"))
print("\n All prime numbers upto ",n," are :")
for num in range(2,n+1):
    i=2
    for i in range(2,num):
        if(num%i==0):
            i=num
            break;
    if(i!=num):
        print(num,end=" ")
