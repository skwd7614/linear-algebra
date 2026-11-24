import numpy as np

u = np.array([1, 2, 3])
v = np.array([-4, 3, 5])

print("거리 =", np.linalg.norm(v - u))