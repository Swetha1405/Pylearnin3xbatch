# Decorators-They are essentially functions that take another function as an argument and extend or alter its behavior.

def my_decorator(func):
    def wrapper():
        print("starting......")
        print("*************")
        func()
        print("ending***********")

    return wrapper()
@my_decorator
def say_hello():
  print('say hello')



