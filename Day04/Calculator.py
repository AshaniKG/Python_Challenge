x = int (input("Enter first number: "))
y = int (input("Enter second number: "))

#function for addition 
def add_function():
    addition = x + y 
    return addition 

#function for subtraction
def sub_function():
    subtraction = x - y
    return subtraction

#function for multiplication
def multi_function():
    multiplication = x * y
    return multiplication

#function for division
def div_function():
    division = x / y
    return division

print ("\nOperation Menu\n 1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n 5.Exit Operation\n")

operation = int (input("Choose an operation (Enter operation number): "))

while operation != 5:

    #if operation is addition
    if operation == 1:
        print ("The answer is:",add_function())


    #if operation is subtraction
    elif operation == 2:
        print ("The answer is:",sub_function())

    #if oeration is multiplication
    elif operation == 3:
        print ("The answer is",multi_function())

    #if oeration is division 
    elif operation == 4:
        print ("The answer is",div_function())

    operation = int (input("\nChoose an operation (Enter operation number): "))
        


        
