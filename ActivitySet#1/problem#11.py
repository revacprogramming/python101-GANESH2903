# Tuples

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
x=handle.read()
l=[]
d={}
for line in handle:
    if not line.startswith("From "):
        
        continue
    if line.startswith("From"):
        y=line.split()
        a=y[5]
	m=a.split(':')
    h=m[0]
    l.append(h)
    l.sort()
for word in l:
    d[word]=d.get(word,0)+1

for a,b in d.items():
    print(a,b)
    