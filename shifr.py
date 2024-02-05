def caesars_code(alpha, n, w):
    res = ''
    for i in w:
        if i in alpha:
            id = alpha.index(i)
            n_id = (id + n) % len(alpha)
            res += alpha[n_id]
    return res


def decode(alpha, n, w):
    res = ''
    for i in w:
        if i in alpha:
            id = alpha.index(i)
            n_id = (id - n) % len(alpha)
            res += alpha[n_id]
    return res


alphabet_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя ,.?:;"'
alphabet_eng = 'abcdefghijklmnopqrstuvwxyz ,.?:;"'
while True:
    try:
        num, word = int(input("Key: ")), input('Word: ')
        break
    except ValueError:
        print("Try once more")

while True:
    try:
        choice = int(input("Your choice(1 - ru, 2 - eng, 3 - decode ru, 4 - decode eng): "))
        if 1 <= choice <= 4:
            break
    except ValueError:
        print("Try once more")

if choice == 1:
    print(caesars_code(alphabet_ru, num, word))
elif choice == 2:
    print(caesars_code(alphabet_eng, num, word))
elif choice == 3:
    print(decode(alphabet_ru, num, word))
elif choice == 4:
    print(decode(alphabet_eng, num, word))