# Herramienta interactiva: Diagrama Fasorial del Circuito RLC

::: {.card-module}
### 📐 Diagrama Fasorial Interactivo — Ejemplo Integrado RLC {.unnumbered}

Activa o desactiva cada fasor para construir el diagrama paso a paso. Con **I**, **V_R**, **V_L** y **V_C** activos, verás además la cadena punta-cola (líneas punteadas) que demuestra geométricamente por qué $\mathbf V_R+\mathbf V_L+\mathbf V_C=\mathbf V$.

```{=html}
<div class="d-flex flex-wrap gap-2 justify-content-center mb-3" id="fasorToggles">
  <button class="btn btn-sm fasor-toggle active" data-key="I" style="--c:#475569;" onclick="toggleFasor('I')">
    <i class="bi bi-check-circle-fill me-1"></i> I = 3.80&ang;11.57&deg; A
  </button>
  <button class="btn btn-sm fasor-toggle active" data-key="VR" style="--c:#0284c7;" onclick="toggleFasor('VR')">
    <i class="bi bi-check-circle-fill me-1"></i> V<sub>R</sub> = 114.0&ang;11.57&deg; V
  </button>
  <button class="btn btn-sm fasor-toggle active" data-key="VL" style="--c:#10b981;" onclick="toggleFasor('VL')">
    <i class="bi bi-check-circle-fill me-1"></i> V<sub>L</sub> = 190.0&ang;101.57&deg; V
  </button>
  <button class="btn btn-sm fasor-toggle active" data-key="VC" style="--c:#f59e0b;" onclick="toggleFasor('VC')">
    <i class="bi bi-check-circle-fill me-1"></i> V<sub>C</sub> = 152.0&ang;-78.43&deg; V
  </button>
  <button class="btn btn-sm fasor-toggle active" data-key="VT" style="--c:#8b5cf6;" onclick="toggleFasor('VT')">
    <i class="bi bi-check-circle-fill me-1"></i> V<sub>T</sub> = 120.0&ang;30.00&deg; V
  </button>
</div>

<div class="d-flex justify-content-center mb-3">
  <div class="form-check form-switch">
    <input class="form-check-input" type="checkbox" id="chainToggle" checked onchange="dibujarTodo()">
    <label class="form-check-label small" for="chainToggle">Mostrar cadena punta-cola (KVL)</label>
  </div>
</div>

<style>
.fasor-toggle {
  border: 1.5px solid var(--c);
  color: var(--c);
  background: #fff;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.8rem;
  opacity: 0.45;
  transition: all 0.15s ease;
}
.fasor-toggle.active {
  background: var(--c);
  color: #fff;
  opacity: 1;
}
</style>

<div class="text-center">
  <div class="p-3 bg-white rounded-3 border shadow-sm d-inline-block">
    <canvas id="fasorRLCCanvas" width="560" height="420" style="max-width: 100%; height: auto;"></canvas>
    <div class="small text-muted mt-2" style="max-width: 520px;">
      Nota: <strong>I</strong> se grafica con longitud independiente de V<sub>R</sub>, V<sub>L</sub>, V<sub>C</sub>, V<sub>T</sub>
      (unidades distintas — A vs. V). Lo relevante de I en este diagrama es su <strong>ángulo</strong>,
      no su longitud relativa a las tensiones.
    </div>
  </div>
</div>

<script>
const datosF = {
  I:  { mag: 3.80,  ang: 11.57,  color: "#475569", esCorriente: true  },
  VR: { mag: 114.0, ang: 11.57,  color: "#0284c7", esCorriente: false },
  VL: { mag: 190.0, ang: 101.57, color: "#10b981", esCorriente: false },
  VC: { mag: 152.0, ang: -78.43, color: "#f59e0b", esCorriente: false },
  VT: { mag: 120.0, ang: 30.00,  color: "#8b5cf6", esCorriente: false }
};
const activos = { I: true, VR: true, VL: true, VC: true, VT: true };

function toggleFasor(key) {
  activos[key] = !activos[key];
  document.querySelector(`.fasor-toggle[data-key="${key}"]`).classList.toggle('active', activos[key]);
  dibujarTodo();
}

function aXY(mag, angDeg) {
  const r = angDeg * Math.PI / 180;
  return { x: mag * Math.cos(r), y: mag * Math.sin(r) };
}

function dibujarFlecha(ctx, cx, cy, vx, vy, color, grosor, dash) {
  ctx.save();
  if (dash) ctx.setLineDash(dash);
  ctx.strokeStyle = color;
  ctx.fillStyle = color;
  ctx.lineWidth = grosor;
  ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(vx, vy); ctx.stroke();
  ctx.restore();
  if (!dash) {
    const headLen = 11;
    const ang = Math.atan2(vy - cy, vx - cx);
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.moveTo(vx, vy);
    ctx.lineTo(vx - headLen * Math.cos(ang - Math.PI / 6), vy - headLen * Math.sin(ang - Math.PI / 6));
    ctx.lineTo(vx - headLen * Math.cos(ang + Math.PI / 6), vy - headLen * Math.sin(ang + Math.PI / 6));
    ctx.closePath();
    ctx.fill();
  }
}

function dibujarTodo() {
  const canvas = document.getElementById("fasorRLCCanvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");
  const w = canvas.width, h = canvas.height, cx = w / 2, cy = h / 2;
  ctx.clearRect(0, 0, w, h);

  // Grilla y ejes
  ctx.strokeStyle = "#f1f5f9";
  ctx.lineWidth = 1;
  for (let px = cx % 24; px < w; px += 24) { ctx.beginPath(); ctx.moveTo(px, 0); ctx.lineTo(px, h); ctx.stroke(); }
  for (let py = cy % 24; py < h; py += 24) { ctx.beginPath(); ctx.moveTo(0, py); ctx.lineTo(w, py); ctx.stroke(); }
  ctx.strokeStyle = "#94a3b8";
  ctx.lineWidth = 1.5;
  ctx.beginPath(); ctx.moveTo(15, cy); ctx.lineTo(w - 15, cy); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(cx, h - 15); ctx.lineTo(cx, 15); ctx.stroke();
  ctx.fillStyle = "#64748b";
  ctx.font = "bold 11px 'JetBrains Mono', monospace";
  ctx.fillText("Re", w - 30, cy - 8);
  ctx.fillText("+j Im", cx + 8, 20);

  // Escala para las tensiones (V)
  const maxV = Math.max(
    ...['VR','VL','VC','VT'].filter(k => activos[k]).map(k => datosF[k].mag), 1
  );
  const scaleV = (Math.min(w, h) / 2 - 55) / maxV;

  // Escala independiente para la corriente (solo referencia angular, longitud fija visualmente)
  const scaleI = (maxV * 0.6 * scaleV) / datosF.I.mag;

  // Cadena punta-cola: VR -> VR+VL -> VR+VL+VC
  if (document.getElementById("chainToggle").checked &&
      activos.VR && activos.VL && activos.VC) {
    const pR = aXY(datosF.VR.mag, datosF.VR.ang);
    const pL = aXY(datosF.VL.mag, datosF.VL.ang);
    const pC = aXY(datosF.VC.mag, datosF.VC.ang);
    const p0 = { x: cx, y: cy };
    const p1 = { x: cx + pR.x * scaleV, y: cy - pR.y * scaleV };
    const p2 = { x: p1.x + pL.x * scaleV, y: p1.y - pL.y * scaleV };
    const p3 = { x: p2.x + pC.x * scaleV, y: p2.y - pC.y * scaleV };

    ctx.save();
    ctx.setLineDash([5, 4]);
    ctx.strokeStyle = "#94a3b8";
    ctx.lineWidth = 1.6;
    ctx.beginPath();
    ctx.moveTo(p0.x, p0.y); ctx.lineTo(p1.x, p1.y); ctx.lineTo(p2.x, p2.y); ctx.lineTo(p3.x, p3.y);
    ctx.stroke();
    ctx.restore();

    [p1, p2, p3].forEach(p => {
      ctx.fillStyle = "#94a3b8";
      ctx.beginPath(); ctx.arc(p.x, p.y, 3, 0, 2 * Math.PI); ctx.fill();
    });
  }

  // Fasores desde el origen
  Object.keys(datosF).forEach(key => {
    if (!activos[key]) return;
    const d = datosF[key];
    const p = aXY(d.mag, d.ang);
    const scale = d.esCorriente ? scaleI : scaleV;
    const vx = cx + p.x * scale;
    const vy = cy - p.y * scale;
    dibujarFlecha(ctx, cx, cy, vx, vy, d.color, d.esCorriente ? 2.5 : 3.2, d.esCorriente ? [6, 3] : null);
  });

  ctx.fillStyle = "#0f172a";
  ctx.beginPath(); ctx.arc(cx, cy, 3.5, 0, 2 * Math.PI); ctx.fill();
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", dibujarTodo);
} else {
  setTimeout(dibujarTodo, 50);
}
</script>
```
:::
