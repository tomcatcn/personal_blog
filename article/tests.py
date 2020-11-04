from django.test import TestCase
import time
# Create your tests here.


def logit(name='文件'):
    def show_time(func):
        def wrapper(a,*args,**kwargs):
            print('装饰器内',args,kwargs,a)
            s = time.time()
            func(a,*args,**kwargs)
            e = time.time()
            print(e-s)
            print(name)
        return wrapper
    return show_time





@logit()
def my_func(a):
    print(a)
    print('程序正在运行')

my_func(1)



