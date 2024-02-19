class NewError(Exception):
    pass


class FallError(NewError):
    pass


number = 10

try:
    num1 = 7
    if num1 < number:
        raise NewError
    elif num1 < number:
        raise FallError

except FallError:
    print("Ошибка 2")
except NewError:
    print("Ошибка 1")


class NewFall(Exception):
    def __init__(self, leg):
        self.leg = 2


try:
    leg = 5
    if leg > 3:
        raise NewFall('Ошибка. Слишком много ног')
except NewFall:
    print("Слишком много ног")

else:
    print(leg)
