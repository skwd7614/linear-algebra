import numpy as np

u = np.array([2, -5, -1])
v = np.array([-7, -4, 6])

print("u · v =", np.dot(u, v))
print("||u||^2 =", np.dot(u, u))
print("||u - v||^2 =", np.dot(u - v, u - v))