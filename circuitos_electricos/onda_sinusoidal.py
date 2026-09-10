import numpy as np
import matplotlib.pyplot as plt

# Configuración de estilo
plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
})

# Parámetros de la señal senoidal
Vm = 10          # Amplitud máxima
theta_deg = 45   # Fase inicial en grados
theta_rad = np.radians(theta_deg)
omega = 2 * np.pi * 50 # Frecuencia de 50 Hz

# Crear figura acoplada
fig = plt.figure(figsize=(10, 3))
ax1 = plt.subplot(1, 2, 1, projection='polar') # Plano Complejo
ax2 = plt.subplot(1, 2, 2)                     # Dominio del Tiempo

# 1. Graficar Fasor en Plano Complejo (t = 0 s)
ax1.annotate('', xy=(theta_rad, Vm), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", color="#003891", lw=2.5, mutation_scale=15))
ax1.plot(theta_rad, Vm, 'o', color="#003891", markersize=7)
ax1.set_title(f'Fasor V = {Vm} ∠ {theta_deg}° (t = 0 s)', pad=15, weight='bold', color="#0F172A")
ax1.set_yticks([5, 10])
ax1.grid(True, linestyle='--', alpha=0.6)

# 2. Graficar Onda Senoidal en el Tiempo
t = np.linspace(0, 0.04, 500) # Dos ciclos para 50 Hz (T = 0.02 s)
v_t = Vm * np.cos(omega * t + theta_rad)

ax2.plot(t * 1000, v_t, color='#1E40AF', linewidth=2.2, label=r'$v(t) = V_m\cos(\omega t + \theta)$')
v_0 = Vm * np.cos(theta_rad)
ax2.plot(0, v_0, 'ro', markersize=7, label=r'Valor en $t=0$ ($V_m\cos\theta$)')
ax2.axhline(0, color='black', linewidth=0.8, linestyle='--')

ax2.set_xlabel('Tiempo (ms)')
ax2.set_ylabel('Voltaje (V)')
ax2.set_title('Dominio del Tiempo', weight='bold')
ax2.set_xlim(-2, 40)
ax2.set_ylim(-12, 12)
ax2.grid(True, linestyle=':', alpha=0.8)
ax2.legend(loc='upper right', fontsize=11)

OUTPUT_PATH = 'imagenes/onda_sinusoidal.svg'  # <-- ajusta a tu ruta real imagenes/...
plt.savefig(OUTPUT_PATH, format='svg', bbox_inches='tight')
plt.savefig(OUTPUT_PATH.replace('.svg', '.png'), format='png', bbox_inches='tight', dpi=200)
plt.close()
print(f"Listo: {OUTPUT_PATH}")