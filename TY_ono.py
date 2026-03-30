import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Параметры системы
g = 9.81         # ускорение свободного падения, м/с² 

# ======================
# Система дифференциальных уравнений
# Управление 1: u'' = -a*φ - b*φ'
# ======================
def system(y, t, l, g, a, b):
    phi, phi_dot, u, u_dot = y
    
    # Управление
    u_ddot = a * phi + b * phi_dot
    
    # Уравнение движения маятника
    phi_ddot = (g / l) * phi + u_ddot / l
    
    return [phi_dot, phi_ddot, u_dot, u_ddot]


# ======================
# Система дифференциальных уравнений
# Управление 2: u'' = a*φ + b*φ' + с*u + d*u'
# ======================
def system2(y,t,l,g,a,b,c,d):
    phi, phi_dot, u, u_dot = y
    
    # Управление
    u_ddot = a*phi + b*phi_dot + c*u + d*u_dot
    
    # Уравнение движения маятника
    phi_ddot = (g/l)*phi + u_ddot/l

    return [phi_dot, phi_ddot, u_dot, u_ddot]

# ======================
# Параметры
# ======================
l1 = 1.0          # длина маятника (УПРАВЛЕНИЕ 1)
l2 = 0.5          # длина маятника (УПРАВЛЕНИЕ 2)

# Начальные условия 1
phi0 = 0.3       # начальный угол
phi_dot0 = 0.0   # начальная угловая скорость
u0 = 0.0         # начальное положение опоры
u_dot0 = 0.0     # начальная скорость опоры


# Начальные условия 2
phi02 = 0.1       # начальный угол
phi_dot02 = 0.0   # начальная угловая скорость
u02 = 0.1         # начальное положение опоры
u_dot02 = 0.0     # начальная скорость опоры

# Параметры для первых графиков
# Параметры управления (управление 1)
a1 = -30.0         # коэффициент при φ (должен быть < -g для устойчивости)
b1 = -5.0          # коэффициент при φ' (должен быть < 0)

# Параметры управления (управление 2)
c = 3.0          # коэффициент при u (должен быть > 0 для уст)
d = 2.0          # коэффициент при u' (должен быть > 0 для уст)
a2 = -30     # коэффициент при φ (должен быть < 0)
b2 = -5     # коэффициент при φ' (должен быть < 0)


# Время моделирования
t_max = 20.0
t = np.linspace(0, t_max, 1000)


# Начальный вектор состояния
y0_1 = [phi0, phi_dot0, u0, u_dot0]
y0_2 = [phi02, phi_dot02, u02, u_dot02]
# Решение системы
sol1 = odeint(system, y0_1, t, args=(l1, g, a1, b1))
sol2 = odeint(system2, y0_2,t,args=(l2,g,a2,b2,c,d))
# Извлечение результатов
phi1 = sol1[:, 0]
u1 = sol1[:, 2]


phi2 = sol2[:, 0]
u2 = sol2[:, 2]

# ======================
# Построение графиков как на Рис. 2
# ======================
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# График 1: угол отклонения маятника φ(t)
ax1.plot(t, phi1, color='green', linewidth=2, label='φ(t)') 
ax1.set_xlabel('t, c')
ax1.set_ylabel('φ, рад')
ax1.set_title('Угол отклонения маятника φ(t)')
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_xlim(0, 10)
ax1.set_ylim(-0.2, 0.35)
ax1.legend()

# График 2: положение точки опоры u(t)
ax2.plot(t, u1, color='orange', linewidth=2, label='u(t)') 
ax2.set_xlabel('t, c')
ax2.set_ylabel('u, м')
ax2.set_title('Положение точки опоры u(t)')
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.set_xlim(0, 10)
ax2.legend()

plt.tight_layout()
plt.savefig('fig2_phi_and_u.png', dpi=150)
plt.show()


# ======================
# Построение графиков как на Рис 3
# ======================
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# График 1: угол отклонения маятника φ(t)
ax1.plot(t, phi2, color='green', linewidth=2, label='φ(t)') 
ax1.set_xlabel('t, c')
ax1.set_ylabel('φ, рад')
ax1.set_title('Угол отклонения маятника φ(t)')
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_xlim(0, 20)
ax1.set_ylim(-0.5, 0.5)
ax1.legend()

# График 2: положение точки опоры u(t)
ax2.plot(t, u2, color='orange', linewidth=2, label='u(t)')  
ax2.set_xlabel('t, c')
ax2.set_ylabel('u, м')
ax2.set_title('Положение точки опоры u(t)')
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.set_xlim(0, 20)
ax2.set_ylim(-1.3, 0.2)
ax2.legend()

plt.tight_layout()
plt.savefig('fig3_phi_and_u.png', dpi=150)
plt.show()

# =========================================================
# Дальше идет исследования коэф
# =========================================================

# =========================================================
# влияние a (УПРАВЛЕНИЕ 1)
# =========================================================
a_values = [-15, -30,-60]  # есть и неустойчивый случай (a<-g)

plt.figure()
for a in a_values:
    sol = odeint(system, y0_1, t, args=(l1, g, a, -5))
    plt.plot(t, sol[:, 0], label=f"a={a}")

plt.title("Влияние коэффициента a (управление 1)")
plt.xlabel("t")
plt.ylabel("phi")
plt.legend()
plt.ylim(-0.2, 0.5)
plt.grid()
plt.show()

# =========================================================
# влияние b (УПРАВЛЕНИЕ 1)
# =========================================================
b_values = [-1, -5, -10]

plt.figure()
for b in b_values:
    sol = odeint(system, y0_1, t, args=(l1, g, -30, b))
    plt.plot(t, sol[:, 0], label=f"b={b}")

plt.title("Влияние коэффициента b (управление 1)")
plt.xlabel("t")
plt.ylabel("phi")
plt.legend()
plt.grid()
plt.show()


# =========================================================
# ВЛИЯНИЕ a (УПРАВЛЕНИЕ 2)
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
# ВЛИЯНИЕ b (УПРАВЛЕНИЕ 2)
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
#  ВЛИЯНИЕ c
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
    if(c_values == 1 or c_values == 3 or c_values == 5):
        plt.ylim(-0.2, 0.2)
        


# =========================================================
# ВЛИЯНИЕ d
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
