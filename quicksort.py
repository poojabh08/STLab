
def partition(a, s, h):
    pi = a[s]
    l = s + 1
    h = h

    while True:
        
        while l <= h and a[h] >= pi:
            h = h - 1

        while l <= h and a[l] <= pi:
            l = l + 1

        if l <= h:
            a[l], a[h] = a[h], a[l]
        else:
            break

    a[s], a[h] = a[h], a[s]

    return h



def quicksort(a,l,h):
    if(l<h):
        p=partition(a,l,h)
        quicksort(a,l,p-1)
        quicksort(a,p+1,h)

n=int(input("Enter no of elements: "))
print("Enter elements of a: ")
l=[]
for i in range(n):
    e = int(input())
    l.append(e)
print("Before sorting: ")
for i in range(n):
    print(l[i], end =" ")
print("\nAfter sorting: ")
quicksort(l,0,n-1)
for i in range(n):
    print(l[i], end =" ")
print()