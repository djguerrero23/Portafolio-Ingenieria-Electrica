import math
import sys

# Forzar salida en UTF-8 para que la consola de Windows renderice superíndices (⁻¹) y emojis (✅)
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

def angulo_polar_grados(x, y):
    """Calcula el ángulo de fase real con resolución completa de cuadrantes."""
    return math.degrees(math.atan2(y, x))

def arctan_sin_ajuste_grados(x, y):
    """Fórmula simple de calculadora (tan⁻¹(y/x)) sin corrección de cuadrante."""
    try:
        return math.degrees(math.atan(y / x))
    except ZeroDivisionError:
        return None

# Batería de pruebas: (Nombre del caso, x, y, Ángulo esperado, Observación didáctica)
casos_de_prueba = [
    ("Q1 (+, +)",      3,  4,   53.13, "Coinciden"),
    ("Q2 (-, +)",     -5,  5,  135.00, "Ejercicio 2: Desfase 180°"),
    ("Q3 (-, -)",     -4, -4, -135.00, "Signos se cancelan (+ vs -)"),
    ("Q4 (+, -)",      3, -4,  -53.13, "Coinciden"),
    ("Eje +x (j=0)",   5,  0,    0.00, "Resistivo puro / Referencia"),
    ("Eje +j (x=0)",   0,  5,   90.00, "División entre cero evitada"),
    ("Eje -x (y=0)",  -5,  0,  180.00, "Contrafase a 180°")
]

print("=" * 80)
print(f"{'CASO':<14} | {'ENTRADA z':<10} | {'tan⁻¹(y/x)':<12} | {'ATAN2 REAL':<11} | {'ESTADO tan⁻¹'}")
print("=" * 80)

for caso, x, y, ang_esperado, observacion in casos_de_prueba:
    texto_z = f"{x:+d}{y:+d}j" if y != 0 else f"{x:+d}+0j"
    ang_atan2_real = angulo_polar_grados(x, y)
    ang_sin_ajuste = arctan_sin_ajuste_grados(x, y)
    
    # Aserción de prueba unitaria (valida que atan2 entregue el ángulo real esperado)
    assert round(ang_atan2_real, 2) == round(ang_esperado, 2)
    
    texto_sin_ajuste = f"{ang_sin_ajuste:+6.1f}°" if ang_sin_ajuste is not None else "ERROR (y/0)"

    # Evaluamos si la fórmula simple arctan(y/x) acierta o falla:
    if ang_sin_ajuste is None:
        estado_arctan = "ERROR 💥"
    elif round(ang_sin_ajuste, 2) == round(ang_esperado, 2):
        estado_arctan = "PASA ✅"
    else:
        estado_arctan = "NO PASA ❌"

    print(f"{caso:<14} | {texto_z:<10} | {texto_sin_ajuste:<12} | {ang_atan2_real:+7.2f}°   | {estado_arctan} ({observacion})")

print("=" * 80)
print("🎯 Conclusión: atan2(y, x) supera el 100% de las pruebas de cuadrante.")