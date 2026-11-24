import numpy as np

u = np.array([1, 1, 0])
v = np.array([0, 1, 1])

cos_theta = np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
theta = np.degrees(np.arccos(cos_theta))

print("거리 =", np.linalg.norm(u - v))
print("각도 =", round(theta, 4))