学习笔记

函数的调用
fun    传递对象
fun()  传递函数执行结果

类的调用
class     类的一个对象
class()   把类实例化


命名空间(作用域)
LEGB规则

LEGB 含义解释：
- L-Local(function)；函数内的名字空间
- E-Enclosing function locals；外部嵌套函数的名字空间（例如closure） 
- G-Global(module)；函数定义所在模块（文件）的名字空间
- B-Builtin(Python)；Python 内置模块的名字空间

可变长参数
def fun(*args, **kargs)

Lambda表达式
k = lambda x:x+1
print(k(1))

偏函数
def add(x, y):
    return x + y
固定一个参数为1
funtools.partial(add, 1)

返回的对象
- 可调用对象 -- 闭包（装饰器）
- 内部函数对外部函数作用域里变量的引用则称为内部函数为闭包
- nonlocal 访问外部函数的局部变量
    ```
    def line_conf(a, b):
        def line(x):
            return a*x+b
        return line

    my_line = line_conf(1,3)
    print(my_line(5))
    ```

装饰器
- 增强而不改变原有函数
- 装饰器强调函数的定义态而不是运行态

    ```
    @decorate
    def target():
        print('do something')

    装饰器语法糖展开
    def target():
        print('do something')
    target = decorete(target)
    ```

 - 内置的装饰器方法函数
    ```
    functools.wraps
    @wraps接受一个函数进行装饰
    并加入了复制函数名称、注释文档、参数列表等等的功能
    在装饰器里面可以访问在装饰器之前的函数的属性
    ```

- 类装饰器 
    ```
    1. __init__(self, func)
    2. __call__(self, *args, **kargs)
    @wraps(func)
    ```
 

对象协议
鸭子类型的概念
 容器类型协议
 - __str__    打印对象时，more输出该方法的返回值
 - __getitem__, __setitem__, __delitem__  字典索引操作
 - __iter__  迭代器
 - __call__  可调用对象协议


生成器
return 返回后，函数状态终止
yield 保持函数执行状态，返回后，函数回到之前保存的状态继续执行, 不能重复取