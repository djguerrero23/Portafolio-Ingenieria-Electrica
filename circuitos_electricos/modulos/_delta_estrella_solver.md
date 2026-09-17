::: {.card-module}
### 🧮 Solver de redes complejas (análisis nodal) {.unnumbered}

```{=html}
<p class="small text-muted mb-2">
Escribe cada elemento como <code>nodoA nodoB R X</code>, donde la impedancia serie entre ambos nodos es
<em>Z = R + jX</em> (&Omega;). Una línea por elemento. Los símbolos <code>#</code> inician comentarios y los nodos
pueden nombrarse con números o letras.
</p>

<div style="display:flex; flex-wrap:wrap; gap:1.25rem; margin-bottom:1rem; align-items:stretch;">
<div style="flex:0 0 240px; min-width:210px; max-width:270px;">
<label class="small fw-bold">Netlist de ramas (R + jX):</label>
<textarea id="netlist" class="form-control form-control-sm font-monospace" rows="14" spellcheck="false" oninput="resolverRed()"># Red en delta de la imagen
1 2 3 6
1 2 3 6
2 3 3 6
2 3 6 6
1 3 3 6
1 3 6 6</textarea>
</div>
<div style="flex:1 1 440px;">
<label class="small fw-bold">Esquema del circuito:</label>
<div class="border rounded-3 bg-white shadow-sm p-1">
<svg id="svgCircuito" width="100%" height="380" viewBox="0 0 520 380" preserveAspectRatio="xMidYMid meet" style="background:#ffffff; border-radius:6px;"></svg>
</div>
<p class="small text-muted mt-1 mb-0">
Nodo <span style="color:#0284c7;font-weight:bold">A (+)</span>,
nodo <span style="color:#dc2626;font-weight:bold">B (−)</span>. Símbolo <span class="fw-bold">||</span> indica ramas en paralelo.
</p>
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
<button class="btn btn-sm btn-outline-secondary" onclick="cargarEjemploImagen()">Red Delta (Ejemplo)</button>
<button class="btn btn-sm btn-outline-secondary" onclick="cargarEjemploAnterior()">Red Estrella (Ejemplo)</button>
</div>

<div id="resultadoRed"></div>

<script>
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
    if (maxMag < 1e-12) throw new Error('Matriz singular (¿existen nodos aislados o flotantes?)');
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

function renderBranchTexts(Z, yOffset) {
  const r = Number(Z.r.toFixed(2));
  const x = Number(Z.i.toFixed(2));
  let html = '';
  
  if (r !== 0 && x !== 0) {
    const txtR = `R: ${r}&Omega;`;
    const txtX = x > 0 ? `I: ${x}&Omega;` : `C: ${Math.abs(x)}&Omega;`;
    html += `<text x="-16" y="${yOffset}" font-size="12" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" fill="#0f172a" text-anchor="end">${txtR}</text>`;
    html += `<text x="16" y="${yOffset}" font-size="12" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" fill="#0f172a" text-anchor="start">${txtX}</text>`;
  } else if (r !== 0) {
    html += `<text x="-16" y="${yOffset}" font-size="12" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" fill="#0f172a" text-anchor="end">R: ${r}&Omega;</text>`;
  } else if (x !== 0) {
    const txtX = x > 0 ? `I: ${x}&Omega;` : `C: ${Math.abs(x)}&Omega;`;
    html += `<text x="16" y="${yOffset}" font-size="12" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" fill="#0f172a" text-anchor="start">${txtX}</text>`;
  } else {
    html += `<text x="0" y="${yOffset}" font-size="12" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" fill="#0f172a" text-anchor="middle">0&Omega;</text>`;
  }
  return html;
}

function calcularPosiciones(nodos, elementos, W, H) {
  const nSet = new Set(nodos.map(String));
  const pos = {};

  if (nSet.size === 3 && nSet.has('1') && nSet.has('2') && nSet.has('3')) {
    pos['2'] = { x: W * 0.50, y: 55 };
    pos['1'] = { x: W * 0.16, y: 320 };
    pos['3'] = { x: W * 0.84, y: 320 };
    return pos;
  }

  if (nSet.size === 4 && nSet.has('1') && nSet.has('2') && nSet.has('3')) {
    const neutro = nodos.find(n => !['1', '2', '3'].includes(String(n)));
    pos['2'] = { x: W * 0.50, y: 55 };
    pos['1'] = { x: W * 0.16, y: 320 };
    pos['3'] = { x: W * 0.84, y: 320 };
    pos[neutro] = { x: W * 0.50, y: 205 };
    return pos;
  }

  nodos.forEach((n, i) => {
    const ang = (2 * Math.PI * i) / nodos.length - Math.PI / 2;
    pos[n] = { x: W / 2 + Math.min(W, H) * 0.40 * Math.cos(ang),
               y: H / 2 + Math.min(W, H) * 0.40 * Math.sin(ang) };
  });
  return pos;
}

function dibujarCircuito(elementos, nodos, termA, termB) {
  const svg = document.getElementById('svgCircuito');
  if (!svg) return;
  const W = 520, H = 380;
  svg.setAttribute('viewBox', `0 0 ${W} ${H}`);

  const pos = calcularPosiciones(nodos, elementos, W, H);

  let html = '';

  const grupos = {};
  elementos.forEach(el => {
    const key = [el.a, el.b].sort().join('||');
    (grupos[key] = grupos[key] || []).push(el);
  });

  Object.entries(grupos).forEach(([key, els]) => {
    const [n1, n2] = key.split('||');
    const p1 = pos[n1], p2 = pos[n2];
    if (!p1 || !p2) return;

    html += `<line x1="${p1.x}" y1="${p1.y}" x2="${p2.x}" y2="${p2.y}" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>`;

    const dx = p2.x - p1.x;
    const dy = p2.y - p1.y;
    const mx = (p1.x + p2.x) / 2;
    const my = (p1.y + p2.y) / 2;

    let deg = Math.atan2(dy, dx) * 180 / Math.PI;
    if (deg > 90 || deg < -90) {
      deg += 180;
    }

    html += `<g transform="translate(${mx}, ${my}) rotate(${deg})">`;

    if (els.length > 1) {
      // Doble barra de paralelo separada del texto
      html += `<line x1="-4" y1="-16" x2="-4" y2="24" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round"/>`;
      html += `<line x1="4" y1="-16" x2="4" y2="24" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round"/>`;

      // Rama 1 (arriba/afuera)
      html += renderBranchTexts(els[0].Z, -12);

      // Rama 2 (abajo/adentro)
      html += renderBranchTexts(els[1].Z, 22);
    } else {
      // Rama única
      html += renderBranchTexts(els[0].Z, -12);
    }

    html += `</g>`;
  });

  // Nodos circulares
  nodos.forEach(n => {
    const p = pos[n];
    if (!p) return;
    const isA = n === termA;
    const isB = n === termB;

    let fillCircle = '#bfdbfe';
    let strokeCircle = '#0284c7';
    if (isA) { fillCircle = '#93c5fd'; strokeCircle = '#0284c7'; }
    if (isB) { fillCircle = '#fecaca'; strokeCircle = '#dc2626'; }

    html += `<circle cx="${p.x}" cy="${p.y}" r="17" fill="${strokeCircle}" opacity="0.18"/>`;
    html += `<circle cx="${p.x}" cy="${p.y}" r="14" fill="${fillCircle}" stroke="${strokeCircle}" stroke-width="2.8"/>`;
    
    if (n === '1') {
      html += `<text x="${p.x - 24}" y="${p.y + 5}" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">${n}</text>`;
    } else if (n === '3') {
      html += `<text x="${p.x + 24}" y="${p.y + 5}" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">${n}</text>`;
    } else if (n === '2') {
      html += `<text x="${p.x}" y="${p.y - 22}" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">${n}</text>`;
    } else {
      html += `<text x="${p.x}" y="${p.y + 6}" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">${n}</text>`;
    }
  });

  svg.innerHTML = html;
}

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
    const svg = document.getElementById('svgCircuito');
    if (svg) svg.innerHTML = '';
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

  dibujarCircuito(elementos, nodos, A, B);

  const inc = nodos.filter(n => n !== B);
  const idx = Object.fromEntries(inc.map((n, i) => [n, i]));
  const n = inc.length;

  const Y = Array.from({ length: n }, () => Array.from({ length: n }, () => ({ r: 0, i: 0 })));
  const I = Array.from({ length: n }, () => ({ r: 0, i: 0 }));

  for (const el of elementos) {
    if (el.Z.r === 0 && el.Z.i === 0) continue;
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
  try {
    V = solveComplex(Y, I);
  } catch (e) {
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

  out.innerHTML = `
    <div class="card p-3 border-0 bg-white shadow-sm" style="border-left:4px solid #10b981 !important;">
      <div class="d-flex justify-content-between align-items-center mb-2">
        <h6 class="fw-bold mb-0" style="color:#059669;">
          🎯 Impedancia Equivalente Total Z<sub>T</sub> (entre terminales ${A} y ${B})
        </h6>
        <span class="badge bg-success">Solución Nodal</span>
      </div>
      <div class="p-3 bg-light rounded-3 my-2 text-center">
        <span class="fs-4 fw-bold text-dark">Z<sub>T</sub> = ${p.mag.toFixed(4)} &ang; ${p.ang.toFixed(2)}&deg; &Omega;</span>
        <span class="text-muted ms-2 fs-5">(${ZT.r.toFixed(4)} ${signo} j${Math.abs(ZT.i).toFixed(4)} &Omega;)</span>
      </div>
      <details class="mt-2">
        <summary class="small fw-bold text-primary" style="cursor:pointer;">
          🔍 Ver distribución de tensiones nodales (Inyección de prueba I = 1&ang;0&deg; A)
        </summary>
        <div class="table-responsive mt-2">
          <table class="table table-sm table-hover align-middle mb-0">
            <thead class="table-light">
              <tr><th>Nodo</th><th class="text-end">Tensión Fasorial (Rectangular)</th><th class="text-end">Tensión Fasorial (Polar)</th></tr>
            </thead>
            <tbody>${filas}</tbody>
          </table>
        </div>
      </details>
    </div>`;
}

function cargarEjemploImagen() {
  const nl = document.getElementById('netlist');
  if (nl) {
    nl.value =
`# Red en delta de la imagen
1 2 3 6
1 2 3 6
2 3 3 6
2 3 6 6
1 3 3 6
1 3 6 6`;
  }
  const tA = document.getElementById('termA');
  const tB = document.getElementById('termB');
  if (tA) tA.value = '1';
  if (tB) tB.value = '2';
  resolverRed();
}

function cargarEjemploAnterior() {
  const nl = document.getElementById('netlist');
  if (nl) {
    nl.value =
`# Red en Estrella (Y): 3 ramas de (1+j2 || 1+j2) conectadas a 'd'
2 d 1 2
2 d 1 2
1 d 1 2
1 d 1 2
3 d 1 2
3 d 1 2`;
  }
  const tA = document.getElementById('termA');
  const tB = document.getElementById('termB');
  if (tA) tA.value = '1';
  if (tB) tB.value = '2';
  resolverRed();
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", cargarEjemploImagen);
} else {
  setTimeout(cargarEjemploImagen, 60);
}
</script>
```
:::