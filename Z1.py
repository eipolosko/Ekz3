def number_credit(num):
    for i in num[:-4]:
        i = '*'
        print(i,end='')
    print(num[-4:])

n=input('Введите номер карточки  ')
number_credit(n)