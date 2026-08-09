class FourCal:
    
    def __init__(self, first, second):
        self.first = first
        self.second = second
        
    def setdata(self, first, second):
        self.first = first
        self.second = second
        
    def add(self):
        result = self.first + self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4,2)
b = FourCal(3,7)
print(a.first)
print(b.first)

print(a.add())

"""
상속 기능 쓰는 이유?
상속 기능을 쓰면 기존 클래스의 기능을 그대로 사용하면서 새로운 기능을 추가할 수 있습니다.
예를 들어, 기존 클래스가 있고 새로운 클래스를 만들 때 기존 클래스의 기능을 그대로 사용하면서 새로운 기능을 추가할 수 있습니다.        
""" 

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

class MoreFourCal(FourCal):
    pass   
    


e = SafeFourCal(4,0)
print(e.div())
c = MoreFourCal(4,2)
print(c.add())
print(c.mul())
print(c.sub())
print(c.div())