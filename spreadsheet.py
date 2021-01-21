import os
from openpyxl import Workbook
wb = Workbook()
ws = wb.active

ws.append(["Name","USN","Marks1","Marks2","Marks3"])

for i in range(10):
    print("Enter Name, USN, Marks1, Marks2, Marks3 for student")
    data = input().split(" ")
    ws.append([data[0],data[1],data[2],data[3],data[4]])

wb.save("studentdetails.xlsx")
os.system("studentdetails.xlsx")



