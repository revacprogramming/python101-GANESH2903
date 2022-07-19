import math
n = int(input("Enter how many rectangles do you have???"))
a,p,Points=[],(),[]

def findarea():
  for i in range(n):
    x1,y1,x2,y2,x3,y3 =map(float,input('Enter any three points of a   rectangle:').split())
    
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
    p1,p2,p3 = (x1,y1),(x2,y2),(x3,y3)
    Pi = (p1,p2,p3)
    Points.append(Pi)
  return a,Points
def output():
  for i in range(n):
    Point = Points[i]
    y = str(a[i])
    print('Area of rectangle with vertices {0[0]},{0[1]},{0[2]}'.format(Point)+" is "+y)
findarea()
output()
