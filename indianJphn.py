pairs=[]
n = int(input('Введите число от 3 до 20: '))
for i in range(1, n):
    for j in range(i, n):
        if n % (i + j) == 0:
            pairs.append((i,j))
    #Хранилище пароля и добавление пары в строку
    result = ''.join(f'{i}{j}' for i, j in pairs) # принимаем в результат пустую строку через join мы присоединяем
    # к одной строке другую /для каждого j и i

print(f'Нужный пароль: {result}')



