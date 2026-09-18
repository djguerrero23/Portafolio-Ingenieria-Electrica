::: {.card-module}
### 🧮 Solver de redes complejas (análisis nodal) {.unnumbered}

```{=html}
<p class="small text-muted mb-2">
Escribe cada elemento como <code>nodo1 nodo2 R X</code>, donde la impedancia serie entre ambos nodos es
<em>Z = R + jX</em> (&Omega;). Una línea por elemento. Los símbolos <code>#</code> inician comentarios y los nodos
pueden nombrarse con números o letras. Varias líneas con el mismo par de nodos se interpretan como <b>ramas en paralelo</b>.
</p>

<details class="mb-3">
  <summary class="small fw-bold text-primary" style="cursor:pointer;">
    📖 Guía rápida: Sintaxis del Netlist y cómo se dibuja cada elemento
  </summary>
  <div class="border rounded-3 p-2 bg-light mt-2" style="font-size:0.83rem;">
    <div class="d-flex justify-content-between py-1 border-bottom fw-bold text-muted" style="font-size:0.78rem;">
      <span style="flex:1.1;">CASO</span>
      <span style="flex:0.9;" class="text-center">NETLIST (R + jX)</span>
      <span style="flex:1.4;" class="text-end">REPRESENTACIÓN</span>
    </div>
    <div class="d-flex justify-content-between align-items-center py-1 border-bottom">
      <span style="flex:1.1;"><strong>Solo R</strong> (Resistor)</span>
      <span style="flex:0.9;" class="text-center font-monospace"><code>1 2 3 0</code></span>
      <span style="flex:1.4;" class="text-end">Zigzag, <span class="badge bg-white text-dark border">3&Omega;</span></span>
    </div>
    <div class="d-flex justify-content-between align-items-center py-1 border-bottom">
      <span style="flex:1.1;"><strong>Solo L</strong> (Inductor)</span>
      <span style="flex:0.9;" class="text-center font-monospace"><code>1 2 0 6</code></span>
      <span style="flex:1.4;" class="text-end">Bobina, <span class="badge bg-white text-dark border">j6&Omega;</span></span>
    </div>
    <div class="d-flex justify-content-between align-items-center py-1 border-bottom">
      <span style="flex:1.1;"><strong>Solo C</strong> (Capacitor)</span>
      <span style="flex:0.9;" class="text-center font-monospace"><code>1 2 0 -6</code></span>
      <span style="flex:1.4;" class="text-end">Placas, <span class="badge bg-white text-dark border">&minus;j6&Omega;</span></span>
    </div>
    <div class="d-flex justify-content-between align-items-center py-1 border-bottom">
      <span style="flex:1.1;"><strong>R + L</strong> (Serie)</span>
      <span style="flex:0.9;" class="text-center font-monospace"><code>1 2 3 6</code></span>
      <span style="flex:1.4;" class="text-end">Zigzag + Bobina, <span class="badge bg-white text-dark border">3&Omega;</span> y <span class="badge bg-white text-dark border">j6&Omega;</span></span>
    </div>
    <div class="d-flex justify-content-between align-items-center py-1 border-bottom">
      <span style="flex:1.1;"><strong>R + C</strong> (Serie)</span>
      <span style="flex:0.9;" class="text-center font-monospace"><code>1 2 3 -6</code></span>
      <span style="flex:1.4;" class="text-end">Zigzag + Placas, <span class="badge bg-white text-dark border">3&Omega;</span> y <span class="badge bg-white text-dark border">&minus;j6&Omega;</span></span>
    </div>
    <div class="d-flex justify-content-between align-items-center py-1">
      <span style="flex:1.1;"><strong>Corto ideal</strong></span>
      <span style="flex:0.9;" class="text-center font-monospace"><code>1 2 0 0</code></span>
      <span style="flex:1.4;" class="text-end">Línea continua sin impedancia</span>
    </div>
  </div>
</details>

<div style="display:flex; flex-wrap:wrap; gap:1.25rem; margin-bottom:1rem; align-items:stretch;">

<div style="flex:0 0 240px; min-width:210px; max-width:270px;">
<label class="small fw-bold">Netlist de ramas (R + jX):</label>
<textarea id="netlist" class="form-control form-control-sm font-monospace" rows="14" spellcheck="false" oninput="resolverRed()"># Ejemplo: Red en delta
# Rama 1-2
1 2 3 6
1 2 2 3.5
# Rama 2-3
2 3 3 6
2 3 4 1
# Rama 3-1
1 3 3 6
1 3 1 2</textarea>
</div>

<div style="flex:1 1 500px; display:flex; flex-wrap:wrap; gap:0.75rem;">
  <div style="flex:1 1 300px; min-width:270px;">
    <label class="small fw-bold">🔌 Esquema con componentes (R, L, C):</label>
    <div class="border rounded-3 bg-white shadow-sm p-1">
      <svg id="svgComponentes" width="100%" height="380" viewBox="0 0 560 430" preserveAspectRatio="xMidYMid meet" style="background:#ffffff; border-radius:6px;"></svg>
    </div>
    <p class="small text-muted mt-1 mb-0">
      <b>R</b> = zigzag · <b>L</b> = bobina · <b>C</b> = placas paralelas.
    </p>
  </div>
  <div style="flex:1 1 300px; min-width:270px;">
    <label class="small fw-bold">📐 Esquema con impedancias equivalentes:</label>
    <div class="border rounded-3 bg-white shadow-sm p-1">
      <svg id="svgImpedancias" width="100%" height="380" viewBox="0 0 560 430" preserveAspectRatio="xMidYMid meet" style="background:#ffffff; border-radius:6px;"></svg>
    </div>
    <p class="small text-muted mt-1 mb-0">
      Cada rama muestra su Z = R + jX en forma compacta.
    </p>
  </div>
</div>
</div>

<div class="d-flex flex-wrap gap-2 align-items-end mb-3 mt-2">
<div>
<label class="small fw-bold">Terminal A (+):</label>
<input id="termA" class="form-control form-control-sm" style="width:90px" value="1" oninput="resolverRed()">
</div>
<div>
<label class="small fw-bold">Terminal B (−):</label>
<input id="termB" class="form-control form-control-sm" style="width:90px" value="2" oninput="resolverRed()">
</div>
<button class="btn btn-sm btn-primary fw-bold px-3" onclick="resolverRed()">⚡ Calcular Z<sub>T</sub></button>
<button class="btn btn-sm btn-outline-secondary" onclick="cargarEjemploDeltaEstrella()">Red Delta (Ejemplo)</button>
<button class="btn btn-sm btn-outline-secondary" onclick="cargarEjemploEstrellaDelta()">Red Estrella (Ejemplo)</button>
</div>

<div id="resultadoRed"></div>

<script>
/* =====================================================================
   1) Álgebra compleja
   ===================================================================== */
var CZ = window.CZ || {
  add: (a, b) => ({ r: a.r + b.r, i: a.i + b.i }),
  mul: (a, b) => ({ r: a.r * b.r - a.i * b.i, i: a.r * b.i + a.i * b.r }),
  div: (a, b) => { const d = b.r * b.r + b.i * b.i; return { r: (a.r * b.r + a.i * b.i) / d, i: (a.i * b.r - a.r * b.i) / d }; },
  polar: (c) => ({ mag: Math.hypot(c.r, c.i), ang: Math.atan2(c.i, c.r) * 180 / Math.PI }),
  fmt: (c) => {
    const p = CZ.polar(c);
    const signo = c.i >= 0 ? '+' : '−';
    return `<b>${p.mag.toFixed(3)}&ang;${p.ang.toFixed(2)}&deg; &Omega;</b> <span class="text-muted small">(${c.r.toFixed(3)} ${signo} j${Math.abs(c.i).toFixed(3)})</span>`;
  }
};
window.CZ = CZ;

function fmtCorto(c) {
  const r = Math.abs(c.r) < 1e-9 ? 0 : c.r;
  const i = Math.abs(c.i) < 1e-9 ? 0 : c.i;
  if (i === 0) return `${r.toFixed(3)}`;
  if (r === 0) return `j${i.toFixed(3)}`;
  return `${r.toFixed(3)}${i >= 0 ? '+' : '−'}j${Math.abs(i).toFixed(3)}`;
}

/* =====================================================================
   2) Solver lineal complejo
   ===================================================================== */
function solveComplex(A, b) {
  const n = A.length;
  const M = A.map(row => row.map(v => ({ r: v.r, i: v.i })));
  const x = b.map(v => ({ r: v.r, i: v.i }));
  for (let k = 0; k < n; k++) {
    let p = k, maxMag = CZ.polar(M[k][k]).mag;
    for (let i = k + 1; i < n; i++) {
      const m = CZ.polar(M[i][k]).mag;
      if (m > maxMag) { maxMag = m; p = i; }
    }
    if (maxMag < 1e-12) throw new Error('Matriz singular (¿nodos aislados o ramas nulas?)');
    if (p !== k) {
      [M[k], M[p]] = [M[p], M[k]];
      [x[k], x[p]] = [x[p], x[k]];
    }
    const piv = M[k][k];
    for (let i = k + 1; i < n; i++) {
      const f = CZ.div(M[i][k], piv);
      const nf = { r: -f.r, i: -f.i };
      for (let j = k; j < n; j++) M[i][j] = CZ.add(M[i][j], CZ.mul(nf, M[k][j]));
      x[i] = CZ.add(x[i], CZ.mul(nf, x[k]));
    }
  }
  for (let i = n - 1; i >= 0; i--) {
    let s = { r: 0, i: 0 };
    for (let j = i + 1; j < n; j++) s = CZ.add(s, CZ.mul(M[i][j], x[j]));
    x[i] = CZ.div(CZ.add(x[i], { r: -s.r, i: -s.i }), M[i][i]);
  }
  return x;
}

/* =====================================================================
   3) Parser del netlist + agrupador de paralelos
   ===================================================================== */
function parseNetlist(texto) {
  const elementos = [];
  const nodosSet = new Set();
  for (let linea of texto.split(/\r?\n/)) {
    linea = linea.replace(/#.*$/, '').trim();
    if (!linea) continue;
    const p = linea.split(/[\s,;]+/);
    if (p.length < 4) continue;
    const a = String(p[0]).trim(), b = String(p[1]).trim();
    const R = Number(p[2]), X = Number(p[3]);
    if (!isFinite(R) || !isFinite(X) || a === b) continue;
    elementos.push({ a, b, Z: { r: R, i: X } });
    nodosSet.add(a); nodosSet.add(b);
  }
  return { elementos, nodos: [...nodosSet] };
}

function agruparParalelos(elementos) {
  const grupos = {};
  elementos.forEach(el => {
    const key = [el.a, el.b].sort().join('||');
    (grupos[key] = grupos[key] || []).push(el);
  });
  return grupos;
}

function equivalenteParalelo(els) {
  let ysum = { r: 0, i: 0 };
  els.forEach(el => { ysum = CZ.add(ysum, CZ.div({ r: 1, i: 0 }, el.Z)); });
  return CZ.div({ r: 1, i: 0 }, ysum);
}

/* =====================================================================
   4) Detección de nodos flotantes
   ===================================================================== */
function detectarFlotantes(elementos, nodos, B) {
  const adj = {};
  nodos.forEach(n => adj[n] = []);
  elementos.forEach(el => { adj[el.a].push(el.b); adj[el.b].push(el.a); });
  const visited = new Set([B]);
  const queue = [B];
  while (queue.length) {
    const n = queue.shift();
    for (const m of adj[n]) if (!visited.has(m)) { visited.add(m); queue.push(m); }
  }
  return nodos.filter(n => !visited.has(n));
}

/* =====================================================================
   5) Layout de nodos
   ===================================================================== */
function calcularPosiciones(nodos, elementos, W, H) {
  const nSet = new Set(nodos.map(String));
  const pos = {};

  if (nSet.size === 3 && nSet.has('1') && nSet.has('2') && nSet.has('3')) {
    pos['2'] = { x: W * 0.50, y: 50 };
    pos['1'] = { x: W * 0.14, y: 335 };
    pos['3'] = { x: W * 0.86, y: 335 };
    return pos;
  }
  if (nSet.size === 4 && nSet.has('1') && nSet.has('2') && nSet.has('3')) {
    const neutro = nodos.find(n => !['1', '2', '3'].includes(String(n)));
    pos['2'] = { x: W * 0.50, y: 50 };
    pos['1'] = { x: W * 0.14, y: 335 };
    pos['3'] = { x: W * 0.86, y: 335 };
    pos[neutro] = { x: W * 0.50, y: 240 };
    return pos;
  }
  nodos.forEach((n, i) => {
    const ang = (2 * Math.PI * i) / nodos.length - Math.PI / 2;
    pos[n] = { x: W / 2 + Math.min(W, H) * 0.40 * Math.cos(ang),
               y: H / 2 + Math.min(W, H) * 0.40 * Math.sin(ang) };
  });
  return pos;
}

/* =====================================================================
   6) Símbolos SVG de componentes (R, L, C)
   ===================================================================== */
function svgResistor(cx, cy, deg, largo) {
  const h = 7;
  const n = 6;
  const seg = largo / n;
  const start = -largo / 2;
  const pts = [`${start.toFixed(1)},0`];
  for (let i = 0; i < n; i++) {
    const x = start + seg * (i + 0.5);
    const y = i % 2 === 0 ? -h : h;
    pts.push(`${x.toFixed(1)},${y}`);
  }
  pts.push(`${(largo / 2).toFixed(1)},0`);
  return `<g transform="translate(${cx.toFixed(1)},${cy.toFixed(1)}) rotate(${deg.toFixed(1)})">
    <polyline points="${pts.join(' ')}" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
  </g>`;
}

function svgInductor(cx, cy, deg, largo) {
  const n = 4;
  const r = largo / (2 * n);
  let d = `M ${(-largo / 2).toFixed(1)} 0`;
  for (let i = 0; i < n; i++) {
    d += ` a ${r.toFixed(1)} ${r.toFixed(1)} 0 0 1 ${(2 * r).toFixed(1)} 0`;
  }
  return `<g transform="translate(${cx.toFixed(1)},${cy.toFixed(1)}) rotate(${deg.toFixed(1)})">
    <path d="${d}" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round"/>
  </g>`;
}

function svgCapacitor(cx, cy, deg, largo) {
  const gap = 4;
  const plateH = 16;
  const lead = Math.max(4, (largo / 2) - gap);
  return `<g transform="translate(${cx.toFixed(1)},${cy.toFixed(1)}) rotate(${deg.toFixed(1)})">
    <line x1="${-lead.toFixed(1)}" y1="0" x2="${-gap.toFixed(1)}" y2="0" stroke="#0f172a" stroke-width="2.2"/>
    <line x1="${gap.toFixed(1)}" y1="0" x2="${lead.toFixed(1)}" y2="0" stroke="#0f172a" stroke-width="2.2"/>
    <line x1="${-gap.toFixed(1)}" y1="${(-plateH / 2).toFixed(1)}" x2="${-gap.toFixed(1)}" y2="${(plateH / 2).toFixed(1)}" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round"/>
    <line x1="${gap.toFixed(1)}" y1="${(-plateH / 2).toFixed(1)}" x2="${gap.toFixed(1)}" y2="${(plateH / 2).toFixed(1)}" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round"/>
  </g>`;
}

function labelBox(x, y, texto) {
  const clean = texto.replace(/&[^;]+;/g, 'x');
  const w = Math.max(24, clean.length * 6.2 + 8);
  return `<g transform="translate(${x.toFixed(1)},${y.toFixed(1)})">
    <rect x="${(-w / 2).toFixed(1)}" y="-8.5" width="${w.toFixed(1)}" height="17" rx="3.5"
          fill="#ffffff" stroke="#94a3b8" stroke-width="0.85" filter="drop-shadow(0 1px 2px rgba(0,0,0,0.06))"/>
    <text x="0" y="3.5" font-size="9" font-family="'JetBrains Mono', monospace"
          font-weight="700" fill="#0f172a" text-anchor="middle">${texto}</text>
  </g>`;
}

/* =====================================================================
   7) Rama con símbolos R/L/C sobre un segmento recto
   ===================================================================== */
function dibujarRamaSimbolos(p1, p2, Z, escala, labelSide, normalVec) {
  escala = escala || 1;
  if (labelSide === undefined || labelSide === 0) labelSide = 1;

  const dx = p2.x - p1.x, dy = p2.y - p1.y;
  const L = Math.hypot(dx, dy) || 1;
  const ux = dx / L, uy = dy / L;
  
  // Usar el vector normal exterior garantizado
  const nx = (normalVec && isFinite(normalVec.x)) ? normalVec.x : -uy;
  const ny = (normalVec && isFinite(normalVec.y)) ? normalVec.y : ux;

  let deg = Math.atan2(dy, dx) * 180 / Math.PI;
  if (deg > 90 || deg < -90) deg += 180;

  const R = Z.r, X = Z.i;
  const tieneR = R !== 0, tieneX = X !== 0;

  if (!tieneR && !tieneX) {
    return `<line x1="${p1.x.toFixed(1)}" y1="${p1.y.toFixed(1)}" x2="${p2.x.toFixed(1)}" y2="${p2.y.toFixed(1)}" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round"/>`;
  }

  const rLen = tieneR ? Math.min(38 * escala, L * 0.35) : 0;
  const xLen = tieneX ? (Math.abs(X) > 0 && X < 0 ? Math.min(28 * escala, L * 0.30) : Math.min(34 * escala, L * 0.34)) : 0;
  const gapInter = (tieneR && tieneX) ? Math.max(16, 22 * escala) : 0;
  const totalSym = rLen + xLen + gapInter;
  const startD = Math.max(4, (L - totalSym) / 2);

  let html = '';
  // Cable inicial hasta el primer símbolo
  html += `<line x1="${p1.x.toFixed(1)}" y1="${p1.y.toFixed(1)}" x2="${(p1.x + ux * startD).toFixed(1)}" y2="${(p1.y + uy * startD).toFixed(1)}" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round"/>`;

  const nlx = nx * labelSide, nly = ny * labelSide;
  const lblOffset = Math.max(15, 17 * escala);

  let cursor = startD;
  if (tieneR) {
    const cx = p1.x + ux * (cursor + rLen / 2);
    const cy = p1.y + uy * (cursor + rLen / 2);
    html += svgResistor(cx, cy, deg, rLen);
    html += labelBox(cx + nlx * lblOffset, cy + nly * lblOffset, `${Number(R.toFixed(2))}&Omega;`);
    cursor += rLen;
  }
  if (tieneR && tieneX) {
    // Tramo de cable intermedio entre R y X
    html += `<line x1="${(p1.x + ux * cursor).toFixed(1)}" y1="${(p1.y + uy * cursor).toFixed(1)}" x2="${(p1.x + ux * (cursor + gapInter)).toFixed(1)}" y2="${(p1.y + uy * (cursor + gapInter)).toFixed(1)}" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round"/>`;
    cursor += gapInter;
  }
  if (tieneX) {
    const cx = p1.x + ux * (cursor + xLen / 2);
    const cy = p1.y + uy * (cursor + xLen / 2);
    if (X > 0) html += svgInductor(cx, cy, deg, xLen);
    else html += svgCapacitor(cx, cy, deg, xLen);
    const etiq = X > 0
      ? `j${Number(X.toFixed(2))}&Omega;`
      : `&minus;j${Math.abs(Number(X.toFixed(2)))}&Omega;`;
    html += labelBox(cx + nlx * lblOffset, cy + nly * lblOffset, etiq);
    cursor += xLen;
  }

  // Cable final desde el último símbolo hasta p2
  html += `<line x1="${(p1.x + ux * cursor).toFixed(1)}" y1="${(p1.y + uy * cursor).toFixed(1)}" x2="${p2.x.toFixed(1)}" y2="${p2.y.toFixed(1)}" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round"/>`;

  return html;
}

/* =====================================================================
   8) Etiquetas de impedancia
   ===================================================================== */
function etiquetaRama(Z) {
  const r = Number(Z.r.toFixed(2));
  const x = Number(Z.i.toFixed(2));
  if (r !== 0 && x !== 0) {
    const tag = x > 0 ? 'X_L' : 'X_C';
    return `R: ${r}&Omega;  ${tag}: ${Math.abs(x)}&Omega;`;
  }
  if (r !== 0) return `R: ${r}&Omega;`;
  if (x !== 0) return `${x > 0 ? 'X_L' : 'X_C'}: ${Math.abs(x)}&Omega;`;
  return `0&Omega;`;
}

function etiquetaRamaCorta(Z) {
  const r = Number(Z.r.toFixed(1));
  const x = Number(Z.i.toFixed(1));
  if (r === 0 && x === 0) return '0&Omega;';
  if (r === 0) return `j${x}&Omega;`;
  if (x === 0) return `${r}&Omega;`;
  return `${r}${x >= 0 ? '+' : '−'}j${Math.abs(x)}&Omega;`;
}

/* =====================================================================
   9) Rama con etiqueta de impedancia (vista simbólica)
   ===================================================================== */
function dibujarRamaImpedancia(p1, p2, Z, compacta, labelSide, normalVec) {
  if (labelSide === undefined || labelSide === 0) labelSide = 1;

  const dx = p2.x - p1.x, dy = p2.y - p1.y;
  const L = Math.hypot(dx, dy) || 1;
  const ux = dx / L, uy = dy / L;
  const nx = (normalVec && isFinite(normalVec.x)) ? normalVec.x : -uy;
  const ny = (normalVec && isFinite(normalVec.y)) ? normalVec.y : ux;
  const mx = (p1.x + p2.x) / 2, my = (p1.y + p2.y) / 2;

  let deg = Math.atan2(dy, dx) * 180 / Math.PI;
  if (deg > 90 || deg < -90) deg += 180;

  const label = compacta ? etiquetaRamaCorta(Z) : etiquetaRama(Z);
  const labelLen = Math.min(label.replace(/&[^;]+;/g, 'x').length, compacta ? 14 : 22);
  const fs = compacta ? 10 : 11;

  const lx = mx + nx * labelSide * 16;
  const ly = my + ny * labelSide * 16;

  return `<line x1="${p1.x.toFixed(1)}" y1="${p1.y.toFixed(1)}" x2="${p2.x.toFixed(1)}" y2="${p2.y.toFixed(1)}" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round"/>
    <g transform="translate(${lx.toFixed(1)}, ${ly.toFixed(1)}) rotate(${deg.toFixed(1)})">
      <rect x="${(-labelLen * 3.4 - 5).toFixed(1)}" y="-9" width="${(labelLen * 6.8 + 10).toFixed(1)}" height="18" rx="4" fill="white" stroke="#94a3b8" stroke-width="1" filter="drop-shadow(0 1px 2px rgba(0,0,0,0.06))"/>
      <text x="0" y="3.5" font-size="${fs}" font-family="'JetBrains Mono', monospace" font-weight="700" fill="#0f172a" text-anchor="middle">${label}</text>
    </g>`;
}

/* =====================================================================
   10) Dibujo completo con derivación ortogonal (90°) y nodos de unión
   ===================================================================== */
function dibujarCircuito(elementos, nodos, termA, termB, flotantes) {
  const W = 560, H = 430;
  const svgComp = document.getElementById('svgComponentes');
  const svgImp = document.getElementById('svgImpedancias');
  if (svgComp) svgComp.setAttribute('viewBox', `0 0 ${W} ${H}`);
  if (svgImp) svgImp.setAttribute('viewBox', `0 0 ${W} ${H}`);

  const pos = calcularPosiciones(nodos, elementos, W, H);
  const grupos = agruparParalelos(elementos);
  let htmlComp = '', htmlImp = '';

  const nSet = new Set(nodos.map(String));
  const hasNeutro = nSet.size >= 4 && (nSet.has('4') || nSet.has('D') || nSet.has('d') || nSet.has('0'));
  const neutroId = hasNeutro ? nodos.find(n => !['1', '2', '3'].includes(String(n))) : null;

  // Centro geométrico para orientar normales hacia afuera
  let cxSum = 0, cySum = 0, nTotal = 0;
  nodos.forEach(n => {
    if (pos[n]) { cxSum += pos[n].x; cySum += pos[n].y; nTotal++; }
  });
  const C_x = nTotal ? cxSum / nTotal : W / 2;
  const C_y = nTotal ? cySum / nTotal : H / 2;

  Object.entries(grupos).forEach(([key, els]) => {
    const [n1, n2] = key.split('||');
    const p1 = pos[n1], p2 = pos[n2];
    if (!p1 || !p2) return;

    const dx = p2.x - p1.x, dy = p2.y - p1.y;
    const len = Math.hypot(dx, dy) || 1;
    const ux = dx / len, uy = dy / len;
    
    // Vector normal orientado estrictamente hacia el exterior del circuito
    let nx = -uy, ny = ux;
    const midX = (p1.x + p2.x) / 2, midY = (p1.y + p2.y) / 2;
    if (nx * (midX - C_x) + ny * (midY - C_y) < 0) {
      nx = -nx;
      ny = -ny;
    }
    const normVec = { x: nx, y: ny };

    const M = els.length;
    const isInternal = neutroId && (n1 === neutroId || n2 === neutroId);
    const isPerimeter = neutroId && !isInternal;

    if (M === 1) {
      // Rama simple directa sobre el eje
      const escala = Math.min(1.0, Math.max(0.60, len / 220));
      htmlComp += dibujarRamaSimbolos(p1, p2, els[0].Z, escala, 1, normVec);
      htmlImp += dibujarRamaImpedancia(p1, p2, els[0].Z, false, 1, normVec);
    } else {
      // Línea recta central directa entre los dos nodos (troncal continua)
      const lineaCentral = `<line x1="${p1.x.toFixed(1)}" y1="${p1.y.toFixed(1)}" x2="${p2.x.toFixed(1)}" y2="${p2.y.toFixed(1)}" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round"/>`;
      htmlComp += lineaCentral;
      htmlImp += lineaCentral;

      const dLead = Math.min(45, Math.max(22, len * 0.18));
      const J1 = { x: p1.x + ux * dLead, y: p1.y + uy * dLead };
      const J2 = { x: p2.x - ux * dLead, y: p2.y - uy * dLead };

      // Puntos de unión (nodos de derivación sobre la troncal)
      const puntosUnion = `
        <circle cx="${J1.x.toFixed(1)}" cy="${J1.y.toFixed(1)}" r="3.2" fill="#0f172a"/>
        <circle cx="${J2.x.toFixed(1)}" cy="${J2.y.toFixed(1)}" r="3.2" fill="#0f172a"/>
      `;
      htmlComp += puntosUnion;
      htmlImp += puntosUnion;

      let offsets, sep, escala;

      if (isPerimeter) {
        // En ramas perimetrales, todos los rieles paralelos se derivan hacia AFUERA (off > 0)
        // para que el triángulo interior quede 100% despejado y nunca intersecte las ramas radiales
        sep = M === 2 ? 34 : 26;
        escala = Math.min(0.70, len / 300);
        if (M === 2) {
          offsets = [18, 48];
        } else {
          offsets = els.map((_, i) => (i + 1) * sep);
        }
      } else if (isInternal) {
        // En ramas internas al neutro, usamos derivación compacta simétrica
        sep = M === 2 ? 24 : 20;
        escala = Math.min(0.55, len / 240);
        offsets = els.map((_, i) => (i - (M - 1) / 2) * sep);
      } else {
        // Red estándar de 3 nodos (sin nodo central)
        sep = M === 2 ? 36 : (M === 3 ? 28 : 24);
        escala = Math.min(0.75, len / 280);
        offsets = els.map((_, i) => (i - (M - 1) / 2) * sep);
      }

      // Extremos de las barras transversales a 90°
      const minOff = Math.min(...offsets);
      const maxOff = Math.max(...offsets);

      const barJ1_A = { x: J1.x + nx * (isPerimeter ? 0 : minOff), y: J1.y + ny * (isPerimeter ? 0 : minOff) };
      const barJ1_B = { x: J1.x + nx * maxOff, y: J1.y + ny * maxOff };
      const barJ2_A = { x: J2.x + nx * (isPerimeter ? 0 : minOff), y: J2.y + ny * (isPerimeter ? 0 : minOff) };
      const barJ2_B = { x: J2.x + nx * maxOff, y: J2.y + ny * maxOff };

      const barrasTransversales = `
        <line x1="${barJ1_A.x.toFixed(1)}" y1="${barJ1_A.y.toFixed(1)}" x2="${barJ1_B.x.toFixed(1)}" y2="${barJ1_B.y.toFixed(1)}" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round"/>
        <line x1="${barJ2_A.x.toFixed(1)}" y1="${barJ2_A.y.toFixed(1)}" x2="${barJ2_B.x.toFixed(1)}" y2="${barJ2_B.y.toFixed(1)}" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round"/>
      `;
      htmlComp += barrasTransversales;
      htmlImp += barrasTransversales;

      // Dibujar cada riel paralelo
      els.forEach((el, i) => {
        const off = offsets[i];
        const a = { x: J1.x + nx * off, y: J1.y + ny * off };
        const b = { x: J2.x + nx * off, y: J2.y + ny * off };
        
        // En ramas perimetrales con 2 rieles:
        // Riel 0 (i=0): etiqueta hacia el conductor central (labelSide = -1)
        // Riel 1 (i=1): etiqueta hacia el exterior (labelSide = 1)
        const labelSide = isPerimeter ? (i === 0 ? -1 : 1) : (off >= 0 ? 1 : -1);

        // Vista Componentes (R, L, C)
        htmlComp += dibujarRamaSimbolos(a, b, el.Z, escala, labelSide, normVec);

        // Vista Impedancias (Z)
        htmlImp += dibujarRamaImpedancia(a, b, el.Z, true, labelSide, normVec);
      });
    }
  });

  const nodosHTML = nodos.map(n => {
    const p = pos[n]; if (!p) return '';
    const isA = n === termA, isB = n === termB;
    const isFloat = flotantes && flotantes.includes(n);

    let fillCircle = '#bfdbfe', strokeCircle = '#0284c7';
    if (isA) { fillCircle = '#93c5fd'; strokeCircle = '#0284c7'; }
    if (isB) { fillCircle = '#fecaca'; strokeCircle = '#dc2626'; }
    if (isFloat) { fillCircle = '#e2e8f0'; strokeCircle = '#94a3b8'; }

    let s = '';
    s += `<circle cx="${p.x}" cy="${p.y}" r="17" fill="${strokeCircle}" opacity="0.18"/>`;
    s += `<circle cx="${p.x}" cy="${p.y}" r="14" fill="${fillCircle}" stroke="${strokeCircle}" stroke-width="2.8"/>`;

    let tx = p.x, ty = p.y + 5, anchor = 'middle';
    if (n === '1') { tx = p.x - 24; }
    else if (n === '3') { tx = p.x + 24; }
    else if (n === '2') { ty = p.y - 22; }
    s += `<text x="${tx}" y="${ty}" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="${anchor}">${n}</text>`;
    if (isFloat) s += `<text x="${p.x}" y="${p.y + 30}" font-size="10" fill="#94a3b8" text-anchor="middle" font-style="italic">flotante</text>`;
    return s;
  }).join('');

  htmlComp += nodosHTML;
  htmlImp += nodosHTML;

  if (svgComp) svgComp.innerHTML = htmlComp;
  if (svgImp) svgImp.innerHTML = htmlImp;
}

/* =====================================================================
   11) Tablas y sistema nodal
   ===================================================================== */
function renderTablaEquivalentes(grupos) {
  let filas = '';
  Object.entries(grupos).forEach(([key, els]) => {
    const [n1, n2] = key.split('||');
    const Zeq = equivalenteParalelo(els);
    filas += `<tr>
      <td><span class="badge bg-secondary">${n1}</span> – <span class="badge bg-secondary">${n2}</span></td>
      <td class="text-center">${els.length}</td>
      <td class="text-end font-monospace">${fmtCorto(Zeq)} &Omega;</td>
    </tr>`;
  });
  return `
    <details class="mt-2">
      <summary class="small fw-bold text-primary" style="cursor:pointer;">
        📊 Ver impedancia equivalente por par de nodos
      </summary>
      <div class="table-responsive mt-2">
        <table class="table table-sm table-hover align-middle mb-0">
          <thead class="table-light">
            <tr><th>Par de nodos</th><th class="text-center"># ramas</th><th class="text-end">Z equivalente</th></tr>
          </thead>
          <tbody>${filas}</tbody>
        </table>
      </div>
    </details>`;
}

function renderSistemaNodal(Y, I, inc, B) {
  const n = inc.length;
  let html = '<div class="table-responsive"><table class="table table-sm table-bordered mb-0 font-monospace" style="font-size:0.78rem;">';
  html += '<thead class="table-light"><tr><th></th>';
  inc.forEach(nm => html += `<th class="text-center">V<sub>${nm}</sub></th>`);
  html += '<th class="text-center bg-warning bg-opacity-25">I</th></tr></thead><tbody>';
  for (let i = 0; i < n; i++) {
    html += `<tr><th class="table-light" style="white-space:nowrap;">Nodo ${inc[i]}</th>`;
    for (let j = 0; j < n; j++) html += `<td class="text-end">${fmtCorto(Y[i][j])}</td>`;
    html += `<td class="text-end bg-warning bg-opacity-10">${fmtCorto(I[i])}</td></tr>`;
  }
  html += '</tbody></table></div>';
  return `
    <details class="mt-2">
      <summary class="small fw-bold text-primary" style="cursor:pointer;">
        🧮 Ver sistema nodal complejo (Y · V = I)
      </summary>
      <p class="small text-muted mt-2 mb-1">
        Cada fila corresponde a la LCK en un nodo (referencia: <b>${B}</b> = 0 V).
        Unidades: Y en S, V en V, I en A. Los coeficientes son complejos (R + jX).
      </p>
      ${html}
    </details>`;
}

/* =====================================================================
   12) Resolver red (función principal)
   ===================================================================== */
function resolverRed() {
  const out = document.getElementById('resultadoRed');
  const netlistEl = document.getElementById('netlist');
  if (!out || !netlistEl) return;

  const { elementos, nodos } = parseNetlist(netlistEl.value);
  const termAEl = document.getElementById('termA');
  const termBEl = document.getElementById('termB');
  const A = termAEl ? String(termAEl.value).trim() : '1';
  const B = termBEl ? String(termBEl.value).trim() : '2';

  if (!elementos.length) {
    out.innerHTML = '<div class="alert alert-warning py-2">Netlist vacío o con sintaxis inválida.</div>';
    const s1 = document.getElementById('svgComponentes');
    const s2 = document.getElementById('svgImpedancias');
    if (s1) s1.innerHTML = '';
    if (s2) s2.innerHTML = '';
    return;
  }
  if (!nodos.includes(A) || !nodos.includes(B)) {
    out.innerHTML = `<div class="alert alert-warning py-2">Los terminales <b>${A}</b> y <b>${B}</b> deben existir en el netlist.</div>`;
    return;
  }
  if (A === B) {
    out.innerHTML = '<div class="alert alert-warning py-2">Los terminales de entrada y retorno deben ser diferentes.</div>';
    return;
  }

  const flotantes = detectarFlotantes(elementos, nodos, B);
  dibujarCircuito(elementos, nodos, A, B, flotantes);

  const inc = nodos.filter(n => n !== B && !flotantes.includes(n));
  const idx = Object.fromEntries(inc.map((n, i) => [n, i]));
  const n = inc.length;

  const Y = Array.from({ length: n }, () => Array.from({ length: n }, () => ({ r: 0, i: 0 })));
  const I = Array.from({ length: n }, () => ({ r: 0, i: 0 }));

  for (const el of elementos) {
    if (el.Z.r === 0 && el.Z.i === 0) continue;
    if (flotantes.includes(el.a) || flotantes.includes(el.b)) continue;
    const y = CZ.div({ r: 1, i: 0 }, el.Z);
    const iu = el.a === B ? -1 : idx[el.a];
    const iv = el.b === B ? -1 : idx[el.b];
    if (iu >= 0) Y[iu][iu] = CZ.add(Y[iu][iu], y);
    if (iv >= 0) Y[iv][iv] = CZ.add(Y[iv][iv], y);
    if (iu >= 0 && iv >= 0) {
      Y[iu][iv] = CZ.add(Y[iu][iv], { r: -y.r, i: -y.i });
      Y[iv][iu] = CZ.add(Y[iv][iu], { r: -y.r, i: -y.i });
    }
  }
  I[idx[A]] = { r: 1, i: 0 };

  let V;
  try { V = solveComplex(Y, I); }
  catch (e) {
    out.innerHTML = `<div class="alert alert-danger py-2">${e.message}</div>`;
    return;
  }

  const ZT = V[idx[A]];
  const p = CZ.polar(ZT);
  const signo = ZT.i >= 0 ? '+' : '−';

  let filas = '';
  inc.forEach((nm, i) => {
    const v = V[i];
    const pv = CZ.polar(v);
    const sg = v.i >= 0 ? '+' : '−';
    filas += `<tr>
      <td><span class="badge bg-secondary">${nm}</span></td>
      <td class="text-end font-monospace">${v.r.toFixed(4)} ${sg} j${Math.abs(v.i).toFixed(4)} V</td>
      <td class="text-end font-monospace">${pv.mag.toFixed(4)} &ang; ${pv.ang.toFixed(2)}&deg; V</td>
    </tr>`;
  });
  filas += `<tr class="table-light">
    <td><span class="badge bg-danger">${B} (Tierra)</span></td>
    <td class="text-end font-monospace">0.0000 + j0.0000 V</td>
    <td class="text-end font-monospace">0.0000 &ang; 0.00&deg; V</td>
  </tr>`;

  const avisoFlotantes = flotantes.length
    ? `<div class="alert alert-info py-2 small mb-2">
         ℹ️ Nodos flotantes detectados (sin camino a ${B}): <b>${flotantes.join(', ')}</b>. No afectan Z<sub>T</sub> y fueron excluidos del sistema nodal.
       </div>`
    : '';

  const grupos = agruparParalelos(elementos);

  out.innerHTML = `
    <div class="card p-3 border-0 bg-white shadow-sm" style="border-left:4px solid #10b981 !important;">
      <div class="d-flex justify-content-between align-items-center mb-2">
        <h6 class="fw-bold mb-0" style="color:#059669;">
          🎯 Impedancia Equivalente Total Z<sub>T</sub> (entre terminales ${A} y ${B})
        </h6>
        <span class="badge bg-success">Solución Nodal</span>
      </div>
      ${avisoFlotantes}
      <div class="p-3 bg-light rounded-3 my-2 text-center">
        <span class="fs-4 fw-bold text-dark">Z<sub>T</sub> = ${p.mag.toFixed(4)} &ang; ${p.ang.toFixed(2)}&deg; &Omega;</span>
        <span class="text-muted ms-2 fs-5">(${ZT.r.toFixed(4)} ${signo} j${Math.abs(ZT.i).toFixed(4)} &Omega;)</span>
      </div>
      ${renderTablaEquivalentes(grupos)}
      ${renderSistemaNodal(Y, I, inc, B)}
      <details class="mt-2">
        <summary class="small fw-bold text-primary" style="cursor:pointer;">
          🔍 Ver tensiones nodales (Inyección de prueba I = 1&ang;0&deg; A)
        </summary>
        <div class="table-responsive mt-2">
          <table class="table table-sm table-hover align-middle mb-0">
            <thead class="table-light">
              <tr><th>Nodo</th><th class="text-end">Tensión fasorial (rect.)</th><th class="text-end">Tensión fasorial (polar)</th></tr>
            </thead>
            <tbody>${filas}</tbody>
          </table>
        </div>
      </details>
    </div>`;
}

/* =====================================================================
   13) Ejemplos precargados
   ===================================================================== */
function cargarEjemploDeltaEstrella() {
  const nl = document.getElementById('netlist');
  if (nl) nl.value =
`# Red en delta de ejemplo
# Rama 1-2: (3+j6) || (3+j6)
1 2 3 6
1 2 3 6
# Rama 2-3: (3+j6) || (6+j6)
2 3 3 6
2 3 6 6
# Rama 1-3: (3+j6) || (6+j6)
1 3 3 6
1 3 6 6`;
  const tA = document.getElementById('termA');
  const tB = document.getElementById('termB');
  if (tA) tA.value = '1';
  if (tB) tB.value = '2';
  resolverRed();
}

function cargarEjemploEstrellaDelta() {
  const nl = document.getElementById('netlist');
  if (nl) nl.value =
`# Red en Estrella (Y): 3 ramas de (1+j2 || 1+j2) conectadas a 'd'
# Rama 1-d: (1+j2) || (1+j2)
1 d 1 2
1 d 1 2
# Rama 2-d: (1+j2) || (1+j2)
2 d 1 2
2 d 1 2
# Rama 3-d: (1+j2) || (1+j2)
3 d 1 2
3 d 1 2`;
  const tA = document.getElementById('termA');
  const tB = document.getElementById('termB');
  if (tA) tA.value = '1';
  if (tB) tB.value = '2';
  resolverRed();
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", cargarEjemploDeltaEstrella);
} else {
  setTimeout(cargarEjemploDeltaEstrella, 60);
}
</script>
```
:::