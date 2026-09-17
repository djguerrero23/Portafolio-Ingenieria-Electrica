# Laboratorio 1: Señal ↔ Fasor

::: {.card-module}
### 🔬 Laboratorio Interactivo — De la Señal al Fasor {.unnumbered}

Mueve el tiempo (o dale reproducir) y observa **la misma información física** expresada de dos formas simultáneas: el vector rotatorio en el plano de Gauss y el trazo instantáneo en el dominio del tiempo. El fasor no es una simple foto arbitraria: es la "semilla" compleja que reconstruye toda la onda sinusoidal.

```{=html}
<!-- 1. Tres Controles Principales (Lado a Lado Forzado) -->
<div class="lab-controls-row mb-3">
  
  <!-- Amplitud Vm -->
  <div class="lab-control-card p-3 bg-white rounded-3 border shadow-sm" style="border-top: 3px solid #0284c7 !important;">
    <div class="d-flex justify-content-between align-items-center mb-1">
      <label for="numVm" class="form-label mb-0 small fw-bold text-dark">
        <i class="bi bi-arrows-vertical text-primary me-1"></i> Amplitud <i>V</i><sub>m</sub> (V)
      </label>
      <span class="badge bg-light text-primary border" id="tagModoVm" style="font-size:0.7rem;">Pico</span>
    </div>
    
    <div class="input-group input-group-sm mb-2">
      <input type="number" class="form-control fw-bold" id="numVm" value="120" min="0.1" max="10000" step="1" oninput="onManualInput('Vm')">
      <span class="input-group-text bg-light">V</span>
    </div>
    
    <input type="range" class="form-range mb-1" id="ctrlVm" min="1" max="400" step="1" value="120" oninput="onSliderInput('Vm')">
    
    <div class="d-flex flex-wrap gap-1">
      <button type="button" class="btn btn-xs btn-outline-secondary py-0 px-1" style="font-size:0.68rem;" onclick="setPresetVm(12)">12V</button>
      <button type="button" class="btn btn-xs btn-outline-secondary py-0 px-1" style="font-size:0.68rem;" onclick="setPresetVm(120)">120V</button>
      <button type="button" class="btn btn-xs btn-outline-secondary py-0 px-1" style="font-size:0.68rem;" onclick="setPresetVm(170)">170V</button>
      <button type="button" class="btn btn-xs btn-outline-secondary py-0 px-1" style="font-size:0.68rem;" onclick="setPresetVm(220)">220V</button>
      <button type="button" class="btn btn-xs btn-outline-secondary py-0 px-1" style="font-size:0.68rem;" onclick="setPresetVm(311)">311V</button>
    </div>
  </div>

  <!-- Frecuencia f -->
  <div class="lab-control-card p-3 bg-white rounded-3 border shadow-sm" style="border-top: 3px solid #10b981 !important;">
    <div class="d-flex justify-content-between align-items-center mb-1">
      <label for="numF" class="form-label mb-0 small fw-bold text-dark">
        <i class="bi bi-speedometer2 text-success me-1"></i> Frecuencia <i>f</i> (Hz)
      </label>
      <span class="badge bg-light text-success border" id="tagOmega" style="font-size:0.7rem;">377 rad/s</span>
    </div>
    
    <div class="input-group input-group-sm mb-2">
      <input type="number" class="form-control fw-bold" id="numF" value="60" min="0.1" max="2000" step="1" oninput="onManualInput('f')">
      <span class="input-group-text bg-light">Hz</span>
    </div>
    
    <input type="range" class="form-range mb-1" id="ctrlF" min="1" max="120" step="1" value="60" oninput="onSliderInput('f')">
    
    <div class="d-flex flex-wrap gap-1">
      <button type="button" class="btn btn-xs btn-outline-secondary py-0 px-1" style="font-size:0.68rem;" onclick="setPresetF(1)">1 Hz</button>
      <button type="button" class="btn btn-xs btn-outline-secondary py-0 px-1" style="font-size:0.68rem;" onclick="setPresetF(50)">50 Hz</button>
      <button type="button" class="btn btn-xs btn-outline-secondary py-0 px-1" style="font-size:0.68rem;" onclick="setPresetF(60)">60 Hz</button>
      <button type="button" class="btn btn-xs btn-outline-secondary py-0 px-1" style="font-size:0.68rem;" onclick="setPresetF(400)">400 Hz</button>
    </div>
  </div>

  <!-- Fase inicial phi -->
  <div class="lab-control-card p-3 bg-white rounded-3 border shadow-sm" style="border-top: 3px solid #f59e0b !important;">
    <div class="d-flex justify-content-between align-items-center mb-1">
      <label for="numPhi" class="form-label mb-0 small fw-bold text-dark">
        <i class="bi bi-compass text-warning me-1"></i> Fase Inicial <i>&phi;</i> (&deg;)
      </label>
      <span class="badge bg-light text-warning border" id="tagCuad" style="font-size:0.7rem;">Cuad. I</span>
    </div>
    
    <div class="input-group input-group-sm mb-2">
      <input type="number" class="form-control fw-bold" id="numPhi" value="0" min="-180" max="180" step="1" oninput="onManualInput('phi')">
      <span class="input-group-text bg-light">&deg;</span>
    </div>
    
    <input type="range" class="form-range mb-1" id="ctrlPhi" min="-180" max="180" step="1" value="0" oninput="onSliderInput('phi')">
    
    <div class="d-flex flex-wrap gap-1">
      <button type="button" class="btn btn-xs btn-outline-secondary py-0 px-1" style="font-size:0.68rem;" onclick="setPresetPhi(-90)">-90&deg;</button>
      <button type="button" class="btn btn-xs btn-outline-secondary py-0 px-1" style="font-size:0.68rem;" onclick="setPresetPhi(0)">0&deg;</button>
      <button type="button" class="btn btn-xs btn-outline-secondary py-0 px-1" style="font-size:0.68rem;" onclick="setPresetPhi(30)">+30&deg;</button>
      <button type="button" class="btn btn-xs btn-outline-secondary py-0 px-1" style="font-size:0.68rem;" onclick="setPresetPhi(90)">+90&deg;</button>
      <button type="button" class="btn btn-xs btn-outline-secondary py-0 px-1" style="font-size:0.68rem;" onclick="setPresetPhi(180)">180&deg;</button>
    </div>
  </div>

</div>

<!-- 2. Barra de Reproducción y Modo Pico / RMS -->
<div class="p-2 bg-light rounded-3 border d-flex flex-wrap justify-content-between align-items-center gap-2 mb-3">
  <div class="d-flex align-items-center gap-2">
    <div class="btn-group btn-group-sm" role="group">
      <button class="btn btn-primary fw-bold" id="btnPico" onclick="setModo('pico')">Valor Pico (<i>V</i><sub>m</sub>)</button>
      <button class="btn btn-outline-primary fw-bold" id="btnRms" onclick="setModo('rms')">Valor RMS (<i>V</i><sub>rms</sub>)</button>
    </div>
    <span class="small text-muted ms-2 d-none d-md-inline">Forma canónica: <i>v</i>(<i>t</i>) = <i>V</i><sub>m</sub> cos(&omega;<i>t</i> + &phi;)</span>
  </div>

  <div class="d-flex align-items-center gap-2">
    <button class="btn btn-sm btn-success fw-bold px-3" id="btnPlay" onclick="togglePlay()">
      <i class="bi bi-play-fill me-1"></i> Reproducir
    </button>
    <button class="btn btn-sm btn-outline-secondary" onclick="resetTiempo()" title="Reiniciar a t=0">
      <i class="bi bi-arrow-counterclockwise"></i>
    </button>
  </div>
</div>

<!-- 3. Control del Tiempo Angular wt -->
<div class="p-3 bg-white rounded-3 border shadow-sm mb-3">
  <div class="d-flex justify-content-between align-items-center mb-1">
    <label for="ctrlWt" class="form-label mb-0 small fw-bold">
      <i class="bi bi-clock-history text-danger me-1"></i> Evolución Temporal angular <i>&omega;t</i>: <span id="lblWt" class="text-danger fw-bold fs-6">0</span>&deg;
    </label>
    <span class="small text-muted" id="lblTiempoSegundos">t = 0.000 ms</span>
  </div>
  <input type="range" class="form-range" id="ctrlWt" min="0" max="720" step="1" value="0" oninput="onTimeChange()">
  <div class="d-flex justify-content-between text-muted" style="font-size: 0.72rem; font-family: monospace;">
    <span>0&deg; (t = 0)</span>
    <span>180&deg; (T/2)</span>
    <span>360&deg; (1 Ciclo)</span>
    <span>540&deg; (1.5 T)</span>
    <span>720&deg; (2 Ciclos)</span>
  </div>
</div>

<!-- 4. Lienzos Gráficos Lado a Lado (Flexbox Estricto en 1 Fila) -->
<div class="lab-canvas-container mb-3">
  
  <!-- Columna Izquierda: Plano de Gauss -->
  <div class="lab-canvas-box-left p-2 bg-white rounded-3 border shadow-sm text-center d-flex flex-column justify-content-between">
    <div class="d-flex justify-content-between align-items-center w-100 mb-1 px-1">
      <span class="badge bg-secondary" style="font-size: 0.72rem;"><i class="bi bi-grid-3x3 me-1"></i> Plano de Gauss</span>
      <span class="badge bg-primary" style="font-size: 0.72rem;" id="badgeFasorDinamico">Fasor rotando</span>
    </div>
    <div class="d-flex justify-content-center align-items-center flex-grow-1 py-1">
      <canvas id="labPhasorCanvas" width="340" height="280"></canvas>
    </div>
    <div class="small text-muted mt-1" style="font-size:0.72rem;">
      <span style="display:inline-block; width:10px; height:3px; background:#bae6fd; vertical-align:middle;"></span> Fasor en <i>t</i> = 0 &nbsp;|&nbsp;
      <span style="display:inline-block; width:10px; height:3px; background:#0284c7; vertical-align:middle;"></span> Vector rotatorio <b>V</b>(<i>t</i>)
    </div>
  </div>

  <!-- Columna Derecha: Dominio del Tiempo -->
  <div class="lab-canvas-box-right p-2 bg-white rounded-3 border shadow-sm text-center d-flex flex-column justify-content-between">
    <div class="d-flex justify-content-between align-items-center w-100 mb-1 px-1">
      <span class="badge bg-secondary" style="font-size: 0.72rem;"><i class="bi bi-graph-up me-1"></i> Dominio del Tiempo</span>
      <span class="badge bg-danger" style="font-size: 0.72rem;" id="badgeValorInst">v(t) instantáneo</span>
    </div>
    <div class="d-flex justify-content-center align-items-center flex-grow-1 py-1">
      <canvas id="labWaveCanvas" width="500" height="280"></canvas>
    </div>
    <div class="small text-muted mt-1" style="font-size:0.72rem;">
      <span style="color:#0284c7; font-weight:bold;">—</span> <i>v</i>(<i>t</i>) = <i>V</i><sub>m</sub> cos(&omega;<i>t</i> + &phi;) &nbsp;|&nbsp;
      <span style="color:#f59e0b; font-weight:bold;">- -</span> Nivel RMS &nbsp;|&nbsp;
      <span style="color:#dc2626; font-weight:bold;">●</span> Punto en <i>t</i>
    </div>
  </div>

</div>

<!-- 5. Métricas Numéricas en Tiempo Real -->
<div class="lab-metrics-row mb-3">
  <div class="lab-metric-card p-2 rounded-3 bg-light border text-center">
    <div class="text-muted" style="font-size:0.74rem;">Valor Instantáneo <i>v</i>(<i>t</i>)</div>
    <code id="outVt" class="fs-6 fw-bold text-danger">0.00 V</code>
  </div>
  <div class="lab-metric-card p-2 rounded-3 bg-light border text-center">
    <div class="text-muted" style="font-size:0.74rem;">Ángulo Total (&omega;<i>t</i> + &phi;)</div>
    <code id="outAngInst" class="fs-6 fw-bold text-primary">30.0&deg;</code>
  </div>
  <div class="lab-metric-card p-2 rounded-3 bg-light border text-center">
    <div class="text-muted" style="font-size:0.74rem;">Frecuencia Angular &omega;</div>
    <code id="outOmega" class="fs-6 fw-bold text-success">376.99 rad/s</code>
  </div>
  <div class="lab-metric-card p-2 rounded-3 bg-light border text-center">
    <div class="text-muted" style="font-size:0.74rem;">Periodo <i>T</i> = 1/<i>f</i></div>
    <code id="outT" class="fs-6 fw-bold text-secondary">16.67 ms</code>
  </div>
</div>

<!-- 6. Tarjeta de Expresión Fasorial Resultante -->
<div class="p-3 rounded-3" style="background:#f0f9ff; border-left:4px solid #0284c7;">
  <div class="d-flex flex-wrap justify-content-between align-items-center gap-2">
    <div>
      <strong style="color:#0369a1;"><i class="bi bi-lightning-charge-fill me-1"></i> Expresión Fasorial Resultante:</strong>
      <code id="outFasor" class="fs-5 fw-bold ms-2" style="color:#0369a1;">120.00 &ang; 30.0&deg; V</code>
    </div>
    <div class="small text-muted">
      <i class="bi bi-info-circle me-1"></i> El fasor es invariante en el tiempo; lo que rota es <i>e</i><sup><i>j&omega;t</i></sup>.
    </div>
  </div>
</div>

<style>
/* Forzado estricto de una sola fila lado a lado */
.lab-controls-row {
  display: flex !important;
  flex-direction: row !important;
  flex-wrap: nowrap !important;
  gap: 12px;
  width: 100%;
}
.lab-control-card {
  flex: 1 1 0 !important;
  min-width: 0 !important;
}

.lab-canvas-container {
  display: flex !important;
  flex-direction: row !important;
  flex-wrap: nowrap !important;
  gap: 12px;
  align-items: stretch;
  width: 100%;
}
.lab-canvas-box-left {
  flex: 1 1 40% !important;
  min-width: 0 !important;
}
.lab-canvas-box-right {
  flex: 1.45 1 60% !important;
  min-width: 0 !important;
}

#labPhasorCanvas, #labWaveCanvas {
  touch-action: none;
  width: 100% !important;
  max-width: 100% !important;
  height: auto !important;
  display: block;
}

.lab-metrics-row {
  display: flex !important;
  flex-direction: row !important;
  flex-wrap: nowrap !important;
  gap: 10px;
  width: 100%;
}
.lab-metric-card {
  flex: 1 1 0 !important;
  min-width: 0 !important;
}

@media (max-width: 580px) {
  .lab-controls-row, .lab-canvas-container, .lab-metrics-row {
    flex-wrap: wrap !important;
  }
  .lab-control-card, .lab-canvas-box-left, .lab-canvas-box-right, .lab-metric-card {
    flex: 1 1 100% !important;
  }
}
</style>

<script>
const labState = {
  Vm: 120,
  f: 60,
  phi: 0,
  modo: 'pico',
  wt: 0,
  playing: false,
  rafId: null
};

function setModo(m) {
  labState.modo = m;
  document.getElementById('btnPico').classList.toggle('btn-primary', m === 'pico');
  document.getElementById('btnPico').classList.toggle('btn-outline-primary', m !== 'pico');
  document.getElementById('btnRms').classList.toggle('btn-primary', m === 'rms');
  document.getElementById('btnRms').classList.toggle('btn-outline-primary', m !== 'rms');
  
  const tagVm = document.getElementById('tagModoVm');
  if (tagVm) tagVm.textContent = m === 'pico' ? 'Pico' : 'RMS';
  
  actualizarLab();
}

function onManualInput(param) {
  if (param === 'Vm') {
    const val = Math.max(0.1, Number(document.getElementById('numVm').value) || 1);
    labState.Vm = val;
    document.getElementById('ctrlVm').value = Math.min(val, 400);
  } else if (param === 'f') {
    const val = Math.max(0.1, Number(document.getElementById('numF').value) || 1);
    labState.f = val;
    document.getElementById('ctrlF').value = Math.min(val, 120);
  } else if (param === 'phi') {
    let val = Number(document.getElementById('numPhi').value) || 0;
    while (val > 180) val -= 360;
    while (val < -180) val += 360;
    labState.phi = val;
    document.getElementById('ctrlPhi').value = val;
  }
  actualizarLab();
}

function onSliderInput(param) {
  if (param === 'Vm') {
    labState.Vm = Number(document.getElementById('ctrlVm').value);
    document.getElementById('numVm').value = labState.Vm;
  } else if (param === 'f') {
    labState.f = Number(document.getElementById('ctrlF').value);
    document.getElementById('numF').value = labState.f;
  } else if (param === 'phi') {
    labState.phi = Number(document.getElementById('ctrlPhi').value);
    document.getElementById('numPhi').value = labState.phi;
  }
  actualizarLab();
}

function setPresetVm(v) {
  labState.Vm = v;
  document.getElementById('numVm').value = v;
  document.getElementById('ctrlVm').value = Math.min(v, 400);
  actualizarLab();
}

function setPresetF(f) {
  labState.f = f;
  document.getElementById('numF').value = f;
  document.getElementById('ctrlF').value = Math.min(f, 120);
  actualizarLab();
}

function setPresetPhi(p) {
  labState.phi = p;
  document.getElementById('numPhi').value = p;
  document.getElementById('ctrlPhi').value = p;
  actualizarLab();
}

function onTimeChange() {
  labState.wt = Number(document.getElementById('ctrlWt').value);
  actualizarLab();
}

function resetTiempo() {
  labState.wt = 0;
  document.getElementById('ctrlWt').value = 0;
  actualizarLab();
}

function togglePlay() {
  labState.playing = !labState.playing;
  const btn = document.getElementById('btnPlay');
  if (btn) {
    btn.innerHTML = labState.playing
      ? '<i class="bi bi-pause-fill me-1"></i> Pausar'
      : '<i class="bi bi-play-fill me-1"></i> Reproducir';
    btn.classList.toggle('btn-success', !labState.playing);
    btn.classList.toggle('btn-warning', labState.playing);
  }
  if (labState.playing) {
    animarLab();
  } else if (labState.rafId) {
    cancelAnimationFrame(labState.rafId);
  }
}

function animarLab() {
  if (!labState.playing) return;
  const step = Math.min(3, Math.max(0.8, labState.f * 0.05));
  labState.wt = (labState.wt + step) % 720;
  document.getElementById('ctrlWt').value = labState.wt.toFixed(0);
  actualizarLab();
  labState.rafId = requestAnimationFrame(animarLab);
}

function calcValorInstantaneo(thetaDeg) {
  const rad = (thetaDeg + labState.phi) * Math.PI / 180;
  return labState.Vm * Math.cos(rad);
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
  if (!canvas) return;
  const ctx = canvas.getContext("2d");
  const w = canvas.width, h = canvas.height, cx = w / 2, cy = h / 2;
  dibujarGrillaYEjes(ctx, w, h, cx, cy);

  const magMostrada = labState.modo === 'pico' ? labState.Vm : labState.Vm / Math.SQRT2;
  const radioMax = Math.min(w, h) / 2 - 36;
  const scale = radioMax / (magMostrada > 0 ? magMostrada : 1);

  // Círculo de amplitud máxima
  ctx.beginPath();
  ctx.arc(cx, cy, magMostrada * scale, 0, 2 * Math.PI);
  ctx.strokeStyle = "#e2e8f0";
  ctx.setLineDash([3, 3]);
  ctx.lineWidth = 1.2;
  ctx.stroke();
  ctx.setLineDash([]);

  // Ejes Re e Im
  ctx.strokeStyle = "#94a3b8";
  ctx.lineWidth = 1.5;
  ctx.beginPath(); ctx.moveTo(15, cy); ctx.lineTo(w - 15, cy); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(cx, h - 15); ctx.lineTo(cx, 15); ctx.stroke();
  ctx.fillStyle = "#64748b";
  ctx.font = "bold 11px 'JetBrains Mono', monospace";
  ctx.fillText("Re (+)", w - 45, cy - 8);
  ctx.fillText("+j Im", cx + 8, 20);

  // 1. Fasor estático en t=0 (referencia fija)
  const anguloFijo = labState.phi * Math.PI / 180;
  const vxFijo = cx + magMostrada * scale * Math.cos(anguloFijo);
  const vyFijo = cy - magMostrada * scale * Math.sin(anguloFijo);
  
  ctx.strokeStyle = "#93c5fd";
  ctx.lineWidth = 2;
  ctx.setLineDash([4, 4]);
  ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(vxFijo, vyFijo); ctx.stroke();
  ctx.setLineDash([]);
  
  ctx.fillStyle = "#3b82f6";
  ctx.beginPath(); ctx.arc(vxFijo, vyFijo, 3, 0, 2 * Math.PI); ctx.fill();

  // 2. Fasor instantáneo rotatorio (wt + phi)
  const anguloInst = (labState.wt + labState.phi) * Math.PI / 180;
  const vx = cx + magMostrada * scale * Math.cos(anguloInst);
  const vy = cy - magMostrada * scale * Math.sin(anguloInst);

  // Arco angular
  const arcR = Math.min(32, radioMax * 0.4);
  ctx.strokeStyle = "#f59e0b";
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.arc(cx, cy, arcR, 0, -anguloInst, anguloInst > 0);
  ctx.stroke();

  // Flecha del fasor rotatorio
  ctx.strokeStyle = "#0284c7";
  ctx.fillStyle = "#0284c7";
  ctx.lineWidth = 3;
  ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(vx, vy); ctx.stroke();
  
  const headLen = 11;
  const angleRad = Math.atan2(vy - cy, vx - cx);
  ctx.beginPath();
  ctx.moveTo(vx, vy);
  ctx.lineTo(vx - headLen * Math.cos(angleRad - Math.PI / 6), vy - headLen * Math.sin(angleRad - Math.PI / 6));
  ctx.lineTo(vx - headLen * Math.cos(angleRad + Math.PI / 6), vy - headLen * Math.sin(angleRad + Math.PI / 6));
  ctx.closePath(); ctx.fill();

  // Proyección de la función elegida
  ctx.strokeStyle = "#f87171";
  ctx.lineWidth = 1;
  ctx.setLineDash([2, 2]);
  if (labState.funcion === 'cos') {
    // Proyección sobre el eje real
    ctx.beginPath(); ctx.moveTo(vx, vy); ctx.lineTo(vx, cy); ctx.stroke();
  } else {
    // Proyección sobre el eje imaginario (seno)
    ctx.beginPath(); ctx.moveTo(vx, vy); ctx.lineTo(cx, vy); ctx.stroke();
  }
  ctx.setLineDash([]);

  // Origen
  ctx.fillStyle = "#0f172a";
  ctx.beginPath(); ctx.arc(cx, cy, 3.5, 0, 2 * Math.PI); ctx.fill();
  
  // Etiqueta de magnitud
  ctx.fillStyle = "#0284c7";
  ctx.font = "bold 11px sans-serif";
  ctx.fillText(`${magMostrada.toFixed(1)} V`, cx + (radioMax + 8) * Math.cos(anguloFijo), cy - (radioMax + 8) * Math.sin(anguloFijo));
}

function dibujarOndaLab() {
  const canvas = document.getElementById("labWaveCanvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");
  const w = canvas.width, h = canvas.height;
  ctx.clearRect(0, 0, w, h);

  const margenIzq = 48, margenDer = 18, margenTop = 18, margenBot = 18;
  const plotW = w - margenIzq - margenDer;
  const plotH = h - margenTop - margenBot;
  const midY = margenTop + plotH / 2;

  const maxPlotV = labState.Vm > 0 ? labState.Vm * 1.2 : 1;
  const escalaY = (plotH / 2) / maxPlotV;

  // Grilla vertical (cada 90°)
  ctx.strokeStyle = "#f1f5f9";
  ctx.lineWidth = 1;
  for (let gx = 0; gx <= 720; gx += 90) {
    const px = margenIzq + (gx / 720) * plotW;
    ctx.beginPath(); ctx.moveTo(px, margenTop); ctx.lineTo(px, margenTop + plotH); ctx.stroke();
  }

  // Ejes coordenados
  ctx.strokeStyle = "#94a3b8";
  ctx.lineWidth = 1.5;
  ctx.beginPath(); ctx.moveTo(margenIzq, midY); ctx.lineTo(w - margenDer, midY); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(margenIzq, margenTop); ctx.lineTo(margenIzq, margenTop + plotH); ctx.stroke();

  // Marcas en eje Y (Voltios)
  ctx.fillStyle = "#64748b";
  ctx.font = "10px 'JetBrains Mono', monospace";
  ctx.textAlign = "right";
  ctx.fillText(`+${labState.Vm.toFixed(0)}V`, margenIzq - 6, midY - labState.Vm * escalaY + 4);
  ctx.fillText("0V", margenIzq - 6, midY + 4);
  ctx.fillText(`-${labState.Vm.toFixed(0)}V`, margenIzq - 6, midY + labState.Vm * escalaY + 4);

  // Marcas en eje X (Grados)
  ctx.textAlign = "center";
  [0, 180, 360, 540, 720].forEach(gx => {
    const px = margenIzq + (gx / 720) * plotW;
    ctx.fillText(gx + "°", px, margenTop + plotH + 15);
  });

  // Curva sinusoidal completa
  ctx.strokeStyle = "#0284c7";
  ctx.lineWidth = 2.4;
  ctx.beginPath();
  for (let gx = 0; gx <= 720; gx += 2) {
    const v = calcValorInstantaneo(gx);
    const px = margenIzq + (gx / 720) * plotW;
    const py = midY - v * escalaY;
    if (gx === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
  }
  ctx.stroke();

  // Nivel RMS de referencia
  const vrms = labState.Vm / Math.SQRT2;
  ctx.strokeStyle = "#f59e0b";
  ctx.setLineDash([4, 4]);
  ctx.lineWidth = 1.3;
  ctx.beginPath(); ctx.moveTo(margenIzq, midY - vrms * escalaY); ctx.lineTo(w - margenDer, midY - vrms * escalaY); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(margenIzq, midY + vrms * escalaY); ctx.lineTo(w - margenDer, midY + vrms * escalaY); ctx.stroke();
  ctx.setLineDash([]);

  // Punto instantáneo actual en el tiempo
  const vInst = calcValorInstantaneo(labState.wt);
  const pxInst = margenIzq + (labState.wt / 720) * plotW;
  const pyInst = midY - vInst * escalaY;

  // Líneas guías del punto instantáneo
  ctx.strokeStyle = "#dc2626";
  ctx.setLineDash([3, 3]);
  ctx.lineWidth = 1.2;
  ctx.beginPath(); ctx.moveTo(pxInst, margenTop); ctx.lineTo(pxInst, margenTop + plotH); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(margenIzq, pyInst); ctx.lineTo(pxInst, pyInst); ctx.stroke();
  ctx.setLineDash([]);

  // Círculo del punto instantáneo
  ctx.fillStyle = "#dc2626";
  ctx.beginPath(); ctx.arc(pxInst, pyInst, 5, 0, 2 * Math.PI); ctx.fill();
  ctx.fillStyle = "#ffffff";
  ctx.beginPath(); ctx.arc(pxInst, pyInst, 2, 0, 2 * Math.PI); ctx.fill();
}

function actualizarLab() {
  const omega = 2 * Math.PI * labState.f;
  const T = 1 / labState.f;
  const magMostrada = labState.modo === 'pico' ? labState.Vm : labState.Vm / Math.SQRT2;
  const anguloInst = ((labState.wt + labState.phi) % 360 + 360) % 360;
  const anguloInstSigned = anguloInst > 180 ? anguloInst - 360 : anguloInst;
  const vInst = calcValorInstantaneo(labState.wt);
  const tRealMs = ((labState.wt / 360) * T) * 1000;

  // Actualizar indicadores numéricos
  const elLblWt = document.getElementById('lblWt');
  if (elLblWt) elLblWt.textContent = labState.wt.toFixed(0);

  const elTReal = document.getElementById('lblTiempoSegundos');
  if (elTReal) elTReal.textContent = `t = ${tRealMs.toFixed(2)} ms`;

  const elOutVt = document.getElementById('outVt');
  if (elOutVt) elOutVt.textContent = vInst.toFixed(2) + " V";

  const elOutAng = document.getElementById('outAngInst');
  if (elOutAng) elOutAng.textContent = anguloInstSigned.toFixed(1) + "°";

  const elOutOmega = document.getElementById('outOmega');
  if (elOutOmega) elOutOmega.textContent = omega.toFixed(2) + " rad/s";

  const elTagOmega = document.getElementById('tagOmega');
  if (elTagOmega) elTagOmega.textContent = `${omega.toFixed(1)} rad/s`;

  const elOutT = document.getElementById('outT');
  if (elOutT) elOutT.textContent = `${(T * 1000).toFixed(2)} ms`;

  // Cuadrante de fase
  const elTagCuad = document.getElementById('tagCuad');
  if (elTagCuad) {
    let cText = "Cuad. I";
    const p = labState.phi;
    if (p > 0 && p < 90) cText = "Cuadrante I";
    else if (p > 90 && p < 180) cText = "Cuadrante II";
    else if (p < -90 && p > -180) cText = "Cuadrante III";
    else if (p < 0 && p > -90) cText = "Cuadrante IV";
    else if (p === 0) cText = "En fase (0°)";
    else if (p === 90) cText = "+90° (Cuadratura)";
    else if (p === -90) cText = "-90° (Cuadratura)";
    else if (Math.abs(p) === 180) cText = "Oposición (180°)";
    elTagCuad.textContent = cText;
  }

  // Notación fasorial
  const elOutFasor = document.getElementById('outFasor');
  if (elOutFasor) {
    const sufijo = labState.modo === 'rms' ? 'V (RMS)' : 'V (Pico)';
    elOutFasor.innerHTML = `${magMostrada.toFixed(2)} &ang; ${labState.phi.toFixed(1)}&deg; ${sufijo}`;
  }

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
