import math
def funct():
    fun = input("Введите необходимую функцию (Сложение, вычитание, умножение, деление, возведение в степень, логарифм, округление в большую сторону до N знака после запятой, округление в меньшую сторону до N знака после запятой):")
    if (fun == 'Вычитание' or fun == 'вычитание' or fun == 'Сложение' or fun == 'сложение' or fun == 'Умножение' or fun == 'умножение' or fun == 'Деление' or fun == 'деление' or fun == 'Возведение в степень' or fun == 'возведение в степень' or fun == 'логарифм' or fun == 'Логарифм' or fun == 'округление в большую сторону до N знака после запятой' or fun == 'Округление в большую сторону до N знака после запятой' or fun == 'округление в меньшую сторону до N знака после запятой' or fun == 'Округление в меньшую сторону до N знака после запятой'):
        return first(fun)
    else:
        print('Функция неверная')
        funct()
def first(fun):
    first = input('Введите первый элемент:')
    arr = []
    for i in first:
        arr.append(i.isalpha())
    return proverka(arr, first, fun)

def proverka(arr, chislo1, fun):
    if True in arr:
        print('Введенный элемент не является числом')
        return first()
    else:
        return second(float(chislo1), fun)

def second(chislo1, fun):
    second = input('Введите второй элемент:')
    arr = []
    for i in second:
        arr.append(i.isalpha())
    return proverka2(arr, second, chislo1, fun)

def proverka2(arr, chislo2,chislo1, fun):
    if True in arr:
        print('Введенный элемент не является числом')
        return second(chislo1)
    else:
        return funi(float(chislo1), float(chislo2), fun)

def funi(chislo1,chislo2, fun):
    if fun == 'Вычитание' or fun == 'вычитание':
        print(chislo1 - chislo2)
    elif fun == 'Сложение' or fun == 'сложение':
        print(chislo1 + chislo2)
    elif fun == 'Умножение' or fun == 'умножение':
        print(chislo1 * chislo2)
    elif (fun == 'Деление' or fun == 'деление') and chislo2!=0:
        print(chislo1 // chislo2)
    elif (fun == 'Деление' or fun == 'деление') and chislo2==0:
        print("На ноль делить нельзя!")
        second(chislo2)
    elif (fun == 'Возведение в степень' or fun == 'возведение в степень'):
        print(chislo1**chislo2)
    elif (fun == 'логарифм' or fun == 'Логарифм'):
        print(math.log(chislo2, chislo1))
    elif (fun == 'округление в большую сторону до N знака после запятой' or fun == 'Округление в большую сторону до N знака после запятой'):
        chislo2 = int (chislo2)
        if chislo2 == 0:
            chislo1 += 0.5
        else:
            chislo1 += 0.5 * (0.1 ** chislo2)
        print(round(chislo1, chislo2))
    elif (fun == 'округление в меньшую сторону до N знака после запятой' or fun == 'Округление в меньшую сторону до N знака после запятой'):
        chislo2 = int(chislo2)
        if chislo2 == 0:
            chislo1 -= 0.5
        else:
            chislo1 -= 0.5 * (0.1 ** chislo2)
        print(round(chislo1, chislo2))
funct()