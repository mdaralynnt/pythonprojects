#first define the functions neede when working with mathematical calculations
#these functions are add, subtract, multiply, divide
#the program should be able to provide the user with some options upon inserting some numbers into the calculator
# call the functions
#add while loop to continue the program until the user wnats to exit

def add(a,b):
    answer=a+b
    print(str(a)+ "+"+str(b)+"="+str(answer)+"\nc")

def sub(a,b):
    difference=a-b
    print(str(a)+ "-"+str(b)+"="+str(difference)+"\n")

def mul(a,b):
    multiple=a*b
    print(str(a)+ "*"+str(b)+"="+str(multiple)+"\n")

def div(a,b):
    quotient=a/b
    print(str(a)+ "/"+str(b)+"="+str(quotient)+"\n")

while True:
    print("A.Addition")
    print("B.Subtraction")
    print("C.Multiplication")
    print("D.Division")
    print("E.Exit")

    operation=input("Enter your preffered operation:")
    if operation =='a' or operation=='A':
        print ('Addition')
        a= int(input("enter the first number:"))
    
        b=int(input("enter the second number:"))
        add(a,b)

    elif operation=='b'or operation=='B':
        print("subtraction")
        a=int(input("enter the first number:"))
        b=int(input("enter the second number:"))
        sub(a,b)

    elif operation=='c'or operation=='C':
        print("multiplication")
        a=int(input("enter the first number:"))
        b=int(input("enter the second number:"))
        mul(a,b)

    elif operation=='d'or operation=='D':
        print("division")
        a=int(input("enter the first number:"))
        b=int(input("enter the second number:"))
        div(a,b) 

    elif operation=='e'or operation=='E':
        print("program ended")
        quit()



