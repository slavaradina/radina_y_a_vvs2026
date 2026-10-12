def calc(a, b, c):
        if b == '+':
            return a + c
        elif b == '-':
            return a - c
        elif b == '*':
            return a * c
        elif b == '/':
            return a // c
        else:
            return "ошибка"
while True:
    print("напиши первое число")
    a = int(input())
    print("напиши операцию(+, -, *, /)")
    b = input()
    print("напиши второе число")
    c = int(input())
    print(calc(a, b, c))
    
