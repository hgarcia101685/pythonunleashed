class Example:
    def __init__(self, a, b):
        print("Class Constructed")
        self.a = a
        self.b = b

    def class_method1(self):
        print("I am  class method 1")

    def class_method2(self, a, b):
        return a + b

    def class_method3(self, a, b):
        return a * b

