::: {.card-module}
### 🔬 Laboratorio 3 — Transformación Complejo ↔ Polar y Cuadrantes {.unnumbered}

En ingeniería eléctrica, la conversión fluida entre la **forma rectangular** ($x + jy$, ideal para sumar y restar fasores) y la **forma polar** ($r\angle\theta$, ideal para multiplicar, dividir y calcular potencias) es esencial.

$$
\mathbf Z = x + jy = r\angle\theta = r\mathrm{e}^{j\theta}
$$

donde:
$$
r = \sqrt{x^2 + y^2}, \qquad \theta = \operatorname{atan2}(y, x)
$$

```{=html}
<!-- ============================================================
     LABORATORIO 3 — CONVERSOR COMPLEJO <-> POLAR BIDIRECCIONAL
     ============================================================ -->
<div class="lab3-container p-3 mb-3 bg-white rounded-3 border shadow-sm">

  <!-- Selector de Modo con Pestañas -->
  <ul class="nav nav-pills mb-3 justify-content-center gap-2" id="lab3_tab" role="tablist">
    <li class="nav-item" role="presentation">
      <button class="nav-link active px-4 py-2 fw-bold" id="lab3_tab_rec2pol" type="button" onclick="lab3_setMode('rec2pol')">
        <i class="bi bi-arrow-right-circle me-1"></i> Rectangular ➔ Polar
      </button>
    </li>
    <li class="nav-item" role="presentation">
      <button class="nav-link px-4 py-2 fw-bold" id="lab3_tab_pol2rec" type="button" onclick="lab3_setMode('pol2rec')">
        <i class="bi bi-arrow-left-circle me-1"></i> Polar ➔ Rectangular
      </button>
    </li>
  </ul>

  <!-- Presets Rápidos de Ingeniería -->
  <div class="p-2 mb-3 bg-light rounded-3 border d-flex flex-wrap align-items-center justify-content-center gap-2">
    <span class="small fw-bold text-muted me-2"><i class="bi bi-bookmark-star-fill text-warning"></i> Casos típicos:</span>
    <button type="button" class="btn btn-sm btn-outline-primary" onclick="lab3_loadPreset(3, 4)">3 + <i>j</i>4 (5 &ang; 53.1&deg;)</button>
    <button type="button" class="btn btn-sm btn-outline-primary" onclick="lab3_loadPreset(6, -8)">6 &minus; <i>j</i>8 (10 &ang; -53.1&deg;)</button>
    <button type="button" class="btn btn-sm btn-outline-warning text-dark" onclick="lab3_loadPreset(-5, 5)">&minus;5 + <i>j</i>5 (C-II)</button>
    <button type="button" class="btn btn-sm btn-outline-danger" onclick="lab3_loadPreset(-4, -3)">&minus;4 &minus; <i>j</i>3 (C-III)</button>
    <button type="button" class="btn btn-sm btn-outline-secondary" onclick="lab3_loadPreset(10, 0)">10 &ang; 0&deg; (Resistivo)</button>
    <button type="button" class="btn btn-sm btn-outline-success" onclick="lab3_loadPreset(0, 10)">10 &ang; 90&deg; (Inductivo)</button>
  </div>

  <!-- Panel de Entradas: Rectangular a Polar -->
  <div id="lab3_panel_rec2pol" class="row g-3 align-items-end mb-3">
    <div class="col-md-6">
      <label for="lab3_in_x" class="form-label mb-1 small fw-bold">Parte Real <i>x</i> (Resistencia <i>R</i>):</label>
      <div class="input-group">
        <span class="input-group-text bg-light fw-bold text-primary">Re (x)</span>
        <input id="lab3_in_x" type="number" class="form-control" value="3" step="0.5" oninput="lab3_calcRec2Pol()">
      </div>
      <input id="lab3_slider_x" type="range" class="form-range mt-1" min="-20" max="20" step="0.5" value="3" oninput="lab3_syncSlider('x')">
    </div>

    <div class="col-md-6">
      <label for="lab3_in_y" class="form-label mb-1 small fw-bold">Parte Imaginaria <i>y</i> (Reactancia <i>X</i>):</label>
      <div class="input-group">
        <span class="input-group-text bg-light fw-bold text-success">+<i>j</i> Im (y)</span>
        <input id="lab3_in_y" type="number" class="form-control" value="4" step="0.5" oninput="lab3_calcRec2Pol()">
      </div>
      <input id="lab3_slider_y" type="range" class="form-range mt-1" min="-20" max="20" step="0.5" value="4" oninput="lab3_syncSlider('y')">
    </div>
  </div>

  <!-- Panel de Entradas: Polar a Rectangular -->
  <div id="lab3_panel_pol2rec" class="row g-3 align-items-end mb-3" style="display: none;">
    <div class="col-md-6">
      <label for="lab3_in_r" class="form-label mb-1 small fw-bold">Magnitud o Módulo <i>r</i> (|<b>Z</b>| o |<b>V</b>|):</label>
      <div class="input-group">
        <span class="input-group-text bg-light fw-bold text-primary">|r|</span>
        <input id="lab3_in_r" type="number" class="form-control" value="5" min="0" step="0.5" oninput="lab3_calcPol2Rec()">
      </div>
      <input id="lab3_slider_r" type="range" class="form-range mt-1" min="0" max="25" step="0.5" value="5" oninput="lab3_syncSlider('r')">
    </div>

    <div class="col-md-6">
      <label for="lab3_in_theta" class="form-label mb-1 small fw-bold">Ángulo de Fase <i>&theta;</i> (Grados &deg;):</label>
      <div class="input-group">
        <span class="input-group-text bg-light fw-bold text-warning">&ang; &theta;</span>
        <input id="lab3_in_theta" type="number" class="form-control" value="53.13" step="1" oninput="lab3_calcPol2Rec()">
        <span class="input-group-text bg-light">&deg;</span>
      </div>
      <input id="lab3_slider_theta" type="range" class="form-range mt-1" min="-180" max="180" step="1" value="53" oninput="lab3_syncSlider('theta')">
    </div>
  </div>

  <!-- Resultados y Gráfico del Plano Fasorial -->
  <div class="row g-3 align-items-stretch">
    <!-- Tarjeta de Resultados Analíticos -->
    <div class="col-lg-5">
      <div id="lab3_results_card" class="card p-3 border-0 bg-light h-100 shadow-sm" style="border-left: 4px solid #0284c7 !important;">
        <!-- Dinámicamente llenado por JS -->
      </div>
    </div>

    <!-- Plano de Gauss (Canvas) -->
    <div class="col-lg-7">
      <div class="p-3 bg-white rounded-3 border shadow-sm h-100 d-flex flex-column justify-content-center align-items-center">
        <div class="d-flex justify-content-between align-items-center w-100 mb-2 px-1">
          <span class="badge bg-secondary"><i class="bi bi-grid-3x3 me-1"></i> Plano Complejo (Gauss)</span>
          <span id="lab3_badge_cuadrante" class="badge bg-primary">Cuadrante I</span>
        </div>
        <div class="d-flex justify-content-center w-100">
          <canvas id="lab3_canvas" width="460" height="320" style="max-width: 100%; height: auto; border-radius: 8px; background: #fafafa;"></canvas>
        </div>
        <div class="text-center small text-muted mt-2">
          Vector fasorial en azul, proyecciones ortogonales punteadas y arco de fase en naranja.
        </div>
      </div>
    </div>
  </div>

</div>

<script>
(function() {
  let lab3_mode = 'rec2pol';

  window.lab3_setMode = function(mode) {
    lab3_mode = mode;
    const btnRec = document.getElementById('lab3_tab_rec2pol');
    const btnPol = document.getElementById('lab3_tab_pol2rec');
    const panelRec = document.getElementById('lab3_panel_rec2pol');
    const panelPol = document.getElementById('lab3_panel_pol2rec');

    if (!btnRec || !btnPol || !panelRec || !panelPol) return;

    if (mode === 'rec2pol') {
      btnRec.classList.add('active');
      btnPol.classList.remove('active');
      panelRec.style.display = 'flex';
      panelPol.style.display = 'none';
      lab3_calcRec2Pol();
    } else {
      btnPol.classList.add('active');
      btnRec.classList.remove('active');
      panelRec.style.display = 'none';
      panelPol.style.display = 'flex';
      lab3_calcPol2Rec();
    }
  };

  window.lab3_loadPreset = function(x, y) {
    const elX = document.getElementById('lab3_in_x');
    const elY = document.getElementById('lab3_in_y');
    const slX = document.getElementById('lab3_slider_x');
    const slY = document.getElementById('lab3_slider_y');
    if (elX) elX.value = x;
    if (elY) elY.value = y;
    if (slX) slX.value = x;
    if (slY) slY.value = y;
    lab3_setMode('rec2pol');
  };

  window.lab3_syncSlider = function(param) {
    if (param === 'x') {
      const sl = document.getElementById('lab3_slider_x');
      const inp = document.getElementById('lab3_in_x');
      if (sl && inp) { inp.value = sl.value; lab3_calcRec2Pol(); }
    } else if (param === 'y') {
      const sl = document.getElementById('lab3_slider_y');
      const inp = document.getElementById('lab3_in_y');
      if (sl && inp) { inp.value = sl.value; lab3_calcRec2Pol(); }
    } else if (param === 'r') {
      const sl = document.getElementById('lab3_slider_r');
      const inp = document.getElementById('lab3_in_r');
      if (sl && inp) { inp.value = sl.value; lab3_calcPol2Rec(); }
    } else if (param === 'theta') {
      const sl = document.getElementById('lab3_slider_theta');
      const inp = document.getElementById('lab3_in_theta');
      if (sl && inp) { inp.value = sl.value; lab3_calcPol2Rec(); }
    }
  };

  window.lab3_calcRec2Pol = function() {
    const elX = document.getElementById('lab3_in_x');
    const elY = document.getElementById('lab3_in_y');
    if (!elX || !elY) return;

    const x = parseFloat(elX.value) || 0;
    const y = parseFloat(elY.value) || 0;

    const slX = document.getElementById('lab3_slider_x');
    const slY = document.getElementById('lab3_slider_y');
    if (slX) slX.value = x;
    if (slY) slY.value = y;

    const r = Math.hypot(x, y);
    let theta = Math.atan2(y, x) * 180 / Math.PI;
    if (Math.abs(theta) < 1e-10) theta = 0;

    // Sincronizar inputs polares
    const inR = document.getElementById('lab3_in_r');
    const inTh = document.getElementById('lab3_in_theta');
    const slR = document.getElementById('lab3_slider_r');
    const slTh = document.getElementById('lab3_slider_theta');
    if (inR) inR.value = r.toFixed(2);
    if (inTh) inTh.value = theta.toFixed(2);
    if (slR) slR.value = r.toFixed(2);
    if (slTh) slTh.value = Math.round(theta);

    lab3_updateView(x, y, r, theta, 'rec2pol');
  };

  window.lab3_calcPol2Rec = function() {
    const inR = document.getElementById('lab3_in_r');
    const inTh = document.getElementById('lab3_in_theta');
    if (!inR || !inTh) return;

    const r = Math.max(0, parseFloat(inR.value) || 0);
    let theta = parseFloat(inTh.value) || 0;

    const slR = document.getElementById('lab3_slider_r');
    const slTh = document.getElementById('lab3_slider_theta');
    if (slR) slR.value = r;
    if (slTh) slTh.value = theta;

    const rad = theta * Math.PI / 180;
    const x = r * Math.cos(rad);
    const y = r * Math.sin(rad);

    // Sincronizar inputs rectangulares
    const elX = document.getElementById('lab3_in_x');
    const elY = document.getElementById('lab3_in_y');
    const slX = document.getElementById('lab3_slider_x');
    const slY = document.getElementById('lab3_slider_y');
    if (elX) elX.value = x.toFixed(2);
    if (elY) elY.value = y.toFixed(2);
    if (slX) slX.value = x.toFixed(2);
    if (slY) slY.value = y.toFixed(2);

    lab3_updateView(x, y, r, theta, 'pol2rec');
  };

  function lab3_updateView(x, y, r, theta, origin) {
    let cuadrante = "Sobre el eje";
    let tipoFisico = "Resistivo puro (FP = 1.0)";
    let badgeColor = "bg-primary";

    if (x > 0 && y > 0) {
      cuadrante = "Cuadrante I (0° < θ < 90°)";
      tipoFisico = "Inductivo (La tensión adelanta a la corriente)";
      badgeColor = "bg-primary";
    } else if (x < 0 && y > 0) {
      cuadrante = "Cuadrante II (90° < θ < 180°)";
      tipoFisico = "Generador activo en adelanto (R < 0)";
      badgeColor = "bg-warning text-dark";
    } else if (x < 0 && y < 0) {
      cuadrante = "Cuadrante III (-180° < θ < -90°)";
      tipoFisico = "Generador activo en atraso (Potencia inversa)";
      badgeColor = "bg-danger";
    } else if (x > 0 && y < 0) {
      cuadrante = "Cuadrante IV (-90° < θ < 0°)";
      tipoFisico = "Capacitivo (La corriente adelanta a la tensión)";
      badgeColor = "bg-info text-dark";
    } else if (Math.abs(y) < 1e-5 && x !== 0) {
      cuadrante = x > 0 ? "Eje Real Positivo (θ = 0°)" : "Eje Real Negativo (θ = 180°)";
      tipoFisico = "Resistivo Puro (En fase)";
      badgeColor = "bg-secondary";
    } else if (Math.abs(x) < 1e-5 && y !== 0) {
      cuadrante = y > 0 ? "Eje Imaginario Positivo (θ = +90°)" : "Eje Imaginario Negativo (θ = -90°)";
      tipoFisico = y > 0 ? "Inductivo Puro (θ = +90°)" : "Capacitivo Puro (θ = -90°)";
      badgeColor = y > 0 ? "bg-primary" : "bg-info text-dark";
    }

    const badgeCuad = document.getElementById("lab3_badge_cuadrante");
    if (badgeCuad) {
      badgeCuad.className = `badge ${badgeColor}`;
      badgeCuad.textContent = cuadrante.split("(")[0].trim();
    }

    const signo = y >= 0 ? "+" : "&minus;";
    const yi = Math.abs(y);

    const resCard = document.getElementById("lab3_results_card");
    if (resCard) {
      let pasosHtml = "";
      if (origin === 'rec2pol') {
        pasosHtml = `
          <div class="small text-muted mb-2">
            <strong>Procedimiento analítico:</strong><br>
            • Módulo: <code>r = &radic;(${x.toFixed(2)}&sup2; + ${y.toFixed(2)}&sup2;) = ${r.toFixed(4)}</code><br>
            • Ángulo: <code>&theta; = atan2(${y.toFixed(2)}, ${x.toFixed(2)}) = ${theta.toFixed(2)}&deg;</code>
          </div>
        `;
      } else {
        pasosHtml = `
          <div class="small text-muted mb-2">
            <strong>Procedimiento analítico:</strong><br>
            • Parte Real: <code>x = ${r.toFixed(2)} &middot; cos(${theta.toFixed(2)}&deg;) = ${x.toFixed(4)}</code><br>
            • Parte Imag: <code>y = ${r.toFixed(2)} &middot; sin(${theta.toFixed(2)}&deg;) = ${y.toFixed(4)}</code>
          </div>
        `;
      }

      resCard.innerHTML = `
        <h6 class="text-primary mb-3 fw-bold d-flex align-items-center">
          <i class="bi bi-check2-circle me-2"></i> Resultados de Transformación
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
          <i class="bi bi-lightning-charge text-primary me-1"></i> <strong>Comportamiento:</strong> ${tipoFisico}
        </div>
      `;
    }

    lab3_drawCanvas(x, y, r, theta);
  }

  function lab3_drawCanvas(x, y, r, theta) {
    const canvas = document.getElementById("lab3_canvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const w = canvas.width;
    const h = canvas.height;
    const cx = w / 2;
    const cy = h / 2;

    ctx.clearRect(0, 0, w, h);

    const maxVal = Math.max(Math.abs(x), Math.abs(y), 1);
    const scale = (Math.min(w, h) / 2 - 40) / maxVal;

    // 1. Rejilla
    ctx.strokeStyle = "#f1f5f9";
    ctx.lineWidth = 1;
    const gridStep = Math.max(scale, 20);
    for (let px = cx % gridStep; px < w; px += gridStep) {
      ctx.beginPath(); ctx.moveTo(px, 0); ctx.lineTo(px, h); ctx.stroke();
    }
    for (let py = cy % gridStep; py < h; py += gridStep) {
      ctx.beginPath(); ctx.moveTo(0, py); ctx.lineTo(w, py); ctx.stroke();
    }

    // Círculo guía
    if (r > 1e-4) {
      ctx.beginPath();
      ctx.arc(cx, cy, r * scale, 0, 2 * Math.PI);
      ctx.strokeStyle = "#e2e8f0";
      ctx.setLineDash([3, 3]);
      ctx.stroke();
      ctx.setLineDash([]);
    }

    // 2. Ejes coordenados
    ctx.strokeStyle = "#94a3b8";
    ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.moveTo(15, cy); ctx.lineTo(w - 15, cy); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(cx, h - 15); ctx.lineTo(cx, 15); ctx.stroke();

    // Textos de ejes
    ctx.fillStyle = "#64748b";
    ctx.font = "bold 11px monospace";
    ctx.fillText("Re (+)", w - 46, cy - 8);
    ctx.fillText("+j Im", cx + 8, 20);
    ctx.fillText("-j Im", cx + 8, h - 8);
    ctx.fillText("Re (-)", 6, cy - 8);

    if (r > 1e-4) {
      const vx = cx + x * scale;
      const vy = cy - y * scale;

      // 3. Proyecciones punteadas
      ctx.strokeStyle = "#93c5fd";
      ctx.lineWidth = 1.2;
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(vx, cy); ctx.lineTo(vx, vy); ctx.lineTo(cx, vy);
      ctx.stroke();
      ctx.setLineDash([]);

      // 4. Arco del ángulo
      const arcRadius = Math.min(36, Math.max(16, r * scale * 0.45));
      ctx.strokeStyle = "#f59e0b";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      const endAngle = -theta * Math.PI / 180;
      ctx.arc(cx, cy, arcRadius, 0, endAngle, theta > 0);
      ctx.stroke();

      // Etiqueta del ángulo
      ctx.fillStyle = "#d97706";
      ctx.font = "bold 11px sans-serif";
      const midAngle = (-theta * Math.PI / 180) / 2;
      const tx = cx + (arcRadius + 16) * Math.cos(midAngle);
      const ty = cy + (arcRadius + 16) * Math.sin(midAngle);
      ctx.fillText(`${theta.toFixed(1)}°`, tx - 10, ty + 4);

      // 5. Vector Fasorial (Azul)
      ctx.strokeStyle = "#0284c7";
      ctx.fillStyle = "#0284c7";
      ctx.lineWidth = 3.5;

      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.lineTo(vx, vy);
      ctx.stroke();

      // Cabeza de flecha
      const headLen = 12;
      const angleRad = Math.atan2(-y, x);
      ctx.beginPath();
      ctx.moveTo(vx, vy);
      ctx.lineTo(vx - headLen * Math.cos(angleRad - Math.PI / 6), vy - headLen * Math.sin(angleRad - Math.PI / 6));
      ctx.lineTo(vx - headLen * Math.cos(angleRad + Math.PI / 6), vy - headLen * Math.sin(angleRad + Math.PI / 6));
      ctx.closePath();
      ctx.fill();

      // Puntos
      ctx.fillStyle = "#0f172a";
      ctx.beginPath(); ctx.arc(cx, cy, 3.5, 0, 2 * Math.PI); ctx.fill();
      ctx.fillStyle = "#0284c7";
      ctx.beginPath(); ctx.arc(vx, vy, 4, 0, 2 * Math.PI); ctx.fill();
    }
  }

  // Inicialización
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function() { lab3_calcRec2Pol(); });
  } else {
    setTimeout(function() { lab3_calcRec2Pol(); }, 50);
  }
})();
</script>
```

:::
