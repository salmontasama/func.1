#######1########
def num_1 (x):
    if x%2==0:
        print('good')
    elif x%2!=0:
        print('not good')
num_1( int(input('enter numbr')))
#######2########
def avrege(n):
    sum_=0
    count=0
    for i in range(n):
        n=int(input('enter number'))
        sum_=sum_+n
        count=count+1
    return (sum_/count)
print(avrege(6))
########3##########
def sum_():
    x = int(input("enter number"))
    y = str(x)
    print(len(y))
sum_()

########4############
def change(n):
    x = n // 20
    res = n - (20*x)
    y = res // 10
    res = n - ((20*x) + (10*y))
    z = res // 5
    o = n - ((20*x) + (10*y) + (5*z))
    txt = "change contin:\n{} of 2os,\n{} of 10s,\n{} of 5s,\nand {} ones"
    return txt.format(x, y, z, o)
res = change(89)
print(res)
#######5#######
def sum_(x,y):
    z=x**y
    print(z)
sum_(3,3)
######6#######
def discount(y):
    x = int(input('enter pruce:'))
    y = 30/100*x
    return

def price (x):
    #x = int(input('enter price'))
    if x>1000:
       discount(x)
    else:x<1000
    print(10/100*x)
price(1200)
#####7#######
#####9#######
def menu (x,y):
    s = input('choos a,b,c,d,e:')
    if s == "a":
        print(max(x,y))
    elif s == 'b':
        print(min(x,y))
    elif s == 'c':
        print(x**y)
    elif s == 'd':
        print(x-y)
    elif s == 'e':
        print("good bay")
menu(9,5)