#calling 2 decorators at a time
def my_decorator1(func):
    def wrapper():
        print("Decorator1")
        func()
    return wrapper

def my_decorator2(func):
    def wrapper():
        print("Decorator2")
        func()
    return wrapper


@my_decorator1
@my_decorator2
def say_hello():
    print("Say hello")

say_hello()