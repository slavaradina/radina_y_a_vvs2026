class Normal_weight:
    high = None
    weight = None
    def calc(self, high, weight):
        k = round(weight / (high**2), 2)
        if k < 16:
            return k, "дефицит массы тела"
        elif 16 <= k < 18.4:
            return k, "недостаточная масса тела"
        elif 18.4 <= k < 24.9:
            return k, "нормальная масса тела"
        elif 24.9 <= k < 29.9:
            return k, "избыточная масса тела"
        elif k >= 29.9:
            return k, "ожирение разной степени"
print("напишите свой вес (в кг)")
w = float(input())
print("напишите свой рост (в м)")
h = float(input())
ans = Normal_weight()

print(ans.calc(h, w))


