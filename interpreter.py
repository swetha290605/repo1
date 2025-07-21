exp= input("Expression: ")
exp=exp.split(" ")
x=exp[0]
y=exp[1]
z=exp[2]
if y=="+":
    res=int(x)+int(z)
    print(float(res))
elif y=="-":
    res=int(x)-int(z)
    print(float(res))
elif y=="*":
    res=int(x)*int(z)
    print(float(res))
elif y=="/" and z!="0":
    res=int(x)/int(z)
    print(res)
else:
    print("Invalid Expression")