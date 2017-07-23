"""
python 3.5
EDA模型不适合于对实时性，交互性高的场景
同时注意不要将事件分得太细，会明显加大CPU的负担

class EventManager
{
	Init()#initialization of event engine,事件引擎线程的初始化
	Start(),#事件引擎的启动
	Stop(),
	AddEventListener(),#add listener for certain event,为特定事件添加监听者
	RemoveEventListener(),#remove certain listener for certain event,去掉特定事件的特定监听者
	SendEvent(),#manager send event to event engine,发起事件
	set_Interval(),#set certain fucntion to act every X secs,设置按时间循环的轮循函数
	set_Timer()#set certain function to act after certain secs,设置定时器函数
}
class Event
{
	self.type = ''
	self.dict = {}
}
"""

from queue import Queue, Empty
from threading import Thread,Timer

class EventManager:
    def __init__(self):
        """初始化事件管理器"""
        #事件管理器开关
        self.__active = False
        #事件处理线程
        self.__thread = Thread(target = self.__Run)
        #事件管理器列表
        self.__eventQueue = Queue()
        #这里的__handlers是一个字典，用来保存__eventQueue中对应事件的响应函数
        #其中每个键对应的值是一个列表，列表中保存了对该事件监听的响应函数，一对多
        self.__handlers = {}

    def __Run(self):
        """引擎运行"""
        while self.__active == True:
            try:
                #获取事件的阻塞时间设为1秒
                event = self.__eventQueue.get(block = True, timeout = 1)
                self.__EventProcess(event)
            except Empty:
                pass

    def __EventProcess(self, event):
        #这个可以有两种处理方式，一种就是像现在这样子在列表中一个一个地顺序取出在本线程执行，还有就是可以本线程只跑获取句柄，然后每个处理函数新开线程并行跑
        """处理事件"""
        #检查是否存在对该事件进行监听的处理函数
        if event.type_ in self.__handlers:
            #若存在，则按顺序将事件传递给处理函数执行
            for handler in self.__handlers[event.type_]:
                handler(event)#这里面启动匹配的执行函数，绑定在hangdler中实行,处理函数handlers单线程顺序运行
                #handlerThread = Thread(target=handler)#处理函数handlers多线程并行运算
        else:
            print ("Error !this type of event haven't registered in __handlers:",event.type_)

    def Start(self):
        """启动"""
        #将事件管理器设为启动
        self.__active = True
        self.__thread.start()

    def Stop(self):
        """停止"""
        #将事件管理器设为停止
        self.__active = False
        #等待事件处理线程退出
        self.__thread.join()

    def AddEventListener(self,type_,handler):
        """绑定事件和监听器处理函数"""
        #尝试获取该事件类型对应的处理函数列表，若无该事件类型则创建
        try:
            handlerList = self.__handlers[type_]
        except KeyError:
            handlerList = []

        self.__handlers[type_] = handlerList
        #若要注册的处理函数不在该时间的处理函数列表中，则注册该事件

        if handler not in handlerList:
            handlerList .append(handler)

    def RemoceEventListener(self, type_, handler):
        """移除监听器的处理函数"""    
        try:
            handlerList = self.__handlers[type_]
            if handler in handlerList:
                handlerList.remove(handler)
            else:
                print ("this handler haven't registered in this event")
        except KeyError:
            print ("this type of event haven't registered in __handlers yet")

    def SendEvent(self,event):
        """发送事件，向事件队列中存入事件"""
        self.__eventQueue.put(event)
        pass#callback函数

    def setInterval(self,func,sec,intervalName):#每个任务新建一个线程，任务多时建议少用或者对任务进行包装,原函数无参数，无返回值
        def func_wrapper():
            try:
                self.setInterval(func,sec,intervalName)
                func()#type: function
            except BaseException as e:
                print ("Error in set_Interval",e)
                return
                #self.set_Interval(func, sec)
                #print type(func)
        self.intervalDict = {}
        try:
            self.intervalDict[intervalName] = Timer(sec, func_wrapper)#无需等待函数返回，非递归
            self.intervalDict[intervalName].start()
        except BaseException as e:
            print ("Error in setInterval ",e)
    #通过self.intervalDict[intervalName].cancel()取消

    def setTimer(self,func,sec):#每个任务新建一个线程，任务多时建议少用或者对任务进行包装
        t = Timer(interval=sec,function=func)
        t.start()
        return t
    #通过 t.cancel() 取消

"""事件对象"""
class Event:
    def __init__(self, type_=None):
        self.type_ = type_  #事件类型
        self.dict = {}      #字典用于保存具体的事件数据



count = 0
if __name__ == '__main__':
    def functionA(event):
        print ("function A done",str(event))

    CPU = EventManager()
    CPU.AddEventListener(type_='A',handler=functionA)
    CPU.Start()
    eventA = Event()
    eventA.type_ = 'A'
    CPU.SendEvent(eventA)
    def interval():
        global count
        count = count + 1
        print ("function interval done",count)
    CPU.setInterval(func=interval, sec=1,intervalName='hi')
    while (1):
        if count == 6:
            CPU.intervalDict['hi'].cancel()