# 实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
import time

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