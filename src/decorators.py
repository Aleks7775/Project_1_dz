def log(filename=None):
    """Декоратор который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Начало работы функции {func.__name__}")
            try:
                result = func(*args, **kwargs)
                print(f"Конец работы функции {func} и её результат {result}")
                if filename:
                    with open(filename, 'a') as file:
                        file.write(f'{func.__name__} ok\n')
                else:
                    print(f'{func.__name__} ok')
                return result
            except Exception as e:
                log_error = f'{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}'
                if filename:
                    with open(filename, 'a') as file:
                        file.write(log_error + "\n")
                else:
                    print(log_error)
                raise e
        return wrapper
    return decorator


@log
def log_func(x, y):
    """Проверка декоратора"""
    return x + y