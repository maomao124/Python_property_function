"""
 * Project name(项目名称)：Python_property函数
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 21:51
 * Version(版本): 1.0
 * Description(描述)： 
 """


class C:
    # 构造函数
    def __init__(self, name):
        self.name = name

    # 设置 name 属性值的函数
    def setName(self, name):
        self.name = name

    # 访问name属性值的函数
    def getName(self):
        return self.name

    # 删除name属性值的函数
    def delName(self):
        del self.name


if __name__ == '__main__':
    c = C("hello")
    # 获取name属性值
    print(c.getName())
    # 设置name属性值
    c.setName("hello world")
    print(c.getName())
    # 删除name属性值
    c.delName()
    # print(c.getName())
