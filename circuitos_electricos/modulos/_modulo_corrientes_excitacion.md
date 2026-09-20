::: {.card-module}
### ⚡ Analizador de Corrientes de Rama y Potencias bajo Tensión de Excitación {.unnumbered}

```{=html}
<p class="small text-muted mb-2">
  Este módulo calcula las <b>tensiones nodales reales</b>, la <b>corriente total de entrada (<i>I</i><sub>T</sub>)</b> y la <b>corriente fasorial exacta que circula por cada una de las ramas</b> cuando se aplica una fuente de tensión conocida <b>V</b><sub>s</sub> = <i>V</i>&ang;<i>&theta;</i><sub>V</sub> entre dos terminales de la red.
</p>

<div style="display:flex; flex-wrap:wrap; gap:1.25rem; margin-bottom:1rem; align-items:stretch;">

  <!-- Columna Netlist -->
  <div style="flex:1 1 280px; min-width:250px;">
    <label class="small fw-bold">1. Netlist de la red (R + jX):</label>
    <textarea id="netlist_corr" class="form-control form-control-sm font-monospace" rows="9" spellcheck="false" oninput="resolverCorrientesRed()"># Ejercicio 1: Delta equilibrado de 6 ohms
1 2 6 0
2 3 6 0
1 3 6 0</textarea>
    <div class="d-flex gap-2 mt-2">
      <button class="btn btn-xs btn-outline-secondary" style="font-size:0.75rem;" onclick="cargarNetlistEj1()">Delta 6&Omega; (Ej. 1)</button>
      <button class="btn btn-xs btn-outline-secondary" style="font-size:0.75rem;" onclick="cargarNetlistPuente()">Puente con fuente</button>
    </div>
  </div>

  <!-- Columna Parámetros de Excitación -->
  <div style="flex:1 1 320px; min-width:280px; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.85rem;">
    <label class="small fw-bold text-dark d-block mb-2">2. Parámetros de la Fuente de Tensión (<b>V</b><sub>s</sub>):</label>
    
    <div class="row g-2 mb-2">
      <div class="col-6">
        <label class="small text-muted" style="font-size:0.78rem;">Terminal (+) [Fuente]:</label>
        <input id="termA_corr" class="form-control form-control-sm font-monospace" value="1" oninput="resolverCorrientesRed()">
      </div>
      <div class="col-6">
        <label class="small text-muted" style="font-size:0.78rem;">Terminal (−) [Referencia]:</label>
        <input id="termB_corr" class="form-control form-control-sm font-monospace" value="2" oninput="resolverCorrientesRed()">
      </div>
    </div>

    <div class="row g-2 mb-2">
      <div class="col-6">
        <label class="small text-muted" style="font-size:0.78rem;">Magnitud <i>V</i><sub>s</sub> (V):</label>
        <input id="vs_mag" type="number" step="any" class="form-control form-control-sm font-monospace" value="12" oninput="resolverCorrientesRed()">
      </div>
      <div class="col-6">
        <label class="small text-muted" style="font-size:0.78rem;">Ángulo <i>&theta;</i><sub>V</sub> (&deg;):</label>
        <input id="vs_ang" type="number" step="any" class="form-control form-control-sm font-monospace" value="0" oninput="resolverCorrientesRed()">
      </div>
    </div>

    <button class="btn btn-sm btn-success fw-bold w-100 mt-2 shadow-sm" onclick="resolverCorrientesRed()">
      ⚡ Calcular Corrientes y Potencias
    </button>
  </div>

</div>

<div id="resultadoCorrientes"></div>

<script>
/* =====================================================================
   MÓDULO 2: RESOLVER CORRIENTES DE RAMA Y POTENCIAS REALES
   ===================================================================== */

function resolverCorrientesRed() {
  const out = document.getElementById('resultadoCorrientes');
  const netlistEl = document.getElementById('netlist_corr');
  if (!out || !netlistEl) return;

  const { elementos, nodos } = parseNetlist(netlistEl.value);
  const termAEl = document.getElementById('termA_corr');
  const termBEl = document.getElementById('termB_corr');
  const vsMagEl = document.getElementById('vs_mag');
  const vsAngEl = document.getElementById('vs_ang');

  const A = termAEl ? String(termAEl.value).trim() : '1';
  const B = termBEl ? String(termBEl.value).trim() : '2';
  const vMag = vsMagEl ? parseFloat(vsMagEl.value) : 12;
  const vAngDeg = vsAngEl ? parseFloat(vsAngEl.value) : 0;

  if (isNaN(vMag) || isNaN(vAngDeg)) {
    out.innerHTML = '<div class="alert alert-warning py-2 small">Ingrese valores numéricos válidos para la tensión de excitación.</div>';
    return;
  }

  if (!elementos.length) {
    out.innerHTML = '<div class="alert alert-warning py-2 small">Netlist vacío o con sintaxis inválida.</div>';
    return;
  }
  if (!nodos.includes(A) || !nodos.includes(B)) {
    out.innerHTML = `<div class="alert alert-warning py-2 small">Los terminales <b>${A}</b> y <b>${B}</b> deben existir en el netlist.</div>`;
    return;
  }
  if (A === B) {
    out.innerHTML = '<div class="alert alert-warning py-2 small">Los terminales de conexión deben ser distintos.</div>';
    return;
  }

  // Fasor de la fuente de tensión Vs = V_mag * (cos(ang) + j*sin(ang))
  const vAngRad = (vAngDeg * Math.PI) / 180;
  const Vs = { r: vMag * Math.cos(vAngRad), i: vMag * Math.sin(vAngRad) };

  // 1. Detección de flotantes respecto a B
  const flotantes = detectarFlotantes(elementos, nodos, B);

  // 2. Hallar Z_T mediante el sistema nodal de prueba
  const inc = nodos.filter(n => n !== B && !flotantes.includes(n));
  const idx = Object.fromEntries(inc.map((n, i) => [n, i]));
  const n = inc.length;

  const Y = Array.from({ length: n }, () => Array.from({ length: n }, () => ({ r: 0, i: 0 })));
  const I_test = Array.from({ length: n }, () => ({ r: 0, i: 0 }));

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

  I_test[idx[A]] = { r: 1, i: 0 };

  let V_unit;
  try {
    V_unit = solveComplex(Y, I_test);
  } catch (e) {
    out.innerHTML = `<div class="alert alert-danger py-2 small">${e.message}</div>`;
    return;
  }

  const ZT = V_unit[idx[A]];
  const pZT = CZ.polar(ZT);

  if (pZT.mag < 1e-12) {
    out.innerHTML = '<div class="alert alert-danger py-2 small">Cortocircuito directo entre los terminales (ZT ≈ 0 &Omega;).</div>';
    return;
  }

  // Corriente Total IT = Vs / ZT
  const IT = CZ.div(Vs, ZT);
  const pIT = CZ.polar(IT);

  // Escalar las tensiones nodales unitarias por la corriente real inyectada IT
  // V_real_node = V_unit_node * IT
  const V_nodal = {};
  nodos.forEach(nod => {
    if (nod === B) {
      V_nodal[nod] = { r: 0, i: 0 };
    } else if (flotantes.includes(nod)) {
      V_nodal[nod] = { r: 0, i: 0 };
    } else {
      V_nodal[nod] = CZ.mul(V_unit[idx[nod]], IT);
    }
  });

  // Potencia Compleja Total S = Vs * conj(IT)
  const IT_conj = { r: IT.r, i: -IT.i };
  const S_total = CZ.mul(Vs, IT_conj);
  const P_total = S_total.r;
  const Q_total = S_total.i;
  const S_mag = CZ.polar(S_total).mag;
  const FP = S_mag > 1e-9 ? P_total / S_mag : 1.0;
  const tipoFP = Q_total > 1e-6 ? 'Inductivo (en atraso)' : (Q_total < -1e-6 ? 'Capacitivo (en adelanto)' : 'Resistivo puro');

  // 3. Cálculo de corriente fasorial y potencia por cada rama del netlist
  let filasRamas = '';
  let sumP = 0, sumQ = 0;

  elementos.forEach((el, idxEl) => {
    const Va = V_nodal[el.a] || { r: 0, i: 0 };
    const Vb = V_nodal[el.b] || { r: 0, i: 0 };
    const V_rama = CZ.add(Va, { r: -Vb.r, i: -Vb.i }); // Va - Vb
    const pVrama = CZ.polar(V_rama);

    let I_rama = { r: 0, i: 0 };
    let pIrama = { mag: 0, ang: 0 };
    let S_rama = { r: 0, i: 0 };

    const pZ = CZ.polar(el.Z);
    if (pZ.mag > 1e-12) {
      I_rama = CZ.div(V_rama, el.Z);
      pIrama = CZ.polar(I_rama);
      // S_k = V_rama * conj(I_rama)
      S_rama = CZ.mul(V_rama, { r: I_rama.r, i: -I_rama.i });
    }

    sumP += S_rama.r;
    sumQ += S_rama.i;

    const signoI = I_rama.i >= 0 ? '+' : '−';
    const signoV = V_rama.i >= 0 ? '+' : '−';

    filasRamas += `<tr>
      <td class="text-center font-monospace fw-bold">${idxEl + 1}</td>
      <td><span class="badge bg-secondary">${el.a}</span> &rarr; <span class="badge bg-secondary">${el.b}</span></td>
      <td class="text-end font-monospace">${fmtCorto(el.Z)} &Omega;</td>
      <td class="text-end font-monospace text-primary">${pVrama.mag.toFixed(3)} &ang; ${pVrama.ang.toFixed(1)}&deg; V</td>
      <td class="text-end font-monospace text-success fw-bold">${pIrama.mag.toFixed(3)} &ang; ${pIrama.ang.toFixed(1)}&deg; A</td>
      <td class="text-end font-monospace small text-muted">(${I_rama.r.toFixed(3)} ${signoI} j${Math.abs(I_rama.i).toFixed(3)})</td>
      <td class="text-end font-monospace">${S_rama.r.toFixed(2)} W</td>
      <td class="text-end font-monospace">${S_rama.i >= 0 ? '+' : ''}${S_rama.i.toFixed(2)} var</td>
    </tr>`;
  });

  const signoIT = IT.i >= 0 ? '+' : '−';
  const signoVs = Vs.i >= 0 ? '+' : '−';
  const signoZT = ZT.i >= 0 ? '+' : '−';

  out.innerHTML = `
    <div class="card p-3 border-0 bg-white shadow-sm mt-3" style="border-left:4px solid #3b82f6 !important;">
      
      <!-- Resumen de Corriente Total y Potencia -->
      <div class="d-flex justify-content-between align-items-center mb-2">
        <h6 class="fw-bold mb-0 text-primary">
          📊 Respuesta en Régimen Permanente bajo Excitación <b>V</b><sub>s</sub>
        </h6>
        <span class="badge bg-primary">Fuente: ${vMag} &ang; ${vAngDeg}&deg; V</span>
      </div>

      <div class="row g-2 text-center my-2">
        <div class="col-md-4">
          <div class="p-2 border rounded bg-light">
            <div class="small text-muted">Impedancia Total Vista (<i>Z</i><sub>T</sub>)</div>
            <div class="fw-bold text-dark font-monospace">${pZT.mag.toFixed(3)} &ang; ${pZT.ang.toFixed(2)}&deg; &Omega;</div>
            <div class="small text-muted font-monospace">(${ZT.r.toFixed(3)} ${signoZT} j${Math.abs(ZT.i).toFixed(3)} &Omega;)</div>
          </div>
        </div>
        <div class="col-md-4">
          <div class="p-2 border rounded bg-primary bg-opacity-10">
            <div class="small text-primary fw-bold">⚡ Corriente Total de Entrada (<i>I</i><sub>T</sub>)</div>
            <div class="fs-5 fw-bold text-primary font-monospace">${pIT.mag.toFixed(4)} &ang; ${pIT.ang.toFixed(2)}&deg; A</div>
            <div class="small text-muted font-monospace">(${IT.r.toFixed(4)} ${signoIT} j${Math.abs(IT.i).toFixed(4)} A)</div>
          </div>
        </div>
        <div class="col-md-4">
          <div class="p-2 border rounded bg-light">
            <div class="small text-muted">Potencia Compleja Total (<i>S</i><sub>T</sub>)</div>
            <div class="fw-bold text-dark font-monospace">${S_mag.toFixed(2)} VA | FP: ${FP.toFixed(3)}</div>
            <div class="small text-muted font-monospace">P = ${P_total.toFixed(2)} W | Q = ${Q_total.toFixed(2)} var</div>
          </div>
        </div>
      </div>

      <!-- Tabla de Corrientes por Rama -->
      <div class="mt-3">
        <h6 class="small fw-bold text-dark mb-1">📋 Corrientes fasoriales y potencias en cada elemento de la red:</h6>
        <div class="table-responsive">
          <table class="table table-sm table-hover align-middle mb-0" style="font-size:0.83rem;">
            <thead class="table-light">
              <tr>
                <th class="text-center">#</th>
                <th>Rama</th>
                <th class="text-end">Impedancia <i>Z</i></th>
                <th class="text-end">Tensión de rama <i>V</i><sub>rama</sub></th>
                <th class="text-end text-success">Corriente <i>I</i><sub>rama</sub> (Polar)</th>
                <th class="text-end text-muted">Corriente (Rect.)</th>
                <th class="text-end">P (Activa)</th>
                <th class="text-end">Q (Reactiva)</th>
              </tr>
            </thead>
            <tbody>
              ${filasRamas}
            </tbody>
            <tfoot class="table-light fw-bold">
              <tr>
                <td colspan="6" class="text-end">Balance Total (Tellegen):</td>
                <td class="text-end font-monospace text-primary">${sumP.toFixed(2)} W</td>
                <td class="text-end font-monospace text-primary">${sumQ >= 0 ? '+' : ''}${sumQ.toFixed(2)} var</td>
              </tr>
            </tfoot>
          </table>
        </div>
        <div class="small text-muted mt-1 text-end" style="font-size:0.75rem;">
          * Las corrientes se orientan según el sentido de definición nodo <i>a</i> &rarr; nodo <i>b</i>.
        </div>
      </div>

    </div>
  `;
}

function cargarNetlistEj1() {
  const nl = document.getElementById('netlist_corr');
  if (nl) nl.value = 
`# Ejercicio 1: Delta equilibrado de 6 ohms
1 2 6 0
2 3 6 0
1 3 6 0`;
  const tA = document.getElementById('termA_corr');
  const tB = document.getElementById('termB_corr');
  const vM = document.getElementById('vs_mag');
  const vA = document.getElementById('vs_ang');
  if (tA) tA.value = '1';
  if (tB) tB.value = '2';
  if (vM) vM.value = '12';
  if (vA) vA.value = '0';
  resolverCorrientesRed();
}

function cargarNetlistPuente() {
  const nl = document.getElementById('netlist_corr');
  if (nl) nl.value = 
`# Red Puente en AC con cargas reactivas
1 2 10 0
1 3 0 15
2 4 0 -10
3 4 20 0
2 3 5 5`;
  const tA = document.getElementById('termA_corr');
  const tB = document.getElementById('termB_corr');
  const vM = document.getElementById('vs_mag');
  const vA = document.getElementById('vs_ang');
  if (tA) tA.value = '1';
  if (tB) tB.value = '4';
  if (vM) vM.value = '120';
  if (vA) vA.value = '0';
  resolverCorrientesRed();
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", () => setTimeout(resolverCorrientesRed, 120));
} else {
  setTimeout(resolverCorrientesRed, 120);
}
</script>
```
:::
