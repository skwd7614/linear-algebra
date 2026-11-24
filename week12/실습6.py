import numpy as np

u = np.array([1, -1, 0])
v = np.array([2, -1, 2])

cos_theta = np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
theta = np.degrees(np.arccos(cos_theta))

print("각도 =", round(theta, 4))