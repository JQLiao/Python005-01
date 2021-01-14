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