import warnings

num = 63644

for i in range(1):
    res = num / 26744444444
    if res <= 0.01:
        warnings.warn('Функция близится к делению на "0"')

print(f' resultat {int(res)}')
