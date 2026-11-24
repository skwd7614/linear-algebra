
import numpy as np
import matplotlib.pyplot as plt

# 세 벡터 정의
v1 = np.array([0, 1, 1])
v2 = np.array([1, 0, 1])
v3 = np.array([1, 1, 2])

# 3차원 그래프 생성
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection='3d')

# 평면 방정식: z = x + y
x = np.linspace(-1, 2, 20)
y = np.linspace(-1, 2, 20)
X, Y = np.meshgrid(x, y)
Z = X + Y

# 평면 그리기
ax.plot_surface(X, Y, Z, alpha=0.25, color='skyblue')

# 원점에서 시작하는 벡터 그리기
ax.quiver(0, 0, 0, *v1, color='red', linewidth=2)
ax.quiver(0, 0, 0, *v2, color='green', linewidth=2)
ax.quiver(0, 0, 0, *v3, color='blue', linewidth=2)

# 벡터 끝에 이름 표시
ax.text(*v1, 'v1', color='red', fontsize=12)
ax.text(*v2, 'v2', color='green', fontsize=12)
ax.text(*v3, 'v3 = v1 + v2', color='blue', fontsize=12)

# 좌표축 및 범위 설정
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_xlim(-1, 2)
ax.set_ylim(-1, 2)
ax.set_zlim(-2, 4)

ax.set_title('Span of v1, v2, v3')
ax.view_init(elev=25, azim=45)

plt.tight_layout()
plt.savefig('vector_plane.png', dpi=300)
plt.show()
