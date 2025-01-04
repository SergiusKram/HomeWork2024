pairs = []
n = int(input('Введите число от 3 до 20: '))

# Основной цикл для поиска пар
for i in range(1, n):
    for j in range(i + 1, n):  # Начинаем с i + 1, чтобы исключить повторения
        if n % (i + j) == 0:
            pairs.append((i, j))  # Добавляем пару в список

# Генерация пароля
result = ''.join(f'{i}{j}' for i, j in pairs)  # Объединяем пары в строку

print(f'Нужный пароль: {result}')



