# 自定义一个 python 函数，实现 map() 函数的功能
def new_map(fun, args):
    def inner():
        list_new = []
        for i in args:
            k = fun(i)
            list_new.append(k)
        return list_new
    return inner()

def fun(x):
    return x ** 2

list_tmp = [1, 2, 3, 4, 5]
mappy = new_map(fun, list_tmp)
print(mappy)