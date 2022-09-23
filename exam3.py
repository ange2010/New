# 1. Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками

def credit_card(card):
    return '*' * len(card[:-4]) + card[-4:]
card = str(input('Введите номер кредитной карты: '))
print(credit_card(card))
print(credit_card('123456781234'))

# 2. Напишите функцию, которая проверяет: является ли слово палиндромом
# 1 способ
def palindrom(a):
    if a == a[::-1]:
        return True
    else:
        return False
print(palindrom('ара'))

# 2 способ
def palindrom(a):
    if a == a[::-1]:
        print('Слово - палиндром!')
    else:
        print('Слово не является палиндромом')
a = input('Введите слово: ')
palindrom(a)