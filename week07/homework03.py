import os, time

def timer(fun):
    def inner(*args, **kargs):
        start_time = time.time()
        f = fun(*args, **kargs)
        time.sleep(1)
        exec_time = time.time() - start_time
        print(f"exec_time:{exec_time}")
        return f
    return inner


@timer
def add(x, y, z=5):
    return x + y + z

k = add(3, 4)
print(k)