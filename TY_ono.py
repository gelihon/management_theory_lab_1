import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# ======================
# ПАРАМЕТРЫ
# ======================
g = 9.81

# ======================
# СИСТЕМА 1
# u'' = -aφ - bφ'
# ======================
def system1(y, t, l, g, a, b):
    phi, phi_dot, u, u_dot = y
    
    u_ddot = -a * phi - b * phi_dot
    phi_ddot = (g / l) * phi + u_ddot / l
    
    return [phi_dot, phi_ddot, u_dot, u_ddot]

# ======================
# СИСТЕМА 2
# u'' = aφ + bφ' + cu + du'
# ======================
def system2(y, t, l, g, a, b, c, d):
    phi, phi_dot, u, u_dot = y
    
    u_ddot = a * phi + b * phi_dot + c * u + d * u_dot
    phi_ddot = (g / l) * phi + u_ddot / l
    
    return [phi_dot, phi_ddot, u_dot, u_ddot]

# ======================
# ОБЩИЕ НАСТРОЙКИ
# ======================
t = np.linspace(0, 20, 1000)

# ======================
# НАЧАЛЬНЫЕ УСЛОВИЯ
# ======================
y0_1 = [0.3, 0, 0, 0]
y0_2 = [0.1, 0, 0.1, 0]

l1 = 1.0
l2 = 0.5

# =========================================================
# 🔥 1. ВЛИЯНИЕ a (УПРАВЛЕНИЕ 1)
# =========================================================
a_values = [5, 12, 30, 50]  # есть и неустойчивый случай (a<g)

plt.figure()
for a in a_values:
    sol = odeint(system1, y0_1, t, args=(l1, g, a, 5))
    plt.plot(t, sol[:, 0], label=f"a={a}")

plt.title("Влияние коэффициента a (управление 1)")
plt.xlabel("t")
plt.ylabel("phi")
plt.legend()
plt.grid()
plt.show()

# =========================================================
# 🔥 2. ВЛИЯНИЕ b (УПРАВЛЕНИЕ 1)
# =========================================================
b_values = [0, 1, 5, 10]

plt.figure()
for b in b_values:
    sol = odeint(system1, y0_1, t, args=(l1, g, 30, b))
    plt.plot(t, sol[:, 0], label=f"b={b}")

plt.title("Влияние коэффициента b (управление 1)")
plt.xlabel("t")
plt.ylabel("phi")
plt.legend()
plt.grid()
plt.show()

# =========================================================
# 🔥 3. НЕУСТОЙЧИВЫЙ СЛУЧАЙ (управление 1)
# =========================================================
plt.figure()

# a < g (неустойчиво)
sol_bad = odeint(system1, y0_1, t, args=(l1, g, 5, 5))
plt.plot(t, sol_bad[:, 0], label="a < g (неустойчиво)")

plt.title("Неустойчивость (управление 1)")
plt.xlabel("t")
plt.ylabel("phi")
plt.legend()
plt.grid()
plt.show()

# =========================================================
# 🔥 4. УПРАВЛЕНИЕ 2 (СТАБИЛЬНЫЙ СЛУЧАЙ)
# =========================================================
a2 = -30
b2 = -5
c = 3
d = 2

sol = odeint(system2, y0_2, t, args=(l2, g, a2, b2, c, d))

plt.figure()
plt.plot(t, sol[:, 0], label="phi(t)")
plt.plot(t, sol[:, 2], label="u(t)")
plt.title("Полная стабилизация (управление 2)")
plt.xlabel("t")
plt.legend()
plt.grid()
plt.show()

# =========================================================
# 🔥 5. ВЛИЯНИЕ a (УПРАВЛЕНИЕ 2)
# =========================================================
a_values2 = [-15, -30, -50]

plt.figure()
for a in a_values2:
    sol = odeint(system2, y0_2, t, args=(l2, g, a, -5, 3, 2))
    plt.plot(t, sol[:, 0], label=f"a={a}")

plt.title("Влияние a (управление 2)")
plt.xlabel("t")
plt.ylabel("phi")
plt.legend()
plt.grid()
plt.show()

# =========================================================
# 🔥 6. ВЛИЯНИЕ b (УПРАВЛЕНИЕ 2)
# =========================================================
b_values2 = [-2, -5, -10]

plt.figure()
for b in b_values2:
    sol = odeint(system2, y0_2, t, args=(l2, g, -30, b, 3, 2))
    plt.plot(t, sol[:, 0], label=f"b={b}")

plt.title("Влияние b (управление 2)")
plt.xlabel("t")
plt.ylabel("phi")
plt.legend()
plt.grid()
plt.show()

# =========================================================
# 🔥 7. ВЛИЯНИЕ c
# =========================================================
c_values = [1, 3, 5, 10]

plt.figure()
for c_val in c_values:
    sol = odeint(system2, y0_2, t, args=(l2, g, -30, -5, c_val, 2))
    plt.plot(t, sol[:, 2], label=f"c={c_val}")

plt.title("Влияние c на u(t)")
plt.xlabel("t")
plt.ylabel("u")
plt.legend()
plt.grid()
plt.show()

# =========================================================
# 🔥 8. ВЛИЯНИЕ d
# =========================================================
d_values = [0.5, 2, 5]

plt.figure()
for d_val in d_values:
    sol = odeint(system2, y0_2, t, args=(l2, g, -30, -5, 3, d_val))
    plt.plot(t, sol[:, 2], label=f"d={d_val}")

plt.title("Влияние d на u(t)")
plt.xlabel("t")
plt.ylabel("u")
plt.legend()
plt.grid()
plt.show()