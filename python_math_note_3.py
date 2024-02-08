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