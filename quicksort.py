def quicksort(a,l1,h):
    if(l1<h):
        pi = a[l1]
        l = l1 + 1
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
        a[l1], a[h] = a[h], a[l1]
        p = h
        quicksort(a,l1,p-1)
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