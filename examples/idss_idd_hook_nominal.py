"""

act = active
pas = passive
"""
import numpy as np
import matplotlib.pyplot as plt


deg_to_rad = np.pi / 180.0

# passive hook:
y_mating_plane_pas = 2.8
print(f"y_mating_plane_pas = {y_mating_plane_pas}")

theta_pas = np.pi/2.0 - 82.5*deg_to_rad
print(f"theta_pas = {theta_pas}")

r_pas = 15.0
print(f"r_pas = {r_pas}")

width_pas = 11.0
print(f"width_pas = {width_pas}")

x_coc_from_front_face_pas = 5.0 - 2.0
print(f"x_coc_from_front_face_pas = {x_coc_from_front_face_pas}")


# active hook:
y_mating_plane_act = 2.8
print(f"y_mating_plane_act = {y_mating_plane_act}")

theta_act = np.pi/2.0 - 82.5*deg_to_rad
print(f"theta_act = {theta_act}")

r_act = 15.0
print(f"r_act = {r_pas}")

width_act = 11.0
print(f"width_act = {width_act}")

x_coc_from_inside_face_act = width_act - (23.0 - 20.0)
print(f"x_coc_from_inside_face_act = {x_coc_from_inside_face_act}")


# combined:

# distance beteen the hooks due to offset from mating plane:
y_mating_plane = y_mating_plane_pas + y_mating_plane_act
print(f"y_mating_plane = {y_mating_plane}")

# need to find distance between centers of curvature
# datum = inside face of active hook

gap = np.max([0.0, width_act - width_pas])
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


x_range = np.linspace(0.0, xdist, 100)
y_list = []

for x in x_range:

    if x < x1:
        theta = np.arcsin(x/r_act)
        h = r_act * (1.0 - np.cos(theta))
        y2 = (xdist - x2 - x) * m_pas
        y = h2 + h + y2
    
    elif x > xdist - x2:
        theta = np.arcsin((xdist - x)/r_act)
        h = r_pas * (1.0 - np.cos(theta))
        y1 = (x - x1) * m_act
        y = h1 + h + y1
    elif x > x1 and x < xdist - x2:
        y1 = (x - x1) * m_act
        y2 = (xdist - x2 - x) * m_pas
        y = h1 + h2 + y1 + y2
    else:
        y = 0.0
    y_list.append(y)


min_y_dist = np.min(y_list)
print(f"min_y_dist = {min_y_dist}")


plt.figure()
plt.plot(x_range, y_list)
plt.plot([0],[0],marker=',')
plt.grid()
plt.savefig('nominal_y_dist')

plt.show()
