# Вывести результат BMI в виде текста

a_weight, b_hight, a_index, b_index = float(input('Масса тела = ')), float(input("Рост равен = ")), 10, 40
index_mass = a_weight / (b_hight ** 2)
print(f"Ваш индекс массы тела : {index_mass}\n")

# Вывести результат BMI в виде шкалы

x_min, x_max = index_mass - a_index, b_index - index_mass
print('10' + int(x_min) * '=' + '|' + int(x_max) * '=' + '40')

