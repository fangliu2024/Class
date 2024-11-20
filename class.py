import numpy as np
import matplotlib.pyplot as plt

class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

# str.format() 
# 1. name = "Alice" age = 30 
# greeting = "Hello, {}. You are {} years old.".format(name, age)
# print(greeting)
# 2. greeting = "Hello, {0}. You are {1} years old. {0}, have a nice day!".format(name, age)
# print(greeting) 这里，{0} 和 {1} 分别指代 .format() 中的第一个和第二个参数。你可以重复使用这些位置参数
#3. greeting = "Hello, {name}. You are {age} years old.".format(name="Alice", age=30)
# print(greeting)
#4. number = 123.456
# formatted = "The number is {:.2f}".format(number)  # 保留两位小数
# print(formatted)
#5. text = "Hello"
# formatted = "|{:<10}|{:^10}|{:>10}|".format(text, text, text)
# print(formatted)
#:<10 表示左对齐并且填充至 10 个字符宽。
# :^10 表示居中对齐并且填充至 10 个字符宽。
# :>10 表示右对齐并且填充至 10 个字符宽。
#name = "Alice" age = 30
# greeting = f"Hello, {name}. You are {age} years old."
# print(greeting)

    #def show(self):
    #    print("{} + {}j".format(self.real,self.imag))

    def show(self):
        print(f"{self.real} + {self.imag}j")

        # 运算符重载
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imaginary_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imaginary_part)

    def __truediv__(self, other):
        denom = other.real ** 2 + other.imag ** 2
        real_part = (self.real * other.real + self.imag * other.imag) / denom
        imaginary_part = (self.imag * other.real - self.real * other.imag) / denom
        return Complex(real_part, imaginary_part)

    def __pow__(self, power):
        r = np.sqrt(self.real**2 + self.imag**2)
        theta = np.arctan2(self.imag, self.real)
        r_pow = r ** power
        new_real = r_pow * np.cos(power * theta)
        new_imag = r_pow * np.sin(power * theta)
        return Complex(new_real, new_imag)

    def __str__(self):
        return f"{self.real} + {self.imag}j"
# 返回复数的模和相位
    def magnitude(self):
        return np.sqrt(self.real**2 + self.imag**2)

    def phase(self):
        return np.arctan2(self.imag, self.real)
# 极坐标复数类，继承自 Complex

class PolarComplexNumber(Complex):
    def __init__(self,Complex):
        modulus = Complex.magnitude()
        argument = Complex.phase()
        real = modulus * np.cos(argument)
        imaginary = modulus * np.sin(argument)
        super().__init__(real, imaginary)
        self.modulus = modulus
        self.argument = argument

    def show_polar(self):
        print(f"{self.modulus} * (cos({self.argument}) + i*sin({self.argument}))")

    def __str__(self):
        # 输出极坐标格式
        return f"{self.modulus} * (cos({self.argument}) + i*sin({self.argument}))"

# 绘制复数函数的实部和虚部
def plot_complex_function():
    x_values = np.linspace(-2, 2, 400)#np.linspace 生成 400 个从 -2 到 2 的点作为 x 值
    y_real = []
    y_imaginary = []

    for x in x_values:
        y = Complex(x, x) ** 3  # y(x) = (x + xj)^3
        y_real.append(y.real)
        y_imaginary.append(y.imag)

    plt.plot(x_values, y_real, label="Real part")
    plt.plot(x_values, y_imaginary, label="Imaginary part")
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.legend()
    plt.title("y(x) = (x + xj)^3 的实部和虚部")
    plt.grid()
    plt.show()

#plot_complex_function()
a = Complex(1,2)
print(a)
pa = PolarComplexNumber(a)
print(pa)
pa.show_polar()	
print(str(pa))
