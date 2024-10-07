# def fact(n):
#     if(n == 0 or n==1):
#         # print("The factorial of 0 and 1 is: 1")
#         return 1
#     elif n<0:
#         print("Factorial can not defined for negative integers")
#         return None
#     else:
        # return n*fact(n-1)


def disp():
    print("hello")

# res = disp()
# print(res)

def cal_avg(a, b, c, d):
    sum = a+b+c+d
    avg = sum/4
    print(avg)
    return avg

cal_avg(1, 2 , 3,4)

anlist =["camera", "studio", "network", "wires","batteries","tripord or stands"]
def len_list(lists):
    print(len(lists))


len_list(anlist)

def on_count(a):
    for i in a:
        print(i, end=" ")

on_count(anlist)

