#decorator.py 廖雪峰-装饰器
'''def log(func):
    def wraper(*args,**kw):
        print("begin call")
        func(*args,**kw)
        print("end call")
    return wraper
@log
def printf(something='1'):
    print("hello!{}".format(something))
printf()
'''
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        func(*args, **kw)
    return wrapper
@log
def now():
    print('2015-3-25')
now()
