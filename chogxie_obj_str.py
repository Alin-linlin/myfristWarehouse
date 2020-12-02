# 测试重写object__str__()


class Person:   # 默认继承obje类

    def __int__(self, name, age):
        self.name = name

    def __str__(self):
        self


p = Person('搞起')
print(p)