# Strings

text = "X-DSPAM-Confidence:    0.8475"
str=text
x=str.find("0.8")
y=str[x:]
print(float(y))
