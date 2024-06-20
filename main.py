import hashlib
import string
from random import randint, choice, sample
def hash_password(password):
    salt = b"secret"
    hasher = hashlib.sha256()
    hasher.update(password.encode())
    hasher.update(salt)
    return hasher.digest()
def generate_password(*args):
    characterList = ""
    i = 0
    args = list(args)
    while (i < args[0]):
        if (args[1] % 2 == 1):
            characterList += choice(string.ascii_letters)
            args[1] += 1
        elif (args[2] % 2 == 1):
            characterList += choice(string.punctuation)
            args[2] += 1
        elif (args[3] % 2 == 1):
            characterList += choice(string.digits)
            args[3] += 1
        else:
            if args[1] >= 2:
                args[1] += 1
            if args[2] >= 2:
                args[2] += 1
            if args[3] >= 2:
                args[3] += 1
            i -= 1
        i += 1
    return ''.join(sample(characterList, len(characterList)))

def main():
    a = int(input("Какая длина пароля? - "))
    b = input("Добавить символы верхнего регистра? (да/нет) - ") == 'да'
    c = input("Добавить специальные символы? (да/нет) -  ") == 'да'
    d = input("Добавить цифры? (да/нет) -  ") == 'да'
    e = input("Нужно ли сделать хэширвоание? (да/нет) - ") == 'да'
    result = generate_password(a, b, c, d)
    if e:
        print(f'Ваш сгенерированный пароль: {result}\nХэш сгенерированного пароля: {hash_password(result)}')
    else:
        print(f'Ваш сгенерированный пароль: {result}')

if __name__ == '__main__':
    main()