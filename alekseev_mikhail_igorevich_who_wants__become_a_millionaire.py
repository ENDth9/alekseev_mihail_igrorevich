import time
print('Who wants become a millionaire \n', '-' * 20)
count = 0


def start():
    """Приветствие"""
    print('Добро пожаловать в игру "Кто хочет стать миллионером" \n Цель игры отвечать на вопросы, выбрав верный ответ из 4 предложенных, за каждый верный ответ в Ваш банк начисляется деньга, ответил верно идешь дальше, не верно ПРОИГРАЛ. \n Так же в игре есть 3 подсказки 1. Помощь зала, 2. Звонок другу, 3. 50/50. Все понятно? \n', '-' * 20 )
    a = input('Да иил Нет : ' )
    if a in 'нет' or a in 'Нет' or a in 'НЕТ':
        return again()
    if a in 'Да' or a in 'ДА' or a in 'да':
        return print(f'Что же начнем игру! Введите следующие данные.\n', '-' * 20 )
    return profile()
    
def again():
    """Повторение правил"""
    print('Цель игры отвечать на вопросы, выбрав верный ответ из 4 предложенных, за каждый верный ответ в Ваш банк начисляется деньга, ответил верно идешь дальше, не верно ПРОИГРАЛ. Так же в игре есть 3 подсказки 1. Помощь зала, 2. Звонок другу, 3. 50/50. Все понятно? \n', '-' * 20)
    b = input('Да иил Нет : ' )
    if b in 'нет' or b in 'Нет' or b in 'НЕТ':
        return again()
    if b in 'Да' or b in 'ДА' or b in 'да':
        return print(f'Что же начнем игру! Введите следующие данные.\n', '-' * 20)
    return profile()

def profile(firstname: str, lastname: str, age: str, work: str):
    """Профиль"""
    print('Добрый день!', lastname, firstname, 'Начнем игру! \n', "-" * 20)
    return game_one(count)

def game_one(count):
    """Игра, 1 вопрос"""
    print('1. Вопрос : \n Столица России \n Варианты ответов \n A. Париж, B. Лондон \n C. Осло D. Москва \n', 'Если нужна помощь, воспользуйтесь подсказкой \n', '-' * 20)
    first_question = input('Выберите верный ответ, либо воспользуйтесь подсказкой введите 0,  A, B, C, D : ' )
    if first_question == 'D' or first_question == 'd': 
        count += 100
        print()
        print()
        print('Верно!, + 100$, Следущий вопрос.')
        print()
        print()
        return game_two(count)
    elif first_question == '0':
        return help_question()
    else:
        return print('Не верно, Вы проиграли!, Cумма проигрыша 100$.\n')
    

def game_two(count):
    print()
    print()
    print('2. Вопрос : \n Кол-во людей на земле \n Варианты ответов \n A. 7 002 321 980, B. 8 114 646 831 \n C. 8 002 213 232 D. 7 994 123 748 \n', 'Если нужна помощь, воспользуйтесь подсказкой \n', '-' * 20)
    first_question = input('Выберите верный ответ, либо воспользуйтесь подсказкой введите 0,  A, B, C, D : ' )
    if first_question == 'B' or first_question == 'b': 
        count += 100
        print()
        print()
        print('Верно!, + 100$, Следущий вопрос.')
        print()
        print()
        return game_three(count)
    elif first_question == '0':
        return help_question()
    else:
        return print('Не верно, Вы проиграли!, Cумма проигрыша 100$.\n')
     

def game_three(count):
    print()
    print()
    print('3. Вопрос : \n Кол-во планет в солнечной системе \n Варианты ответов \n A. 7 B. 6 \n C. 8 D. 9 \n', 'Если нужна помощь, воспользуйтесь подсказкой \n', '-' * 20)
    first_question = input('Выберите верный ответ, либо воспользуйтесь подсказкой введите 0,  A, B, C, D : ' )
    if first_question == 'c' or first_question == 'c': 
        count += 100
        print()
        print()
        print('Верно!, + 100$, Следущий вопрос.')
        print()
        print()
        return game_four(count)
    elif first_question == '0':
        return help_question()
    else:
        return print('Не верно, Вы проиграли!, Cумма проигрыша 100$.\n')
    

def game_four(count):
    print()
    print()
    print('4. Вопрос : \n Японская марка машины \n Варианты ответов \n A. Toyota B. Renault \n C. Opel D. BMW \n', 'Если нужна помощь, воспользуйтесь подсказкой \n', '-' * 20)
    first_question = input('Выберите верный ответ, либо воспользуйтесь подсказкой введите 0,  A, B, C, D : ' )
    if first_question == 'A' or first_question == 'a': 
        count += 100
        print()
        print()
        print('Верно!, + 100$, Следущий вопрос.')
        print()
        print()
        return game_five(count)
    elif first_question == '0':
        return help_question()
    else:
        return print('Не верно, Вы проиграли!, Cумма проигрыша 100$.\n')
    
    
def game_five(count):
    print()
    print()
    print('5. Вопрос : \n Хула Хуп это = \n Варианты ответов \n A. Мяч B. Кольцо \n C. Стена D. Люфт \n', 'Если нужна помощь, воспользуйтесь подсказкой \n', '-' * 20)
    first_question = input('Выберите верный ответ, либо воспользуйтесь подсказкой введите 0,  A, B, C, D : ' )
    if first_question == 'B' or first_question == 'b': 
        count += 100
        print()
        print()
        print('Верно!, + 100$, Следущий вопрос.')
        print()
        print()
        return game_six(count)
    elif first_question == '0':
        return help_question()
    else:
        return print('Не верно, Вы проиграли!, Cумма проигрыша 100$.\n')


def game_six(count):
    print()
    print()
    print('6. Вопрос : \n Одним из направлений какой религиозной философии является учение дзен?  = \n Варианты ответов \n A. Даосизм B. Индуизм \n C. Иудаизм D. Буддизм \n', 'Если нужна помощь, воспользуйтесь подсказкой \n', '-' * 20)
    first_question = input('Выберите верный ответ, либо воспользуйтесь подсказкой введите 0,  A, B, C, D : ' )
    if first_question == 'd' or first_question == 'D': 
        count += 100
        print()
        print()
        print('Верно!, + 100$, Следущий вопрос.')
        print()
        print()
        return game_seven(count)
    elif first_question == '0':
        return help_question()
    else:
        return print('Не верно, Вы проиграли!, Cумма проигрыша 100$.\n')
    


def game_seven(count):
    print()
    print()
    print('7. Вопрос : \n Кто из перечисленных был пажом во времена Екатерины II?  = \n Варианты ответов \n A. Д. И. Фонвизин B. Г. Р. Державин \n C. А. Н. Радищев D. Н. М. Карамзин \n', 'Если нужна помощь, воспользуйтесь подсказкой \n', '-' * 20)
    first_question = input('Выберите верный ответ, либо воспользуйтесь подсказкой введите 0,  A, B, C, D : ' )
    if first_question == 'c' or first_question == 'C': 
        count += 100
        print()
        print()
        print('Верно!, + 100$, Следущий вопрос.')
        print()
        print()
        return game_eight(count)
    elif first_question == '0':
        return help_question()
    else:
        return print('Не верно, Вы проиграли!, Cумма проигрыша 100$.\n')
    
def game_eight(count):
    print()
    print()
    print('8. Вопрос : \n Какой химический элемент назван в честь злого подземного гнома?  = \n Варианты ответов \n A. Гафний B. Кобальт \n C. Бериллий D. Теллур \n', 'Если нужна помощь, воспользуйтесь подсказкой \n', '-' * 20)
    first_question = input('Выберите верный ответ, либо воспользуйтесь подсказкой введите 0,  A, B, C, D : ' )
    if first_question == 'b' or first_question == 'B': 
        count += 100
        print()
        print()
        print('Верно!, + 100$, Следущий вопрос.')
        print()
        print()
        return game_nine(count)
    elif first_question == '0':
        return help_question()
    else:
        return print('Не верно, Вы проиграли!, Cумма проигрыша 100$.\n')
    
def game_nine(count):
    print()
    print()
    print('9. В какой из этих столиц бывших союзных республик раньше других появилось метро? : \n Одним из направлений какой религиозной философии является учение дзен?  = \n Варианты ответов \n A. Тбилиси B. Баку \n C. Минск D. Ереван \n', 'Если нужна помощь, воспользуйтесь подсказкой \n', '-' * 20)
    first_question = input('Выберите верный ответ, либо воспользуйтесь подсказкой введите 0,  A, B, C, D : ' )
    if first_question == 'A' or first_question == 'a': 
        count += 100
        print()
        print()
        print('Верно!, + 100$, Следущий вопрос.')
        print()
        print()
        return game_ten(count)
    elif first_question == '0':
        return help_question()
    else:
        return print('Не верно, Вы проиграли!, Cумма проигрыша 100$.\n')


def game_ten(count):
    print()
    print()
    print('10. Вопрос : \n С какой буквы начинаются слова, опубликованные в 16-м томе последнего издания Большой советской энциклопедии?  = \n Варианты ответов \n A. М B. О \n C. Н D. П \n', 'Если нужна помощь, воспользуйтесь подсказкой \n', '-' * 20)
    first_question = input('Выберите верный ответ, либо воспользуйтесь подсказкой введите 0,  A, B, C, D : ' )
    if first_question == 'a' or first_question == 'A': 
        count += 100
        print()
        print()
        print('Верно!, + 100$, Следущий вопрос.')
        print()
        print()
        return print(f'Поздравляю Вы выигарли {count} $')
    elif first_question == '0':
        return help_question()
    else:
        return print('Не верно, Вы проиграли!, Cумма проигрыша 100$.\n')

        
    



def help_question():
    help = int(input('Выберите подсказку 1. Помощь зала, 2. Звонок другу, 3. 50/50 : '))
    help_answer = [1, 2, 3] 
    if help == help_answer[0]:
        print()
        print()
        print('HELP ALL')
        print()
        print() 
        help_answer = help_answer.pop(0)
        return game_one(count)
    if help == help_answer[1]:
        print()
        print()
        print('CALL FRIEND')
        print()
        print()
        help_answer = help_answer.pop(1)
        return game_one(count)
    if help == help_answer[2]:
        print()
        print()
        print('50 / 50')
        print()
        print()
        help_answer = help_answer.pop(2)
        return game_one(count)
    if help != help_answer():
        print()
        print()
        print("Выберите 1 = 2 = 3")
        print()
        print()
        return help_question()
    
    
    
    
start()
profile(firstname=input('Имя : ' ), lastname=input('Фамилия ; '), age=input('Возраст : '), work=input('Род деятельности (Чем Вы занимаетесь?) : ' ))
