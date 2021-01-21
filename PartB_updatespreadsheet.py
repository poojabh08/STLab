import os
import openpyxl
from openpyxl import Workbook 
if os.path.exists('student.xlsx'):
    wb = openpyxl.load_workbook('student.xlsx')
    ws = wb.active    
else:
    wb = Workbook()
    ws = wb.active
    ws.append(["Name","USN","Marks 1","Marks 2","Marks 3"])

n = int(input("Enter number of students: "))
for i in range(n):
    print("Enter Name, USN, m1,m2,m3 for student ",i+1)
    data = input().split(" ")
    ws.append([data[0],data[1],data[2],data[3],data[4]])

wb.save('student.xlsx')
os.system('student.xlsx')