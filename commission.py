l = 45.0
s = 30.0
b = 25.0
no_lock = 0
tl = 0
ts = 0
tb = 0
while(no_lock != -1):
    no_lock = int(input("Enter no. of locks:"))
    no_stock = int(input("Enter no. of stocks:"))
    no_barrel = int(input("Enter no. of barrels:"))
   
    tl,ts,tb=tl + no_lock,ts + no_stock,tb + no_barrel
    if(tl > 70 or tb > 90 or ts > 80):
        print("Limit exceeded")
        tl -= no_lock
        tb -= no_barrel
        ts -= no_stock

sales = (ts* s) + (tb * b) + (tl * l)
if(sales > 1800):
    comm = 0.1 * 1000
    comm += 0.15 * 800
    comm += 0.2 * (sales - 1800)
elif sales > 1000:
    comm = 0.1 * 1000
    comm += 0.15 * (sales - 1000)
else:
    comm = 0.1 * sales
print("Total Sales: {}".format(sales))
print("Commission: {}".format(comm))