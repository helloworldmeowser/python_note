"""The following notes are from module four Google IT Automation with Python through Coursera."""
print("--------------String: Index Method Example-------------------")
txt = "Hello, welcome to my world."
a = txt.index("e") # count the letter e
print(a)
answer = "YES" # turn these to lowercase
if answer.lower() == "yes": 
  print("User said yes")
print("--------------String: .strip Method Example-------------------")
word = "     banana     " # remove spaces
b = word.strip()
print("of all fruits", b, "is my favorite")
print("--------------String: .count Method Example-------------------")
fruits = ['apple', 'banana', 'cherry']
d = fruits.count("cherry")
print(d)
print("--------------String: .isnumeric Method Example-------------------")
number = "565543"
c = number.isnumeric()
print(c)
print("--------------String: .endswith Method Example-------------------")
test = "Hello, welcome to my world."
f = test.endswith("my world.")
print(f)
print("--------------String: formatting Method Example-------------------")
def to_celsius(m):
  return (m-32)*5/9
for m in range(0,101,10):
  print("{:>3} F | {:>6.2f} C".format(m, to_celsius(m)))
print("--------------List: List and Tuples Method Example-------------------")
fullname = ('Grace', 'M', 'Hopper')
print(fullname)
print("--------------List: List and Tuples Method Other Example -------------------")
def convert_seconds(seconds):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  remaining_seconds = seconds - hours * 3600 - minutes * 60
  return hours, minutes, remaining_seconds
result = convert_seconds(5000)
type(result)
print(result)
print("--------------List: List and Tuples Method Other Example -------------------")
def convert_seconds(seconds):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  remaining_seconds = seconds - hours * 3600 - minutes * 60
  return hours, minutes, remaining_seconds
hours, minutes, seconds = convert_seconds(1000)
print(hours, minutes, seconds)
print("--------------List: List and Tuples Method Other Example -------------------")
print("The winners: ")
winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
  print("{} - {}".format(index + 1, person))
print("--------------List: List Comprehension Example -------------------")
languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)
print("--------------List: List Comprehension For Loop Example -------------------")
# This block of code changes the year on a list of dates.
# The "years" list is given with existing elements. 
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

# The variable "updated_years" is initialized as a list data type 
# using empty square brackets []. This list will hold the new list
# with the updated years. 
updated_years = []
# The for loop checks each "year" element in the list "years".
for year in years:
    # The if-statement checks if the "year" element ends with the 
    # substring "2023". 
    if year.endswith("2023"):
        # If True, then a temporary variable "new" will hold the 
        # modified "year" element where the "2023" substring is 
        # replaced with the substring "2024".
        new = year.replace("2023","2024")
        # Then, the list "updated_years" is appended with the changed
        # element held in the temporary variable "new".
        updated_years.append(new)
    # If False, the original "year" element will be appended to the 
    # the "updated_years" list unchanged.
    else:
        updated_years.append(year)

print(updated_years) 
# Should print ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]
print("--------------List: List Comprehension with Return Example -------------------")
# This list comprehension creates a list of squared numbers (n*n). It
# accepts two integer variables through the function’s parameters.
def squares(start, end):
    # The list comprehension calculates the square of a variable integer 
    # "n", where "n" ranges from the "start" to "end" variables inclusively.
    # To be inclusive in a range(), add +1 to the end of range variable.
    return [n*n for n in range(start,end+1)] 

print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
