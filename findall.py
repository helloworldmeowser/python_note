#Assigment Summary: problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

import re #must import re for regular expression
import urllib.request #import this because it is easier to open a website than to download it to open it

url = 'https://py4e-data.dr-chuck.net/regex_sum_1987754.txt' #the website that it will open
response = urllib.request.urlopen(url)
data = response.read().decode('utf-8')

total = 0
string_nums = re.findall('[0-9]+', data) #tell us what is in the string and give us the number for the assignment
for value in string_nums:
    total += int(value)

print(total)#Answer is 364254

#Second way to solve this assignment
#import re
#h = open("file name file location", "r")
#numlist = []
#for line in hand:
#   line = line.restrip()
#   integers = re.findall('([0-9]+)', line)
#   for number in integers:
#       numlist.append(int(number))
#print(sum(numlist))