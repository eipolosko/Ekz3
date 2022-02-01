def polindrom(slovo):
    if slovo == slovo[::-1]:
        print('Слово являестя полиндромом ')
    else:
        print('Слово не полиндром')


slovo = input('Введите слово    ')
polindrom(slovo)
