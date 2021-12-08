a=int(input('Enter some numbers with 3 or more characters'))
b=0
while a>0:
    b=b+a%10
    a=a//10
print(b)

