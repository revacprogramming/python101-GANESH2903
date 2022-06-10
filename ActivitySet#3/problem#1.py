import math
n = int(input("Enter how many rectangles do you have???"))
px=[]
py=[]
a=[]
for i in range(n):
  x1,y1,x2,y2,x3,y3 =map(float,input('Enter any three points of a rectangle:').split())
  
  #px.extend([x1,x2,x3])
  #py.extend([y1,y2,y3])
  l1=math.sqrt(math.pow(x1-x2,2) + math.pow(y2-y1,2))
  l2=math.sqrt(math.pow(x2-x3,2) + math.pow(y2-y3,2))
  l3=math.sqrt(math.pow(x3-x1,2) + math.pow(y3-y1,2))
  if (l1>l2 and l1>l3):
      area = l2*l3
  elif (l2>l1 and l2>l3):
      area = l1*l3
  else :
      area = l1*l2
  a.append(area)      
print(a)
#print(type(x1))
#print(type(x2))
#print(type(x3))
#print(type(y1))
#print(type(y2))