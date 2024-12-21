# def summa (n):
#     if n == 0:
#         return 0
#     else:
#         return n + summa(n - 1)
#
# print(summa(5))
from calendar import firstweekday


# stack=[]
# stack.append(1)
# print('Добавили элемент', stack)
# stack.append(2)
# print('Добавили элемент', stack)
# stack.append(3)
# print('Добавили элемент', stack)
# print(stack)
# stack.pop()
# print('Убрали элемент', stack)
# stack.pop()
# print('Убрали элемент', stack)
# stack.pop()
# print('Убрали элемент', stack)


def get_multiplied_digits (number):
    str_number=str(number)

    if len(str_number) > 1:
        first = int(str_number[0])
        if first == 0:
            return get_multiplied_digits(int(str_number[1:]))
        else:
            return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number) if str_number != '0' else 1


result = get_multiplied_digits(402030)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)


