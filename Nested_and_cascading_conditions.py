# Zoom challenged Flash and offered him a fair fight in the form of a race around the magnetar. If you lose, this neutron star will charge up and destroy the world,
# therefore, Flash decided not to take risks for no reason, and find out from his friend Cisco Ramon whether it makes sense to accept the challenge. Cisco received
# data that the zoom speed is equal to nn, and the Flash speed is equal to kk.
# Write a program that should output Cisco's answer to Flash's question.

# Зум бросил вызов Флэшу и предложил ему честный поединок в виде гонки вокруг магнетара. В случае проигрыша эта нейтронная звезда зарядится и уничтожит мир,
# поэтому Флэш решил не рисковать без причины, и узнать у своего друга Циско Рамона есть ли смысл принимать вызов. Циско получил данные, что скорость Зума
# равна nn, а скорость Флэша равна kk.
# Напишите программу, которая должна вывести ответ Циско на вопрос Флэша. 

n = int(input())
k = int(input())
if n > k:
    print("NO")
elif n < k:
    print("YES")
else:
    print("Don't know")

# Write a program that accepts three positive numbers and determines the type of triangle whose side lengths are equal to the entered numbers.
# Напишите программу, которая принимает три положительных числа и определяет вид треугольника, длины сторон которого равны введенным числам.

a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print("Равносторонний")
if a == b != c or a != b == c or a == c != b:
    print("Равнобедренный")
if a != b and a != c and c != b:
    print("Разносторонний")

# Three different integers are given. Write a program that finds the average number.
# Даны три различных целых числа. Напишите программу, которая находит среднее по величине число.

a, b, c = int(input()), int(input()), int(input())
if a < b < c or c < b < a:
    print(b)
elif a < c < b or b < c < a:
    print(c)
else:
    print(a)
# The ordinal number of the month is given (1,2,..., 12). Write a program that displays the number of days in this month. Accept that the year is non-leap.
# Дан порядковый номер месяца (1,2,…, 12). Напишите программу, которая выводит на экран количество дней в этом месяце. Принять, что год является невисокосным.

month = int(input()) # Порядковый номер месяца
if month == 12 or month == 5 or month == 1 or month == 3 or month == 10 or month == 7 or month == 8:
    print("31")
elif month == 2:
    print("28")
else:
    print("30")

# The weight of an amateur boxer is known (integer). It is known that the weight is such that a boxer can be assigned to one of three weight categories:
# Light weight – up to 60 kg;
# First welterweight – up to 64 kg;
# Welterweight – up to 69 kg.

# Известен вес боксера-любителя (целое число). Известно, что вес таков, что боксер может быть отнесён к одной из трех весовых категорий:
# Легкий вес – до 60 кг;
# Первый полусредний вес – до 64 кг;
# Полусредний вес – до 69 кг.

a = int(input())
if a < 60:
    print("Легкий вес")
elif 60 <= a < 64:
    print("Первый полусредний вес")
else:
    print("Полусредний вес")

# Write a program that reads the names of the two primary colors for mixing. If the user enters anything other than the names "red",
# "blue" or "yellow", then the program should output an error message. Otherwise, the program should output the name of the secondary color that
# it will turn out as a result.

# Напишите программу, которая считывает названия двух основных цветов для смешивания. Если пользователь вводит что-нибудь помимо названий «красный»,
# «синий» или «желтый», то программа должна вывести сообщение об ошибке. В противном случае программа должна вывести название вторичного цвета, который
# получится в результате.
    
a, b = input(), input()
if (a == "красный" and b == "синий") or (a == "синий" and b == "красный"):
    print("фиолетовый")
elif (a == "красный" and b == "желтый") or (a == "желтый" and b == "красный"):
    print("оранжевый")
elif (a == "синий" and b == "желтый") or (a == "желтый" and b == "синий"):
    print("зеленый")
elif a == b:
    if a == "синий" or a == "желтый" or a == "красный":
        print(a)
    else:
        print("ошибка цвета")
else:
    print("ошибка цвета")
