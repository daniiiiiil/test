# test
1.6(8)

class ExtendedStack(list):
    def sum(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 + top2)
        return self

    def sub(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 - top2)
        return self

    def mul(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 * top2)
        return self

    def div(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 // top2)
        return self
        
(9)

class LoggableList(Loggable, list):
    def append(self, arg):
        super(LoggableList, self).append(arg)
        self.log(arg)
        
2.1(6)

try:
    foo()
except ZeroDivisionError:
    print('ZeroDivisionError')
except ArithmeticError:
    print('ArithmeticError')
except AssertionError:
    print('AssertionError')
    
(9)

class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x > 0:
            super(PositiveList, self).append(x)
        else:
            raise NonPositiveError
