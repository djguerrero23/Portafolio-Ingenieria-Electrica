# -*- coding: utf-8 -*-
"""
Genera la figura "representacion_fasor_senoide.svg" para teoria_fasores.qmd:
correspondencia entre el fasor (sinor) V = Vm∠phi en t=0 y su onda v(t) en el
dominio del tiempo. Paleta alineada con las tarjetas del Carril Táctil del sitio.

Uso: ajusta OUTPUT_PATH a la ruta real de tu carpeta imagenes/ y ejecuta.
"""
import numpy as np
import matplotlib.pyplot as plt

# --- Paleta del sitio (igual que las tarjetas .card-module del Carril Táctil) ---
AZUL = '#0284c7'
GRIS = '#475569'
GRIS_CLARO = '#94a3b8'
TINTA = '#0f172a'
ROJO = '#dc2626'

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial']
plt.rcParams['mathtext.fontset'] = 'cm'

# --- Parámetros del fasor de ejemplo ---
Vm = 1.0
phi_deg = 40
phi = np.radians(phi_deg)

fig = plt.figure(figsize=(10.5, 4.7), dpi=300)
fig.patch.set_facecolor('white')

# ==========================================================================
# PANEL IZQUIERDO: plano fasorial (proyección polar nativa de matplotlib)
# ==========================================================================
axp = fig.add_subplot(1, 2, 1, projection='polar')
axp.set_theta_zero_location('E')
axp.set_theta_direction(1)
axp.set_facecolor('white')
axp.set_thetagrids(range(0, 360, 45), fontsize=9, color=GRIS)
axp.set_rgrids([0.5, 1.0], angle=125, fontsize=8, color=GRIS_CLARO)
axp.set_rlim(0, 1.28)
axp.spines['polar'].set_color(GRIS_CLARO)
axp.spines['polar'].set_linewidth(1.1)
axp.grid(color='#e2e8f0', linewidth=0.9)
axp.tick_params(colors=GRIS)

# Fasor V (flecha principal)
axp.annotate('', xy=(phi, Vm), xytext=(0, 0),
             arrowprops=dict(arrowstyle='-|>', color=AZUL, lw=2.8, mutation_scale=22))
axp.text(phi, Vm * 1.16, r'$\mathbf{V}=V_m\angle\phi$', color=AZUL,
          fontsize=12, fontweight='bold', ha='center', va='center')

# Arco del ángulo phi
arc_r = 0.32
thetas_arc = np.linspace(0, phi, 30)
axp.plot(thetas_arc, [arc_r] * len(thetas_arc), color=AZUL, lw=1.7)
axp.text(phi / 2, arc_r + 0.14, r'$\phi$', color=AZUL, fontsize=14,
          fontweight='bold', ha='center', va='center')

# Flecha curva de omega (sentido de giro antihorario), arriba-izquierda
om_thetas = np.linspace(np.radians(155), np.radians(105), 25)
axp.plot(om_thetas, [1.20] * len(om_thetas), color=GRIS, lw=1.6, linestyle='--')
axp.annotate('', xy=(np.radians(103), 1.20), xytext=(np.radians(113), 1.20),
             arrowprops=dict(arrowstyle='-|>', color=GRIS, lw=1.6, mutation_scale=13))
axp.text(np.radians(130), 1.42, r'$\omega$', fontsize=14, fontweight='bold', color=TINTA)

axp.set_title('Plano Fasorial — "Foto" en $t = 0$ s', fontsize=12,
               fontweight='bold', color=TINTA, pad=22)

# ==========================================================================
# PANEL DERECHO: dominio del tiempo v(t) = Vm cos(wt + phi)
# ==========================================================================
axt = fig.add_subplot(1, 2, 2)
axt.set_facecolor('white')

wt = np.linspace(-0.35, 2 * np.pi + 0.35, 500)
v = Vm * np.cos(wt + phi)
axt.plot(wt, v, color=AZUL, lw=2.6, label=r'$v(t)=V_m\cos(\omega t+\phi)$', clip_on=False)
axt.axhline(0, color=GRIS_CLARO, lw=1.0)

# Punto y guías en t = 0  ->  v(0) = Vm cos(phi)
v0 = Vm * np.cos(phi)
axt.plot(0, v0, 'o', color=ROJO, ms=8, zorder=5)
axt.hlines(v0, -0.35, 0, color=ROJO, linestyle=':', lw=1.3)
axt.vlines(0, -1.35, v0, color=ROJO, linestyle=':', lw=1.3)
axt.annotate(r'$v(0)=V_m\cos\phi$', xy=(0, v0), xytext=(1.15, v0 + 0.42),
              fontsize=10.5, color=ROJO, fontweight='bold',
              arrowprops=dict(arrowstyle='->', color=ROJO, lw=1.3))

ticks = [0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi]
labels = ['$0$', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$']
axt.set_xticks(ticks)
axt.set_xticklabels(labels, fontsize=10, color=GRIS)
axt.set_xlim(-0.35, 2 * np.pi + 0.35)
axt.set_ylim(-1.35, 1.55)
for spine in ['top', 'right']:
    axt.spines[spine].set_visible(False)
axt.spines['left'].set_color(GRIS_CLARO)
axt.spines['bottom'].set_color(GRIS_CLARO)
axt.set_xlabel(r'$\omega t$  (rad)', fontsize=10.5, fontweight='bold', color=TINTA)
axt.set_ylabel('Amplitud', fontsize=10.5, fontweight='bold', color=TINTA)
axt.legend(loc='lower right', fontsize=9.5, frameon=False)
axt.grid(True, linestyle='--', alpha=0.35)
axt.set_title('Dominio del Tiempo', fontsize=12, fontweight='bold', color=TINTA, pad=22)

# Nota conceptual conectando ambos paneles
fig.text(0.5, -0.02,
          r'$\mathbf{V}=V_m\angle\phi \;\Longleftrightarrow\; v(t)=\mathrm{Re}\{\mathbf{V}e^{j\omega t}\}=V_m\cos(\omega t+\phi)$',
          ha='center', fontsize=11, color=TINTA)

plt.tight_layout(rect=[0, 0.03, 1, 1])

OUTPUT_PATH = 'fasor_senoide.svg'  # <-- ajusta a tu ruta real imagenes/...
plt.savefig(OUTPUT_PATH, format='svg', bbox_inches='tight')
plt.savefig(OUTPUT_PATH.replace('.svg', '_preview.png'), format='png', bbox_inches='tight', dpi=200)
plt.close()
print(f"Listo: {OUTPUT_PATH}")
