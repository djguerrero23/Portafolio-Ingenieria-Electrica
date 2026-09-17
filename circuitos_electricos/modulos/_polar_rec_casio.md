# Herramienta interactiva: Rectangular ↔ Polar (Bidireccional)

::: {.card-module}
### 🧮 Conversor Interactivo Bidireccional de Fasores {.unnumbered}

```{=html}
<!-- Selector de Modo con Pestañas / Tabs -->
<ul class="nav nav-pills mb-4 justify-content-center" id="phasorTab" role="tablist">
  <li class="nav-item" role="presentation">
    <button class="nav-link active px-4 py-2 fw-bold" id="rec2pol-tab" data-bs-toggle="pill" type="button" role="tab" onclick="cambiarModo('rec2pol')">
      <i class="bi bi-arrow-right-circle me-1"></i> Rectangular ➔ Polar
    </button>
  </li>
  <li class="nav-item" role="presentation">
    <button class="nav-link px-4 py-2 fw-bold" id="pol2rec-tab" data-bs-toggle="pill" type="button" role="tab" onclick="cambiarModo('pol2rec')">
      <i class="bi bi-arrow-left-circle me-1"></i> Polar ➔ Rectangular
    </button>
  </li>
</ul>

<!-- Formulario Rectangular a Polar -->
<div id="panelRec2Pol" class="row g-3 align-items-end">
  <div class="col-md-5">
    <label for="realPart" class="form-label mb-1"><strong>Parte Real <i>x</i> (Resistencia <i>R</i>):</strong></label>
    <div class="input-group">
      <span class="input-group-text bg-light fw-bold text-secondary">Re</span>
      <input id="realPart" type="number" class="form-control" value="3" step="0.5" oninput="calcularDesdeRectangular()">
    </div>
  </div>

  <div class="col-md-5">
    <label for="imagPart" class="form-label mb-1"><strong>Parte Imaginaria <i>y</i> (Reactancia <i>X</i>):</strong></label>
    <div class="input-group">
      <span class="input-group-text bg-light fw-bold text-secondary">+<i>j</i> Im</span>
      <input id="imagPart" type="number" class="form-control" value="4" step="0.5" oninput="calcularDesdeRectangular()">
    </div>
  </div>

  <div class="col-md-2">
    <button class="btn btn-primary w-100" onclick="calcularDesdeRectangular()">
      <i class="bi bi-calculator me-1"></i> Calcular
    </button>
  </div>
</div>

<!-- Formulario Polar a Rectangular -->
<div id="panelPol2Rec" class="row g-3 align-items-end" style="display: none;">
  <div class="col-md-5">
    <label for="magPart" class="form-label mb-1"><strong>Magnitud o Módulo <i>r</i> (|<b>Z</b>| o |<b>V</b>|):</strong></label>
    <div class="input-group">
      <span class="input-group-text bg-light fw-bold text-secondary">|<i>r</i>|</span>
      <input id="magPart" type="number" class="form-control" value="5" min="0" step="0.5" oninput="calcularDesdePolar()">
    </div>
  </div>

  <div class="col-md-5">
    <label for="angPart" class="form-label mb-1"><strong>Ángulo de Fase <i>&theta;</i> (Grados &deg;):</strong></label>
    <div class="input-group">
      <span class="input-group-text bg-light fw-bold text-secondary">&ang; <i>&theta;</i></span>
      <input id="angPart" type="number" class="form-control" value="53.13" step="1" oninput="calcularDesdePolar()">
      <span class="input-group-text bg-light">&deg;</span>
    </div>
  </div>

  <div class="col-md-2">
    <button class="btn btn-primary w-100" onclick="calcularDesdePolar()">
      <i class="bi bi-calculator me-1"></i> Calcular
    </button>
  </div>
</div>

<!-- Área de Resultados y Gráfico del Plano Fasorial -->
<div class="row mt-4 align-items-stretch">
  <div class="col-lg-5 mb-3 mb-lg-0">
    <div id="resultadoComplejo" class="h-100"></div>
  </div>

  <div class="col-lg-7 text-center">
    <div class="p-3 bg-white rounded-3 border shadow-sm d-inline-block w-100 h-100 d-flex flex-column justify-content-center align-items-center">
      <div class="d-flex justify-content-between w-100 mb-2 px-1">
        <span class="badge bg-secondary" style="font-size: 0.75rem;"><i class="bi bi-grid-3x3 me-1"></i> Plano de Gauss ($t=0$)</span>
        <span id="badgeCuadrante" class="badge bg-primary" style="font-size: 0.75rem;">Cuadrante I</span>
      </div>
      <canvas id="phasorCanvas" width="440" height="320" style="max-width: 100%; height: auto; border-radius: 8px;"></canvas>
    </div>
  </div>
</div>

<script>
let modoActual = 'rec2pol';

function cambiarModo(modo) {
  modoActual = modo;
  const btnRec = document.getElementById('rec2pol-tab');
  const btnPol = document.getElementById('pol2rec-tab');
  const panelRec = document.getElementById('panelRec2Pol');
  const panelPol = document.getElementById('panelPol2Rec');

  if (modo === 'rec2pol') {
    btnRec.classList.add('active');
    btnPol.classList.remove('active');
    panelRec.style.display = 'flex';
    panelPol.style.display = 'none';
    calcularDesdeRectangular();
  } else {
    btnPol.classList.add('active');
    btnRec.classList.remove('active');
    panelRec.style.display = 'none';
    panelPol.style.display = 'flex';
    calcularDesdePolar();
  }
}

function dibujarPlano(ctx, w, h, cx, cy, scale, x, y, r, theta) {
  ctx.clearRect(0, 0, w, h);

  // 1. Cuadrícula suave
  ctx.strokeStyle = "#f1f5f9";
  ctx.lineWidth = 1;
  const step = Math.max(scale, 22);
  for (let px = cx % step; px < w; px += step) {
    ctx.beginPath(); ctx.moveTo(px, 0); ctx.lineTo(px, h); ctx.stroke();
  }
  for (let py = cy % step; py < h; py += step) {
    ctx.beginPath(); ctx.moveTo(0, py); ctx.lineTo(w, py); ctx.stroke();
  }

  // Círculo unitario/guía
  if (r > 1e-4) {
    ctx.beginPath();
    ctx.arc(cx, cy, r * scale, 0, 2 * Math.PI);
    ctx.strokeStyle = "#e2e8f0";
    ctx.setLineDash([3, 3]);
    ctx.stroke();
    ctx.setLineDash([]);
  }

  // 2. Ejes Re e Im
  ctx.strokeStyle = "#94a3b8";
  ctx.lineWidth = 1.5;
  ctx.beginPath(); ctx.moveTo(20, cy); ctx.lineTo(w - 20, cy); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(cx, h - 20); ctx.lineTo(cx, 20); ctx.stroke();

  // Flechas y textos de ejes
  ctx.fillStyle = "#64748b";
  ctx.font = "bold 11px 'JetBrains Mono', monospace";
  ctx.fillText("Re (+)", w - 48, cy - 8);
  ctx.fillText("+j Im", cx + 8, 22);
  ctx.fillText("-j Im", cx + 8, h - 10);
  ctx.fillText("(-)", 8, cy - 8);

  // 3. Proyecciones punteadas
  if (r > 1e-4) {
    const vx = cx + x * scale;
    const vy = cy - y * scale;

    ctx.strokeStyle = "#93c5fd";
    ctx.lineWidth = 1.2;
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.moveTo(vx, cy); ctx.lineTo(vx, vy); ctx.lineTo(cx, vy);
    ctx.stroke();
    ctx.setLineDash([]);

    // 4. Arco del Ángulo θ
    const arcRadius = Math.min(40, Math.max(18, r * scale * 0.45));
    ctx.strokeStyle = "#f59e0b";
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    const endAngle = -theta * Math.PI / 180;
    ctx.arc(cx, cy, arcRadius, 0, endAngle, theta > 0);
    ctx.stroke();

    // Etiqueta del ángulo
    ctx.fillStyle = "#d97706";
    ctx.font = "bold 12px 'Plus Jakarta Sans', sans-serif";
    const midAngle = (-theta * Math.PI / 180) / 2;
    const tx = cx + (arcRadius + 18) * Math.cos(midAngle);
    const ty = cy + (arcRadius + 18) * Math.sin(midAngle);
    ctx.fillText(`${theta.toFixed(1)}°`, tx - 12, ty + 4);

    // 5. Vector Fasorial (Flecha)
    ctx.strokeStyle = "#0284c7";
    ctx.fillStyle = "#0284c7";
    ctx.lineWidth = 3.5;

    ctx.beginPath();
    ctx.moveTo(cx, cy);
    ctx.lineTo(vx, vy);
    ctx.stroke();

    // Cabeza de la flecha
    const headLen = 12;
    const angleRad = Math.atan2(-y, x);
    ctx.beginPath();
    ctx.moveTo(vx, vy);
    ctx.lineTo(vx - headLen * Math.cos(angleRad - Math.PI / 6), vy - headLen * Math.sin(angleRad - Math.PI / 6));
    ctx.lineTo(vx - headLen * Math.cos(angleRad + Math.PI / 6), vy - headLen * Math.sin(angleRad + Math.PI / 6));
    ctx.closePath();
    ctx.fill();

    // Punto en el origen y en la punta
    ctx.fillStyle = "#0f172a";
    ctx.beginPath(); ctx.arc(cx, cy, 3.5, 0, 2*Math.PI); ctx.fill();
    ctx.fillStyle = "#0284c7";
    ctx.beginPath(); ctx.arc(vx, vy, 4, 0, 2*Math.PI); ctx.fill();
  }
}

function actualizarInterfaz(x, y, r, theta, origen) {
  let cuadrante = "Sobre el eje";
  let tipoFisico = "Resistivo puro";
  let badgeColor = "bg-primary";

  if (x > 0 && y > 0) {
    cuadrante = "Cuadrante I (0° < θ < 90°)";
    tipoFisico = "Inductivo (Tensión adelanta a Corriente)";
    badgeColor = "bg-primary";
  } else if (x < 0 && y > 0) {
    cuadrante = "Cuadrante II (90° < θ < 180°)";
    tipoFisico = "Fuente en adelanto / Generación activa";
    badgeColor = "bg-warning text-dark";
  } else if (x < 0 && y < 0) {
    cuadrante = "Cuadrante III (-180° < θ < -90°)";
    tipoFisico = "Fuente en atraso / Potencia inversa";
    badgeColor = "bg-danger";
  } else if (x > 0 && y < 0) {
    cuadrante = "Cuadrante IV (-90° < θ < 0°)";
    tipoFisico = "Capacitivo (Corriente adelanta a Tensión)";
    badgeColor = "bg-info text-dark";
  } else if (y === 0 && x !== 0) {
    cuadrante = x > 0 ? "Eje Real Positivo (θ = 0°)" : "Eje Real Negativo (θ = 180°)";
    tipoFisico = "Resistivo Puro (FP = 1.0)";
  } else if (x === 0 && y !== 0) {
    cuadrante = y > 0 ? "Eje Imaginario Positivo (θ = +90°)" : "Eje Imaginario Negativo (θ = -90°)";
    tipoFisico = y > 0 ? "Inductivo Puro (FP = 0 en atraso)" : "Capacitivo Puro (FP = 0 en adelanto)";
  }

  const badgeCuad = document.getElementById("badgeCuadrante");
  if (badgeCuad) {
    badgeCuad.className = `badge ${badgeColor}`;
    badgeCuad.textContent = cuadrante.split("(")[0].trim();
  }

  const signo = y >= 0 ? "+" : "-";
  const yi = Math.abs(y);

  const res = document.getElementById("resultadoComplejo");
  if (res) {
    let pasosHtml = "";
    if (origen === 'rectangular') {
      pasosHtml = `
        <div class="small text-muted mb-2">
          <strong>Paso a paso analítico:</strong><br>
          • Módulo: <code>r = &radic;(${x.toFixed(2)}&sup2; + ${y.toFixed(2)}&sup2;) = ${r.toFixed(4)}</code><br>
          • Ángulo: <code>&theta; = arctan(${y.toFixed(2)} / ${x.toFixed(2)}) = ${theta.toFixed(2)}&deg;</code>
        </div>
      `;
    } else {
      pasosHtml = `
        <div class="small text-muted mb-2">
          <strong>Paso a paso analítico:</strong><br>
          • Parte Real: <code>x = ${r.toFixed(2)} &middot; cos(${theta.toFixed(2)}&deg;) = ${x.toFixed(4)}</code><br>
          • Parte Imag: <code>y = ${r.toFixed(2)} &middot; sin(${theta.toFixed(2)}&deg;) = ${y.toFixed(4)}</code>
        </div>
      `;
    }

    res.innerHTML = `
      <div class="card p-3 border-0 bg-light h-100 shadow-sm" style="border-left: 4px solid #0284c7 !important;">
        <h6 class="text-primary mb-3 fw-bold d-flex align-items-center">
          <i class="bi bi-check-circle-fill me-2"></i> Resultados de Conversión
        </h6>
        
        <div class="mb-2">
          <span class="text-muted small d-block">Forma Polar:</span>
          <code class="fs-5 text-primary fw-bold">${r.toFixed(3)} &ang; ${theta.toFixed(2)}&deg;</code>
        </div>

        <div class="mb-2">
          <span class="text-muted small d-block">Forma Rectangular:</span>
          <code class="fs-5 text-dark fw-bold">${x.toFixed(3)} ${signo} j${yi.toFixed(3)}</code>
        </div>

        <div class="mb-2">
          <span class="text-muted small d-block">Forma Exponencial de Euler:</span>
          <code class="fs-6 text-secondary">${r.toFixed(3)} &middot; e<sup>j(${theta.toFixed(2)}&deg;)</sup></code>
        </div>

        <hr class="my-2">
        ${pasosHtml}
        <div class="p-2 rounded bg-white border border-light small">
          <i class="bi bi-activity text-primary me-1"></i> <strong>Comportamiento:</strong> ${tipoFisico}
        </div>
      </div>
    `;
  }

  const canvas = document.getElementById("phasorCanvas");
  if (canvas) {
    const ctx = canvas.getContext("2d");
    const w = canvas.width;
    const h = canvas.height;
    const cx = w / 2;
    const cy = h / 2;

    const maxVal = Math.max(Math.abs(x), Math.abs(y), 1);
    const scale = (Math.min(w, h) / 2 - 45) / maxVal;

    dibujarPlano(ctx, w, h, cx, cy, scale, x, y, r, theta);
  }
}

function calcularDesdeRectangular() {
  const elReal = document.getElementById("realPart");
  const elImag = document.getElementById("imagPart");
  if (!elReal || !elImag) return;

  const x = Number(elReal.value) || 0;
  const y = Number(elImag.value) || 0;

  const r = Math.hypot(x, y);
  let theta = Math.atan2(y, x) * 180 / Math.PI;
  if (Math.abs(theta) < 1e-10) theta = 0;

  // Actualizar los inputs del otro panel para mantener sincronía
  const magInput = document.getElementById("magPart");
  const angInput = document.getElementById("angPart");
  if (magInput) magInput.value = r.toFixed(2);
  if (angInput) angInput.value = theta.toFixed(2);

  actualizarInterfaz(x, y, r, theta, 'rectangular');
}

function calcularDesdePolar() {
  const elMag = document.getElementById("magPart");
  const elAng = document.getElementById("angPart");
  if (!elMag || !elAng) return;

  const r = Math.max(0, Number(elMag.value) || 0);
  let theta = Number(elAng.value) || 0;

  const rad = theta * Math.PI / 180;
  const x = r * Math.cos(rad);
  const y = r * Math.sin(rad);

  // Actualizar inputs del panel rectangular
  const realInput = document.getElementById("realPart");
  const imagInput = document.getElementById("imagPart");
  if (realInput) realInput.value = x.toFixed(2);
  if (imagInput) imagInput.value = y.toFixed(2);

  actualizarInterfaz(x, y, r, theta, 'polar');
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", calcularDesdeRectangular);
} else {
  setTimeout(calcularDesdeRectangular, 50);
}
</script>
```
:::