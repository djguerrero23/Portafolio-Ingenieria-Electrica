import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(5, 5))

# Ejes principales Re e Im
ax.axhline(0, color='#1E293B', linewidth=1.5)
ax.axvline(0, color='#1E293B', linewidth=1.5)

lim = 6.2
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)

# Sombreado de cuadrantes con paleta institucional
ax.fill_between([0, lim], 0, lim, color='#EFF6FF', alpha=0.6)   # Q-I: Azul suave
ax.fill_between([-lim, 0], 0, lim, color='#F0FDF4', alpha=0.6)  # Q-II: Verde suave
ax.fill_between([-lim, 0], -lim, 0, color='#FEF3C7', alpha=0.6) # Q-III: Ámbar suave
ax.fill_between([0, lim], -lim, 0, color='#F5F3FF', alpha=0.6)  # Q-IV: Violeta suave

# 4 Fasores de ejemplo representativos
vectors = [
    (1.8, 2.4, '#1E40AF', r'$\mathbf{Z}_1 = 3 + j4$'),
    (-1.8, 2.4, '#047857', r'$\mathbf{Z}_2 = -3 + j4$'),
    (-1.8, -2.4, '#B45309', r'$\mathbf{Z}_3 = -3 - j4$'),
    (1.8, -2.4, '#6D28D9', r'$\mathbf{Z}_4 = 3 - j4$')
]

for x, y, col, lbl in vectors:
    ax.annotate('', xy=(x, y), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color=col, lw=2.5, mutation_scale=16))

# Textos informativos por cuadrante (sin caja y posicionados en los extremos)
ax.text(0.3, 2.8, 
        
        r'CUADRANTE I' + '\n' +
        r'[+x, +y] Inductivo' + '\n' +
        r'$(0^\circ < \theta < +90^\circ)$' + '\n' +
        r'$\theta = \arctan(y/x)$' + '\n' +
        r'$\mathbf{Z}_1 = 3 + j4 = 5\angle 53.1^\circ$' + '\n' +
        r'$ \arctan(4/3) = 53.1^\circ$',
        ha='left', va='bottom', fontsize=9, weight='bold', color='#1E40AF')


ax.text(-0.3, 2.8, 
        r'CUADRANTE II' + '\n' +
        r'[-x, +y] Inductivo' + '\n' +
        r'$(+90^\circ < \theta < +180^\circ)$' + '\n' +
        r'$\theta = 180^\circ - \arctan(|y/x|)$' + '\n' +
        r'$\mathbf{Z}_2 = -3 + j4 = 5\angle 126.9^\circ$' + '\n' +
        r'$ 180^\circ - \arctan(4/3) = 126.9^\circ$',
        ha='right', va='bottom', fontsize=9, weight='bold', color='#047857')

ax.text(-0.3, -2.8, 
        r'CUADRANTE III' + '\n' +
        r'[-x, -y] Capacitivo' + '\n' +
        r'$(-180^\circ < \theta < -90^\circ)$' + '\n' +
        r'$\theta = -180^\circ + \arctan(|y/x|)$' + '\n' +
        r'$\mathbf{Z}_3 = -3 - j4 = 5\angle -126.9^\circ$' + '\n' +
        r'$ -180^\circ + \arctan(4/3) =$'  + '\n' +
        r'$ -126.9^\circ$',
        ha='right', va='top', fontsize=9, weight='bold', color='#B45309')

ax.text(0.3, -2.8, 
        r'CUADRANTE IV' + '\n' +
        r'[+x, -y] Capacitivo' + '\n' +
        r'$(-90^\circ < \theta < 0^\circ)$' + '\n' +
        r'$\theta = -\arctan(|y/x|)$' + '\n' +
        r'$\mathbf{Z}_4 = 3 - j4 = 5\angle -53.1^\circ$' + '\n' +
        r'$ -\arctan(4/3) = -53.1^\circ$',
        ha='left', va='top', fontsize=9, weight='bold', color='#6D28D9')

ax.set_xlabel(r'Eje Real: $\mathrm{Re}(z) = x \quad [\mathrm{Resistencia} \ R]$', fontsize=11, weight='bold', labelpad=6)
ax.set_ylabel(r'Eje J: $\mathrm{Im}(z) = y \quad [+j \ \mathrm{Inductivo}, \ -j \ \mathrm{Capacitivo}]$', fontsize=11, weight='bold', labelpad=6)
ax.set_title('Plano Complejo: Guía Visual de Cuadrantes y Corrección de Fase Fasorial', fontsize=10.5, weight='bold', pad=12)
ax.grid(True, linestyle=':', alpha=0.6)
ax.set_aspect('equal')

OUTPUT_PATH = 'imagenes/cuad_fasorial.svg'  # <-- ajusta a tu ruta real imagenes/...
plt.savefig(OUTPUT_PATH, format='svg', bbox_inches='tight')
plt.savefig(OUTPUT_PATH.replace('.svg', '.png'), format='png', bbox_inches='tight', dpi=200)
plt.close()
print(f"Listo: {OUTPUT_PATH}")
