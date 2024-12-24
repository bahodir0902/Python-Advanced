# import time
from typing import Callable
#
#
# # def say_hello(message: str) -> str:
# #     time.sleep(3)
# #     return f"Hello! {message}"
# #
# # begin = time.time()
# # print(say_hello("World"))
# # end = time.time()
# # print(f"Say hello function took {end - begin} time.")
#
# def timer(func: Callable) -> Callable:
#     def wrapper(message):
#         begin = time.time()
#         r = func(message)
#         end = time.time()
#         print(type(func))
#         print(f"function took {end - begin - 1} seconds to execute.")
#         return r
#
#     return wrapper
#
#
# # @timer
# # def say_hello(message: str) -> str:
# #     time.sleep(1)
# #     return f"Hello, {message}"
#
# # print(say_hello("World!"))
#
# @timer
# def factorial(num: int) -> int:
#     result = 1
#     time.sleep(1)
#     for i in range(2, num):
#         result *= i
#     return result
#
#
# # print(factorial(100))
#
# class Timer:
#     def __init__(self, func):
#         self.func = func
#         print(f"{self.func.__name__} funksiyasi ishladi")
#
#     def __call__(self, *args, **kwargs):
#         print(f"{self.func.__name__} funksiyasi ishladi")
#         start = time.time()
#         result = self.func(*args, **kwargs)
#         end = time.time()
#         print(f"{self.func.__name__} funksiyasi tugadi va {end - start} sekund ishladi")
#         return result
#
#
# # @Timer
# # def fibonacci(num: int) -> int:
# #     if num < 1:
# #         return 0
# #     return fibonacci(num - 1) + fibonacci(num - 2)
# #print(fibonacci(30))
#
#
#
# @Timer
# def factorial_class(num: int) -> int:
#     result = 1
#     time.sleep(1)
#     for i in range(2, num):
#         result *= i
#     return result
#
# print(factorial_class(100))
#
#
def test(msg: str):
    def decorator(func: Callable):
        def wrapper():
            print(func.__name__)
            print(type(func))
            print(msg)
        return wrapper
    return decorator

@test("message")
def dec():
    print(f"Hello")

dec()


