def check_decor(func):
    def wrapper():
        try:

            print("Before 1")
            func()
            print("After 1")
        except Exception as e:
            print("Attempt failed")
    return wrapper

@check_decor
def say_hello():
    print("hello")

say_hello()
