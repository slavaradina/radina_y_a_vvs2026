import random

n = 5
m = 7

pole = []
for y in range(n):
    stroka = []
    for x in range(m):
        stroka.append("пусто")
    pole.append(stroka)

vse_kletki = []
for y in range(n):
    for x in range(m):
        if not (x == 0 and y == 0):
            vse_kletki.append((x, y))

random.shuffle(vse_kletki)

monstr  = random.randint(5, 15)   
zoloto    = random.randint(2, 8)
aptechka  = random.randint(1, 4)

poziciya_klucha        = vse_kletki.pop()
poziciya_sunduka       = vse_kletki.pop()
poziciya_dveri         = vse_kletki.pop()
poziciya_mecha         = vse_kletki.pop()
poziciya_ruzhya        = vse_kletki.pop()
poziciya_zacharovaniya = vse_kletki.pop()

pole[poziciya_klucha[1]][poziciya_klucha[0]]                 = "ключ"
pole[poziciya_sunduka[1]][poziciya_sunduka[0]]               = "сундук"
pole[poziciya_dveri[1]][poziciya_dveri[0]]                   = "дверь"
pole[poziciya_mecha[1]][poziciya_mecha[0]]                   = "меч"
pole[poziciya_ruzhya[1]][poziciya_ruzhya[0]]                 = "ружьё"
pole[poziciya_zacharovaniya[1]][poziciya_zacharovaniya[0]]   = "зачарование"

for i in range(monstr):
    p = vse_kletki.pop()
    pole[p[1]][p[0]] = "монстр"

for i in range(zoloto):
    p = vse_kletki.pop()
    pole[p[1]][p[0]] = "золото"

for i in range(aptechka):
    p = vse_kletki.pop()
    pole[p[1]][p[0]] = "аптечка"

kod = str(random.randint(1000, 9999))

hp = 100
igrok_x = 0
igrok_y = 0

inventar = []
oruzhie = "нет"
zacharovano = False
znaet_kod = False
zoloto = 0

def pokazat_pole():
    print()
    print("  0 1 2 3 4 5 6")
    for y in range(n):
        stroka = ""
        for x in range(m):
            if x == igrok_x and y == igrok_y:
                stroka = stroka + "я "
            else:
                stroka = stroka + "* "
        print(y, stroka)
    print()

print("Добро пожаловать в лабиринт!")
print("Количество монстров и предметов каждый раз случайное!")
print()
print("Управление: w - вверх, s - вниз, a - влево, d - вправо")
print()
print("Что бывает в комнатах:")
print("  монстр      - нападает: 20 урона без оружия,")
print("                15 с оружием, 10 с зачарованным")
print("  меч, ружьё  - оружие (урон от монстров меньше)")
print("  зачарование - усиливает оружие (урон монстра ещё меньше)")
print("  аптечка     - восстанавливает +30 HP")
print("  золото      - просто блестит")
print("  ключ        - нужен для сундука")
print("  сундук      - откроется только с ключом")
print("  дверь       - выход, откроется только со знанием кода")

while True:
    pokazat_pole()
    print("HP:", hp)
    print("Инвентарь:", inventar)
    if oruzhie != "нет":
        if zacharovano == True:
            print("Оружие:", oruzhie, "(ЗАЧАРОВАННОЕ! Монстры бьют всего на 10 HP)")
        else:
            print("Оружие:", oruzhie, "(монстры бьют на 15 HP)")
    print("Золото:", zoloto)

    hod = input("Твой ход (w/s/a/d): ")

    noviy_x = igrok_x
    noviy_y = igrok_y

    if hod == "w":
        noviy_y = noviy_y - 1
    elif hod == "s":
        noviy_y = noviy_y + 1
    elif hod == "a":
        noviy_x = noviy_x - 1
    elif hod == "d":
        noviy_x = noviy_x + 1
    else:
        print("Напиши w, a, s или d.")
        continue

    if noviy_x < 0 or noviy_x >= m or noviy_y < 0 or noviy_y >= n:
        print("Стена!")
        continue

    igrok_x = noviy_x
    igrok_y = noviy_y

    chto_tut = pole[igrok_y][igrok_x]

    if chto_tut == "монстр":
        if zacharovano == True:
            print("Монстр напал! Но зачарованное оружие сильно тебя защищает.")
            hp = hp - 10
            print("Ты потерял 10 HP. Осталось:", hp)
        elif oruzhie != "нет":
            print("Монстр напал! С оружием ты отбился, но не полностью.")
            hp = hp - 15
            print("Ты потерял 15 HP. Осталось:", hp)
        else:
            print("Монстр напал! У тебя нет оружия - получил 20 урона!")
            hp = hp - 20
            print("Осталось HP:", hp)
        pole[igrok_y][igrok_x] = "пусто"
        if hp <= 0:
            print("Монстр тебя победил... Игра проиграна.")
            break

    elif chto_tut == "ключ":
        print("Ты нашёл ключ! Теперь можно открыть сундук.")
        inventar.append("ключ")
        pole[igrok_y][igrok_x] = "пусто"

    elif chto_tut == "сундук":
        if "ключ" in inventar:
            print("Ты открыл сундук. Внутри записка с кодом:", kod)
            inventar.append("записка с кодом")
            znaet_kod = True
            pole[igrok_y][igrok_x] = "пусто"
        else:
            print("Это сундук. Он заперт. Нужен ключ!")

    elif chto_tut == "дверь":
        if znaet_kod == True:
            print("Ты набрал код", kod, "на двери...")
            print("Ты нашел выход! Поздравляю!")
            print("Золота собрано:", zoloto)
            break
        else:
            print("Это дверь-выход. На ней кодовый замок, но ты не знаешь код.")

    elif chto_tut == "меч":
        print("Ты нашёл меч! Теперь монстры бьют тебя слабее (15 вместо 20).")
        oruzhie = "меч"
        inventar.append("меч")
        pole[igrok_y][igrok_x] = "пусто"

    elif chto_tut == "ружьё":
        print("Ты нашёл ружьё! Теперь монстры бьют тебя слабее (15 вместо 20).")
        oruzhie = "ружьё"
        inventar.append("ружьё")
        pole[igrok_y][igrok_x] = "пусто"

    elif chto_tut == "зачарование":
        if oruzhie == "нет":
            print("Здесь алтарь зачарования, но тебе нечего зачаровать.")
            print("Сначала найди меч или ружьё!")
        elif zacharovano == True:
            print("Твоё оружие уже зачаровано.")
        else:
            print("Твоё оружие", oruzhie, "стало зачарованным!")
            print("Теперь монстры бьют тебя всего на 10!")
            zacharovano = True
        pole[igrok_y][igrok_x] = "пусто"

    elif chto_tut == "аптечка":
        hp = hp + 30
        if hp > 100:
            hp = 100
        print("Ты нашёл аптечку! Восстановил здоровье. Теперь HP:", hp)
        pole[igrok_y][igrok_x] = "пусто"

    elif chto_tut == "золото":
        zoloto = zoloto + 10
        print("Ты нашёл золото! +10. Всего золота:", zoloto)
        pole[igrok_y][igrok_x] = "пусто"

    else:
        print("Тут пусто.")

print("Конец игры.")




