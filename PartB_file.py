import os
Fcount = 0
Folcount=0
tif_c=pdf_c=jpg_c=txt_c=ppt_c=oth_c=cpp_c=c_c=py_c=xl_c=html_c=0
d = "/home/poojahegde/newtry/STLab"
for path,dirs,files in os.walk(d):
    for filename in files:
        print(os.path.join(path,filename))
for base,dirs, files in os.walk(d):
    for directories in dirs:
        Folcount += 1
    for file in files:
        if file.endswith('.jpg'):
            jpg_c+=1
        elif file.endswith('.png'):
            jpg_c+=1
        elif file.endswith('.txt'):
            txt_c+=1
        elif file.endswith('.cpp'):
            cpp_c+=1
        elif file.endswith('.c'):
            c_c+=1
        elif file.endswith('.py'):
            py_c+=1
        elif file.endswith('.html'):
            html_c+=1
        elif file.endswith('.xlsx'):
            xl_c+=1
        else: oth_c+=1
        Fcount += 1
print("Folder count: ",Folcount)
print("Images count: ",jpg_c)
print("Text file count: ",txt_c)
print("CPP file count: ",cpp_c)
print("C file count: ",c_c)
print("Python file count: ",py_c)
print("Excel sheets count: ",xl_c)
print("HTML files: ",html_c)
print("Other files: ",oth_c)
print("total file count:", Fcount)