from typing import Callable


def only_positive(func: Callable) -> Callable:
    def wrapper(num: int):
        try:
            if num < 0:
                raise ValueError(f"Only positive integers are accepted!")
        except ValueError as e:
            print(f"Error occurred: {e}")
            return
        result = func(num)
        return result

    return wrapper


@only_positive
def square_number(num: int):
    return num ** 2


print(square_number(20))
print(square_number(-3) if square_number(-3) else "")


# 2
def count_calls(func: Callable) -> Callable:
    count = 0

    def wrapper():
        nonlocal count
        count += 1
        print(f"Function '{func.__name__}' called {count} times.")
        func()

    return wrapper


@count_calls
def hello():
    print(f"Hello")


count = int(input("Count how many times you want to call function?: "))
for i in range(count):
    hello()


# 3
def admin_only(func: Callable) -> Callable:
    def wrapper(user_id, **kwargs):
        for key, value in kwargs.items():
            if key == "role" and value != "admin":
                print(f"No access! Only admin can delete user!")
                return
        func(user_id, **kwargs)

    return wrapper


@admin_only
def delete_user(user_id, **kwargs) -> None:
    print(f"User with {user_id} user ID deleted successfully.")


delete_user(101, role="admin")
delete_user(103, role="user")


# 4
def time_restricted(start_hour: int, end_hour: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper():
            func()

        return wrapper

    return decorator


@time_restricted(9, 17)
def send_report():
    print("Report has been sent successfully!")


send_report()


# 5
def call_limit(lim: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        count: int = 0

        def wrapper():
            nonlocal count
            if count >= 3:
                print(f"Function call limit exceeded. max call is {lim}")
                return
            func()
            count += 1

        return wrapper

    return decorator


@call_limit(3)
def process_data():
    print(f"Data has been processed successfully")


process_data()
process_data()
process_data()
process_data()
