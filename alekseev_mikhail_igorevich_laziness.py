# Запросить у пользователя 3 значения (вводит число Int) 

a, b, c = int(input()), int(input()), int(input())

# Если нет ни одого нуля - вывести: "Нет нулевых значений!!!"(Без if - использовать лень)

print( a and b and c and "Нет нулевых значений!!!")

# Вывести первое ненулевое значение. Если введены все нули - вывести "Введены все нули!" (цикл не использовать) без if - использовать лень

print( a or b or c or "Введены все нули")

# Если первое значение  больше чем сумма второго и третьего вывести a - b - c

if a > b + c:
    print('a - b - c')
    
# Если первое значение меньше чем сумма второго и третьего вывести b + c - a

if a < b + c:
    print('b + c - a')
0
# Если первое значение больше 50 и при этом одно из оставшихся значение больше первого вывести "Вася"

if a > 50 and (b > a or c > a):
    print('Вася')

# Если первое значение больше 5 или оба из оставшихся значений равны 7 вывести "Петя"

if a > 5 or b == 7 and c == 7:
    print('Петя')