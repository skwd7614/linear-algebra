import numpy as np

u = np.array([1, 2])
v = np.array([6, -3])

inner = np.dot(u, v)

print("u · v =", inner)

if inner == 0:
    print("두 벡터는 직교한다.")
else:
    print("두 벡터는 직교하지 않는다.")