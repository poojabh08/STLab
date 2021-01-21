def isTriangle(x,y,z):
    if x>=(y+z):
        return False
    elif y>=(x+z):
        return False
    elif z>=(x+y):
        return False
    else:
        if x == y == z:
            print("Equilateral triangle")
        elif x==y or y==z or z==x:
            print("Isosceles triangle")
        else:
            print("Scalene triangle")
        return True
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))

if a>10 or a<1:
    print("Boundary limit (1-10) exceeded Re-enter a: ")
    a=int(input())

if b>10 or b<1:
    print("Boundary limit (1-10) exceeded Re-enter b: ")
    b=int(input())

if c>10 or c<1:
    print("Boundary limit (1-10) exceeded Re-enter c: ")
    c=int(input())

f=isTriangle(a,b,c)
if f==False:
    print("Impossible")
