```{=html}
<!-- Entradas de los dos operandos -->
<div class="row g-3">
  <div class="col-md-6">
    <div class="p-3 rounded-3 border h-100 bg-white" style="border-left: 4px solid #0284c7 !important;">
      <strong class="text-primary d-flex align-items-center gap-1">
        <i class="bi bi-pin-angle-fill"></i> Operando <b>Z<sub>1</sub></b>
      </strong>
      <div class="row g-2 mt-1">
        <div class="col-6">
          <label class="form-label mb-1 small text-muted"><strong>Parte Real <i>x</i><sub>1</sub></strong></label>
          <div class="input-group input-group-sm">
            <span class="input-group-text bg-light">Re</span>
            <input id="op1Real" type="number" class="form-control" value="4" step="0.5" oninput="calcularOperacion()">
          </div>
        </div>
        <div class="col-6">
          <label class="form-label mb-1 small text-muted"><strong>Parte Imag <i>y</i><sub>1</sub></strong></label>
          <div class="input-group input-group-sm">
            <span class="input-group-text bg-light">+<i>j</i></span>
            <input id="op1Imag" type="number" class="form-control" value="3" step="0.5" oninput="calcularOperacion()">
          </div>
        </div>
      </div>
      <div id="op1Polar" class="small mt-2 p-1 rounded bg-light text-primary" style="font-family:'JetBrains Mono',monospace; font-size:0.82rem;"></div>
    </div>
  </div>

  <div class="col-md-6">
    <div class="p-3 rounded-3 border h-100 bg-white" style="border-left: 4px solid #f59e0b !important;">
      <strong style="color:#d97706;" class="d-flex align-items-center gap-1">
        <i class="bi bi-pin-angle-fill"></i> Operando <b>Z<sub>2</sub></b>
      </strong>
      <div class="row g-2 mt-1">
        <div class="col-6">
          <label class="form-label mb-1 small text-muted"><strong>Parte Real <i>x</i><sub>2</sub></strong></label>
          <div class="input-group input-group-sm">
            <span class="input-group-text bg-light">Re</span>
            <input id="op2Real" type="number" class="form-control" value="2" step="0.5" oninput="calcularOperacion()">
          </div>
        </div>
        <div class="col-6">
          <label class="form-label mb-1 small text-muted"><strong>Parte Imag <i>y</i><sub>2</sub></strong></label>
          <div class="input-group input-group-sm">
            <span class="input-group-text bg-light">+<i>j</i></span>
            <input id="op2Imag" type="number" class="form-control" value="-1" step="0.5" oninput="calcularOperacion()">
          </div>
        </div>
      </div>
      <div id="op2Polar" class="small mt-2 p-1 rounded bg-light text-warning-emphasis" style="font-family:'JetBrains Mono',monospace; font-size:0.82rem; color: #b45309 !important;"></div>
    </div>
  </div>
</div>

<!-- Selector de operación -->
<ul class="nav nav-pills mb-3 mt-4 justify-content-center gap-1" id="opTab" role="tablist">
  <li class="nav-item"><button class="nav-link active px-3 py-2 fw-bold" data-op="suma" onclick="seleccionarOperacion('suma')">Z<sub>1</sub> + Z<sub>2</sub> (Suma)</button></li>
  <li class="nav-item"><button class="nav-link px-3 py-2 fw-bold" data-op="resta" onclick="seleccionarOperacion('resta')">Z<sub>1</sub> − Z<sub>2</sub> (Resta)</button></li>
  <li class="nav-item"><button class="nav-link px-3 py-2 fw-bold" data-op="mult" onclick="seleccionarOperacion('mult')">Z<sub>1</sub> &times; Z<sub>2</sub> (Producto)</button></li>
  <li class="nav-item"><button class="nav-link px-3 py-2 fw-bold" data-op="div" onclick="seleccionarOperacion('div')">Z<sub>1</sub> &divide; Z<sub>2</sub> (División)</button></li>
</ul>

<!-- Resultado + gráfico -->
<div class="row mt-3 align-items-stretch">
  <div class="col-lg-5 mb-3 mb-lg-0">
    <div id="resultadoOperacion" class="h-100"></div>
  </div>

  <div class="col-lg-7 text-center">
    <div class="p-3 bg-white rounded-3 border shadow-sm d-inline-block w-100 h-100 d-flex flex-column justify-content-center align-items-center">
      <div class="d-flex justify-content-center gap-3 w-100 mb-2 px-1 flex-wrap">
        <span class="badge" style="background:#0284c7;">&#9679; Z<sub>1</sub></span>
        <span class="badge" style="background:#f59e0b;">&#9679; Z<sub>2</sub></span>
        <span class="badge" style="background:#8b5cf6;">&#9679; Resultado</span>
      </div>
      <canvas id="opCanvas" width="440" height="320" style="max-width: 100%; height: auto; border-radius: 8px;"></canvas>
    </div>
  </div>
</div>

<script>
let operacionActual = 'suma';

function seleccionarOperacion(op) {
  operacionActual = op;
  document.querySelectorAll('#opTab .nav-link').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.op === op);
  });
  calcularOperacion();
}

function aPolarOp(x, y) {
  const r = Math.hypot(x, y);
  let theta = Math.atan2(y, x) * 180 / Math.PI;
  if (Math.abs(theta) < 1e-10) theta = 0;
  return { r, theta };
}

function fmtRectOp(x, y) {
  const signo = y >= 0 ? '+' : '−';
  return `${x.toFixed(3)} ${signo} j${Math.abs(y).toFixed(3)}`;
}

function dibujarEjesOp(ctx, w, h, cx, cy) {
  ctx.clearRect(0, 0, w, h);
  ctx.strokeStyle = "#f1f5f9";
  ctx.lineWidth = 1;
  const step = 22;
  for (let px = cx % step; px < w; px += step) { ctx.beginPath(); ctx.moveTo(px, 0); ctx.lineTo(px, h); ctx.stroke(); }
  for (let py = cy % step; py < h; py += step) { ctx.beginPath(); ctx.moveTo(0, py); ctx.lineTo(w, py); ctx.stroke(); }

  ctx.strokeStyle = "#94a3b8";
  ctx.lineWidth = 1.5;
  ctx.beginPath(); ctx.moveTo(20, cy); ctx.lineTo(w - 20, cy); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(cx, h - 20); ctx.lineTo(cx, 20); ctx.stroke();

  ctx.fillStyle = "#64748b";
  ctx.font = "bold 11px 'JetBrains Mono', monospace";
  ctx.fillText("Re", w - 32, cy - 8);
  ctx.fillText("+j Im", cx + 8, 22);
}

function dibujarVectorOp(ctx, cx, cy, scale, x, y, color, grosor) {
  const vx = cx + x * scale;
  const vy = cy - y * scale;
  ctx.strokeStyle = color;
  ctx.fillStyle = color;
  ctx.lineWidth = grosor;
  ctx.beginPath();
  ctx.moveTo(cx, cy);
  ctx.lineTo(vx, vy);
  ctx.stroke();

  const headLen = 11;
  const angleRad = Math.atan2(-y, x);
  ctx.beginPath();
  ctx.moveTo(vx, vy);
  ctx.lineTo(vx - headLen * Math.cos(angleRad - Math.PI / 6), vy - headLen * Math.sin(angleRad - Math.PI / 6));
  ctx.lineTo(vx - headLen * Math.cos(angleRad + Math.PI / 6), vy - headLen * Math.sin(angleRad + Math.PI / 6));
  ctx.closePath();
  ctx.fill();
  return { vx, vy };
}

function dibujarOperacionVisual(x1, y1, x2, y2, xr, yr, op) {
  const canvas = document.getElementById("opCanvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");
  const w = canvas.width, h = canvas.height, cx = w / 2, cy = h / 2;

  const maxVal = Math.max(Math.abs(x1), Math.abs(y1), Math.abs(x2), Math.abs(y2), Math.abs(xr), Math.abs(yr), 1);
  const scale = (Math.min(w, h) / 2 - 45) / maxVal;

  dibujarEjesOp(ctx, w, h, cx, cy);

  // Construcción del paralelogramo (en suma/resta)
  if (op === 'suma' || op === 'resta') {
    ctx.setLineDash([4, 4]);
    ctx.lineWidth = 1.2;
    ctx.strokeStyle = "#cbd5e1";
    const p1 = { x: cx + x1 * scale, y: cy - y1 * scale };
    const p2 = { x: cx + x2 * scale, y: cy - y2 * scale };
    const pr = { x: cx + xr * scale, y: cy - yr * scale };
    ctx.beginPath(); ctx.moveTo(p1.x, p1.y); ctx.lineTo(pr.x, pr.y); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(p2.x, p2.y); ctx.lineTo(pr.x, pr.y); ctx.stroke();
    ctx.setLineDash([]);
  }

  dibujarVectorOp(ctx, cx, cy, scale, x1, y1, "#0284c7", 3);
  dibujarVectorOp(ctx, cx, cy, scale, x2, y2, "#f59e0b", 3);
  dibujarVectorOp(ctx, cx, cy, scale, xr, yr, "#8b5cf6", 3.5);

  ctx.fillStyle = "#0f172a";
  ctx.beginPath(); ctx.arc(cx, cy, 3.5, 0, 2 * Math.PI); ctx.fill();
}

function calcularOperacion() {
  const x1 = Number(document.getElementById("op1Real").value) || 0;
  const y1 = Number(document.getElementById("op1Imag").value) || 0;
  const x2 = Number(document.getElementById("op2Real").value) || 0;
  const y2 = Number(document.getElementById("op2Imag").value) || 0;

  const p1 = aPolarOp(x1, y1);
  const p2 = aPolarOp(x2, y2);
  const elP1 = document.getElementById("op1Polar");
  const elP2 = document.getElementById("op2Polar");
  if (elP1) elP1.innerHTML = `<strong>Forma Polar:</strong> ${p1.r.toFixed(3)} &ang; ${p1.theta.toFixed(2)}&deg;`;
  if (elP2) elP2.innerHTML = `<strong>Forma Polar:</strong> ${p2.r.toFixed(3)} &ang; ${p2.theta.toFixed(2)}&deg;`;

  let xr, yr, pasosHtml, tituloOp;

  if (operacionActual === 'suma') {
    xr = x1 + x2; yr = y1 + y2;
    tituloOp = "Z<sub>1</sub> + Z<sub>2</sub>";
    pasosHtml = `
      <div class="small text-muted mb-2">
        <strong>Método: suma en forma rectangular (componente a componente)</strong><br>
        • Real: <code>x = ${x1.toFixed(2)} + (${x2.toFixed(2)}) = ${xr.toFixed(3)}</code><br>
        • Imag: <code>y = ${y1.toFixed(2)} + (${y2.toFixed(2)}) = ${yr.toFixed(3)}</code>
      </div>`;
  } else if (operacionActual === 'resta') {
    xr = x1 - x2; yr = y1 - y2;
    tituloOp = "Z<sub>1</sub> − Z<sub>2</sub>";
    pasosHtml = `
      <div class="small text-muted mb-2">
        <strong>Método: resta en forma rectangular (componente a componente)</strong><br>
        • Real: <code>x = ${x1.toFixed(2)} − (${x2.toFixed(2)}) = ${xr.toFixed(3)}</code><br>
        • Imag: <code>y = ${y1.toFixed(2)} − (${y2.toFixed(2)}) = ${yr.toFixed(3)}</code>
      </div>`;
  } else if (operacionActual === 'mult') {
    const rr = p1.r * p2.r;
    const th = p1.theta + p2.theta;
    xr = rr * Math.cos(th * Math.PI / 180);
    yr = rr * Math.sin(th * Math.PI / 180);
    tituloOp = "Z<sub>1</sub> &times; Z<sub>2</sub>";
    pasosHtml = `
      <div class="small text-muted mb-2">
        <strong>Método: producto en forma polar (magnitudes se multiplican, ángulos se suman)</strong><br>
        • Magnitud: <code>r = ${p1.r.toFixed(3)} &middot; ${p2.r.toFixed(3)} = ${rr.toFixed(3)}</code><br>
        • Ángulo: <code>&theta; = ${p1.theta.toFixed(2)}&deg; + ${p2.theta.toFixed(2)}&deg; = ${th.toFixed(2)}&deg;</code>
      </div>`;
  } else {
    if (p2.r === 0) {
      document.getElementById("resultadoOperacion").innerHTML =
        `<div class="alert alert-danger">No se puede dividir entre Z<sub>2</sub> = 0.</div>`;
      return;
    }
    const rr = p1.r / p2.r;
    const th = p1.theta - p2.theta;
    xr = rr * Math.cos(th * Math.PI / 180);
    yr = rr * Math.sin(th * Math.PI / 180);
    tituloOp = "Z<sub>1</sub> &divide; Z<sub>2</sub>";
    pasosHtml = `
      <div class="small text-muted mb-2">
        <strong>Método: división en forma polar (magnitudes se dividen, ángulos se restan)</strong><br>
        • Magnitud: <code>r = ${p1.r.toFixed(3)} / ${p2.r.toFixed(3)} = ${rr.toFixed(3)}</code><br>
        • Ángulo: <code>&theta; = ${p1.theta.toFixed(2)}&deg; − (${p2.theta.toFixed(2)}&deg;) = ${th.toFixed(2)}&deg;</code>
      </div>`;
  }

  const pr = aPolarOp(xr, yr);

  const resOp = document.getElementById("resultadoOperacion");
  if (resOp) {
    resOp.innerHTML = `
      <div class="card p-3 border-0 bg-light h-100 shadow-sm" style="border-left: 4px solid #8b5cf6 !important;">
        <h6 class="mb-3 fw-bold d-flex align-items-center" style="color:#7c3aed;">
          <i class="bi bi-check-circle-fill me-2"></i> Resultado de ${tituloOp}
        </h6>

        <div class="mb-2">
          <span class="text-muted small d-block">Forma Rectangular:</span>
          <code class="fs-5 text-dark fw-bold">${fmtRectOp(xr, yr)}</code>
        </div>

        <div class="mb-2">
          <span class="text-muted small d-block">Forma Polar:</span>
          <code class="fs-5 fw-bold" style="color:#7c3aed;">${pr.r.toFixed(3)} &ang; ${pr.theta.toFixed(2)}&deg;</code>
        </div>

        <hr class="my-2">
        ${pasosHtml}
      </div>
    `;
  }

  dibujarOperacionVisual(x1, y1, x2, y2, xr, yr, operacionActual);
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", calcularOperacion);
} else {
  setTimeout(calcularOperacion, 50);
}
</script>
```