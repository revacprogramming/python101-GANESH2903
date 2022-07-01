#list
fname = input("Enter file name: ")
fh = open(fname)
x= list()
y=fh.read()
words=y.split()


for n in words: 
    if n not in x:
        x.append(n)
        
x.sort()
print(x)
