print("The following code is to print three student's name, age, and major: ")
def student_list(people):
    # Iterate over each "person" in the given "people" list of tuples. 
    for people in people: 
        # Separate the 3 items in each tuple into 3 variables:
        # "name", "age", and "major"   
        name, age, major = people  
        # Format the required sentence and place the 3 variables 
        # in the correct placeholders using the .format() method.
        print("{} is {} years old and major in {}".format(name,age, major))

# Call to the function:
student_list([("Amy", 20, "computer science"), ("Helen", 21, "mechanical engineer"), ("Maria", 25, "aeronautical science")])

print("The following code is to add items together (cheese, milk, eggs, bread, coffee, ham, oil, potatoes): ")
def addition_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for item, price in basket.items():
		# Add each price to the total calculation
		# dictionary items
		total += price
	# Limit the return value to 2 decimal places
	return round(total, 2)  
groceries = {"cheese": 1.56, "milk": 5.50, "eggs": 12.99, "bread": 4.59, 
	"coffee": 6.99, "ham": 3.39, "oil": 2.98, "potatoes": 2.44}
print(addition_prices(groceries))

print("The following code print 1 - 10 :")
number = 1 # Initialize the variable
while number <= 10: # Complete the while loop condition
    print(number, end=" ")
    number += 1 # Increment the variable
print("The following code print yes and no:")
for number in range(5):
    # number % 2 without it the code would just print yes only once
    if number % 2 == 0:
        print("yes")
    else:
        print("no")

print("Multiplication table till 5 for 3,5,8:")
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    # Complete the while loop condition.
    while multiplier <= 5:
        result = number * multiplier 
        if  result > 25:
            break
            # Enter the action to take if the result > 25
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        
        # Increment the appropriate variable
        multiplier += 1
multiplication_table(3) 
multiplication_table(5) 
multiplication_table(8) 

print("Best practice for writing code: ")
def reminder_code(sentence, word):
    # Complete the return statement using a string method.
    #word = will not capitalize but word.upper() will capitalize
    return sentence.replace(word, word.upper())
print(reminder_code("create a reuseable function", "reuseable"))
print(reminder_code("add comment where leave yourself notes", "add"))
print(reminder_code("refactor code", "refactor"))

print("The following code will print bill cost: ")
def bill_history(payment_prices):
  result = ""
  # Complete the for loop to iterate through the key and value items 
  # in the dictionary.
  for pay, price in payment_prices.items(): 
    result += "A {} costs {} dollars\n".format(pay, price) # Use a string method to format the required string. 
  return result
print(bill_history({"Rent":1600, "Internet":80, "Renter Insurance":17, "Car Insurance":420}))

#note that range(start, stop, step)
height = eval(input("Enter height of christmas tree: "))
for row in range(height):
    #From small to large number
    for count in range(height - row):
        print(end=" ")
    for count in range(2*row + 1):
        print(end="*")
    print()
