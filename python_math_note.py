"""The following notes are from module one and two Google IT Automation with Python through Coursera."""
print(10 + 30) # ADDITION: Add two numbers with +
print(50 - 30) # SUBTRACTION: Subtract a number with -
print(4 * 6) # MULTIPLICATION: Multiply two numbers with *
print(22 / 7) # DIVISION: Divide a number by another with /
print(22 // 7) # FLOOR DIVISION: Integer divide a number with //
print(3 ** 4) # EXPONENT: Raise to the power with **
print(22 % 7) # MODULO OPERATION: Returns 1 # Get the remainder  after division with %

#Python's order of operation is PEMDAS
#Parentheses: (),{},[]

print(2+2/((2+2)+(2**2)))

#Keywords: special words that are reserved for specific purposes and that can only be used for those purpose
#in, not, or, for, while, return

#Python Data Type Reminder:
print(type("a"))
#class str
print(type(2))
#class int
print(type(2.5))
#class float

#other examples
print(7+8.5)
print("a"+"b"+"c")
base = 6
height = 3
area = (base*height)/2
print("The area of the triangle is: " + str(area))

#Variables Annotated Reminder
import typing
# Define a variable of type str
z: str = "Hello, world!"
# Define a variable of type int
x: int = 10
# Define a variable of type float
y: float = 1.23
# Define a variable of type list
list_of_numbers: typing.List[int] = [1, 2, 3]
# Define a variable of type tuple
tuple_of_numbers: typing.Tuple[int, int, int] = (1, 2, 3)
# Define a variable of type dict
dictionary: typing.Dict[str, int] = {"key1": 1, "key2": 2}
# Define a variable of type set
set_of_numbers: typing.Set[int] = {1, 2, 3}

# This function calculates the number of days in a variable number of 
# years, months, and days. These variables are provided by the user and
# are passed to the function through the function’s parameters.
def find_total_days(years, months, days):
# Assign a variable to hold the calculations for the number of days in
# a year (years*365) plus the number of days in a month (months*30) plus
# the number of days provided through the "days" parameter variable.
    my_days = (years*365) + (months*30) + days
# Use the "return" keyword to send the result of the "my_days"  
# calculation to the function call. 
    return my_days
 
# Function call with user provided parameter values. 
print(find_total_days(2,5,23))

# This function converts fluid ounces to milliliters and returns the 
# result of the conversion.
def convert_volume(fluid_ounce):
# Calculate value of the "ml" variable using the parameter variable 
# "fluid_ounce". There are approximately 29.5 milliliters in 1 fluid
# ounce.
    ml = fluid_ounce * 29.5  
# Return the result of the calculation.  
    return ml
 
# Call the conversion from within the print() function using 2 fluid 
# ounces. Convert the return value from a float to a string.  
print("The volume in milliliters is " + str(convert_volume(2)))
 
# Call the function again and double the 2 fluid ounces from within
# the print function.
print("The volume in milliliters is " + str(convert_volume(2)*2))
# Alternative calculation:
# print("The volume in milliliters is " + str(convert_volume(4))

#Practice Quiz
# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# Comparing 
print(10>1)
#True
print("cat" == "dog")
#False
print (1 != 2)
#True

# Comparison Operators with Equations
#== equality != not equal to > greater than < less than
#>= greater than or equal to <= less than or equal to


print(32 == 30+2)   # The == operator checks if the 2 values are 
True                # equal to each other. If they are equal, 
                    # Python returns a True result.


print(5+10 == 6+7)  # If the two values are not equal, as in the
False               # expression 5+10 == 6+7 (or 15 == 13), Python          
                    # returns a False result.


print(10-4 != 10+4) # The != operator checks if the 2 values are
True                # NOT equal to each other. If true, Python              
                    # returns a True result. 


print(9/3 != 3*1)   # In this last example, 9/3 != 3*1 (or 3 != 3)
False               # is false. So, Python returns a False value.

# The == operator can check if two strings are equal to each other. 
# If they are equal, the Python interpreter returns a True result.
print("a string" == "a string")
True


# In this example, the equality == comparison is between "4 + 5" and
# 4 + 5. Since the left data type is a string and the right data type
# is an integer, the two values cannot be equal. So, the comparison
# returns a False result.
print("4 + 5" == 4 + 5)
False


# The != operator can check if the two strings are NOT equal to each
# other. If they are indeed not equal, then Python returns a True result.
print("rabbit" != "frog")
True


# In this example, the variable event_city has been assigned the string 
# value "Shanghai". This variable is compared to a static string, 
# "Shanghai", using the != operator. As, the strings "Shanghai" and 
# "Shanghai" are the same, the comparison of "Shanghai" != "Shanghai" 
# is false. Accordingly, Python will return a False result.
event_city = "Shanghai"
print(event_city != "Shanghai")
False

# This last example illustrates the result of trying to compare two
# items of different data types using the equality == operator. The
# two items are not equal, so the comparison returns False.
print("three" == 3)
False

# Use the Unicode chart in Part 2 to determine if the Unicode values of 
# the first letters of each string are higher, lower, or equal to one
# another. 


var1 = "my computer" >= "my chair"
var2 = "Spring" <= "Winter"
var3 = "pineapple" >= "pineapple"
 
print("Is \"my computer\" greater than or equal to \"my chair\"? Result: ", var1)
print("Is \"Spring\" less than or equal to \"Winter\"? Result: ", var2)
print("Is \"pineapple\" less than or equal to \"pineapple\"? Result: ", var3)

#Logical Operators: and, or, not
# Example 1
print((6*3 >= 18) and (9+9 <= 36/2))

# A function is created with the def() keyword. The parameter
# variable "time_as_string" is passed to the function through a 
# call to the function.
def task_reminder(time_as_string):

    # The following if-elif-else block assigns various strings to
    # the variable "task" depending on specific conditions. The
    # test conditions are set using the == equality comparison 
    # operator. In this case, the time passed through the 
    # "time_as_string" parameter variable is tested as the 
    # specific condition. So, if the time  is "11:30 a.m.", then 
    # "task" is assigned the value: "Run TPS report".
    if time_as_string == "8:00 a.m.":
        task = "Check overnight backup images"
    elif time_as_string == "11:30 a.m.":
        task = "Run TPS report"
    elif time_as_string == "5:30 p.m.":
        task = "Reboot servers"
    # The else statement is a catchall for all other values of 
    # the "time_as_string" parameter variable not listed in the
    # if-elif block of code.
    else:
        task = "Provide IT Support to employees"

    # This line returns the value of "task" to the function call.
    return task

# This line calls the function and passes a parameter  
# ("10:00 a.m.") to the function.
print(task_reminder("10:00 a.m."))
# Should print "Provide IT Support to employees"
