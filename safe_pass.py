import random

digits = '0123456789'
let_low = 'abcdefghigklmnopqrstuvwxyz'
let_upp = 'ABCDEFGHIGKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

char = ''

count_pass = int(input('Сколько паролей сделать?'))
len_pass = int(input('Длина пароля'))
num_include = input('Включать ли цифры 0123456789? (y/n)')
let_upp_include = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
let_low_include = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
punctuation_include = input('Включать ли символы !#$%&*+-=?@^_? (y/n)')
sym_del = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)')

if num_include == 'y':
    char += digits
if let_upp_include == 'y':
    char += let_upp
if let_low_include == 'y':
    char += let_low
if punctuation_include == 'y':
    char += punctuation
if sym_del == 'n':
    char += 'il1Lo0O'



def generate_password(l, char):
    new = []
    for i in range(l):
        new += random.choice(char)

    
    return new

for j in range(count_pass):
    print(''.join(generate_password(len_pass, char)))


