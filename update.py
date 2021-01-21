import os
Folcount = 0
filecount = 0
jpgc = cppc = cc = pyc = xlsxc = htmlc= oc = 0
for path,dirs,files in os.walk("/home/poojahegde/newtry/STLab"):
    for fi in files:
        print(os.path.join(path,fi))

for base,dirs,files in os.walk("/home/poojahegde/newtry/STLab"):
    for d in dirs:
        Folcount+=1
    for f in files:
        filecount+=1
        if f.endswith(".jpg"):
            jpgc+=1
        elif f.endswith('.cpp'):
            cppc+=1
        elif f.endswith('.c'):
            cc+=1
        elif f.endswith('.py'):
            pyc+=1
        elif f.endswith('.xlsx'):
            xlsxc+=1
        elif f.endswith('.html'):
            htmlc+=1
        else:
            oc+=1

print("image files ",jpgc)
print("cpp files ",cppc)
print("c files ",cc)
print("python files ",pyc)
print("HTML files ",htmlc)
print("Excel files ",xlsxc)
print("Other files ",oc)
print("Files ",filecount)
print("Directory ",Folcount)