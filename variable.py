num1, num2 = 1, 2
print("기존 변수값=",num1, num2)
num1, num2 = num2, num1
print("교환에 의한 변수값=",num1, num2)

num1, num2 = 1, 2
print("기존 변수값=",num1, num2)

temp = num1
num1 = num2
num2 = temp

print("교환에 의한 변수값=",num1, num2)
