# Regular Expressions
# https://www.py4e.com/lessons/regex
import re
data=open('http://py4e-data.dr-chuck.net/regex_sum_1551146.txt')
sum=0
y=[]
for line in data:
     line=line.rstrip()
     x=re.findall('[0-9]+')
     if len(x)>0:
       #print(x)
       for i in range of len(x):
          y.appent(int(x[i]))   
                  sum = sum+y[i]
print('The sum of numbers in given data is' ,sum)
