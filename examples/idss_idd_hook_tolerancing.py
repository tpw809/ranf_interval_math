"""

act = active
pas = passive
"""
import numpy as np
import matplotlib.pyplot as plt
from interval_math import Interval, arcsin, min, max

deg_to_rad = np.pi / 180.0

# passive hook:
y_mating_plane_pas = Interval(2.8-0.07, 2.8+0.05)
print(f"y_mating_plane_pas = {y_mating_plane_pas}")

theta_pas = Interval(np.pi/2.0 - 82.0*deg_to_rad, np.pi/2.0 - 83.0*deg_to_rad)
print(f"theta_pas = {theta_pas}")

r_pas = Interval(15.0-0.25, 15.0+0.25)
print(f"r_pas = {r_pas}")

width_pas = Interval(11.0, 11.0+0.43)
print(f"width_pas = {width_pas}")

x_coc_from_front_face_pas = 5.0 - Interval(2.0-0.1, 2.0+0.1)
print(f"x_coc_from_front_face_pas = {x_coc_from_front_face_pas}")


# active hook:
y_mating_plane_act = Interval(2.8-0.07, 2.8+0.05)
print(f"y_mating_plane_act = {y_mating_plane_act}")

theta_act = Interval(np.pi/2.0 - 82.0*deg_to_rad, np.pi/2.0 - 83.0*deg_to_rad)
print(f"theta_act = {theta_act}")

r_act = Interval(15.0-0.25, 15.0+0.25)
print(f"r_act = {r_pas}")

width_act = Interval(11.0, 11.0+0.24)
print(f"width_act = {width_act}")

x_coc_from_inside_face_act = width_act - (Interval(23.0-0.1, 23.0+0.1) - (Interval(20.0-0.1, 20.0+0.1)))
print(f"x_coc_from_inside_face_act = {x_coc_from_inside_face_act}")


# combined:

# distance beteen the hooks due to offset from mating plane:
y_mating_plane = y_mating_plane_pas + y_mating_plane_act
print(f"y_mating_plane = {y_mating_plane}")

# need to find distance between centers of curvature
# datum = inside face of active hook

gap = np.max([0.0, width_act - width_pas])
gap.min = 0.0
print(f"gap = {gap}")

x_coc_act = x_coc_from_inside_face_act
x_coc_pas = gap + x_coc_from_front_face_pas

xdist = x_coc_act - x_coc_pas
print(f"xdist = {xdist}")

# distance between contact in y direction:
h1 = r_act * (1.0 - np.cos(theta_act))
h2 = r_pas * (1.0 - np.cos(theta_pas))
print(f"h1 = {h1}")
print(f"h2 = {h2}")

x1 = r_act * np.sin(theta_act)
x2 = r_pas * np.sin(theta_pas)
print(f"x1 = {x1}")
print(f"x2 = {x2}")

# line slopes:
m_act = np.tan(theta_act)
m_pas = np.tan(theta_pas)
print(f"m_act = {m_act}")
print(f"m_pas = {m_pas}")


# how to do xrange with interval?
x_range = np.linspace(0.0, max(xdist), 100)
# instead only look at linear overlap zone:
x_range = np.linspace(min(x1), max(x1), 100)
# print(x_range)
y_min_list = []
y_max_list = []

# need case consistency for these discreet behaviors...
for x in x_range:
    
    theta1 = arcsin(x/r_act)
    theta2 = arcsin((xdist - x)/r_act)

    # if x < x1:
    #     h = r_act * (1.0 - np.cos(theta1))
    #     y2 = (xdist - x2 - x) * m_pas
    #     y = h2 + h + y2
    # 
    # elif x > xdist - x2:
    #     h = r_pas * (1.0 - np.cos(theta2))
    #     y1 = (x - x1) * m_act
    #     y = h1 + h + y1
    # elif x > x1 and x < xdist - x2:
    #     y1 = (x - x1) * m_act
    #     y2 = (xdist - x2 - x) * m_pas
    #     y = h1 + h2 + y1 + y2
    # else:
    #     y = 0.0
    
    y1 = (x - x1) * m_act
    y2 = (xdist - x2 - x) * m_pas
    y = h1 + h2 + y1 + y2
    
    # print(f"y = {y}")
    # print(f"min(y) = {min(y)}")
    y_min_list.append(min(y))
    y_max_list.append(max(y))


y_min_list = np.array(y_min_list)
# print(y_min_list)

min_y_dist = np.min(y_min_list)
print(f"min_y_dist = {min_y_dist}")

max_y_dist = np.min(y_max_list)
print(f"max_y_dist = {max_y_dist}")


plt.figure()
plt.plot(x_range, y_min_list)
plt.plot(x_range, y_max_list)
plt.plot([2.0],[0],marker=',')
plt.grid()
plt.savefig('toleranced_y_dist')

plt.show()
