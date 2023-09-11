
 # Creating a class of name Calculator
 # Remember that a class is a blue-print of an Object in OOP (Object Oriented Programming)
class MiniCalculator:
    
    # Creating the initializing function
    # i.e. the characteristics of the Object at the initial runtime
    # You wil parse the "self" parameter to it to enable the function to be found anywhere in the code
    def __init__(self):
        
        # Creating a variable result and initializing its value
        # NB: you use the "self" parameter so that the variable can be accessible from anywhere in the code 
        # i.e (self.variable_name)
        self.result = 0
        
    # Defining a function to add the 2 numbers gotten above
    def add_numbers(self, num1, num2):
        
        # Assigning the value of the result variable to be equal to the sum of num1 and num2
        self.result = num1 + num2
								# We are returning the value of the result field(variable)
        return self.result
        
        
    # Defining a function to subtract the 2 numbers gotten above
    def subtract_numbers(self, num1, num2):
        
        # Assigning the value of the result variable to be equal to the difference between num1 and num2
        self.result = num1 - num2
        return self.result
       
        
        
print(" Hello, and Welcome to my Mini Calculator!")

# Creating two fields(variables)
# presizing the data types using the "int()" method
# And getting their values using the "input()" method
# A method in OOP is what we call a function in programming. So, don't be confused
# NB: you use the "self" parameter so that the variable can be accessible from anywhere in the code
first_num = int(input("Enter a number: "))
second_num = int(input("Enter another number: "))

# Here we are creating an instance(Object) of the class "MiniCalculator" 
# We then store it in a reference variable(calc)
calc = MiniCalculator()

response = int(input("1. Addition\n2. Subtration\nChoose your operator: "))

# Here the code will react based on the response of the user
if (response == 1):
    # "calc" the becomes an Object of MiniCalculator and then has the same functionalities
    # Such as the add_numbers() method defined originaly in the MiniCalculator class
    answer = calc.add_numbers(first_num, second_num)
elif (response == 2):
    answer = calc.subtract_numbers(first_num, second_num)
else:
    print("Choice out of range!") # If the user enters a value other than 1 or 2
	quit()


# Displaying the value of answer
print("Result: " + answer)

# So this is a small overview of OOP in python.
# Thank you!
        
