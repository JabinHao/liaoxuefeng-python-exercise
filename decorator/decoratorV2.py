#decorator2.py
import functools
def log(text='nonename'):
	if isinstance(text,str):
		def decortaor(func):
			@functools.wraps(func)
			def wrapper(*args, **kw):
				print('%s %s():' % (text, func.__name__))
				return func(*args, **kw)
			return wrapper
		return decortaor
	else:
#	elif type(text)=='function':                                                               
		@functools.wraps(text)
		def wrapper(*args, **kw):
			print('call %s():' % text.__name__)
			return text(*args, **kw)
#		print('call %s():' % text.__name__)
		return wrapper
@log
def f1():
	print('Good evening')
@log()
def f2():
	print('hello guys')
@log('execute')
def f3():
	print('Good night')
f1()
f2()
f3()

