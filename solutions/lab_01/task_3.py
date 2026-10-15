import math

x = 17
y = 5
print("x + y =", x + y, "|", type(x + y))
print("x - y =", x - y, "|", type(x - y))
print("x * y =", x * y, "|", type(x * y))
print("x / y =", x / y, "|", type(x / y))
print("x // y =", x // y, "|", type(x // y))
print("x % y =", x % y, "|", type(x % y))
print("x ** y =", x ** y, "|", type(x ** y))

n = 2 ** 1000
print("2**1000 =", n)
print("Длина числа (знаков):", len(str(n)))
print("Тип:", type(n))

result = 0.1 + 0.2
print("result =", result)
print("result == 0.3:", result == 0.3)
print("result - 0.3 =", result - 0.3)
print("math.isclose(result, 0.3):", math.isclose(result, 0.3))

print("int('42') =", int("42"), "|", type(int("42")))
print("float('3.14') =", float("3.14"),  "|", type(float("3.14")))
print("str(2026) =", str(2026), "|", type(str(2026)))

print("bool(0) =", bool(0), "|", type(bool(0)))
print("bool(-1) =", bool(-1), "|", type(bool(-1)))
print("bool('') =", bool(""), "|", type(bool("")))
print("bool('False') =", bool("False"),  "|", type(bool("False")))

z = complex(2, -3)
print("z =", z, "| тип:", type(z))
print("Действительная часть:", z.real)
print("Мнимая часть:", z.imag)