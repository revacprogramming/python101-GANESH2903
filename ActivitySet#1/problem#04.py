# Conditional Execution

hrs = input("Enter hours? ")
h = float(hrs)
r=float(input("Enter rate:"))
if h<=40:
    rp=h*r
    print(rp)
else:
    otp=40*r+(h-40)*r*1.5
    print(otp)
