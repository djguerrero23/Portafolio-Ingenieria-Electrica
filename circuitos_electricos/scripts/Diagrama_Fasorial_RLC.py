import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 3, figsize=(9, 2.5), subplot_kw={'projection': 'polar'})
titles = ['Resistor (En Fase)', 'Inductor (ELI: V Adelanta)', 'Capacitor (ICE: I Adelanta)']

data = [
    [(8, 0), (5, 0)],                      # Resistor: En fase
    [(8, np.pi/2), (5, 0)],                # Inductor: Voltaje adelanta 90°
    [(8, 0), (5, np.pi/2)]                 # Capacitor: Corriente adelanta 90°
]

colors = ['#DC2626', '#059669'] # Rojo para Voltaje, Verde para Corriente

for i, ax in enumerate(axs):
    V_param, I_param = data[i]
    
    # Vector de Voltaje
    ax.annotate('', xy=(V_param[1], V_param[0]), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", color=colors[0], lw=2.5, mutation_scale=12))
    # Vector de Corriente
    ax.annotate('', xy=(I_param[1], I_param[0]), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", color=colors[1], lw=2.5, mutation_scale=12))
    
    ax.set_rmax(10)
    ax.set_yticks([5, 8])
    ax.set_yticklabels([])
    ax.tick_params(axis='y', labelsize=11)
    ax.tick_params(axis='x', labelsize=13)
    ax.set_title(titles[i], pad=15, weight='bold', size=11)
    ax.grid(True, linestyle='--', alpha=0.5)
    

OUTPUT_PATH = 'imagenes/diagrama_fasorial_RLC.svg'  # <-- ajusta a tu ruta real imagenes/...
plt.savefig(OUTPUT_PATH, format='svg', bbox_inches='tight')
plt.savefig(OUTPUT_PATH.replace('.svg', '_preview.png'), format='png', bbox_inches='tight', dpi=200)
plt.close()
print(f"Listo: {OUTPUT_PATH}")
