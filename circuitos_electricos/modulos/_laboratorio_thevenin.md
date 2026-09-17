---
title: "Laboratorio Interactivo: Teorema de Thévenin en CA"
format: html
---

::: {.callout-note}
⚡ **Construye y Calcula**
Selecciona los valores del circuito. El cálculo se realiza en tiempo real en tu navegador, replicando la lógica de análisis fasorial.
:::

```{=html}

<div class="card p-4 shadow-sm border-0 bg-light">
  <div class="row">
    <!-- Panel de Entrada -->
    <div class="col-md-5">
      <h6 class="text-primary fw-bold"><i class="bi bi-sliders"></i> Parámetros del Circuito</h6>
      
      <div class="mb-3">
        <label class="form-label small fw-bold">Fuente de Voltaje $\mathbf{E}$ (V)</label>
        <div class="input-group input-group-sm">
          <input type="number" id="th_E_mag" class="form-control" value="9" step="0.1">
          <span class="input-group-text">∠</span>
          <input type="number" id="th_E_ang" class="form-control" value="0" step="1">
          <span class="input-group-text">°</span>
        </div>
      </div>

      <div class="mb-3">
        <label class="form-label small fw-bold">Impedancia $\mathbf{Z_1}$ ($\Omega$)</label>
        <div class="input-group input-group-sm">
          <input type="number" id="th_Z1_real" class="form-control" value="6" step="0.1">
          <span class="input-group-text">+ j</span>
          <input type="number" id="th_Z1_imag" class="form-control" value="-8" step="0.1">
        </div>
      </div>

      <div class="mb-3">
        <label class="form-label small fw-bold">Impedancia $\mathbf{Z_2}$ ($\Omega$)</label>
        <div class="input-group input-group-sm">
          <input type="number" id="th_Z2_real" class="form-control" value="0" step="0.1">
          <span class="input-group-text">+ j</span>
          <input type="number" id="th_Z2_imag" class="form-control" value="8" step="0.1">
        </div>
      </div>
      
      <button class="btn btn-primary w-100 btn-sm" onclick="calcularThevenin()">
        <i class="bi bi-calculator"></i> Calcular Equivalente Thévenin
      </button>
    </div>

    <!-- Panel de Resultados -->
    <div class="col-md-7">
      <h6 class="text-success fw-bold"><i class="bi bi-check-circle"></i> Resultados Fasoriales</h6>
      <div id="resultado_thevenin" class="p-3 bg-white rounded border">
        <p class="text-muted small text-center mt-4">Presiona "Calcular" para ver los resultados fasoriales.</p>
      </div>
      
      <!-- Aquí podrías agregar un SVG dinámico que cambie de color según los valores -->
      <div class="mt-3 text-center">
        <small class="text-muted">Representación visual del circuito (Esquemático estático con valores dinámicos)</small>
        <div class="p-2 border rounded bg-white mt-1 font-monospace small" id="esquema_texto">
          E --- Z1 ---+--- Z2 ---|<br>
                    |<br>
                   Vth (Salida)
        </div>
      </div>
    </div>
  </div>
</div>

<script>
// Pequeña librería de Números Complejos en JS (reemplaza a numpy)
const C = {
  add: (a, b) => ({ r: a.r + b.r, i: a.i + b.i }),
  sub: (a, b) => ({ r: a.r - b.r, i: a.i - b.i }),
  mul: (a, b) => ({ r: a.r * b.r - a.i * b.i, i: a.r * b.i + a.i * b.r }),
  div: (a, b) => {
    const den = b.r * b.r + b.i * b.i;
    return { r: (a.r * b.r + a.i * b.i) / den, i: (a.i * b.r - a.r * b.i) / den };
  },
  polar: (c) => {
    const mag = Math.hypot(c.r, c.i);
    const ang = Math.atan2(c.i, c.r) * (180 / Math.PI);
    return { mag, ang };
  },
  fromPolar: (mag, angDeg) => {
    const rad = angDeg * (Math.PI / 180);
    return { r: mag * Math.cos(rad), i: mag * Math.sin(rad) };
  },
  fmt: (c, unit = "") => {
    const p = C.polar(c);
    const signo = c.i >= 0 ? "+" : "−";
    return `${p.mag.toFixed(2)} ∠ ${p.ang.toFixed(1)}° ${unit} <br><span class="text-muted small">(${c.r.toFixed(2)} ${signo} j${Math.abs(c.i).toFixed(2)} ${unit})</span>`;
  }
};

function calcularThevenin() {
  // 1. Obtener valores
  const E_mag = parseFloat(document.getElementById('th_E_mag').value) || 0;
  const E_ang = parseFloat(document.getElementById('th_E_ang').value) || 0;
  const E = C.fromPolar(E_mag, E_ang);

  const Z1 = { r: parseFloat(document.getElementById('th_Z1_real').value) || 0, i: parseFloat(document.getElementById('th_Z1_imag').value) || 0 };
  const Z2 = { r: parseFloat(document.getElementById('th_Z2_real').value) || 0, i: parseFloat(document.getElementById('th_Z2_imag').value) || 0 };

  // 2. Cálculos (Lógica idéntica a tu verificacion_calculos.py)
  const Z1_plus_Z2 = C.add(Z1, Z2);
  const Zth = C.div(C.mul(Z1, Z2), Z1_plus_Z2);
  const Vth = C.mul(E, C.div(Z2, Z1_plus_Z2));
  const IN = C.div(Vth, Zth);

  // 3. Mostrar resultados
  const html = `
    <div class="row">
      <div class="col-6">
        <div class="p-2 mb-2 bg-light rounded border-start border-4 border-primary">
          <strong class="small text-primary">Voltaje Thévenin ($\mathbf{V_{th}}$)</strong><br>
          ${C.fmt(Vth, "V")}
        </div>
        <div class="p-2 bg-light rounded border-start border-4 border-success">
          <strong class="small text-success">Impedancia Thévenin ($\mathbf{Z_{th}}$)</strong><br>
          ${C.fmt(Zth, "Ω")}
        </div>
      </div>
      <div class="col-6">
        <div class="p-2 mb-2 bg-light rounded border-start border-4 border-warning">
          <strong class="small text-warning">Corriente Norton ($\mathbf{I_N}$)</strong><br>
          ${C.fmt(IN, "A")}
        </div>
        <div class="p-2 bg-light rounded border-start border-4 border-info">
          <strong class="small text-info">Comportamiento de $\mathbf{Z_{th}}$</strong><br>
          <span class="small">${Zth.i > 0.01 ? "Inductivo (Reactancia +)" : Zth.i < -0.01 ? "Capacitivo (Reactancia -)" : "Resistivo Puro"}</span>
        </div>
      </div>
    </div>
  `;
  document.getElementById('resultado_thevenin').innerHTML = html;
}

// Calcular al cargar
document.addEventListener("DOMContentLoaded", calcularThevenin);
</script>

```