::: {.card-module}
### 🧮 Solver de redes complejas (análisis nodal) {.unnumbered}

```{=html}
<p class="small text-muted mb-2">
Este solver calcula y retorna la <b>Impedancia Equivalente Total (<i>Z</i><sub>T</sub>) entre los dos terminales externos seleccionados (A y B)</b> mediante análisis nodal complejo. Escribe cada elemento como <code>nodo1 nodo2 R X</code>, donde la impedancia serie entre ambos nodos es <em>Z = R + jX</em> (&Omega;). Una línea por elemento. Los símbolos <code>#</code> inician comentarios y los nodos pueden nombrarse con números o letras. Varias líneas con el mismo par de nodos se interpretan como <b>ramas en paralelo</b>.
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
    <div class="border rounded-3 bg-white shadow-sm p-2 w-100">
      <svg id="svgComponentes" width="100%" height="auto" viewBox="0 0 560 410" preserveAspectRatio="xMidYMid meet" style="display:block; background:#ffffff; font-family:'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;"></svg>
    </div>
  </div>
  <div style="flex:1 1 300px; min-width:270px;">
    <div class="border rounded-3 bg-white shadow-sm p-2 w-100">
      <svg id="svgImpedancias" width="100%" height="auto" viewBox="0 0 560 410" preserveAspectRatio="xMidYMid meet" style="display:block; background:#ffffff; font-family:'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;"></svg>
    </div>
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
    pos['2'] = { x: W * 0.50, y: 70 };
    pos['1'] = { x: W * 0.16, y: 325 };
    pos['3'] = { x: W * 0.84, y: 325 };
    return pos;
  }
  if (nSet.size === 4 && nSet.has('1') && nSet.has('2') && nSet.has('3')) {
    const neutro = nodos.find(n => !['1', '2', '3'].includes(String(n)));
    pos['2'] = { x: W * 0.50, y: 70 };
    pos['1'] = { x: W * 0.16, y: 325 };
    pos['3'] = { x: W * 0.84, y: 325 };
    pos[neutro] = { x: W * 0.50, y: 240 };
    return pos;
  }
  nodos.forEach((n, i) => {
    const ang = (2 * Math.PI * i) / nodos.length - Math.PI / 2;
    pos[n] = {
      x: W / 2 + Math.min(W, H) * 0.36 * Math.cos(ang),
      y: H / 2 + Math.min(W, H) * 0.36 * Math.sin(ang) + 10
    };
  });
  return pos;
}

/* =====================================================================
   6) Símbolos SVG de componentes (R, L, C)
   ===================================================================== */
function svgResistor(cx, cy, deg, largo) {
  const h = 6.5;
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
    <polyline points="${pts.join(' ')}" fill="none" stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
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
    <path d="${d}" fill="none" stroke="black" stroke-width="1.5" stroke-linecap="round"/>
  </g>`;
}

function svgCapacitor(cx, cy, deg, largo) {
  const gap = 4;
  const plateH = 16;
  const lead = Math.max(4, (largo / 2) - gap);
  return `<g transform="translate(${cx.toFixed(1)},${cy.toFixed(1)}) rotate(${deg.toFixed(1)})">
    <line x1="${-lead.toFixed(1)}" y1="0" x2="${-gap.toFixed(1)}" y2="0" stroke="black" stroke-width="1.5"/>
    <line x1="${gap.toFixed(1)}" y1="0" x2="${lead.toFixed(1)}" y2="0" stroke="black" stroke-width="1.5"/>
    <line x1="${-gap.toFixed(1)}" y1="${(-plateH / 2).toFixed(1)}" x2="${-gap.toFixed(1)}" y2="${(plateH / 2).toFixed(1)}" stroke="black" stroke-width="1.8" stroke-linecap="round"/>
    <line x1="${gap.toFixed(1)}" y1="${(-plateH / 2).toFixed(1)}" x2="${gap.toFixed(1)}" y2="${(plateH / 2).toFixed(1)}" stroke="black" stroke-width="1.8" stroke-linecap="round"/>
  </g>`;
}

function labelBox(x, y, texto) {
  const clean = texto.replace(/<[^>]+>/g, '').replace(/&[^;]+;/g, 'x');
  const w = Math.max(26, clean.length * 6.5 + 8);
  return `<g transform="translate(${x.toFixed(1)},${y.toFixed(1)})">
    <rect x="${(-w / 2).toFixed(1)}" y="-8.5" width="${w.toFixed(1)}" height="17" rx="3"
          fill="#ffffff" stroke="#cbd5e1" stroke-width="0.8"/>
    <text x="0" y="3.5" font-size="11" font-weight="600" fill="black" text-anchor="middle">${texto}</text>
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
  
  const nx = (normalVec && isFinite(normalVec.x)) ? normalVec.x : -uy;
  const ny = (normalVec && isFinite(normalVec.y)) ? normalVec.y : ux;

  let deg = Math.atan2(dy, dx) * 180 / Math.PI;
  if (deg > 90) deg -= 180;
  if (deg < -90) deg += 180;

  const R = Z.r, X = Z.i;
  const tieneR = Math.abs(R) > 1e-6, tieneX = Math.abs(X) > 1e-6;

  if (!tieneR && !tieneX) {
    return `<line x1="${p1.x.toFixed(1)}" y1="${p1.y.toFixed(1)}" x2="${p2.x.toFixed(1)}" y2="${p2.y.toFixed(1)}" stroke="black" stroke-width="1.5" stroke-linecap="round"/>`;
  }

  const rLen = tieneR ? Math.min(38 * escala, L * 0.35) : 0;
  const xLen = tieneX ? (X < 0 ? Math.min(26 * escala, L * 0.28) : Math.min(34 * escala, L * 0.34)) : 0;
  const gapInter = (tieneR && tieneX) ? Math.max(16, 22 * escala) : 0;
  const totalSym = rLen + xLen + gapInter;
  const startD = Math.max(4, (L - totalSym) / 2);

  let html = '';
  // Cable inicial hasta el primer símbolo
  html += `<line x1="${p1.x.toFixed(1)}" y1="${p1.y.toFixed(1)}" x2="${(p1.x + ux * startD).toFixed(1)}" y2="${(p1.y + uy * startD).toFixed(1)}" stroke="black" stroke-width="1.5" stroke-linecap="round"/>`;

  const nlx = nx * labelSide, nly = ny * labelSide;
  const lblOffset = Math.max(16, 18 * escala);

  let cursor = startD;
  if (tieneR) {
    const cx = p1.x + ux * (cursor + rLen / 2);
    const cy = p1.y + uy * (cursor + rLen / 2);
    html += svgResistor(cx, cy, deg, rLen);
    const rVal = Number(R.toFixed(2));
    html += labelBox(cx + nlx * lblOffset, cy + nly * lblOffset, `<tspan font-style="italic">R</tspan> = ${rVal}&thinsp;&Omega;`);
    cursor += rLen;
  }
  if (tieneR && tieneX) {
    // Tramo de cable intermedio entre R y X
    html += `<line x1="${(p1.x + ux * cursor).toFixed(1)}" y1="${(p1.y + uy * cursor).toFixed(1)}" x2="${(p1.x + ux * (cursor + gapInter)).toFixed(1)}" y2="${(p1.y + uy * (cursor + gapInter)).toFixed(1)}" stroke="black" stroke-width="1.5" stroke-linecap="round"/>`;
    cursor += gapInter;
  }
  if (tieneX) {
    const cx = p1.x + ux * (cursor + xLen / 2);
    const cy = p1.y + uy * (cursor + xLen / 2);
    if (X > 0) {
      html += svgInductor(cx, cy, deg, xLen);
      const xVal = Number(X.toFixed(2));
      html += labelBox(cx + nlx * lblOffset, cy + nly * lblOffset, `<tspan font-style="italic">X</tspan><tspan baseline-shift="sub" font-size="0.75em">L</tspan> = ${xVal}&thinsp;&Omega;`);
    } else {
      html += svgCapacitor(cx, cy, deg, xLen);
      const xVal = Math.abs(Number(X.toFixed(2)));
      html += labelBox(cx + nlx * lblOffset, cy + nly * lblOffset, `<tspan font-style="italic">X</tspan><tspan baseline-shift="sub" font-size="0.75em">C</tspan> = ${xVal}&thinsp;&Omega;`);
    }
    cursor += xLen;
  }

  // Cable final desde el último símbolo hasta p2
  html += `<line x1="${(p1.x + ux * cursor).toFixed(1)}" y1="${(p1.y + uy * cursor).toFixed(1)}" x2="${p2.x.toFixed(1)}" y2="${p2.y.toFixed(1)}" stroke="black" stroke-width="1.5" stroke-linecap="round"/>`;

  return html;
}

/* =====================================================================
   8) Formato y bloque de impedancia (estilo _genera_delta / IEEE)
   ===================================================================== */
function fmtZbox(z) {
  const r = Math.abs(z.r) < 1e-6 ? 0 : Number(z.r.toFixed(2));
  const i = Math.abs(z.i) < 1e-6 ? 0 : Number(z.i.toFixed(2));
  if (r === 0 && i === 0) return '0&thinsp;&Omega;';
  if (i === 0) return `${r}&thinsp;&Omega;`;
  if (r === 0) {
    return i > 0 ? `j${i}&thinsp;&Omega;` : `&minus;j${Math.abs(i)}&thinsp;&Omega;`;
  }
  const s = i > 0 ? '+' : '&minus;';
  return `${r} ${s} j${Math.abs(i)}&thinsp;&Omega;`;
}

function dibujarRamaImpedancia(p1, p2, Z, branchLabel) {
  const dx = p2.x - p1.x, dy = p2.y - p1.y;
  const mx = (p1.x + p2.x) / 2, my = (p1.y + p2.y) / 2;
  let deg = Math.atan2(dy, dx) * 180 / Math.PI;
  if (deg > 90) deg -= 180;
  if (deg < -90) deg += 180;

  if (Math.abs(Z.r) < 1e-6 && Math.abs(Z.i) < 1e-6) {
    return `<line x1="${p1.x.toFixed(1)}" y1="${p1.y.toFixed(1)}" x2="${p2.x.toFixed(1)}" y2="${p2.y.toFixed(1)}" stroke="black" stroke-width="1.5" stroke-linecap="round"/>`;
  }

  const zText = fmtZbox(Z);
  const fullText = branchLabel
    ? `Z<tspan baseline-shift="sub" font-size="0.75em">${branchLabel}</tspan>: ${zText}`
    : zText;
  const cleanLen = (branchLabel ? 3 + branchLabel.length : 0) + zText.replace(/&[^;]+;/g, 'x').replace(/<[^>]+>/g, '').length;
  const w = Math.max(56, cleanLen * 6.8 + 14);
  const h = 24;

  return `
    <line x1="${p1.x.toFixed(1)}" y1="${p1.y.toFixed(1)}" x2="${p2.x.toFixed(1)}" y2="${p2.y.toFixed(1)}" stroke="black" stroke-width="1.5" stroke-linecap="round"/>
    <g transform="translate(${mx.toFixed(1)}, ${my.toFixed(1)}) rotate(${deg.toFixed(1)})">
      <rect x="${(-w / 2).toFixed(1)}" y="${(-h / 2).toFixed(1)}" width="${w.toFixed(1)}" height="${h}" fill="white" stroke="black" stroke-width="1.5"/>
      <text x="0" y="4.5" font-size="12" font-style="italic" fill="black" text-anchor="middle">${fullText}</text>
    </g>
  `;
}

/* =====================================================================
   9) Dibujo completo con derivación ortogonal (90°) y formato editorial
   ===================================================================== */
function dibujarCircuito(elementos, nodos, termA, termB, flotantes) {
  const W = 560, H = 410;
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

  // Encabezados editoriales tipo libro
  const headerComp = `<text x="${W / 2}" y="26" font-size="15" font-weight="bold" fill="black" text-anchor="middle">Esquema con componentes (R, L, C)</text>`;
  const headerImp = `<text x="${W / 2}" y="26" font-size="15" font-weight="bold" fill="black" text-anchor="middle">Esquema con impedancias equivalentes</text>`;
  htmlComp += headerComp;
  htmlImp += headerImp;

  // Polígono sombreado interior para red Delta (consistencia con _genera_delta.md)
  if (pos['1'] && pos['2'] && pos['3']) {
    const bgDelta = `<polygon points="${pos['2'].x.toFixed(1)},${pos['2'].y.toFixed(1)} ${pos['3'].x.toFixed(1)},${pos['3'].y.toFixed(1)} ${pos['1'].x.toFixed(1)},${pos['1'].y.toFixed(1)}" fill="#3b82f6" opacity="0.10" stroke="none"/>`;
    htmlComp += bgDelta;
    htmlImp += bgDelta;
  }

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
      htmlImp += dibujarRamaImpedancia(p1, p2, els[0].Z, `${n1}${n2}`);
    } else {
      // Línea recta central directa entre los dos nodos (troncal continua)
      const lineaCentral = `<line x1="${p1.x.toFixed(1)}" y1="${p1.y.toFixed(1)}" x2="${p2.x.toFixed(1)}" y2="${p2.y.toFixed(1)}" stroke="black" stroke-width="1.5" stroke-linecap="round"/>`;
      htmlComp += lineaCentral;
      htmlImp += lineaCentral;

      const dLead = Math.min(45, Math.max(22, len * 0.18));
      const J1 = { x: p1.x + ux * dLead, y: p1.y + uy * dLead };
      const J2 = { x: p2.x - ux * dLead, y: p2.y - uy * dLead };

      // Puntos de unión (nodos de derivación sobre la troncal)
      const puntosUnion = `
        <circle cx="${J1.x.toFixed(1)}" cy="${J1.y.toFixed(1)}" r="3" fill="black"/>
        <circle cx="${J2.x.toFixed(1)}" cy="${J2.y.toFixed(1)}" r="3" fill="black"/>
      `;
      htmlComp += puntosUnion;
      htmlImp += puntosUnion;

      let offsets, sep, escala;

      if (isPerimeter) {
        sep = M === 2 ? 34 : 26;
        escala = Math.min(0.70, len / 300);
        if (M === 2) {
          offsets = [18, 48];
        } else {
          offsets = els.map((_, i) => (i + 1) * sep);
        }
      } else if (isInternal) {
        sep = M === 2 ? 24 : 20;
        escala = Math.min(0.55, len / 240);
        offsets = els.map((_, i) => (i - (M - 1) / 2) * sep);
      } else {
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
        <line x1="${barJ1_A.x.toFixed(1)}" y1="${barJ1_A.y.toFixed(1)}" x2="${barJ1_B.x.toFixed(1)}" y2="${barJ1_B.y.toFixed(1)}" stroke="black" stroke-width="1.5" stroke-linecap="round"/>
        <line x1="${barJ2_A.x.toFixed(1)}" y1="${barJ2_A.y.toFixed(1)}" x2="${barJ2_B.x.toFixed(1)}" y2="${barJ2_B.y.toFixed(1)}" stroke="black" stroke-width="1.5" stroke-linecap="round"/>
      `;
      htmlComp += barrasTransversales;
      htmlImp += barrasTransversales;

      // Dibujar cada riel paralelo
      els.forEach((el, i) => {
        const off = offsets[i];
        const a = { x: J1.x + nx * off, y: J1.y + ny * off };
        const b = { x: J2.x + nx * off, y: J2.y + ny * off };
        
        const labelSide = isPerimeter ? (i === 0 ? -1 : 1) : (off >= 0 ? 1 : -1);

        // Vista Componentes (R, L, C)
        htmlComp += dibujarRamaSimbolos(a, b, el.Z, escala, labelSide, normVec);

        // Vista Impedancias (Z)
        htmlImp += dibujarRamaImpedancia(a, b, el.Z, `${n1}${n2},${i + 1}`);
      });
    }
  });

  const nodosHTML = nodos.map(n => {
    const p = pos[n]; if (!p) return '';
    const isA = n === termA, isB = n === termB;
    const isFloat = flotantes && flotantes.includes(n);
    const isNeutro = neutroId && n === neutroId;

    if (isNeutro) {
      return `
        <circle cx="${p.x.toFixed(1)}" cy="${p.y.toFixed(1)}" r="3" fill="black"/>
        <text x="${(p.x - 14).toFixed(1)}" y="${(p.y + 4).toFixed(1)}" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="end">${n === '4' ? 'O' : n}</text>
      `;
    }

    let tx = p.x, ty = p.y, anchor = 'middle';
    if (n === '1') { tx = p.x - 14; ty = p.y + 18; anchor = 'end'; }
    else if (n === '3') { tx = p.x + 14; ty = p.y + 18; anchor = 'start'; }
    else if (n === '2') { tx = p.x; ty = p.y - 12; anchor = 'middle'; }
    else {
      const vx = p.x - C_x, vy = p.y - C_y;
      const vlen = Math.hypot(vx, vy) || 1;
      tx = p.x + (vx / vlen) * 16;
      ty = p.y + (vy / vlen) * 16 + 4;
      anchor = vx < -5 ? 'end' : (vx > 5 ? 'start' : 'middle');
    }

    let strokeCol = 'black', strokeW = '1.5', fillCol = 'white', dash = '';
    let badgeText = '';

    if (isA) {
      strokeCol = '#2563eb';
      strokeW = '2';
      badgeText = `<tspan font-style="normal" font-weight="bold" font-size="11" fill="#2563eb"> (A+)</tspan>`;
    } else if (isB) {
      strokeCol = '#dc2626';
      strokeW = '2';
      badgeText = `<tspan font-style="normal" font-weight="bold" font-size="11" fill="#dc2626"> (B−)</tspan>`;
    } else if (isFloat) {
      strokeCol = '#94a3b8';
      fillCol = '#f8fafc';
      dash = 'stroke-dasharray="2 2"';
      badgeText = `<tspan font-style="italic" font-weight="normal" font-size="10" fill="#64748b"> (flotante)</tspan>`;
    }

    return `
      <circle cx="${p.x.toFixed(1)}" cy="${p.y.toFixed(1)}" r="4.5" fill="${fillCol}" stroke="${strokeCol}" stroke-width="${strokeW}" ${dash}/>
      <text x="${tx.toFixed(1)}" y="${ty.toFixed(1)}" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="${anchor}">${n}${badgeText}</text>
    `;
  }).join('');

  htmlComp += nodosHTML;
  htmlImp += nodosHTML;

  // Leyendas explicativas al pie del esquema (consistencia con _genera_delta.md)
  const footerComp = `<text x="${W / 2}" y="${H - 12}" font-size="11" fill="#475569" text-anchor="middle">R = resistencia (zigzag) · L = inductancia (bobina) · C = capacitancia (placas)</text>`;
  const footerImp = `<text x="${W / 2}" y="${H - 12}" font-size="11" fill="#475569" text-anchor="middle">Ramas modeladas como bloques de impedancia Z = R + jX</text>`;
  htmlComp += footerComp;
  htmlImp += footerImp;

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
        <` + `table class="table table-sm table-hover align-middle mb-0">
          <` + `thead class="table-light">
            <tr><th>Par de nodos</th><th class="text-center"># ramas</th><th class="text-end">Z equivalente</th></tr>
          </` + `thead>
          <` + `tbody>${filas}</` + `tbody>
        </` + `table>
      </div>
    </details>`;
}

function renderSistemaNodal(Y, I, inc, B) {
  const n = inc.length;
  let html = '<div class="table-responsive"><' + 'table class="table table-sm table-bordered mb-0 font-monospace" style="font-size:0.78rem;">';
  html += '<' + 'thead class="table-light"><tr><th></th>';
  inc.forEach(nm => html += `<th class="text-center">V<sub>${nm}</sub></th>`);
  html += '<th class="text-center bg-warning bg-opacity-25">I</th></tr></' + 'thead><' + 'tbody>';
  for (let i = 0; i < n; i++) {
    html += `<tr><th class="table-light" style="white-space:nowrap;">Nodo ${inc[i]}</th>`;
    for (let j = 0; j < n; j++) html += `<td class="text-end">${fmtCorto(Y[i][j])}</td>`;
    html += `<td class="text-end bg-warning bg-opacity-10">${fmtCorto(I[i])}</td></tr>`;
  }
  html += '</' + 'tbody></' + 'table></div>';
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
   12) Detección automática y visualización editorial de transformaciones Δ y Y
   ===================================================================== */
function renderTransformacionesDY(elementos, nodos, termA, termB) {
  const grupos = agruparParalelos(elementos);
  const adj = {};
  nodos.forEach(n => { adj[n] = new Set(); });

  const zeqPar = {};
  Object.entries(grupos).forEach(([key, els]) => {
    const [n1, n2] = key.split('||');
    adj[n1].add(n2);
    adj[n2].add(n1);
    zeqPar[key] = equivalenteParalelo(els);
  });

  function getZeq(a, b) {
    return zeqPar[[a, b].sort().join('||')] || null;
  }

  function fmtZeq(z) {
    if (!z) return '0 &Omega;';
    const p = CZ.polar(z);
    const sg = z.i >= 0 ? '+' : '−';
    return `<b>${p.mag.toFixed(4)}&ang;${p.ang.toFixed(2)}&deg; &Omega;</b> <span class="text-muted">(${z.r.toFixed(4)} ${sg} j${Math.abs(z.i).toFixed(4)})</span>`;
  }

  function fmtZpolar(z) {
    if (!z) return '0 &Omega;';
    const p = CZ.polar(z);
    return `${p.mag.toFixed(2)}∠${p.ang.toFixed(1)}° Ω`;
  }

  // Helper para bloque de impedancia sobre rama en SVG vertical de alta resolución
  function svgRamaBloque(p1, p2, labelSym, zVal, color = '#1e293b', isDashed = false) {
    const dx = p2.x - p1.x, dy = p2.y - p1.y;
    const mx = (p1.x + p2.x) / 2, my = (p1.y + p2.y) / 2;
    let deg = Math.atan2(dy, dx) * 180 / Math.PI;
    if (deg > 90) deg -= 180;
    if (deg < -90) deg += 180;

    const rot = (Math.abs(deg) < 20 || Math.abs(Math.abs(deg) - 90) < 20) ? 0 : deg;
    const zPol = zVal ? fmtZpolar(zVal) : '';
    const w = Math.max(96, Math.max(labelSym.length * 8, zPol.length * 7.5) + 22);
    const h = zPol ? 34 : 24;
    const dash = isDashed ? 'stroke-dasharray="5 5"' : '';

    return `
      <line x1="${p1.x.toFixed(1)}" y1="${p1.y.toFixed(1)}" x2="${p2.x.toFixed(1)}" y2="${p2.y.toFixed(1)}" stroke="${color}" stroke-width="1.6" stroke-linecap="round" ${dash}/>
      <g transform="translate(${mx.toFixed(1)}, ${my.toFixed(1)}) rotate(${rot.toFixed(1)})">
        <rect x="${(-w / 2).toFixed(1)}" y="${(-h / 2).toFixed(1)}" width="${w.toFixed(1)}" height="${h}" rx="5"
              fill="#ffffff" stroke="${color}" stroke-width="1.5"/>
        <text x="0" y="${zPol ? -3 : 4}" font-size="12" font-style="italic" font-weight="600" fill="black" text-anchor="middle">${labelSym}</text>
        ${zPol ? `<text x="0" y="11.5" font-size="10.5" font-weight="bold" fill="${color}" text-anchor="middle">${zPol}</text>` : ''}
      </g>
    `;
  }

  function svgTerm(p, label, isA, isB, subtext = '') {
    let stroke = 'black', fill = 'white', badge = '';
    if (isA) { stroke = '#2563eb'; badge = `<tspan font-style="normal" font-weight="bold" font-size="11" fill="#2563eb"> (A+)</tspan>`; }
    else if (isB) { stroke = '#dc2626'; badge = `<tspan font-style="normal" font-weight="bold" font-size="11" fill="#dc2626"> (B−)</tspan>`; }

    let tx = p.x, ty = p.y - 14, anchor = 'middle';
    if (p.align === 'top') { ty = p.y - 14; }
    else if (p.align === 'bl') { tx = p.x - 14; ty = p.y + 18; anchor = 'end'; }
    else if (p.align === 'br') { tx = p.x + 14; ty = p.y + 18; anchor = 'start'; }

    return `
      <circle cx="${p.x.toFixed(1)}" cy="${p.y.toFixed(1)}" r="5" fill="${fill}" stroke="${stroke}" stroke-width="2"/>
      <text x="${tx.toFixed(1)}" y="${ty.toFixed(1)}" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="${anchor}">${label}${badge}</text>
      ${subtext ? `<text x="${tx.toFixed(1)}" y="${(ty + 13).toFixed(1)}" font-size="10.5" fill="#64748b" text-anchor="${anchor}">${subtext}</text>` : ''}
    `;
  }

  function svgNodoO(p, label) {
    return `
      <circle cx="${p.x.toFixed(1)}" cy="${p.y.toFixed(1)}" r="4" fill="black"/>
      <text x="${(p.x - 12).toFixed(1)}" y="${(p.y + 4).toFixed(1)}" font-size="13" font-weight="bold" font-style="italic" fill="black" text-anchor="end">${label}</text>
    `;
  }

  // Conector vertical con flecha hacia abajo ↓
  function svgConectorVertical(badgeText, descText, color = '#2563eb') {
    return `
      <div class="d-flex justify-content-center my-3">
        <div class="d-flex align-items-center gap-2 px-3 py-1.5 border rounded-pill bg-white shadow-sm">
          <span class="badge rounded-pill px-2.5 py-1 text-white fw-bold" style="background:${color};">${badgeText}</span>
          <span class="small fw-semibold text-secondary">${descText}</span>
          <span class="fs-5 fw-bold" style="color:${color};">↓</span>
        </div>
      </div>
    `;
  }

  // =========================================================================
  // CLASIFICACIÓN TOPOLÓGICA INTELIGENTE
  // =========================================================================

  // 1) ¿Existe una Red Mixta? (Anillo Delta + Estrella Interna)
  let mixedNet = null;
  for (let i = 0; i < nodos.length; i++) {
    for (let j = i + 1; j < nodos.length; j++) {
      for (let k = j + 1; k < nodos.length; k++) {
        const p1 = nodos[i], p2 = nodos[j], p3 = nodos[k];
        if (getZeq(p1, p2) && getZeq(p2, p3) && getZeq(p1, p3)) {
          const candidatosO = nodos.filter(n => n !== p1 && n !== p2 && n !== p3 && getZeq(n, p1) && getZeq(n, p2) && getZeq(n, p3));
          if (candidatosO.length > 0) {
            let O = candidatosO.find(n => n !== termA && n !== termB) || candidatosO[0];
            mixedNet = { p1, p2, p3, O };
            break;
          }
        }
      }
      if (mixedNet) break;
    }
    if (mixedNet) break;
  }

  // 2) ¿Es Red Puramente Delta? (3 nodos, sin nodo interno)
  let pureDelta = null;
  if (!mixedNet && nodos.length === 3) {
    const [p1, p2, p3] = nodos;
    if (getZeq(p1, p2) && getZeq(p2, p3) && getZeq(p1, p3)) {
      pureDelta = { p1, p2, p3 };
    }
  }

  // 3) ¿Es Red Puramente Estrella? (1 centro y 3 vecinos sin ramas perimetrales)
  let pureStar = null;
  if (!mixedNet && !pureDelta && nodos.length === 4) {
    const center = nodos.find(n => adj[n] && adj[n].size === 3);
    if (center) {
      const vecinos = [...adj[center]];
      const [v1, v2, v3] = vecinos;
      if (!getZeq(v1, v2) && !getZeq(v2, v3) && !getZeq(v1, v3)) {
        pureStar = { center, v1, v2, v3 };
      }
    }
  }

  let html = '';

  // -------------------------------------------------------------------------
  // CASO A — RED MIXTA (DOBLE TRANSFORMACIÓN COMPLETA VERTICAL)
  // -------------------------------------------------------------------------
  if (mixedNet) {
    const { p1, p2, p3, O } = mixedNet;
    const perim = [p1, p2, p3];
    let topNode = perim.find(n => n === '2') || perim.find(n => n === termB) || perim[1];
    let rest = perim.filter(n => n !== topNode);
    let blNode = rest.find(n => n === '1') || rest.find(n => n === termA) || rest[0];
    let brNode = rest.find(n => n !== blNode);

    const n1 = blNode, n2 = topNode, n3 = brNode;

    const Z12 = getZeq(n1, n2);
    const Z23 = getZeq(n2, n3);
    const Z13 = getZeq(n1, n3);

    const ZO1 = getZeq(O, n1);
    const ZO2 = getZeq(O, n2);
    const ZO3 = getZeq(O, n3);

    if (Z12 && Z23 && Z13 && ZO1 && ZO2 && ZO3) {
      // ETAPA 1: Y interna -> Delta
      const sigma2 = CZ.add(CZ.add(CZ.mul(ZO1, ZO2), CZ.mul(ZO2, ZO3)), CZ.mul(ZO3, ZO1));
      const Zprime12 = CZ.div(sigma2, ZO3);
      const Zprime23 = CZ.div(sigma2, ZO1);
      const Zprime13 = CZ.div(sigma2, ZO2);

      const Zp1 = CZ.div(CZ.mul(Z12, Zprime12), CZ.add(Z12, Zprime12));
      const Zp2 = CZ.div(CZ.mul(Z23, Zprime23), CZ.add(Z23, Zprime23));
      const Zp3 = CZ.div(CZ.mul(Z13, Zprime13), CZ.add(Z13, Zprime13));

      // Coordenadas para SVG vertical amplio (viewBox: 0 0 700 340)
      const ptTop = { x: 350, y: 62, align: 'top' };
      const ptBL  = { x: 110, y: 275, align: 'bl' };
      const ptBR  = { x: 590, y: 275, align: 'br' };
      const ptO   = { x: 350, y: 205 };

      const svgEtapa1_Arriba = `
        <div class="border rounded-3 bg-white shadow-sm p-2 w-100 my-1" style="max-width:740px; margin:0 auto;">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 340" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display:block; font-family:'Plus Jakarta Sans',system-ui,sans-serif;">
            <text x="350" y="26" font-size="15" font-weight="bold" fill="black" text-anchor="middle">1. Red Original: Anillo Δ + Estrella Interna (Y)</text>
            <polygon points="350,62 590,275 110,275" fill="#3b82f6" opacity="0.08" stroke="none"/>
            ${svgRamaBloque(ptTop, ptBL, 'Z' + n1 + n2, Z12, '#1e293b')}
            ${svgRamaBloque(ptTop, ptBR, 'Z' + n2 + n3, Z23, '#1e293b')}
            ${svgRamaBloque(ptBL, ptBR, 'Z' + n1 + n3, Z13, '#1e293b')}
            ${svgRamaBloque(ptO, ptTop, 'Z' + O + n2, ZO2, '#7c3aed')}
            ${svgRamaBloque(ptO, ptBL, 'Z' + O + n1, ZO1, '#7c3aed')}
            ${svgRamaBloque(ptO, ptBR, 'Z' + O + n3, ZO3, '#7c3aed')}
            ${svgNodoO(ptO, O === '4' ? 'O' : O)}
            ${svgTerm(ptTop, n2, n2 === termA, n2 === termB)}
            ${svgTerm(ptBL, n1, n1 === termA, n1 === termB)}
            ${svgTerm(ptBR, n3, n3 === termA, n3 === termB)}
            <text x="350" y="325" font-size="12" fill="#475569" text-anchor="middle">Circuito completo ingresado en el Netlist (anillo exterior con estrella interna)</text>
          </svg>
        </div>
      `;

      const svgEtapa1_Abajo = `
        <div class="border rounded-3 bg-white shadow-sm p-2 w-100 my-1" style="max-width:740px; margin:0 auto;">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 340" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display:block; font-family:'Plus Jakarta Sans',system-ui,sans-serif;">
            <text x="350" y="26" font-size="15" font-weight="bold" fill="black" text-anchor="middle">2. Transformación Y → Δ: Ramas Homólogas en Paralelo</text>
            <polygon points="350,62 590,275 110,275" fill="#3b82f6" opacity="0.08" stroke="none"/>
            ${svgRamaBloque(ptTop, ptBL, 'Zp1 = Z' + n1 + n2 + ' ∥ Z′' + n1 + n2, Zp1, '#2563eb')}
            ${svgRamaBloque(ptTop, ptBR, 'Zp2 = Z' + n2 + n3 + ' ∥ Z′' + n2 + n3, Zp2, '#2563eb')}
            ${svgRamaBloque(ptBL, ptBR, 'Zp3 = Z' + n1 + n3 + ' ∥ Z′' + n1 + n3, Zp3, '#2563eb')}
            ${svgTerm(ptTop, n2, n2 === termA, n2 === termB)}
            ${svgTerm(ptBL, n1, n1 === termA, n1 === termB)}
            ${svgTerm(ptBR, n3, n3 === termA, n3 === termB)}
            <text x="350" y="325" font-size="12" fill="#475569" text-anchor="middle">El nodo interno desaparece y las ramas homólogas quedan en paralelo directo</text>
          </svg>
        </div>
      `;

      // ETAPA 2: Delta Consolidada -> Estrella Final
      const sigmaP = CZ.add(CZ.add(Zp1, Zp2), Zp3);
      const Zstar1 = CZ.div(CZ.mul(Zp1, Zp3), sigmaP);
      const Zstar2 = CZ.div(CZ.mul(Zp1, Zp2), sigmaP);
      const Zstar3 = CZ.div(CZ.mul(Zp2, Zp3), sigmaP);

      const ptN = { x: 350, y: 190 };
      const isN3Open = (n3 !== termA && n3 !== termB);
      const isN1Open = (n1 !== termA && n1 !== termB);
      const isN2Open = (n2 !== termA && n2 !== termB);

      const zFinalVal = CZ.add(n1 === termA ? Zstar1 : (n2 === termA ? Zstar2 : Zstar3), n1 === termB ? Zstar1 : (n2 === termB ? Zstar2 : Zstar3));

      const svgEtapa2_Arriba = `
        <div class="border rounded-3 bg-white shadow-sm p-2 w-100 my-1" style="max-width:740px; margin:0 auto;">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 340" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display:block; font-family:'Plus Jakarta Sans',system-ui,sans-serif;">
            <text x="350" y="26" font-size="15" font-weight="bold" fill="black" text-anchor="middle">1. Delta Consolidada Equivalente (Zp1, Zp2, Zp3)</text>
            <polygon points="350,62 590,275 110,275" fill="#3b82f6" opacity="0.08" stroke="none"/>
            ${svgRamaBloque(ptTop, ptBL, 'Zp1', Zp1, '#2563eb')}
            ${svgRamaBloque(ptTop, ptBR, 'Zp2', Zp2, '#2563eb')}
            ${svgRamaBloque(ptBL, ptBR, 'Zp3', Zp3, '#2563eb')}
            ${svgTerm(ptTop, n2, n2 === termA, n2 === termB)}
            ${svgTerm(ptBL, n1, n1 === termA, n1 === termB)}
            ${svgTerm(ptBR, n3, n3 === termA, n3 === termB)}
            <text x="350" y="325" font-size="12" fill="#475569" text-anchor="middle">Delta equivalente simplificada lista para transformar a Estrella</text>
          </svg>
        </div>
      `;

      const svgEtapa2_Abajo = `
        <div class="border rounded-3 bg-white shadow-sm p-2 w-100 my-1" style="max-width:740px; margin:0 auto;">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 340" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display:block; font-family:'Plus Jakarta Sans',system-ui,sans-serif;">
            <text x="350" y="26" font-size="15" font-weight="bold" fill="black" text-anchor="middle">2. Estrella Final con Reducción Serie Directa</text>
            ${svgRamaBloque(ptN, ptTop, 'Z' + n2, Zstar2, isN2Open ? '#94a3b8' : '#0891b2', isN2Open)}
            ${svgRamaBloque(ptN, ptBL, 'Z' + n1, Zstar1, isN1Open ? '#94a3b8' : '#0891b2', isN1Open)}
            ${svgRamaBloque(ptN, ptBR, 'Z' + n3, Zstar3, isN3Open ? '#94a3b8' : '#0891b2', isN3Open)}
            ${svgNodoO(ptN, 'N')}
            ${svgTerm(ptTop, n2, n2 === termA, n2 === termB, isN2Open ? '(abierto)' : '')}
            ${svgTerm(ptBL, n1, n1 === termA, n1 === termB, isN1Open ? '(abierto)' : '')}
            ${svgTerm(ptBR, n3, n3 === termA, n3 === termB, isN3Open ? '(abierto)' : '')}
            <text x="350" y="325" font-size="12.5" font-weight="bold" fill="black" text-anchor="middle">
              Zeq (${termA}–${termB}) = Z${termA} + Z${termB} = ${fmtZpolar(zFinalVal)}
            </text>
          </svg>
        </div>
      `;

      html += `
        <details class="mt-2" open>
          <summary class="small fw-bold text-primary" style="cursor:pointer; font-size:0.92rem;">
            🔄 Topología Detectada: Red Mixta — Anillo Delta (${n1}-${n2}-${n3}) con Estrella Interna (${O === '4' ? 'O/4' : O})
          </summary>
          <div class="mt-2">
            <!-- ETAPA 1 -->
            <div class="p-3 mb-3 border rounded-3 bg-white shadow-sm" style="max-width:780px; margin-left:auto; margin-right:auto;">
              <h6 class="fw-bold mb-2" style="color:#7c3aed;">
                📌 Etapa 1 — Transformación Y → Δ de la Estrella Interna (${O === '4' ? 'O' : O}) y Ramas en Paralelo
              </h6>
              <p class="small text-muted mb-2">
                Se elimina el nodo interno central <b>${O === '4' ? 'O' : O}</b> transformando sus 3 rayos a una Delta equivalente (Z′). Las ramas resultantes se asocian en paralelo con las ramas del anillo Delta exterior original.
              </p>
              ${svgEtapa1_Arriba}
              ${svgConectorVertical('Transformación Y → Δ', 'La estrella interna se convierte en delta equivalente', '#7c3aed')}
              ${svgEtapa1_Abajo}
              <div class="row g-2 mt-3">
                <div class="col-md-6">
                  <` + `table class="table table-sm table-bordered mb-0 bg-white" style="font-size:0.78rem;">
                    <thead style="background:#7c3aed15;"><tr><th colspan="2" class="text-center" style="color:#7c3aed;">1. Estrella Interna Original (Centro ${O === '4' ? 'O' : O})</th></tr></thead>
                    <tr><td class="fw-bold">Z<sub>${O}-${n1}</sub></td><td class="text-end font-monospace">${fmtZeq(ZO1)}</td></tr>
                    <tr><td class="fw-bold">Z<sub>${O}-${n2}</sub></td><td class="text-end font-monospace">${fmtZeq(ZO2)}</td></tr>
                    <tr><td class="fw-bold">Z<sub>${O}-${n3}</sub></td><td class="text-end font-monospace">${fmtZeq(ZO3)}</td></tr>
                    <tr class="table-light"><td class="fw-bold">&Sigma;<sub>2</sub></td><td class="text-end font-monospace">${fmtZeq(sigma2)}</td></tr>
                  </` + `table>
                </div>
                <div class="col-md-6">
                  <` + `table class="table table-sm table-bordered mb-0 bg-white" style="font-size:0.78rem;">
                    <thead style="background:#2563eb15;"><tr><th colspan="2" class="text-center" style="color:#2563eb;">2. Delta Equivalente &amp; Ramas en Paralelo</th></tr></thead>
                    <tr><td class="fw-bold">Z′<sub>${n1}-${n2}</sub> = &Sigma;<sub>2</sub> / Z<sub>${O}-${n3}</sub></td><td class="text-end font-monospace">${fmtZeq(Zprime12)}</td></tr>
                    <tr><td class="fw-bold">Z′<sub>${n2}-${n3}</sub> = &Sigma;<sub>2</sub> / Z<sub>${O}-${n1}</sub></td><td class="text-end font-monospace">${fmtZeq(Zprime23)}</td></tr>
                    <tr><td class="fw-bold">Z′<sub>${n1}-${n3}</sub> = &Sigma;<sub>2</sub> / Z<sub>${O}-${n2}</sub></td><td class="text-end font-monospace">${fmtZeq(Zprime13)}</td></tr>
                    <tr class="table-light"><td class="fw-bold text-primary">Z<sub>p1</sub> = Z<sub>${n1}${n2}</sub> ∥ Z′<sub>${n1}${n2}</sub></td><td class="text-end font-monospace fw-bold text-primary">${fmtZeq(Zp1)}</td></tr>
                    <tr class="table-light"><td class="fw-bold text-primary">Z<sub>p2</sub> = Z<sub>${n2}${n3}</sub> ∥ Z′<sub>${n2}${n3}</sub></td><td class="text-end font-monospace fw-bold text-primary">${fmtZeq(Zp2)}</td></tr>
                    <tr class="table-light"><td class="fw-bold text-primary">Z<sub>p3</sub> = Z<sub>${n1}${n3}</sub> ∥ Z′<sub>${n1}${n3}</sub></td><td class="text-end font-monospace fw-bold text-primary">${fmtZeq(Zp3)}</td></tr>
                  </` + `table>
                </div>
              </div>
            </div>

            <!-- ETAPA 2 -->
            <div class="p-3 mb-2 border rounded-3 bg-white shadow-sm" style="max-width:780px; margin-left:auto; margin-right:auto;">
              <h6 class="fw-bold mb-2" style="color:#0891b2;">
                📌 Etapa 2 — Transformación Δ → Y de la Delta Consolidada y Reducción Serie Final
              </h6>
              <p class="small text-muted mb-2">
                La red reducida Z<sub>p</sub> forma un único anillo Delta. Al aplicar la transformación $\Delta \to \text{Y}$, se obtiene una Estrella con centro en el nodo neutro <b>N</b>. El terminal en circuito abierto no transporta corriente, dejando una conexión serie directa.
              </p>
              ${svgEtapa2_Arriba}
              ${svgConectorVertical('Transformación Δ → Y', 'Delta consolidada se transforma a Estrella con neutro N', '#0891b2')}
              ${svgEtapa2_Abajo}
              <div class="row g-2 mt-3">
                <div class="col-md-6">
                  <` + `table class="table table-sm table-bordered mb-0 bg-white" style="font-size:0.78rem;">
                    <thead style="background:#2563eb15;"><tr><th colspan="2" class="text-center" style="color:#2563eb;">Delta Consolidada (Z<sub>p</sub>)</th></tr></thead>
                    <tr><td class="fw-bold">Z<sub>p1</sub> (Rama ${n1}-${n2})</td><td class="text-end font-monospace">${fmtZeq(Zp1)}</td></tr>
                    <tr><td class="fw-bold">Z<sub>p2</sub> (Rama ${n2}-${n3})</td><td class="text-end font-monospace">${fmtZeq(Zp2)}</td></tr>
                    <tr><td class="fw-bold">Z<sub>p3</sub> (Rama ${n1}-${n3})</td><td class="text-end font-monospace">${fmtZeq(Zp3)}</td></tr>
                    <tr class="table-light"><td class="fw-bold">&Sigma;<sub>p</sub> = Z<sub>p1</sub> + Z<sub>p2</sub> + Z<sub>p3</sub></td><td class="text-end font-monospace">${fmtZeq(sigmaP)}</td></tr>
                  </` + `table>
                </div>
                <div class="col-md-6">
                  <` + `table class="table table-sm table-bordered mb-0 bg-white" style="font-size:0.78rem;">
                    <thead style="background:#0891b215;"><tr><th colspan="2" class="text-center" style="color:#0891b2;">Estrella Final (Centro Neutro N)</th></tr></thead>
                    <tr><td class="fw-bold">Z<sub>${n1}</sub> = (Z<sub>p1</sub> &middot; Z<sub>p3</sub>) / &Sigma;<sub>p</sub></td><td class="text-end font-monospace">${fmtZeq(Zstar1)}</td></tr>
                    <tr><td class="fw-bold">Z<sub>${n2}</sub> = (Z<sub>p1</sub> &middot; Z<sub>p2</sub>) / &Sigma;<sub>p</sub></td><td class="text-end font-monospace">${fmtZeq(Zstar2)}</td></tr>
                    <tr><td class="fw-bold">Z<sub>${n3}</sub> = (Z<sub>p2</sub> &middot; Z<sub>p3</sub>) / &Sigma;<sub>p</sub></td><td class="text-end font-monospace">${fmtZeq(Zstar3)}</td></tr>
                    <tr class="table-success table-opacity-25">
                      <td class="fw-bold text-success">Z<sub>eq</sub> (${termA}–${termB}) = Z<sub>${termA}</sub> + Z<sub>${termB}</sub></td>
                      <td class="text-end font-monospace fw-bold text-success">${fmtZeq(zFinalVal)}</td>
                    </tr>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </details>`;
    }
  }

  // -------------------------------------------------------------------------
  // CASO B — RED PURAMENTE DELTA (3 NODOS VERTICAL)
  // -------------------------------------------------------------------------
  else if (pureDelta) {
    const { p1, p2, p3 } = pureDelta;
    const Z12 = getZeq(p1, p2);
    const Z23 = getZeq(p2, p3);
    const Z13 = getZeq(p1, p3);

    const Zsum = CZ.add(CZ.add(Z12, Z23), Z13);
    const Za = CZ.div(CZ.mul(Z12, Z13), Zsum);
    const Zb = CZ.div(CZ.mul(Z12, Z23), Zsum);
    const Zc = CZ.div(CZ.mul(Z13, Z23), Zsum);

    const ptTop = { x: 350, y: 62, align: 'top' };
    const ptBL  = { x: 110, y: 275, align: 'bl' };
    const ptBR  = { x: 590, y: 275, align: 'br' };
    const ptN   = { x: 350, y: 190 };

    const isP3Open = (p3 !== termA && p3 !== termB);
    const isP1Open = (p1 !== termA && p1 !== termB);
    const isP2Open = (p2 !== termA && p2 !== termB);

    const svgDelta_Arriba = `
      <div class="border rounded-3 bg-white shadow-sm p-2 w-100 my-1" style="max-width:740px; margin:0 auto;">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 340" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display:block; font-family:'Plus Jakarta Sans',system-ui,sans-serif;">
          <text x="350" y="26" font-size="15" font-weight="bold" fill="black" text-anchor="middle">Delta Original (${p1}-${p2}-${p3})</text>
          <polygon points="350,62 590,275 110,275" fill="#3b82f6" opacity="0.08" stroke="none"/>
          ${svgRamaBloque(ptTop, ptBL, 'Z' + p1 + p2, Z12, '#1e293b')}
          ${svgRamaBloque(ptTop, ptBR, 'Z' + p2 + p3, Z23, '#1e293b')}
          ${svgRamaBloque(ptBL, ptBR, 'Z' + p1 + p3, Z13, '#1e293b')}
          ${svgTerm(ptTop, p2, p2 === termA, p2 === termB)}
          ${svgTerm(ptBL, p1, p1 === termA, p1 === termB)}
          ${svgTerm(ptBR, p3, p3 === termA, p3 === termB)}
        </svg>
      </div>`;

    const svgDelta_Abajo = `
      <div class="border rounded-3 bg-white shadow-sm p-2 w-100 my-1" style="max-width:740px; margin:0 auto;">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 340" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display:block; font-family:'Plus Jakarta Sans',system-ui,sans-serif;">
          <text x="350" y="26" font-size="15" font-weight="bold" fill="black" text-anchor="middle">Estrella Equivalente (Centro N)</text>
          ${svgRamaBloque(ptN, ptTop, 'Z' + p2, Zb, isP2Open ? '#94a3b8' : '#0891b2', isP2Open)}
          ${svgRamaBloque(ptN, ptBL, 'Z' + p1, Za, isP1Open ? '#94a3b8' : '#0891b2', isP1Open)}
          ${svgRamaBloque(ptN, ptBR, 'Z' + p3, Zc, isP3Open ? '#94a3b8' : '#0891b2', isP3Open)}
          ${svgNodoO(ptN, 'N')}
          ${svgTerm(ptTop, p2, p2 === termA, p2 === termB, isP2Open ? '(abierto)' : '')}
          ${svgTerm(ptBL, p1, p1 === termA, p1 === termB, isP1Open ? '(abierto)' : '')}
          ${svgTerm(ptBR, p3, p3 === termA, p3 === termB, isP3Open ? '(abierto)' : '')}
        </svg>
      </div>`;

    html += `
      <details class="mt-2" open>
        <summary class="small fw-bold" style="cursor:pointer; color:#0891b2; font-size:0.92rem;">
          🔄 Transformación Δ → Y detectada — Triángulo ${p1}-${p2}-${p3}
        </summary>
        <div class="p-3 mt-2 border rounded-3 bg-white shadow-sm" style="max-width:780px; margin:0 auto;">
          ${svgDelta_Arriba}
          ${svgConectorVertical('Transformación Δ → Y', 'Delta se convierte en Estrella equivalente con neutro N', '#0891b2')}
          ${svgDelta_Abajo}
          <div class="row g-2 mt-3">
            <div class="col-md-6">
              <` + `table class="table table-sm table-bordered mb-0 bg-white" style="font-size:0.78rem;">
                <thead style="background:#3b82f622;"><tr><th colspan="2" class="text-center" style="color:#3b82f6;">Delta original</th></tr></thead>
                <tr><td class="fw-bold">Z<sub>${p1}-${p2}</sub></td><td class="text-end font-monospace">${fmtZeq(Z12)}</td></tr>
                <tr><td class="fw-bold">Z<sub>${p2}-${p3}</sub></td><td class="text-end font-monospace">${fmtZeq(Z23)}</td></tr>
                <tr><td class="fw-bold">Z<sub>${p1}-${p3}</sub></td><td class="text-end font-monospace">${fmtZeq(Z13)}</td></tr>
                <tr class="table-light"><td class="fw-bold">&Sigma; Z<sub>&Delta;</sub></td><td class="text-end font-monospace">${fmtZeq(Zsum)}</td></tr>
              </` + `table>
            </div>
            <div class="col-md-6">
              <` + `table class="table table-sm table-bordered mb-0 bg-white" style="font-size:0.78rem;">
                <thead style="background:#0891b222;"><tr><th colspan="2" class="text-center" style="color:#0891b2;">Estrella equivalente (Centro N)</th></tr></thead>
                <tr><td class="fw-bold">Z<sub>N-${p1}</sub></td><td class="text-end font-monospace">${fmtZeq(Za)}</td></tr>
                <tr><td class="fw-bold">Z<sub>N-${p2}</sub></td><td class="text-end font-monospace">${fmtZeq(Zb)}</td></tr>
                <tr><td class="fw-bold">Z<sub>N-${p3}</sub></td><td class="text-end font-monospace">${fmtZeq(Zc)}</td></tr>
              </` + `table>
            </div>
          </div>
        </div>
      </details>`;
  }

  // -------------------------------------------------------------------------
  // CASO C — RED PURAMENTE ESTRELLA (4 NODOS VERTICAL)
  // -------------------------------------------------------------------------
  else if (pureStar) {
    const { center, v1, v2, v3 } = pureStar;
    const Z1 = getZeq(center, v1);
    const Z2 = getZeq(center, v2);
    const Z3 = getZeq(center, v3);

    const sigma2 = CZ.add(CZ.add(CZ.mul(Z1, Z2), CZ.mul(Z2, Z3)), CZ.mul(Z3, Z1));
    const Z12 = CZ.div(sigma2, Z3);
    const Z23 = CZ.div(sigma2, Z1);
    const Z13 = CZ.div(sigma2, Z2);

    const ptTop = { x: 350, y: 62, align: 'top' };
    const ptBL  = { x: 110, y: 275, align: 'bl' };
    const ptBR  = { x: 590, y: 275, align: 'br' };
    const ptNeutro = { x: 350, y: 190 };

    const svgStar_Arriba = `
      <div class="border rounded-3 bg-white shadow-sm p-2 w-100 my-1" style="max-width:740px; margin:0 auto;">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 340" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display:block; font-family:'Plus Jakarta Sans',system-ui,sans-serif;">
          <text x="350" y="26" font-size="15" font-weight="bold" fill="black" text-anchor="middle">Estrella Original (Centro ${center})</text>
          ${svgRamaBloque(ptNeutro, ptTop, 'Z' + center + v2, Z2, '#7c3aed')}
          ${svgRamaBloque(ptNeutro, ptBL, 'Z' + center + v1, Z1, '#7c3aed')}
          ${svgRamaBloque(ptNeutro, ptBR, 'Z' + center + v3, Z3, '#7c3aed')}
          ${svgNodoO(ptNeutro, center)}
          ${svgTerm(ptTop, v2, v2 === termA, v2 === termB)}
          ${svgTerm(ptBL, v1, v1 === termA, v1 === termB)}
          ${svgTerm(ptBR, v3, v3 === termA, v3 === termB)}
        </svg>
      </div>`;

    const svgStar_Abajo = `
      <div class="border rounded-3 bg-white shadow-sm p-2 w-100 my-1" style="max-width:740px; margin:0 auto;">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 340" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display:block; font-family:'Plus Jakarta Sans',system-ui,sans-serif;">
          <text x="350" y="26" font-size="15" font-weight="bold" fill="black" text-anchor="middle">Delta Equivalente (${v1}-${v2}-${v3})</text>
          <polygon points="350,62 590,275 110,275" fill="#7c3aed" opacity="0.08" stroke="none"/>
          ${svgRamaBloque(ptTop, ptBL, 'Z' + v1 + v2, Z12, '#7c3aed')}
          ${svgRamaBloque(ptTop, ptBR, 'Z' + v2 + v3, Z23, '#7c3aed')}
          ${svgRamaBloque(ptBL, ptBR, 'Z' + v1 + v3, Z13, '#7c3aed')}
          ${svgTerm(ptTop, v2, v2 === termA, v2 === termB)}
          ${svgTerm(ptBL, v1, v1 === termA, v1 === termB)}
          ${svgTerm(ptBR, v3, v3 === termA, v3 === termB)}
        </svg>
      </div>`;

    html += `
      <details class="mt-2" open>
        <summary class="small fw-bold" style="cursor:pointer; color:#7c3aed; font-size:0.92rem;">
          🔄 Transformación Y → Δ detectada — Estrella con centro en ${center}
        </summary>
        <div class="p-3 mt-2 border rounded-3 bg-white shadow-sm" style="max-width:780px; margin:0 auto;">
          ${svgStar_Arriba}
          ${svgConectorVertical('Transformación Y → Δ', 'Estrella se convierte en Delta equivalente', '#7c3aed')}
          ${svgStar_Abajo}
          <div class="row g-2 mt-3">
            <div class="col-md-6">
              <` + `table class="table table-sm table-bordered mb-0 bg-white" style="font-size:0.78rem;">
                <thead class="table-light"><tr><th colspan="2" class="text-center">Estrella original</th></tr></thead>
                <tr><td class="fw-bold">Z<sub>${center}-${v1}</sub></td><td class="text-end font-monospace">${fmtZeq(Z1)}</td></tr>
                <tr><td class="fw-bold">Z<sub>${center}-${v2}</sub></td><td class="text-end font-monospace">${fmtZeq(Z2)}</td></tr>
                <tr><td class="fw-bold">Z<sub>${center}-${v3}</sub></td><td class="text-end font-monospace">${fmtZeq(Z3)}</td></tr>
                <tr class="table-light"><td class="fw-bold">&Sigma;<sub>2</sub></td><td class="text-end font-monospace">${fmtZeq(sigma2)}</td></tr>
              </` + `table>
            </div>
            <div class="col-md-6">
              <` + `table class="table table-sm table-bordered mb-0 bg-white" style="font-size:0.78rem;">
                <thead style="background:#7c3aed22;"><tr><th colspan="2" class="text-center" style="color:#7c3aed;">Delta equivalente</th></tr></thead>
                <tr><td class="fw-bold">Z<sub>${v1}-${v2}</sub></td><td class="text-end font-monospace">${fmtZeq(Z12)}</td></tr>
                <tr><td class="fw-bold">Z<sub>${v2}-${v3}</sub></td><td class="text-end font-monospace">${fmtZeq(Z23)}</td></tr>
                <tr><td class="fw-bold">Z<sub>${v1}-${v3}</sub></td><td class="text-end font-monospace">${fmtZeq(Z13)}</td></tr>
              </` + `table>
            </div>
          </div>
        </div>
      </details>`;
  }

  if (!html) return '';
  return `
    <div class="mt-3">
      ${html}
    </div>`;
}


/* =====================================================================
   13) Resolver red (función principal)
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
      ${renderTransformacionesDY(elementos, nodos, A, B)}
      ${renderSistemaNodal(Y, I, inc, B)}
      <details class="mt-2">
        <summary class="small fw-bold text-primary" style="cursor:pointer;">
          🔍 Ver tensiones nodales (Inyección de prueba I = 1&ang;0&deg; A)
        </summary>
        <div class="table-responsive mt-2">
          <` + `table class="table table-sm table-hover align-middle mb-0">
            <` + `thead class="table-light">
              <tr><th>Nodo</th><th class="text-end">Tensión fasorial (rect.)</th><th class="text-end">Tensión fasorial (polar)</th></tr>
            </` + `thead>
            <` + `tbody>${filas}</` + `tbody>
          </` + `table>
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
# Rama 1-2: 
1 2 3 6
1 2 3 6
# Rama 2-3: 
2 3 3 6
2 3 6 6
# Rama 1-3: 
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