import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

# Configuración de estilo moderno y limpio
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2), gridspec_kw={'width_ratios': [1, 1.4]}, dpi=300)
fig.patch.set_facecolor('#ffffff')

# --- SUBPLOT 1: PLANO FASORIAL (SINOR ROTATORIO) ---
ax1.set_facecolor('#ffffff')
circle = plt.Circle((0, 0), 1, fill=False, color='#334155', linewidth=1.5)
ax1.add_patch(circle)

# Ejes
ax1.axhline(0, color='#64748b', linewidth=1.2)
ax1.axvline(0, color='#64748b', linewidth=1.2)

# Ángulo phi y vector fasorial
phi_deg = 55
phi_rad = np.radians(phi_deg)
Vm = 1.0

# Vector Fasor V
ax1.annotate('', xy=(Vm * np.cos(phi_rad), Vm * np.sin(phi_rad)), xytext=(0, 0),
             arrowprops=dict(arrowstyle="-|>", color='#0284c7', lw=2.5, mutation_scale=18))

# Arco de ángulo phi
arc = Arc((0, 0), 0.55, 0.55, angle=0, theta1=0, theta2=phi_deg, color='#0284c7', lw=1.5)
ax1.add_patch(arc)
ax1.text(0.35 * np.cos(np.radians(phi_deg / 2)), 0.35 * np.sin(np.radians(phi_deg / 2)),
         r'$\phi$', fontsize=13, color='#0284c7', fontweight='bold')

# Flecha curva de velocidad angular omega
arc_w = Arc((0, 0), 2.25, 2.25, angle=0, theta1=115, theta2=155, color='#475569', lw=1.4, linestyle='--')
ax1.add_patch(arc_w)
ax1.annotate('', xy=(-0.95, 0.65), xytext=(-0.82, 0.82),
             arrowprops=dict(arrowstyle="-|>", color='#475569', lw=1.4, mutation_scale=12))
ax1.text(-1.18, 0.85, r'$\omega$', fontsize=13, fontweight='bold', color='#0f172a')

# Marcas de ejes fasoriales
ax1.text(1.05, -0.15, '$0$', fontsize=10, color='#475569')
ax1.text(-0.15, 1.08, r'$\pi/2$', fontsize=10, color='#475569')
ax1.text(-1.22, -0.15, r'$\pi$', fontsize=10, color='#475569')
ax1.text(-0.15, -1.22, r'$3\pi/2$', fontsize=10, color='#475569')
ax1.text(1.05, -0.32, r'$2\pi$', fontsize=10, color='#475569')

ax1.set_xlim(-1.35, 1.35)
ax1.set_ylim(-1.35, 1.35)
ax1.set_aspect('equal')
ax1.axis('off')
ax1.set_title("Plano Fasorial (Foto en $t=0$)", fontsize=11, fontweight='bold', color='#0f172a', pad=12)

# --- SUBPLOT 2: DOMINIO DEL TIEMPO v(t) ---
ax2.set_facecolor('#ffffff')
wt = np.linspace(-0.2, 2 * np.pi + 0.3, 400)
v = Vm * np.sin(wt + phi_rad)

ax2.axhline(0, color='#64748b', linewidth=1.2)
ax2.axvline(0, color='#64748b', linewidth=1.2, linestyle=':')
ax2.axvline(phi_rad, color='#0284c7', linewidth=1.2, linestyle='--')

ax2.plot(wt, v, color='#0284c7', linewidth=2.4, label=r'$v(t) = V_m \sin(\omega t + \phi)$')

# Proyecciones horizontales entre fasor y onda
y_proj = Vm * np.sin(phi_rad)
con1 = plt.Line2D([Vm * np.cos(phi_rad), 3.2], [y_proj, y_proj], color='#cbd5e1', linestyle='--', lw=1.2, transform=fig.transFigure)
# Línea guía horizontal a nivel de cresta
ax2.axhline(1, color='#e2e8f0', linestyle='--', linewidth=0.8)
ax2.axhline(-1, color='#e2e8f0', linestyle='--', linewidth=0.8)
ax2.axhline(y_proj, color='#94a3b8', linestyle=':', linewidth=1.1)

# Marcas en el eje X de tiempo
ticks_x = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
labels_x = ['$0$', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$']
ax2.set_xticks(ticks_x)
ax2.set_xticklabels(labels_x, fontsize=10, color='#334155')

ax2.set_xlim(-0.2, 2 * np.pi + 0.3)
ax2.set_ylim(-1.35, 1.35)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['bottom'].set_color('#64748b')
ax2.yaxis.set_visible(False)

# Anotación del desfase phi en el tiempo
ax2.annotate('', xy=(phi_rad, -0.4), xytext=(0, -0.4),
             arrowprops=dict(arrowstyle="<->", color='#0284c7', lw=1.4))
ax2.text(phi_rad / 2, -0.65, r'$\phi$', fontsize=12, color='#0284c7', fontweight='bold', ha='center')

ax2.text(2 * np.pi + 0.15, -0.22, r'$\omega t$', fontsize=11, fontweight='bold', color='#0f172a')
ax2.text(0.05, 1.15, r'$v(t)$', fontsize=12, fontweight='bold', color='#0284c7')

ax2.set_title("Dominio del Tiempo (Onda Senoidal)", fontsize=11, fontweight='bold', color='#0f172a', pad=12)

plt.tight_layout()
plt.savefig('/home/david/UNI/AplicacionesPython/WEB/plantillas_arquitectura_electrica/portafolio-quarto/circuitos_electricos/imagenes/representacion_fasor_senoide.svg', format='svg', bbox_inches='tight')
plt.close()
print("SVG generado con éxito.")
