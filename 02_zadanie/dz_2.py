#def dev_by_three(number):
    # if number % 3 == 0:
    #     return 'Да'
    # else:
    #     return 'Нет'

# Пример числа для проверки
#number_to_check = 8  # Вы можете изменить это число на любое другое

# Вызов функции и сохранение результата
#result = dev_by_three(number_to_check)

# Вывод результата в нужном формате
#print(f'Делится ли на три {number_to_check}? - {result}')


def dev_by_three(number):
    return "Да" if number % 3 == 0 else "Нет"

num = int(input("Введите число: "))
result = dev_by_three(num)
print(f"Делится ли на три {num}? - {result}")

