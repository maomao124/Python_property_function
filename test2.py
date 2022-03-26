"""
 * Project name(项目名称)：Python_property函数
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 21:54
 * Version(版本): 1.0
 * Description(描述)： Python 中提供了 property() 函数，可以实现在不破坏类封装原则的前提下，让开发者依旧使用“类对象.属性”的方式操作类中的属性。
 属性名=property(fget=None, fset=None, fdel=None, doc=None)

其中，fget 参数用于指定获取该属性值的类方法，fset 参数用于指定设置该属性值的方法，fdel 参数用于指定删除该属性值的方法，
最后的 doc 是一个文档字符串，用于说明此函数的作用。
 """


class C:
    # 构造函数
    def __init__(self, name):
        self.__name = name

    # 设置 name 属性值的函数
    def setName(self, name):
        self.__name = name

    # 访问name属性值的函数
    def getName(self):
        return self.__name

    # 删除name属性值的函数
    def delName(self):
        del self.__name

    name = property(getName, setName, delName, "name")


if __name__ == '__main__':
    print(C.name.__doc__)
    help(C.name)
    c = C("hello")
    print(c.name)
    c.name = "hello world"
    print(c.name)
    # del c.name
    print(c.name)
