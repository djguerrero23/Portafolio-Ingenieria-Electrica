"""
Script de Cálculo Fasorial y Potencia Compleja en Sistemas Eléctricos CA
Autor: David Josue Guerrero Echeverry
"""

import numpy as np
import matplotlib.pyplot as plt

def calcular_potencia(v_mag: float, v_ang_deg: float, i_mag: float, i_ang_deg: float):
    # Conversión a radianes
    v_rad = np.radians(v_ang_deg)
    i_rad = np.radians(i_ang_deg)
    
    # Representación rectangular fasorial
    V = v_mag * np.exp(1j * v_rad)
    I = i_mag * np.exp(1j * i_rad)
    
    # Potencia compleja: S = V * I^*
    S = V * np.conjugate(I)
    P = S.real
    Q = S.imag
    S_mag = np.abs(S)
    
    diff_deg = v_ang_deg - i_ang_deg
    fp = np.cos(np.radians(diff_deg))
    tipo_fp = "Atraso (Inductivo)" if diff_deg > 0 else ("Adelanto (Capacitivo)" if diff_deg < 0 else "Unitario")
    
    return {
        "V": V,
        "I": I,
        "S": S,
        "P": P,
        "Q": Q,
        "S_mag": S_mag,
        "FP": fp,
        "Tipo_FP": tipo_fp
    }

def graficar_fasores(res, v_mag, v_ang, i_mag, i_ang):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axhline(0, color='gray', linestyle='--', linewidth=0.8)
    ax.axvline(0, color='gray', linestyle='--', linewidth=0.8)
    
    ax.quiver(0, 0, res["V"].real, res["V"].imag, angles='xy', scale_units='xy', scale=1,
              color='blue', label=f'Voltaje ({v_mag} V ∠{v_ang}°)')
    ax.quiver(0, 0, res["I"].real, res["I"].imag, angles='xy', scale_units='xy', scale=1,
              color='red', label=f'Corriente ({i_mag} A ∠{i_ang}°)')
    
    lim = max(v_mag, i_mag) * 1.2
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend()
    ax.set_title("Diagrama Fasorial en el Plano Complejo")
    ax.set_xlabel("Re")
    ax.set_ylabel("Im")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    v_mag, v_ang = 120.0, 0.0
    i_mag, i_ang = 10.0, -30.0
    
    res = calcular_potencia(v_mag, v_ang, i_mag, i_ang)
    print("--- RESULTADOS DE POTENCIA COMPLEJA ---")
    print(f"Potencia Activa (P):   {res['P']:.2f} W")
    print(f"Potencia Reactiva (Q): {res['Q']:.2f} VAR")
    print(f"Potencia Aparente |S|: {res['S_mag']:.2f} VA")
    print(f"Factor de Potencia:    {res['FP']:.4f} ({res['Tipo_FP']})")
    
    graficar_fasores(res, v_mag, v_ang, i_mag, i_ang)
