#__*__coding:UTF-8__*__
#python3中的异常处理技巧

"""python 标准exception http://www.runoob.com/python/python-exceptions.html
BaseException	        所有异常的基类
SystemExit	            解释器请求退出
KeyboardInterrupt	    用户中断执行(通常是输入^C)
Exception	            常规错误的基类
StopIteration	        迭代器没有更多的值
GeneratorExit	        生成器(generator)发生异常来通知退出
StandardError	        所有的内建标准异常的基类
ArithmeticError	        所有数值计算错误的基类
FloatingPointError	    浮点计算错误
OverflowError	        数值运算超出最大限制
ZeroDivisionError	    除(或取模)零 (所有数据类型)
AssertionError	        断言语句失败
AttributeError	        对象没有这个属性
EOFError	            没有内建输入,到达EOF 标记
EnvironmentError	    操作系统错误的基类
IOError	                输入/输出操作失败
OSError	                操作系统错误
WindowsError	        系统调用失败
ImportError	            导入模块/对象失败
LookupError	            无效数据查询的基类
IndexError	            序列中没有此索引(index)
KeyError	            映射中没有这个键
MemoryError	            内存溢出错误(对于Python 解释器不是致命的)
NameError	            未声明/初始化对象 (没有属性)
UnboundLocalError	    访问未初始化的本地变量
ReferenceError	        弱引用(Weak reference)试图访问已经垃圾回收了的对象
RuntimeError	        一般的运行时错误
NotImplementedError	    尚未实现的方法
SyntaxError	Python      语法错误
IndentationError	    缩进错误
TabError	            Tab 和空格混用
SystemError	            一般的解释器系统错误
TypeError	            对类型无效的操作
ValueError	            传入无效的参数
UnicodeError	        Unicode 相关的错误
UnicodeDecodeError	    Unicode 解码时的错误
UnicodeEncodeError	    Unicode 编码时错误
UnicodeTranslateError	Unicode 转换时错误
Warning	                警告的基类
DeprecationWarning	    关于被弃用的特征的警告
FutureWarning	        关于构造将来语义会有改变的警告
OverflowWarning	        旧的关于自动提升为长整型(long)的警告
PendingDeprecationWarning	关于特性将会被废弃的警告
RuntimeWarning	        可疑的运行时行为(runtime behavior)的警告
SyntaxWarning	        可疑的语法的警告
UserWarning	            用户代码生成的警告
"""
#python 异常捕获，处理语句
try:
    #正常的操作，如果有异常则转到下面的异常处理模块
    if 1:
        raise NameError("hi, I'm here to raise a NameError")#也可以自主抛出异常
    else:
        pass
except ValueError:
    #发生类型Exception1时，执行这块代码
    pass
except (KeyError,IndexError):
    #发生列出的任一类型异常时，执行这块代码
    pass
except TypeError as e:
    print (e)#打印Exception5的异常信息
    pass
except:
    #发生任意类型异常时，执行这块代码
    import sys, traceback
    type, value, tracebackInfo = sys.exc_info()#获取系统的错误报告，返回的是一个元组
    print(type, value, tracebackInfo)#分别对应异常对象，异常信息，traceback信息对象
    traceback.print_exc()#等价于上面两句句
    print(traceback.format_exc())#效果等同于上面一句，不同在于上面显示的是红色的报错，这条显示的是黑色的打印信息
    traceback.print_tb(tracebackInfo)#traceback信息的打印
else:
    #如果没有异常执行这块代码
    print ("in else")
finally:
    #无论是否有异常发生，执行try之后都要执行finally，如果有异常则执行完finally之后再去执行except语句
    print("in finally")