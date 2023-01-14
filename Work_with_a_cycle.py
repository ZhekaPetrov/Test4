# The machine receives a three-digit number for input. According to this number, a new number is constructed according to the following rules.
#1. The first and second, as well as the second and third digits of the original number are added.
#2. The resulting two numbers are written one after the other in ascending order (without separators).

# Автомат получает на вход трехзначное число. По этому числу строится новое число по следующим правилам.
#1. Складываются первая и вторая, а также вторая и третья цифры исходного числа.
#2. Получпенные два числа записываются друг за другом в порядке возрастания (без разделителей).

for i in range(100, 1000):      # Перебор чисел от 100 до 999
    a = str(i)                  # i - То что перебирается в текущий момент(любое трехзначное число от 100 до 999)
    x = int(a[0])               # Перевод списка в число
    y = int(a[1])
    z = int(a[2])
    k1 = x + y
    k2 = y + z
    first = str(min(k1, k2))    # Перевод чисел в строку, находим минимальное число
    second = str((max(k1, k2))) # Перевод чисел в строку, находим максимальное число
    s = first + second          # Складываем строки
    if s == '1115':
        print(i)
        break                   # Выход из цикла
        
        
