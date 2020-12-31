class MyClass:

    def __init__(self):
        with open("f1.txt","r") as f:
         global var1
         global var2
         var1 = f.readline()
         var2 = f.readline(2)
    def fun1(self):
        print( "Value of var1 is {} and var2 is {}  ".format(var1,var2))

    def fun2(self):
        global var2
        list = [2,4,6,8,10]
        list.append(int(var2))
        var2=sum(list)



object = MyClass()
object.fun1()
object.fun2()
object.fun1()