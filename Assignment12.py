#Ques 1

import datetime as dt
ob=dt.date(2018,9,1)
print("Day is",ob.weekday())   #since weekday() is an instance method we can't call it directly by class name so it is called by instance of class date


#Ques 2

import webbrowser as wb
y=input("Enter your youtube search: ")
wb.open("https://www.youtube.com/results?search_query=%s"%y)


#Ques 3

import os
os.chdir("C:\\Users\Sahil Sharma\Desktop\py")       #changes the cwd
for file in os.listdir():
    rename=input("Enter the new name: ")
    os.rename(file,rename+'.jpg')
