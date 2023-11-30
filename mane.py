Модуль 1
Задание 1
s = 0
k = 15
d = k - 10
k = 4 * d
s = k - 50
print('ответ 1:', s)
Задание 2
x = 3
y = 4
z = x + y
z = z + 1
x = y
y = 5
x = z + y + 7
print('ответ 2:', x)
Задание 3
n = int(input())
print(n)
print(n + 1)
print(n + 2)
Задание 4
a = int(input())
b = int(input())
c = int(input())
d = a + b + c
print(d)
Задание 5
a = int(input())
b = 6 * (a * a)
print(b)
Задание 6
a = int(input())
b = int(input())
print(3*((a+b)**3)+275*(b**2)-127*a-41)
Модуль 1
Задание 1
s = 0
k = 15
d = k - 10
k = 4 * d
s = k - 50
print('ответ 1:', s)
Задание 2
x = 3
y = 4
z = x + y
z = z + 1
x = y
y = 5
x = z + y + 7
print('ответ 2:', x)
Задание 3
n = int(input())
print(n)
print(n + 1)
print(n + 2)
Задание 4
a = int(input())
b = int(input())
c = int(input())
d = a + b + c
print(d)
Задание 5
a = int(input())
b = 6 * (a * a)
print(b)
Задание 6
a = int(input())
b = int(input())
print(3*((a+b)**3)+275*(b**2)-127*a-41)
Модуль 2
задание 1
print('Введите n')
n = int(input())
print('Введите k')
k = int(input())
if n>k:
print('no')
else:
print('yes')
задание 2
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
print('Треугольник равносторонний')
if a == b != c or b == c != a or a == c != b:
print('Треугольник равнобедренный')
if a != b != c:
print('Треугольник разносторонний')
Задание 3
a = int(input())
b = int(input())
c = int(input())
if a < b < c or a > b > c:
print(b)
elif b < c < a or b > c > a:
print(c)
else:
print(a)
задание 4
a = int(input())
if a == 2:
print ('28')
elif a <= 7:
print(30 + a%2)
else:
print(31 - a%2)
задание 5
a = int(input())
if a < 60:
print('Легкий вес')
elif a < 64:
print('Первый полусредний вес')
elif a < 69:
print('Полусредний вес')
задание 6
a = input()
b = input()
if (a == 'красный' and b == 'синий') or (a == 'синий' and b == 'красный'):
print('фиолетовый')
elif a == 'красный' and b == 'красный':
print('красный')
elif (a == 'красный' and b == 'желтый') or (a == 'желтый' and b == 'красный'):
print('оранжевый')
elif a == 'желтый' and b == 'желтый':
print('желтый')
elif (a == 'синий' and b == 'желтый') or (a == 'желтый' and b == 'синий'):
print('зеленый')
elif a == 'синий' and b == 'синий':
print('синий')
else:
print('ошибка цвета')
задание 7
b = int(input())
if b < 00 or b > 3636:
print('ошибка ввода')
elif b == 0:
print('зеленый')
elif 1111 <= b <= 1010 or 1919 <= b <= 2828:
if b % 2 == 0:
print('черный')
else:
print('красный')
elif 11 <= b <= 1818 or 2929 <= b <= 3636:
if b % 2 == 0:
print ('красный')
else:
print ('черный')
задание 8
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if a2 > b1 or a1 > b2:
print('Пустое множество')
elif a1 == b1:
print(a1)
elif a2 == b1:
print(a2)
else:
if a1 > a2:
a2 = a1
if b1 < b2:
b2 = b1
print(a2, b2)

контрольная работа
Задание 1
Ответ: print()
Задание 2
Ответ:
print(«3.1415»)
print(«I’m a math teacher and a programmer!»)
print(‘Поэма «Мёртвые души» одна из самых интересных’)
print()
Задание 3
Ответ: print(‘Python’, ‘is the best’, ‘!!’)
Задание 4
Решение: 1*2*3*4
Задание 5
Верные:
print("The world's a little blurry", "Or maybe it's my eyes", end='!!!', sep=' :) ')
print("Told you not to worry", "But maybe that's a lie", sep=' :) ')
print("Honey, what's your hurry", end='?')
Задание 6
Ответа: input()
Задание 7
Решение: n = int(input())
Задание 8
Ответ:
Имя переменной не может начинаться с цифры
Имя переменной не может совпадать с ключевым (зарезервированным) словом
Имя переменной может начинаться с символа подчёркивания (_)
Задание 9
s = 13
k = -5
d = s + 2
s = d
k = 2 * s
print(s + k + d)
Результат: 60
Задание 10
a = 17 // (23 % 7)
b = 34 % a * 5 - 29 % 4 * 3
print(a * b)
Результат: 56
Задание 11
print('*****************')
print('* *')
print('* *')
print('*****************')
Задание 12





Рзамножение n-ок
n=int(input('Число от 1 до 9? '))
string=(f'{str(n)} + {str(n)*2} + {str(n)*3}')
print (f'{string} = {eval(string)}')
Задание 2
Ответ: 20

Задание Куб
x = int(input())
print('Объем =', x * x * x)
print('Площадь полной поверхности =', 6 * x * x)
Задание Значение функции
a = int(input())
b = int(input())
print(3 * (a+b) * (a+b) * (a+b) + 275 * b * b - 127 * a - 41
Задание Следующее и предыдущее
score = int(input())
print('Следующее за числом', score, 'число:', score + 1)
print('Для числа', score, 'предыдущее число:', score - 1)
Задание Стоимость покупки
x = int(input())
y = int(input())
z = int(input())
c = int(input())
print(3 * (x + y + z + c))
Задание Арифметические операции
a = int(input())
b = int(input())
print(a, '+', b, '=', a + b)
print(a, '-', b, '=', a - b)
print(a, '*', b, '=', a * b)
Задание Арифметическая прогрессия
a = int(input())
b = int(input())
c = int(input())
x = a + b * (c - 1)
print(x)
Задание Разделяй и властвуй
x = int(input())
print(x, 2 * x, 3 * x, 4 * x, 5 * x, sep='---')
Задание Геометрическая прогрессия
b1 = int(input())
q = int(input())
n = int(input())
print(b1 * q ** (n-1))
Задание Расстояние в метрах
cm = int(input())
m = cm // 100
print(m)
Задание Мандарины
sch = int(input())
fru = int(input())
print(fru // sch)
print(fru % sch)
Задание Сама неотвратимость ?️
n = int(input())
print(n//2 + n%2)
Задание Номер купе ?️
n = int(input())
print((n + 3) // 4)
Задание Пересчет временного интервала
m = int(input())
h = m // 60
s = m % 60
print(m, "мин - это", h, "час", s, "минут.")
Задание Трехзначное число
num = int(input())
a = num % 10
b = (num % 100) // 10
c = num // 100
print("Сумма цифр =", c + b + a)
print("Произведение цифр =", c * b * a)
Задание Перестановка цифр
abc = int(input())
c = abc % 10
b = (abc % 100) // 10
a = abc // 100
print(a, b, c, sep='')
print(a, c, b, sep='')
print(b, a, c, sep='')
print(b, c, a, sep='')
print(c, a, b, sep='')
print(c, b, a, sep='')
Задание Четырёхзначное число
m = int(input())
m1 = m // 1000
m2 = (m // 100) % 10
m3 = (m // 10) % 10
m4 = m % 10
print("Цифра в позиции тысяч равна", m1)
print("Цифра в позиции сотен равна", m2)
print("Цифра в позиции десятков равна", m3)
print("Цифра в позиции единиц равна", m4)
