def op1(a, b):
    return a + b
def op2(a, b):
    return a - b
def op3(a, b):
    return a * b
def op4(a, b):
    return a // b

print("напиши первое число")
a = int(input())
print("напиши операцию(+, -, *, /)")
b = input()
print("напиши второе число")
c = int(input())

if b == '+':
    print(op1(a, c))
elif b == '-':
    print(op2(a, c))
elif b == '*':
    print(op3(a, c))
elif b == '/':
    print(op4(a, c))
else:
    print("ошибка")
