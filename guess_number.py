from random import randint

numb = randint(1,100)
count = 1

while True:
    user_numb = input('\nВведите ваше число: ')
    if int(user_numb) > numb:
        print('Ваше число БОЛЬШЕ загаданного.\nПовторите попытку.')
    elif int(user_numb) < numb:
        print('Ваше число МЕНЬШЕ загаданного.\nПовторите попытку.')
    else:
        break
    count += 1
print(f'Поздравляем! Компьютер действительно загадал число {numb}!\nБыло потрачено {count} попыток!')

