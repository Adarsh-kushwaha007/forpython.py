'''print("enter the first number:")
x=int(input())
print("enter the second number:")
y=int (input())
c=int( x*y)
print(c)
print("aera of square is:", x*x)

if(x<y):
    print("the minimum number is:",x)
else:
    print("the minimum number is:",y)

if(x%2==0):
    print("the number is odd:",x)
else:
    print("the number is odd:",x)'''
def _sumton_():
    a= int(input("enter the number:"))
    sum = 0
    count = 1
    while(count<=a):
        sum +=count
        count += 1
    print(sum)

def isPriime():
    b= int(input("enter the number to check prime:"))
    i=2
    while(i<=(b-1)):
        if(b%i==0):
            print("the number is non-prime")
            break
        else:
            i +=1
        
    print("The number is prime")
    exit
