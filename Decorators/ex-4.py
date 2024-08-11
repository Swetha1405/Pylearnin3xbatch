#printing the logs of func time taken and difference in time
import time
def my_time_decorator(func):

    def wrapper():
        start_time=time.time()
        print(start_time)
        func()
        end_time=time.time()
        print(end_time)
        print("time taken is " + str(end_time-start_time))
    return wrapper()

@my_time_decorator
def say_hello():
    time.sleep(5)
    print("print the logs of function")

#we can add more functions to existing function
@my_time_decorator
def reporting_time():
    time.sleep(2)
    print("reporting time diff")
