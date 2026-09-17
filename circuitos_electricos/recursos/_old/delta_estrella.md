# Herramienta interactiva: Conversión Delta ↔ Estrella

::: {.card-module}
### 🔺🔻 Conversor Bidireccional Delta ↔ Estrella (Impedancias Complejas) {.unnumbered}

```{=html}
<ul class="nav nav-pills mb-3 justify-content-center" id="deTab">
  <li class="nav-item"><button class="nav-link active px-3 py-2 fw-bold" data-dir="d2y" onclick="setDireccion('d2y')">Delta &rarr; Estrella</button></li>
  <li class="nav-item"><button class="nav-link px-3 py-2 fw-bold" data-dir="y2d" onclick="setDireccion('y2d')">Estrella &rarr; Delta</button></li>
</ul>

<div id="panelD2Y" style="display:flex; flex-wrap:wrap; gap:0.75rem;">
  <div style="flex:1 1 220px;" class="p-2 rounded-3 border" style="border-left:4px solid #0284c7;">
    <label class="small fw-bold" style="color:#0284c7;">Z<sub>A</sub> (&Omega;) — opuesta al nodo 1</label>
    <div class="input-group input-group-sm">
      <input type="number" id="deZA_r" class="form-control" value="0" step="0.5" oninput="calcularDE()">
      <span class="input-group-text">+j</span>
      <input type="number" id="deZA_i" class="form-control" value="-4" step="0.5" oninput="calcularDE()">
    </div>
  </div>
  <div style="flex:1 1 220px;" class="p-2 rounded-3 border" style="border-left:4px solid #f59e0b;">
    <label class="small fw-bold" style="color:#d97706;">Z<sub>B</sub> (&Omega;) — opuesta al nodo 2</label>
    <div class="input-group input-group-sm">
      <input type="number" id="deZB_r" class="form-control" value="0" step="0.5" oninput="calcularDE()">
      <span class="input-group-text">+j</span>
      <input type="number" id="deZB_i" class="form-control" value="-4" step="0.5" oninput="calcularDE()">
    </div>
  </div>
  <div style="flex:1 1 220px;" class="p-2 rounded-3 border" style="border-left:4px solid #10b981;">
    <label class="small fw-bold" style="color:#059669;">Z<sub>C</sub> (&Omega;) — opuesta al nodo 3</label>
    <div class="input-group input-group-sm">
      <input type="number" id="deZC_r" class="form-control" value="3" step="0.5" oninput="calcularDE()">
      <span class="input-group-text">+j</span>
      <input type="number" id="deZC_i" class="form-control" value="4" step="0.5" oninput="calcularDE()">
    </div>
  </div>
</div>

<div id="panelY2D" style="display:none; flex-wrap:wrap; gap:0.75rem;">
  <div style="flex:1 1 220px;" class="p-2 rounded-3 border" style="border-left:4px solid #0284c7;">
    <label class="small fw-bold" style="color:#0284c7;">Z<sub>1</sub> (&Omega;) — rama al nodo 1</label>
    <div class="input-group input-group-sm">
      <input type="number" id="deZ1_r" class="form-control" value="1.6" step="0.1" oninput="calcularDE()">
      <span class="input-group-text">+j</span>
      <input type="number" id="deZ1_i" class="form-control" value="0" step="0.1" oninput="calcularDE()">
    </div>
  </div>
  <div style="flex:1 1 220px;" class="p-2 rounded-3 border" style="border-left:4px solid #f59e0b;">
    <label class="small fw-bold" style="color:#d97706;">Z<sub>2</sub> (&Omega;) — rama al nodo 2</label>
    <div class="input-group input-group-sm">
      <input type="number" id="deZ2_r" class="form-control" value="1.6" step="0.1" oninput="calcularDE()">
      <span class="input-group-text">+j</span>
      <input type="number" id="deZ2_i" class="form-control" value="0" step="0.1" oninput="calcularDE()">
    </div>
  </div>
  <div style="flex:1 1 220px;" class="p-2 rounded-3 border" style="border-left:4px solid #10b981;">
    <label class="small fw-bold" style="color:#059669;">Z<sub>3</sub> (&Omega;) — rama al nodo 3</label>
    <div class="input-group input-group-sm">
      <input type="number" id="deZ3_r" class="form-control" value="0" step="0.1" oninput="calcularDE()">
      <span class="input-group-text">+j</span>
      <input type="number" id="deZ3_i" class="form-control" value="1.6" step="0.1" oninput="calcularDE()">
    </div>
  </div>
</div>

<div style="display:flex; flex-wrap:wrap; gap:1rem; margin-top:1.25rem; align-items:stretch;">
  <div style="flex:1 1 420px;">
    <div id="deResultado" class="h-100"></div>
  </div>
  <div style="flex:1 1 420px; display:flex; gap:0.5rem; justify-content:center; align-items:center; flex-wrap:wrap;">
    <div class="text-center p-2 bg-white rounded-3 border shadow-sm">
      <div class="small fw-bold text-muted mb-1">Delta (&Delta;)</div>
      <svg id="svgDelta" width="220" height="200" viewBox="0 0 220 200"></svg>
    </div>
    <div class="text-center p-2 bg-white rounded-3 border shadow-sm">
      <div class="small fw-bold text-muted mb-1">Estrella (Y)</div>
      <svg id="svgEstrella" width="220" height="200" viewBox="0 0 220 200"></svg>
    </div>
  </div>
</div>

<script>
const CZ = {
  add: (a, b) => ({ r: a.r + b.r, i: a.i + b.i }),
  mul: (a, b) => ({ r: a.r * b.r - a.i * b.i, i: a.r * b.i + a.i * b.r }),
  div: (a, b) => { const d = b.r * b.r + b.i * b.i; return { r: (a.r * b.r + a.i * b.i) / d, i: (a.i * b.r - a.r * b.i) / d }; },
  polar: (c) => ({ mag: Math.hypot(c.r, c.i), ang: Math.atan2(c.i, c.r) * 180 / Math.PI }),
  fmt: (c) => {
    const p = CZ.polar(c);
    const signo = c.i >= 0 ? '+' : '−';
    return `${p.mag.toFixed(3)}&ang;${p.ang.toFixed(2)}&deg; &Omega;  <span class="text-muted small">(${c.r.toFixed(3)} ${signo} j${Math.abs(c.i).toFixed(3)})</span>`;
  }
};

let deDireccion = 'd2y';

function setDireccion(dir) {
  deDireccion = dir;
  document.querySelectorAll('#deTab .nav-link').forEach(b => b.classList.toggle('active', b.dataset.dir === dir));
  document.getElementById('panelD2Y').style.display = dir === 'd2y' ? 'flex' : 'none';
  document.getElementById('panelY2D').style.display = dir === 'y2d' ? 'flex' : 'none';
  calcularDE();
}

function leer(id) {
  return { r: Number(document.getElementById(id + '_r').value) || 0, i: Number(document.getElementById(id + '_i').value) || 0 };
}

function dibujarSVGs(ZA, ZB, ZC, Z1, Z2, Z3) {
  const fmtCorto = (c) => {
    const p = CZ.polar(c);
    return `${p.mag.toFixed(2)}&ang;${p.ang.toFixed(0)}&deg;`;
  };

  // Triangulo Delta: nodos 1 (arriba), 2 (abajo-izq), 3 (abajo-der)
  const n1 = { x: 110, y: 25 }, n2 = { x: 25, y: 165 }, n3 = { x: 195, y: 165 };
  const svgD = document.getElementById('svgDelta');
  svgD.innerHTML = `
    <line x1="${n2.x}" y1="${n2.y}" x2="${n3.x}" y2="${n3.y}" stroke="#0284c7" stroke-width="2.5"/>
    <line x1="${n3.x}" y1="${n3.y}" x2="${n1.x}" y2="${n1.y}" stroke="#d97706" stroke-width="2.5"/>
    <line x1="${n1.x}" y1="${n1.y}" x2="${n2.x}" y2="${n2.y}" stroke="#059669" stroke-width="2.5"/>
    <circle cx="${n1.x}" cy="${n1.y}" r="4" fill="#0f172a"/>
    <circle cx="${n2.x}" cy="${n2.y}" r="4" fill="#0f172a"/>
    <circle cx="${n3.x}" cy="${n3.y}" r="4" fill="#0f172a"/>
    <text x="${n1.x}" y="${n1.y - 10}" font-size="11" text-anchor="middle" font-weight="bold">1</text>
    <text x="${n2.x - 12}" y="${n2.y + 14}" font-size="11" text-anchor="middle" font-weight="bold">2</text>
    <text x="${n3.x + 12}" y="${n3.y + 14}" font-size="11" text-anchor="middle" font-weight="bold">3</text>
    <text x="80" y="185" font-size="10" fill="#0284c7" font-weight="bold">Z_A ${fmtCorto(ZA)}</text>
    <text x="140" y="90" font-size="10" fill="#d97706" font-weight="bold">Z_B ${fmtCorto(ZB)}</text>
    <text x="40" y="105" font-size="10" fill="#059669" font-weight="bold">Z_C ${fmtCorto(ZC)}</text>
  `;

  // Estrella: mismos nodos 1,2,3 alrededor, centro O
  const o = { x: 110, y: 115 };
  const svgY = document.getElementById('svgEstrella');
  svgY.innerHTML = `
    <line x1="${o.x}" y1="${o.y}" x2="${n1.x}" y2="${n1.y}" stroke="#0284c7" stroke-width="2.5"/>
    <line x1="${o.x}" y1="${o.y}" x2="${n2.x}" y2="${n2.y}" stroke="#d97706" stroke-width="2.5"/>
    <line x1="${o.x}" y1="${o.y}" x2="${n3.x}" y2="${n3.y}" stroke="#059669" stroke-width="2.5"/>
    <circle cx="${o.x}" cy="${o.y}" r="3.5" fill="#0f172a"/>
    <circle cx="${n1.x}" cy="${n1.y}" r="4" fill="#0f172a"/>
    <circle cx="${n2.x}" cy="${n2.y}" r="4" fill="#0f172a"/>
    <circle cx="${n3.x}" cy="${n3.y}" r="4" fill="#0f172a"/>
    <text x="${n1.x}" y="${n1.y - 10}" font-size="11" text-anchor="middle" font-weight="bold">1</text>
    <text x="${n2.x - 12}" y="${n2.y + 14}" font-size="11" text-anchor="middle" font-weight="bold">2</text>
    <text x="${n3.x + 12}" y="${n3.y + 14}" font-size="11" text-anchor="middle" font-weight="bold">3</text>
    <text x="${(o.x + n1.x) / 2 + 6}" y="${(o.y + n1.y) / 2}" font-size="10" fill="#0284c7" font-weight="bold">Z_1 ${fmtCorto(Z1)}</text>
    <text x="${(o.x + n2.x) / 2 - 45}" y="${(o.y + n2.y) / 2}" font-size="10" fill="#d97706" font-weight="bold">Z_2 ${fmtCorto(Z2)}</text>
    <text x="${(o.x + n3.x) / 2 + 4}" y="${(o.y + n3.y) / 2}" font-size="10" fill="#059669" font-weight="bold">Z_3 ${fmtCorto(Z3)}</text>
  `;
}

function calcularDE() {
  let ZA, ZB, ZC, Z1, Z2, Z3, pasosHtml;

  if (deDireccion === 'd2y') {
    ZA = leer('deZA'); ZB = leer('deZB'); ZC = leer('deZC');
    const Zsigma = CZ.add(CZ.add(ZA, ZB), ZC);
    Z1 = CZ.div(CZ.mul(ZB, ZC), Zsigma);
    Z2 = CZ.div(CZ.mul(ZA, ZC), Zsigma);
    Z3 = CZ.div(CZ.mul(ZA, ZB), Zsigma);
    pasosHtml = `
      <div class="small text-muted mb-2">
        <strong>Z<sub>&Sigma;</sub> = Z<sub>A</sub>+Z<sub>B</sub>+Z<sub>C</sub></strong> = ${CZ.fmt(Zsigma)}<br><br>
        <strong>Z<sub>1</sub> = (Z<sub>B</sub>&middot;Z<sub>C</sub>) / Z<sub>&Sigma;</sub></strong> = ${CZ.fmt(Z1)}<br>
        <strong>Z<sub>2</sub> = (Z<sub>A</sub>&middot;Z<sub>C</sub>) / Z<sub>&Sigma;</sub></strong> = ${CZ.fmt(Z2)}<br>
        <strong>Z<sub>3</sub> = (Z<sub>A</sub>&middot;Z<sub>B</sub>) / Z<sub>&Sigma;</sub></strong> = ${CZ.fmt(Z3)}
      </div>`;
  } else {
    Z1 = leer('deZ1'); Z2 = leer('deZ2'); Z3 = leer('deZ3');
    const Zsum2 = CZ.add(CZ.add(CZ.mul(Z1, Z2), CZ.mul(Z2, Z3)), CZ.mul(Z3, Z1));
    ZA = CZ.div(Zsum2, Z1);
    ZB = CZ.div(Zsum2, Z2);
    ZC = CZ.div(Zsum2, Z3);
    pasosHtml = `
      <div class="small text-muted mb-2">
        <strong>&Sigma;<sub>2</sub> = Z<sub>1</sub>Z<sub>2</sub>+Z<sub>2</sub>Z<sub>3</sub>+Z<sub>3</sub>Z<sub>1</sub></strong> = ${CZ.fmt(Zsum2)}<br><br>
        <strong>Z<sub>A</sub> = &Sigma;<sub>2</sub> / Z<sub>1</sub></strong> = ${CZ.fmt(ZA)}<br>
        <strong>Z<sub>B</sub> = &Sigma;<sub>2</sub> / Z<sub>2</sub></strong> = ${CZ.fmt(ZB)}<br>
        <strong>Z<sub>C</sub> = &Sigma;<sub>2</sub> / Z<sub>3</sub></strong> = ${CZ.fmt(ZC)}
      </div>`;
  }

  const tituloDir = deDireccion === 'd2y' ? 'Delta &rarr; Estrella' : 'Estrella &rarr; Delta';
  document.getElementById('deResultado').innerHTML = `
    <div class="card p-3 border-0 bg-light h-100 shadow-sm" style="border-left:4px solid #8b5cf6 !important;">
      <h6 class="mb-2 fw-bold" style="color:#7c3aed;"><i class="bi bi-arrow-left-right me-2"></i>${tituloDir}</h6>
      ${pasosHtml}
    </div>`;

  dibujarSVGs(ZA, ZB, ZC, Z1, Z2, Z3);
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", calcularDE);
} else {
  setTimeout(calcularDE, 50);
}
</script>
```
:::
