#Que1-->Create a function to calculate the area of a sphere by taking radius from user.
def cal_area(num):
    area=4*3.14*num*num
    print("the area of sphere is:",area)

r=int(input("enter the radius"))
cal_area(r)
print()

#Que2-->Print all the perfect numbers between 1 and 1000
"""An integer number is said to be "perfect number" if its factors ,
including 1(but not the number itself),sum to the number"""
def perfect_num(num):
    sum=0
    for i in range(1,num):
        if num % i == 0:
            sum = sum+i
    if sum == num:
        print(num)
    
n=int(input("enter the number upto which you want to check for perfect number:"))
for i in range(1,n):
    perfect_num(i)
print()

#Que3-->Print Multiplication table of a user defined number
def mul(num):
    for i in range(1,11):
         a=num*i
         print('%d' " * " '%d' "  = " %(num,i),a)
         
num=int(input("enter the number:"))
print("multiplication table for %d is:" %num)
mul(num)
print()

#Que4-->Calculate the power of a number using recursion
def power(a,b):
    if b==1:
        return a
    else:
        return(a*power(a,b-1))

a=int(input("enter the number of which you want to find raised power:"))
b=int(input("enter the  second number:"))        
print(power(a,b))
print()

#CLASS AND OBJECTS-1

#Que1-->Get keys corresponding to a value in user defined dictionary.
n=int(input("enter the number of elements:"))
dict={}
for i in range(n):
    a=input().split()
    dict[a[0]]=int(a[1])
print("dictionary is:",dict)
print()

#Que2-->Create a dictionary and store student names and create nested dictionary to store the subject wise marks of every student.Print the marks of a given student from that ductionary for every subject.
student={'abc':{78,89,58},'lmn':{90,100,68},'def':{46,67,90}}
n=input("enter the name of student whose marks you want to see:")
for key,value in student.items():
    if n == key:
        print(value)
print()
