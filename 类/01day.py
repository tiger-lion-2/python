class Student:
    def __init__(self, name):
        self.name = name
        print("姓名为%s的对象被创建！" % self.name)

    def __del__(self):
        print("姓名为%s的对象被销毁！" % self.name)


def func(name):
    stu = Student(name)


if __name__ == '__main__':
    stu1 = Student("张三")
    stu2 = Student("李四")
    stu3 = stu2
    del stu2  # 使用del删除stu2对象
    func("王五")
    # 如果多个变量对应同一片内存空间，则只有这些变量都删除后才会销毁这些内存空间中所保存的对象，也才会自动执行析构方法
    del stu3
    stu4 = Student("马六")