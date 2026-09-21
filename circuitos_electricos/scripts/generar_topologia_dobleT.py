import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path
import numpy as np

def create_double_t_schematic():
    fig, ax = plt.subplots(figsize=(10, 6.2), dpi=300)
    ax.set_xlim(-5, 105)
    ax.set_ylim(-14, 108)
    ax.set_aspect('equal')
    ax.axis('off')

    # Card background
    card = patches.FancyBboxPatch((-2, -10), 104, 114, boxstyle="round,pad=1.5,rounding_size=4",
                                  facecolor='#f8fafc', edgecolor='#e2e8f0', linewidth=1.5)
    ax.add_patch(card)

    # Title
    ax.text(50, 98, "Red en Doble T (Filtro Notch en Paralelo)", fontsize=14, fontweight='bold',
            color='#0f172a', ha='center', va='center')

    # Main Coordinates
    y_top = 76
    y_mid = 36
    y_gnd = 8
    x_in = 6
    x_out = 94
    x_left = 14
    x_right = 86
    x_o1 = 40
    x_o2 = 66

    lw = 2.0
    wire_color = '#0f172a'

    # Terminals
    ax.plot([x_in, x_left], [56, 56], color=wire_color, lw=lw)
    ax.plot(x_in, 56, marker='o', markersize=8, markerfacecolor='white', markeredgecolor='#2563eb', markeredgewidth=2)
    ax.text(x_in - 2, 56, r"$\mathbf{1\ (A+)}$", fontsize=12, fontweight='bold', color='#2563eb', ha='right', va='center')

    ax.plot([x_right, x_out], [56, 56], color=wire_color, lw=lw)
    ax.plot(x_out, 56, marker='o', markersize=8, markerfacecolor='white', markeredgecolor='#dc2626', markeredgewidth=2)
    ax.text(x_out + 2, 56, r"$\mathbf{2\ (B-)}$", fontsize=12, fontweight='bold', color='#dc2626', ha='left', va='center')

    # Vertical distribution buses
    ax.plot([x_left, x_left], [y_mid, y_top], color=wire_color, lw=lw)
    ax.plot([x_right, x_right], [y_mid, y_top], color=wire_color, lw=lw)
    ax.plot(x_left, 56, marker='o', markersize=5, color=wire_color)
    ax.plot(x_right, 56, marker='o', markersize=5, color=wire_color)
    ax.plot(x_left, y_top, marker='o', markersize=5, color=wire_color)
    ax.plot(x_left, y_mid, marker='o', markersize=5, color=wire_color)
    ax.plot(x_right, y_top, marker='o', markersize=5, color=wire_color)
    ax.plot(x_right, y_mid, marker='o', markersize=5, color=wire_color)

    # Helper function: Resistor zigzag
    def draw_resistor_h(x1, x2, y, n_peaks=5, width=4):
        dx = (x2 - x1)
        xs = [x1]
        ys = [y]
        xs.append(x1 + dx * 0.2)
        ys.append(y)
        for i in range(n_peaks):
            xi = x1 + dx * 0.2 + (dx * 0.6 / n_peaks) * (i + 0.5)
            yi = y + (width if i % 2 == 0 else -width)
            xs.append(xi)
            ys.append(yi)
        xs.append(x1 + dx * 0.8)
        ys.append(y)
        xs.append(x2)
        ys.append(y)
        ax.plot(xs, ys, color=wire_color, lw=lw)

    def draw_resistor_v(x, y1, y2, n_peaks=5, width=3.5):
        dy = (y2 - y1)
        xs = [x]
        ys = [y1]
        xs.append(x)
        ys.append(y1 + dy * 0.2)
        for i in range(n_peaks):
            yi = y1 + dy * 0.2 + (dy * 0.6 / n_peaks) * (i + 0.5)
            xi = x + (width if i % 2 == 0 else -width)
            xs.append(xi)
            ys.append(yi)
        xs.append(x)
        ys.append(y1 + dy * 0.8)
        xs.append(x)
        ys.append(y2)
        ax.plot(xs, ys, color=wire_color, lw=lw)

    # Helper function: Inductor coils
    def draw_inductor_h(x1, x2, y, n_loops=4, radius=3.2):
        ax.plot([x1, x1 + (x2-x1)*0.15], [y, y], color=wire_color, lw=lw)
        start_x = x1 + (x2-x1)*0.15
        end_x = x2 - (x2-x1)*0.15
        coil_len = (end_x - start_x) / n_loops
        for i in range(n_loops):
            cx = start_x + (i + 0.5) * coil_len
            arc = patches.Arc((cx, y), coil_len, radius*2, angle=0, theta1=0, theta2=180, color=wire_color, lw=lw)
            ax.add_patch(arc)
        ax.plot([end_x, x2], [y, y], color=wire_color, lw=lw)

    # Helper function: Capacitor plates
    def draw_capacitor_v(x, y1, y2, plate_w=6, gap=3.5):
        ymid = (y1 + y2) / 2
        ax.plot([x, x], [y1, ymid - gap/2], color=wire_color, lw=lw)
        ax.plot([x - plate_w/2, x + plate_w/2], [ymid - gap/2, ymid - gap/2], color=wire_color, lw=lw + 0.5)
        ax.plot([x - plate_w/2, x + plate_w/2], [ymid + gap/2, ymid + gap/2], color=wire_color, lw=lw + 0.5)
        ax.plot([x, x], [ymid + gap/2, y2], color=wire_color, lw=lw)

    # ================= TOP T (Y1: Z1, Z2, Z3) =================
    # Z1 (Resistor 1 -> O1)
    draw_resistor_h(x_left, x_o1, y_top, n_peaks=5, width=4)
    # Z2 (Resistor O1 -> 2)
    draw_resistor_h(x_o1, x_right, y_top, n_peaks=5, width=4)

    # Z3 (Capacitor O1 -> Ground with Jumper at y_mid)
    draw_capacitor_v(x_o1, y_top, y_mid + 7, plate_w=7, gap=3.5)
    # Vertical line down to jumper
    ax.plot([x_o1, x_o1], [y_mid + 7, y_mid + 3.5], color=wire_color, lw=lw)
    # Jumper arc over lower wire
    jumper = patches.Arc((x_o1, y_mid), 6.5, 6.5, angle=90, theta1=-90, theta2=90, color=wire_color, lw=lw)
    ax.add_patch(jumper)
    # Vertical line from jumper to ground
    ax.plot([x_o1, x_o1], [y_mid - 3.5, y_gnd], color=wire_color, lw=lw)
    ax.plot(x_o1, y_gnd, marker='o', markersize=5, color=wire_color)

    # Node O1
    ax.plot(x_o1, y_top, marker='o', markersize=5.5, color=wire_color)
    ax.text(x_o1, y_top + 6.5, r"$\mathbf{O_1}$", fontsize=12, fontweight='bold', color='#7c3aed', ha='center', va='bottom')

    # ================= BOTTOM T (Y2: Z4, Z5, Z6) =================
    # Z4 (Inductor 1 -> O2, interrupted before jumper and continued)
    ax.plot([x_left, x_o1 - 3.5], [y_mid, y_mid], color=wire_color, lw=lw)
    ax.plot([x_o1 + 3.5, x_o1 + 8], [y_mid, y_mid], color=wire_color, lw=lw)
    draw_inductor_h(x_o1 + 8, x_o2, y_mid, n_loops=3, radius=3.2)

    # Z5 (Inductor O2 -> 2)
    draw_inductor_h(x_o2, x_right, y_mid, n_loops=4, radius=3.2)

    # Z6 (Resistor O2 -> Ground)
    draw_resistor_v(x_o2, y_mid, y_gnd, n_peaks=5, width=3.5)
    ax.plot(x_o2, y_gnd, marker='o', markersize=5, color=wire_color)

    # Node O2
    ax.plot(x_o2, y_mid, marker='o', markersize=5.5, color=wire_color)
    ax.text(x_o2, y_mid + 6.5, r"$\mathbf{O_2}$", fontsize=12, fontweight='bold', color='#7c3aed', ha='center', va='bottom')

    # ================= GROUND BUS =================
    x_gnd_start = 12
    x_gnd_end = 88
    ax.plot([x_gnd_start, x_gnd_end], [y_gnd, y_gnd], color=wire_color, lw=2.2)

    # Ground hash symbol in the middle
    xg_center = 52
    ax.plot([xg_center - 5, xg_center + 5], [y_gnd - 2.5, y_gnd - 2.5], color=wire_color, lw=2.0)
    ax.plot([xg_center - 3, xg_center + 3], [y_gnd - 4.5, y_gnd - 4.5], color=wire_color, lw=1.6)
    ax.plot([xg_center - 1.2, xg_center + 1.2], [y_gnd - 6.5, y_gnd - 6.5], color=wire_color, lw=1.2)

    # Ground label clearly positioned BELOW the hashes with zero collision
    ax.text(xg_center, y_gnd - 9.5, r"$\mathbf{0\ (Tierra\ /\ GND)}$", fontsize=11, fontweight='bold',
            color='#1e293b', ha='center', va='top')

    # ================= BADGES / LABELS =================
    bbox_props = dict(boxstyle='round,pad=0.35', facecolor='white', edgecolor='#cbd5e1', lw=1.2, alpha=0.95)

    # Z1 badge
    ax.text((x_left + x_o1)/2, y_top + 8, r"$\mathbf{R = 2\,\Omega}$" + "\n" + r"($\mathbf{Z_1}$)",
            fontsize=10, ha='center', va='center', color='#0f172a', bbox=bbox_props)

    # Z2 badge
    ax.text((x_o1 + x_right)/2, y_top + 8, r"$\mathbf{R = 2\,\Omega}$" + "\n" + r"($\mathbf{Z_2}$)",
            fontsize=10, ha='center', va='center', color='#0f172a', bbox=bbox_props)

    # Z3 badge
    ax.text(x_o1 - 8, (y_top + y_mid)/2 + 4, r"$\mathbf{X_C = 4\,\Omega}$" + "\n" + r"($\mathbf{Z_3 = -j4\,\Omega}$)",
            fontsize=10, ha='right', va='center', color='#0f172a', bbox=bbox_props)

    # Z4 badge (below inductor)
    ax.text((x_o1 + x_o2)/2 + 2, y_mid - 8.5, r"$\mathbf{X_L = 4\,\Omega}$" + "\n" + r"($\mathbf{Z_4 = j4\,\Omega}$)",
            fontsize=10, ha='center', va='center', color='#0f172a', bbox=bbox_props)

    # Z5 badge (above inductor)
    ax.text((x_o2 + x_right)/2, y_mid + 8.5, r"$\mathbf{X_L = 4\,\Omega}$" + "\n" + r"($\mathbf{Z_5 = j4\,\Omega}$)",
            fontsize=10, ha='center', va='center', color='#0f172a', bbox=bbox_props)

    # Z6 badge (to the right of resistor)
    ax.text(x_o2 + 7.5, (y_mid + y_gnd)/2, r"$\mathbf{R = 2\,\Omega}$" + "\n" + r"($\mathbf{Z_6}$)",
            fontsize=10, ha='left', va='center', color='#0f172a', bbox=bbox_props)

    out_path = "/home/david/UNI/AplicacionesPython/WEB/plantillas_arquitectura_electrica/portafolio-quarto/circuitos_electricos/imagenes/Eje8.png"
    plt.tight_layout()
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor='#f8fafc')
    plt.close()
    print("Successfully generated Eje8.png at", out_path)

if __name__ == "__main__":
    create_double_t_schematic()
