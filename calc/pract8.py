class Calculator:
    last = None
    def __init__(self):
        self.history_array = list()
        

    def sum(self, a, b):
        self.last = "sum({0}, {1}) == {2}".format(a, b, a+b)
        self.history_array.append(self.last)
        return a + b

    def sub(self, a, b):
        self.last = 'sub({0}, {1}) == {2}'.format(a, b, a-b)
        self.history_array.append(self.last)
        return a-b

    def mul(self, a, b):
        self.last = 'mul({0}, {1}) == {2}'.format(a, b, a*b)
        self.history_array.append(self.last)
        return a*b

    def div(self, a, b, mod = False):
        if (not mod):
            c = a/b
            self.last = f"div({a}, {b}) == {c}"
        else:
            c = a%b
            self.last = 'div({0}, {1}) == {2}'.format(a, b, c)
        
        self.history_array.append(self.last)
        return c

    def history(self, n):
        a = len(self.history_array)-n
        if (a < 0) or (a > len(self.history_array)-1): return False
        return self.history_array[a]

    def clear(cls):
        Calculator.last = None

# from classes1_tests import Test

# Test(Calculator).run_all()


calc = Calculator()
print(calc.sum(3,2))
print(calc.sum(2,2))
print(calc.sum(1,2))
print(calc.last)
print(calc.history(1))
print(calc.history(2))
print(calc.history(3))


