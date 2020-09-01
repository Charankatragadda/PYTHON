#program to find the sum of the digits of a number
Number = int(input("enter any Number:"))
Sum = 0

while(Number>0):
    Reminder=Number%10
    Sum=Sum+Reminder
    Number=Number//10

print("\n Sum of the digits of the given number = %d" %Sum)
