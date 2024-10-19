class grandfather():
    def method1(self):
        print("this is the grandpa class")
class father():
    def method2(self):
        print("this is father class")
class son(grandfather,father):
    def method3(self):
        print("this is son class")

object=son()
object.method1() #accessing grandfather class by son's object
object.method2() #accessing father class by son's object
object.method3()# accessing son class
