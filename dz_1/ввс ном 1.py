print("напиши первое число")
a = int(input())
print("напиши операцию(+, -, *, /)")
b = input()
print("напиши второе число")
c = int(input())
if b == '+':
    print(a + c)
elif b == '-':
    print(a - c)
elif b == '*':
    print(a * c)
elif b == '/':
    print(a // c)
else:
    print("ошибка")
