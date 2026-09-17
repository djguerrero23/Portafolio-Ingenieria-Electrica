# Laboratorio 1: Señal ↔ Fasor

::: {.card-module}
### 🔬 Laboratorio Interactivo — De la Señal al Fasor {.unnumbered}

Mueve el tiempo (o dale play) y observa **la misma información** expresada de dos formas: el punto que recorre la onda, y el vector que gira. El fasor no es una "foto" arbitraria — es la semilla que reconstruye toda la onda.

```{=html}
<div class="lab-flex-row">
  <div class="lab-col-3">
    <label class="form-label mb-1 small fw-bold">Amplitud <em>V</em><sub>m</sub>: <span id="lblVm">5.0</span> V</label>
    <input type="range" class="form-range" id="ctrlVm" min="1" max="10" step="0.5" value="5" oninput="onControlChange()">
  </div>
  <div class="lab-col-3">
    <label class="form-label mb-1 small fw-bold">Frecuencia <em>f</em>: <span id="lblF">1.0</span> Hz</label>
    <input type="range" class="form-range" id="ctrlF" min="0.5" max="10" step="0.5" value="1" oninput="onControlChange()">
  </div>
  <div class="lab-col-3">
    <label class="form-label mb-1 small fw-bold">Fase <em>&phi;</em>: <span id="lblPhi">30</span>&deg;</label>
    <input type="range" class="form-range" id="ctrlPhi" min="-180" max="180" step="5" value="30" oninput="onControlChange()">
  </div>
</div>

<div class="d-flex flex-wrap justify-content-between align-items-center gap-2 mb-3">
  <div class="btn-group" role="group">
    <button class="btn btn-sm btn-primary" id="btnPico" onclick="setModo('pico')">Valor Pico</button>
    <button class="btn btn-sm btn-outline-primary" id="btnRms" onclick="setModo('rms')">Valor RMS</button>
  </div>
  <button class="btn btn-sm btn-success" id="btnPlay" onclick="togglePlay()">
    <i class="bi bi-play-fill me-1"></i> Reproducir
  </button>
</div>

<div class="mb-2">
  <label class="form-label mb-1 small fw-bold">Tiempo — <em>&omega;t</em>: <span id="lblWt">0</span>&deg;</label>
  <input type="range" class="form-range" id="ctrlWt" min="0" max="720" step="1" value="0" oninput="onTimeChange()">
</div>

<div class="lab-flex-row">
  <div class="lab-col-5 text-center">
    <div class="p-2 bg-white rounded-3 border shadow-sm h-100 d-flex flex-column justify-content-center align-items-center">
      <div class="small fw-bold text-muted mb-1">Plano Fasorial (girando)</div>
      <canvas id="labPhasorCanvas" width="360" height="320" style="max-width:100%; height:auto;"></canvas>
    </div>
  </div>
  <div class="lab-col-7 text-center">
    <div class="p-2 bg-white rounded-3 border shadow-sm h-100 d-flex flex-column justify-content-center align-items-center">
      <div class="small fw-bold text-muted mb-1">Dominio del Tiempo</div>
      <canvas id="labWaveCanvas" width="560" height="320" style="max-width:100%; height:auto;"></canvas>
    </div>
  </div>
</div>

<div class="lab-flex-row">
  <div class="lab-col-3">
    <div class="p-2 rounded-3 bg-light border">
      <div class="small text-muted">v(t) instantáneo</div>
      <code id="outVt" class="fw-bold">0.00 V</code>
    </div>
  </div>
  <div class="lab-col-3">
    <div class="p-2 rounded-3 bg-light border">
      <div class="small text-muted">Ángulo instantáneo</div>
      <code id="outAngInst" class="fw-bold">30.0&deg;</code>
    </div>
  </div>
  <div class="lab-col-3">
    <div class="p-2 rounded-3 bg-light border">
      <div class="small text-muted"><em>&omega;</em> = 2&pi;f</div>
      <code id="outOmega" class="fw-bold">6.28 rad/s</code>
    </div>
  </div>
  <div class="lab-col-3">
    <div class="p-2 rounded-3 bg-light border">
      <div class="small text-muted">Periodo <em>T</em> = 1/f</div>
      <code id="outT" class="fw-bold">1.000 s</code>
    </div>
  </div>
</div>

<div class="mt-3 p-3 rounded-3" style="background:#f0f9ff; border-left:4px solid #0284c7;">
  <strong style="color:#0369a1;">Fasor actual:</strong>
  <code id="outFasor" class="fs-6 fw-bold" style="color:#0369a1;">5.00&ang;30.0&deg; V</code>
  <span class="small text-muted ms-2">— nota que no cambia mientras mueves el tiempo. El fasor es la "semilla" fija; lo que gira es su reconstrucción en el tiempo.</span>
</div>

<style>
#labPhasorCanvas, #labWaveCanvas { touch-action: none; }
.lab-flex-row { display: flex; flex-wrap: wrap; gap: 1rem; margin: 1rem 0; align-items: stretch; }
.lab-col-3 { flex: 1 1 220px; min-width: 200px; }
.lab-col-5 { flex: 1 1 320px; }
.lab-col-7 { flex: 1.6 1 420px; }
</style>

<script>
const labState = { Vm: 5, f: 1, phi: 30, modo: 'pico', wt: 0, playing: false, rafId: null };

function setModo(m) {
  labState.modo = m;
  document.getElementById('btnPico').classList.toggle('btn-primary', m === 'pico');
  document.getElementById('btnPico').classList.toggle('btn-outline-primary', m !== 'pico');
  document.getElementById('btnRms').classList.toggle('btn-primary', m === 'rms');
  document.getElementById('btnRms').classList.toggle('btn-outline-primary', m !== 'rms');
  actualizarLab();
}

function onControlChange() {
  labState.Vm = Number(document.getElementById('ctrlVm').value);
  labState.f = Number(document.getElementById('ctrlF').value);
  labState.phi = Number(document.getElementById('ctrlPhi').value);
  document.getElementById('lblVm').textContent = labState.Vm.toFixed(1);
  document.getElementById('lblF').textContent = labState.f.toFixed(1);
  document.getElementById('lblPhi').textContent = labState.phi.toFixed(0);
  actualizarLab();
}

function onTimeChange() {
  labState.wt = Number(document.getElementById('ctrlWt').value);
  actualizarLab();
}

function togglePlay() {
  labState.playing = !labState.playing;
  const btn = document.getElementById('btnPlay');
  btn.innerHTML = labState.playing
    ? '<i class="bi bi-pause-fill me-1"></i> Pausar'
    : '<i class="bi bi-play-fill me-1"></i> Reproducir';
  if (labState.playing) {
    animarLab();
  } else if (labState.rafId) {
    cancelAnimationFrame(labState.rafId);
  }
}

function animarLab() {
  if (!labState.playing) return;
  labState.wt = (labState.wt + 1.5) % 720;
  document.getElementById('ctrlWt').value = labState.wt;
  actualizarLab();
  labState.rafId = requestAnimationFrame(animarLab);
}

function dibujarGrillaYEjes(ctx, w, h, cx, cy) {
  ctx.clearRect(0, 0, w, h);
  ctx.strokeStyle = "#f1f5f9";
  ctx.lineWidth = 1;
  for (let px = cx % 22; px < w; px += 22) { ctx.beginPath(); ctx.moveTo(px, 0); ctx.lineTo(px, h); ctx.stroke(); }
  for (let py = cy % 22; py < h; py += 22) { ctx.beginPath(); ctx.moveTo(0, py); ctx.lineTo(w, py); ctx.stroke(); }
}

function dibujarFasorLab() {
  const canvas = document.getElementById("labPhasorCanvas");
  const ctx = canvas.getContext("2d");
  const w = canvas.width, h = canvas.height, cx = w / 2, cy = h / 2;
  dibujarGrillaYEjes(ctx, w, h, cx, cy);

  const magMostrada = labState.modo === 'pico' ? labState.Vm : labState.Vm / Math.SQRT2;
  const radioMax = Math.min(w, h) / 2 - 35;
  const scale = radioMax / 10; // escala fija para que subir Vm no desborde el canvas

  // círculo guía
  ctx.beginPath();
  ctx.arc(cx, cy, magMostrada * scale, 0, 2 * Math.PI);
  ctx.strokeStyle = "#e2e8f0";
  ctx.setLineDash([3, 3]);
  ctx.stroke();
  ctx.setLineDash([]);

  // ejes
  ctx.strokeStyle = "#94a3b8";
  ctx.lineWidth = 1.5;
  ctx.beginPath(); ctx.moveTo(15, cy); ctx.lineTo(w - 15, cy); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(cx, h - 15); ctx.lineTo(cx, 15); ctx.stroke();
  ctx.fillStyle = "#64748b";
  ctx.font = "bold 11px 'JetBrains Mono', monospace";
  ctx.fillText("Re", w - 30, cy - 8);
  ctx.fillText("+j Im", cx + 8, 20);

  // vector rotando: angulo = wt + phi (grados), pero el FASOR fijo se dibuja tenue en su phi original
  const anguloFijo = labState.phi * Math.PI / 180;
  const vxFijo = cx + magMostrada * scale * Math.cos(anguloFijo);
  const vyFijo = cy - magMostrada * scale * Math.sin(anguloFijo);
  ctx.strokeStyle = "#bae6fd";
  ctx.lineWidth = 2;
  ctx.setLineDash([5, 4]);
  ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(vxFijo, vyFijo); ctx.stroke();
  ctx.setLineDash([]);

  const anguloInst = (labState.wt + labState.phi) * Math.PI / 180;
  const vx = cx + magMostrada * scale * Math.cos(anguloInst);
  const vy = cy - magMostrada * scale * Math.sin(anguloInst);

  ctx.strokeStyle = "#0284c7";
  ctx.fillStyle = "#0284c7";
  ctx.lineWidth = 3.2;
  ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(vx, vy); ctx.stroke();
  const headLen = 11;
  ctx.beginPath();
  ctx.moveTo(vx, vy);
  ctx.lineTo(vx - headLen * Math.cos(anguloInst - Math.PI / 6 - 0), vy + headLen * Math.sin(anguloInst - Math.PI / 6));
  ctx.lineTo(vx - headLen * Math.cos(anguloInst + Math.PI / 6), vy + headLen * Math.sin(anguloInst + Math.PI / 6));
  ctx.closePath(); ctx.fill();

  ctx.fillStyle = "#0f172a";
  ctx.beginPath(); ctx.arc(cx, cy, 3.5, 0, 2 * Math.PI); ctx.fill();
}

function dibujarOndaLab() {
  const canvas = document.getElementById("labWaveCanvas");
  const ctx = canvas.getContext("2d");
  const w = canvas.width, h = canvas.height;
  ctx.clearRect(0, 0, w, h);

  const margenIzq = 42, margenDer = 15, margenTop = 15, margenBot = 30;
  const plotW = w - margenIzq - margenDer;
  const plotH = h - margenTop - margenBot;
  const midY = margenTop + plotH / 2;

  const escalaY = (plotH / 2 - 10) / 10; // hasta Vm=10 sin desbordar

  // grilla suave
  ctx.strokeStyle = "#f1f5f9";
  for (let gx = 0; gx <= 720; gx += 90) {
    const px = margenIzq + (gx / 720) * plotW;
    ctx.beginPath(); ctx.moveTo(px, margenTop); ctx.lineTo(px, margenTop + plotH); ctx.stroke();
  }

  // eje horizontal
  ctx.strokeStyle = "#94a3b8";
  ctx.lineWidth = 1.5;
  ctx.beginPath(); ctx.moveTo(margenIzq, midY); ctx.lineTo(w - margenDer, midY); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(margenIzq, margenTop); ctx.lineTo(margenIzq, margenTop + plotH); ctx.stroke();

  // marcas de eje X en grados (2 periodos)
  ctx.fillStyle = "#64748b";
  ctx.font = "10px 'JetBrains Mono', monospace";
  [0, 180, 360, 540, 720].forEach(gx => {
    const px = margenIzq + (gx / 720) * plotW;
    ctx.fillText(gx + "°", px - 10, margenTop + plotH + 18);
  });

  // curva v(theta) = Vm cos(theta + phi), theta en [0,720] grados
  ctx.strokeStyle = "#0284c7";
  ctx.lineWidth = 2.6;
  ctx.beginPath();
  for (let gx = 0; gx <= 720; gx += 2) {
    const rad = (gx + labState.phi) * Math.PI / 180;
    const v = labState.Vm * Math.cos(rad);
    const px = margenIzq + (gx / 720) * plotW;
    const py = midY - v * escalaY;
    if (gx === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
  }
  ctx.stroke();

  // linea RMS de referencia (si modo rms)
  if (labState.modo === 'rms') {
    const vrms = labState.Vm / Math.SQRT2;
    ctx.strokeStyle = "#f59e0b";
    ctx.setLineDash([4, 4]);
    ctx.lineWidth = 1.3;
    ctx.beginPath(); ctx.moveTo(margenIzq, midY - vrms * escalaY); ctx.lineTo(w - margenDer, midY - vrms * escalaY); ctx.stroke();
    ctx.setLineDash([]);
  }

  // punto y guias en el tiempo actual
  const radInst = (labState.wt + labState.phi) * Math.PI / 180;
  const vInst = labState.Vm * Math.cos(radInst);
  const pxInst = margenIzq + (labState.wt / 720) * plotW;
  const pyInst = midY - vInst * escalaY;

  ctx.strokeStyle = "#dc2626";
  ctx.setLineDash([3, 3]);
  ctx.lineWidth = 1.2;
  ctx.beginPath(); ctx.moveTo(pxInst, margenTop); ctx.lineTo(pxInst, margenTop + plotH); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(margenIzq, pyInst); ctx.lineTo(pxInst, pyInst); ctx.stroke();
  ctx.setLineDash([]);

  ctx.fillStyle = "#dc2626";
  ctx.beginPath(); ctx.arc(pxInst, pyInst, 5, 0, 2 * Math.PI); ctx.fill();
}

function actualizarLab() {
  const omega = 2 * Math.PI * labState.f;
  const T = 1 / labState.f;
  const magMostrada = labState.modo === 'pico' ? labState.Vm : labState.Vm / Math.SQRT2;
  const anguloInst = ((labState.wt + labState.phi) % 360 + 360) % 360;
  const anguloInstSigned = anguloInst > 180 ? anguloInst - 360 : anguloInst;
  const vInst = labState.Vm * Math.cos((labState.wt + labState.phi) * Math.PI / 180);
  const tReal = (labState.wt * Math.PI / 180) / omega;

  document.getElementById('lblWt').textContent = labState.wt.toFixed(0);
  document.getElementById('outVt').textContent = vInst.toFixed(2) + " V";
  document.getElementById('outAngInst').textContent = anguloInstSigned.toFixed(1) + "°";
  document.getElementById('outOmega').textContent = omega.toFixed(2) + " rad/s";
  document.getElementById('outT').textContent = T.toFixed(3) + " s  (t=" + tReal.toFixed(3) + " s)";
  document.getElementById('outFasor').innerHTML =
    `${magMostrada.toFixed(2)}&ang;${labState.phi.toFixed(1)}° ${labState.modo === 'rms' ? '(RMS)' : '(pico)'} V`;

  dibujarFasorLab();
  dibujarOndaLab();
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", actualizarLab);
} else {
  setTimeout(actualizarLab, 50);
}
</script>
```
:::
