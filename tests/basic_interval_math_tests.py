import numpy as np
import interval_math
from interval_math import Interval


A = interval_math.Interval(2, 1)
print(f"A = {A}")

B = Interval(1, 2)
print(f"B = {B}")

C = 2.0 * A
print(f"C = {C}")

D = B + 1.0
print(f"D = {D}")

sD = interval_math.sqrt(D)
print(f"sqrt(D) = {sD}")

E = A - 3.0
print(f"E = {E}")

F = B / 3.0
print(f"F = {F}")

print(f"A + B = {A + B}")
print(f"A - B = {A - B}")
print(f"A * B = {A * B}")
print(f"A / Interval(1, 2) = {A / Interval(1, 2)}")

print(f"A == B: {A==B}")

x = Interval(-2, 3)

print(f"x = {x}")
print(f"-x = {-x}")
print(f"abs(x) = {abs(x)}")
print(f"x**2 = {x**2}")
print(f"x.exp() = {x.exp()}")
print(f"x.sin() = {x.sin()}")
print(f"interval.sin(x) = {interval_math.sin(x)}")
print(f"1 in x = {1 in x}")
print(f"x.intersection(Interval(1, 10)) = {x.intersection(Interval(1, 10))}")


# Special tests for trigonometry:
theta = Interval(np.pi/8.0, np.pi/8.0+0.001)
theta = Interval(-0.001, +0.001)
# theta = Interval(np.pi/2.0-0.001, np.pi/2.0+0.001)
theta = Interval(np.pi-0.001, np.pi+0.001)

print(f"sin(theta) = {interval_math.sin(theta)}")
print(f"cos(theta) = {interval_math.cos(theta)}")
print(f"tan(theta) = {interval_math.tan(theta)}")


# Special tests for comparisons:
val1 = Interval(1, 4)
val2 = Interval(2, 3)

print(f"val1 > val2 = {val1 > val2}")
print(f"val1 < val2 = {val1 < val2}")
print(f"val1 == val2 = {val1 == val2}")
print(f"val1 != val2 = {val1 != val2}")


array = np.array([1,2,3,4,5])


try:
    val3 = val1 * array
    print(f"val3 = {val3}")
except:
    print("failed...")

