def lvl_1(method, text):
    if method == "upper":
        return text.upper()
    elif method == "lower":
        return text.lower()
    elif method == "capitalize":
        return text.capitalize()
    
def lvl_2(method, text):
    if method == "find":
        print("напишите слово, индекс которого хотите найти")
        wrd = input()
        return text.find(wrd)
    elif method == "replace":
        print("напишите слово, которое хотите заменить")
        wrd1 = input()
        print("напишите слово для замены")
        wrd2 = input()
        return text.replace(wrd1, wrd2)
    elif method == "count":
        print("напишите символ или строку, количество которых хотите посчитать")
        wrd = input()
        return text.count(wrd)
    
def lvl_3(method, text):
    if method == "split":
        print("напишите символ, по которому делится строка")
        sym = input()
        return text.split(sym)
    elif method == "split + join":
        print("напишите символ, по которому делится строка")
        sym1 = input()
        print("напишите символ, на который заменить предыдущий символ")
        sym2 = input()
        return sym2.join(text.split(sym1))
    elif method == "join":
        print("напишите символ, по которому делятся элементы списка")
        sym = input()
        return sym.join(text.split(','))
    
def lvl_4(method, text):
    if method == "isdigit":
        return text.isdigit()
    elif method == "isalpha":
        return text.isalpha()
    elif method == "strip":
        print("напишите символы, которые хотите удалить")
        sym = input()
        return text.strip(sym)
        
while True:
    print("выберите уровень(1, 2, 3, 4, 5)")
    lvl = int(input())
    if lvl == 1:
        test = "пРиВет МИР"
        print("метод upper: пРиВет МИР -", test.upper())
        print("метод lower: пРиВет МИР -", test.lower())
        print("метод capitalize: пРиВет МИР -", test.capitalize())
        print("выберите метод (upper, lower, capitalize)")
        method = input()
        print("напишите свой текст")
        text = input()
        print(lvl_1(method, text))
    if lvl == 2:
        test = "Ботать это круто. Очень круто"
        print(f"тестовая строка - {test}")
        print("метод find(ищем индекс первого вхождения слова 'круто') - ", test.find("круто"))
        print("метод replace(замена слова 'круто' на слово 'некруто') - ", test.replace("круто", "не круто"))
        print("метод count(считаем количество букв 'о') - ", test.count("о"))
        print("выберите метод(find, replace, count)")
        method = input()
        print("напишите свой текст")
        text = input()
        print(lvl_2(method, text))
    if lvl == 3:
        test = "1,2,3,4"
        print(f"тестовая строка - {test}")
        print("метод split(делим строку по запятым)", test.split(",") )
        print("метод split + join(разделяем строку пробелами)", " ".join(test.split(",")) )
        print("метод join (разделяем список символами '!'):", '!'.join(test.split(",")))
        print("выберите метод(split, split + join, join)")
        method = input()
        print("напишите свой текст (для метода join в виде списка str1,str2,...)")
        text = input()
        print(lvl_3(method, text))
    if lvl == 4:
        test1 = "1234*&%$"
        test2 = "   abc1234   "
        print(f"тестовые строки - '{test1}' и '{test2}'")
        print("метод isdigit (проверяет все ли символы в строке являются цифрами):", test1.isdigit(), test2.isdigit())
        print("метод isalpha (проверяет все ли символы в строке являются буквами):", test1.isalpha(), test2.isalpha())
        print("метод strip (убирает символы в начале и в конце строки):", test1.strip(), test2.strip())
        print("выберите метод(isdigit, isalpha, strip)")
        method = input()
        print("напишите свой текст")
        text = input()
        print(lvl_4(method, text))
    if lvl == 5:
        test = '     pYtHon;is;AWESome;       '
        test = test.strip()
        test = " ".join(test.split(";"))
        test = test.lower()
        print(test.capitalize())
        
