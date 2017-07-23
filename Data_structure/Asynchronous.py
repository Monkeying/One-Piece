from EDA import EventManager,Event

class MASTER(EventManager):
    def __init__(self):
        EventManager.__init__(self)
        self.Start()

    #如果你只是想让多个任务同时跑起来，就是不存在顺序先后的话而且不需要传进去数据的话
    def asynchronous(self, yourTaskList):#直接将你所有的任务包装成新的函数对象（需要添加一个event传入对象，传入的参数是要通过event.dict传入）然后统一发在这个列表中
        self.__TaskList = yourTaskList
        for task in self.__TaskList.values():#将任务添加到CPU的Run时间的任务列表中
            self.AddEventListener("Run",task)
        event = Event()
        event.type_ = "Run"
        self.SendEvent(event)#现在这个线程就开始按着yourTaskList的顺序开始自动跑起你的task列表了

    #绑定两个函数，即函数一二顺序发生
    def certainOrder(self,task1,task2):
        self.AddEventListener("1&2",task1)
        self.AddEventListener("1&2",task2)
        event = Event()
        event.type_ = "1&2"
        self.SendEvent(event)

    def yourHunderdTasks(self,HunderdTaskList):#这里面有两种方法，第一种最简单的方法是每一个Task开一个线程，第二种是对任务进行分解合并，用setInterval去手工实现CPU分时
        #第一种实现方法
        for task in HunderdTaskList:
            self.setTimer(task,1)#一秒后启动该线程
        #第二种实现方法
        self.set_Interval(taskInCommon,1)
        for task in HunderdTaskList:
            self.set_Interval(taskInDifferent,1)