import time

"""Напишите декоратор, который проверяет, что все числа, возвращаемые декорируемой функцией, являются целыми, и округляет их до целых, если это не так."""
import time


def my_decorator(func):
    def number(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, float):
            return round(result)
        else:
            return result
    return number

@my_decorator
def add_one(x):
    return x / 3

#y = add_one(x)
#print(y)

"""Напишите декоратор, который повторно вызывает декорируемую функцию три раза. Каждый раз через три секунды, если произошла ошибка."""
"""декоратор пытается выполнить функцию до трёх раз, делая паузу в 3 секунды между попытками, 
если возникает ошибка. Это полезно в ситуациях, когда ошибка может быть временной и повторная попытка может быть успешной"""

def again_funk(funk):
    def again(*args, **kwargs):
        result = funk(*args, **kwargs)
        for i in range(3):          # делает три попытки, после переходит в исключение
            try:
                return result
            except:
                time.sleep(3)     #import time
        raise Exception("Вызов функции завершился неудачно после нескольких попыток.")
    return again

#@again_funk
#def function_check(x):
#    return x / 3
#try:
#    y = function_check(5)
#    print(y)
#except Exception as e:
#    print(e)
