::: {.card-module}
### 🔄 Calculadora Directa de Transformación $\Delta \leftrightarrow \text{Y}$ (con soporte para Ramas en Paralelo) {.unnumbered}

```{=html}
<p class="small text-muted mb-3">
  Esta herramienta calcula directamente las <b>impedancias de rama transformadas</b> aplicando las fórmulas exactas de conversión. Puedes ingresar impedancias simples ($R + jX$) o activar la opción de <b>ramas en paralelo ($Z_a \parallel Z_b$)</b> en cada lado de forma independiente.
</p>

<!-- Selector de Modo y Ejemplos -->
<div class="d-flex flex-wrap gap-2 mb-3 align-items-center">
  <div class="btn-group btn-group-sm" role="group">
    <button id="btnModoDY" class="btn btn-primary fw-bold" onclick="cambiarModoCalc('DY')">
      Modo &Delta; &rarr; Y (Delta a Estrella)
    </button>
    <button id="btnModoYD" class="btn btn-outline-primary fw-bold" onclick="cambiarModoCalc('YD')">
      Modo Y &rarr; &Delta; (Estrella a Delta)
    </button>
  </div>

  <div class="ms-auto d-flex flex-wrap gap-1">
    <button class="btn btn-xs btn-outline-secondary" style="font-size:0.75rem;" onclick="cargarCasoEj1Calc()">Ej. 1 (6&Omega;)</button>
    <button class="btn btn-xs btn-outline-secondary" style="font-size:0.75rem;" onclick="cargarCasoEj2Calc()">Ej. 2 (4&Omega;)</button>
    <button class="btn btn-xs btn-outline-primary" style="font-size:0.75rem;" onclick="cargarCasoParalelosCalc()">⚡ Delta con Paralelos (R &parallel; L)</button>
  </div>
</div>

<!-- Panel de Entradas -->
<div class="p-3 bg-light rounded-3 border mb-3">
  <div id="panelTituloEntradas" class="small fw-bold text-dark mb-2">
    📥 Ingrese las impedancias de la red Delta original (R + jX en &Omega;):
  </div>

  <div class="row g-2">
    <!-- Rama 1 -->
    <div class="col-md-4">
      <div class="p-2 bg-white rounded border shadow-sm h-100 d-flex flex-column justify-content-between">
        <div>
          <div class="d-flex justify-content-between align-items-center mb-1">
            <label id="lbl_in1" class="small fw-bold text-primary mb-0">Rama Z<sub>A</sub> (2–3):</label>
            <button id="btnPar_1" class="btn btn-xs btn-outline-secondary py-0 px-1" style="font-size:0.70rem;" onclick="toggleParalelo(1)">
              + Paralelo (&parallel;)
            </button>
          </div>

          <!-- Elemento A1 -->
          <div class="input-group input-group-sm mb-1">
            <span class="input-group-text py-0 font-monospace" style="font-size:0.75rem;">R</span>
            <input id="in1_r" type="number" step="any" class="form-control font-monospace form-control-sm" value="6" oninput="calcularTransformacionDirecta()">
            <span class="input-group-text py-0 font-monospace" style="font-size:0.75rem;">+jX</span>
            <input id="in1_i" type="number" step="any" class="form-control font-monospace form-control-sm" value="0" oninput="calcularTransformacionDirecta()">
          </div>

          <!-- Elemento A2 (Paralelo opcional) -->
          <div id="divPar_1" style="display:none;" class="mt-1 pt-1 border-top">
            <div class="small text-muted" style="font-size:0.72rem;">&parallel; Rama en paralelo:</div>
            <div class="input-group input-group-sm">
              <span class="input-group-text py-0 font-monospace" style="font-size:0.75rem;">R<sub>p</sub></span>
              <input id="in1_rp" type="number" step="any" class="form-control font-monospace form-control-sm" value="0" oninput="calcularTransformacionDirecta()">
              <span class="input-group-text py-0 font-monospace" style="font-size:0.75rem;">+jX<sub>p</sub></span>
              <input id="in1_ip" type="number" step="any" class="form-control font-monospace form-control-sm" value="0" oninput="calcularTransformacionDirecta()">
            </div>
          </div>
        </div>

        <div id="badgeZeq_1" class="small font-monospace text-muted mt-2 pt-1 border-top text-end" style="font-size:0.75rem;">
          Z<sub>eq</sub> = 6.000 &Omega;
        </div>
      </div>
    </div>

    <!-- Rama 2 -->
    <div class="col-md-4">
      <div class="p-2 bg-white rounded border shadow-sm h-100 d-flex flex-column justify-content-between">
        <div>
          <div class="d-flex justify-content-between align-items-center mb-1">
            <label id="lbl_in2" class="small fw-bold text-primary mb-0">Rama Z<sub>B</sub> (1–3):</label>
            <button id="btnPar_2" class="btn btn-xs btn-outline-secondary py-0 px-1" style="font-size:0.70rem;" onclick="toggleParalelo(2)">
              + Paralelo (&parallel;)
            </button>
          </div>

          <!-- Elemento B1 -->
          <div class="input-group input-group-sm mb-1">
            <span class="input-group-text py-0 font-monospace" style="font-size:0.75rem;">R</span>
            <input id="in2_r" type="number" step="any" class="form-control font-monospace form-control-sm" value="6" oninput="calcularTransformacionDirecta()">
            <span class="input-group-text py-0 font-monospace" style="font-size:0.75rem;">+jX</span>
            <input id="in2_i" type="number" step="any" class="form-control font-monospace form-control-sm" value="0" oninput="calcularTransformacionDirecta()">
          </div>

          <!-- Elemento B2 (Paralelo opcional) -->
          <div id="divPar_2" style="display:none;" class="mt-1 pt-1 border-top">
            <div class="small text-muted" style="font-size:0.72rem;">&parallel; Rama en paralelo:</div>
            <div class="input-group input-group-sm">
              <span class="input-group-text py-0 font-monospace" style="font-size:0.75rem;">R<sub>p</sub></span>
              <input id="in2_rp" type="number" step="any" class="form-control font-monospace form-control-sm" value="0" oninput="calcularTransformacionDirecta()">
              <span class="input-group-text py-0 font-monospace" style="font-size:0.75rem;">+jX<sub>p</sub></span>
              <input id="in2_ip" type="number" step="any" class="form-control font-monospace form-control-sm" value="0" oninput="calcularTransformacionDirecta()">
            </div>
          </div>
        </div>

        <div id="badgeZeq_2" class="small font-monospace text-muted mt-2 pt-1 border-top text-end" style="font-size:0.75rem;">
          Z<sub>eq</sub> = 6.000 &Omega;
        </div>
      </div>
    </div>

    <!-- Rama 3 -->
    <div class="col-md-4">
      <div class="p-2 bg-white rounded border shadow-sm h-100 d-flex flex-column justify-content-between">
        <div>
          <div class="d-flex justify-content-between align-items-center mb-1">
            <label id="lbl_in3" class="small fw-bold text-primary mb-0">Rama Z<sub>C</sub> (1–2):</label>
            <button id="btnPar_3" class="btn btn-xs btn-outline-secondary py-0 px-1" style="font-size:0.70rem;" onclick="toggleParalelo(3)">
              + Paralelo (&parallel;)
            </button>
          </div>

          <!-- Elemento C1 -->
          <div class="input-group input-group-sm mb-1">
            <span class="input-group-text py-0 font-monospace" style="font-size:0.75rem;">R</span>
            <input id="in3_r" type="number" step="any" class="form-control font-monospace form-control-sm" value="6" oninput="calcularTransformacionDirecta()">
            <span class="input-group-text py-0 font-monospace" style="font-size:0.75rem;">+jX</span>
            <input id="in3_i" type="number" step="any" class="form-control font-monospace form-control-sm" value="0" oninput="calcularTransformacionDirecta()">
          </div>

          <!-- Elemento C2 (Paralelo opcional) -->
          <div id="divPar_3" style="display:none;" class="mt-1 pt-1 border-top">
            <div class="small text-muted" style="font-size:0.72rem;">&parallel; Rama en paralelo:</div>
            <div class="input-group input-group-sm">
              <span class="input-group-text py-0 font-monospace" style="font-size:0.75rem;">R<sub>p</sub></span>
              <input id="in3_rp" type="number" step="any" class="form-control font-monospace form-control-sm" value="0" oninput="calcularTransformacionDirecta()">
              <span class="input-group-text py-0 font-monospace" style="font-size:0.75rem;">+jX<sub>p</sub></span>
              <input id="in3_ip" type="number" step="any" class="form-control font-monospace form-control-sm" value="0" oninput="calcularTransformacionDirecta()">
            </div>
          </div>
        </div>

        <div id="badgeZeq_3" class="small font-monospace text-muted mt-2 pt-1 border-top text-end" style="font-size:0.75rem;">
          Z<sub>eq</sub> = 6.000 &Omega;
        </div>
      </div>
    </div>
  </div>
</div>

<!-- Resultados -->
<div id="resultadoCalcDirecta"></div>

<script>
/* =====================================================================
   MÓDULO: CALCULADORA DIRECTA DELTA <-> ESTRELLA CON PARALELOS
   ===================================================================== */

let modoActualCalc = 'DY'; // 'DY' = Delta -> Y, 'YD' = Y -> Delta
const estadoParalelo = { 1: false, 2: false, 3: false };

function toggleParalelo(num) {
  estadoParalelo[num] = !estadoParalelo[num];
  const div = document.getElementById(`divPar_${num}`);
  const btn = document.getElementById(`btnPar_${num}`);
  if (div) div.style.display = estadoParalelo[num] ? 'block' : 'none';
  if (btn) {
    if (estadoParalelo[num]) {
      btn.className = 'btn btn-xs btn-danger py-0 px-1';
      btn.innerHTML = '&minus; Quitar &parallel;';
    } else {
      btn.className = 'btn btn-xs btn-outline-secondary py-0 px-1';
      btn.innerHTML = '+ Paralelo (&parallel;)';
    }
  }
  calcularTransformacionDirecta();
}

function cambiarModoCalc(modo) {
  modoActualCalc = modo;
  const btnDY = document.getElementById('btnModoDY');
  const btnYD = document.getElementById('btnModoYD');
  const titulo = document.getElementById('panelTituloEntradas');
  const l1 = document.getElementById('lbl_in1');
  const l2 = document.getElementById('lbl_in2');
  const l3 = document.getElementById('lbl_in3');

  if (modo === 'DY') {
    btnDY.className = 'btn btn-primary fw-bold';
    btnYD.className = 'btn btn-outline-primary fw-bold';
    titulo.innerHTML = '📥 Ingrese las impedancias de la red Delta original (R + jX en &Omega;):';
    l1.innerHTML = 'Rama Z<sub>A</sub> (2–3):';
    l2.innerHTML = 'Rama Z<sub>B</sub> (1–3):';
    l3.innerHTML = 'Rama Z<sub>C</sub> (1–2):';
  } else {
    btnYD.className = 'btn btn-primary fw-bold';
    btnDY.className = 'btn btn-outline-primary fw-bold';
    titulo.innerHTML = '📥 Ingrese las impedancias de la red Estrella original (R + jX en &Omega;):';
    l1.innerHTML = 'Brazo Z<sub>1</sub> (hacia 1):';
    l2.innerHTML = 'Brazo Z<sub>2</sub> (hacia 2):';
    l3.innerHTML = 'Brazo Z<sub>3</sub> (hacia 3):';
  }
  calcularTransformacionDirecta();
}

function obtenerImpedanciaRama(num) {
  const r1 = parseFloat(document.getElementById(`in${num}_r`).value) || 0;
  const i1 = parseFloat(document.getElementById(`in${num}_i`).value) || 0;
  const z1 = { r: r1, i: i1 };

  if (!estadoParalelo[num]) {
    actualizarBadgeZeq(num, z1, false);
    return z1;
  }

  const r2 = parseFloat(document.getElementById(`in${num}_rp`).value) || 0;
  const i2 = parseFloat(document.getElementById(`in${num}_ip`).value) || 0;
  const z2 = { r: r2, i: i2 };

  // Paralelo complejo Zeq = (z1 * z2) / (z1 + z2)
  const suma = CZ.add(z1, z2);
  const prod = CZ.mul(z1, z2);
  let zeq = z1;

  if (CZ.polar(suma).mag > 1e-12) {
    zeq = CZ.div(prod, suma);
  } else {
    zeq = { r: 0, i: 0 };
  }

  actualizarBadgeZeq(num, zeq, true);
  return zeq;
}

function actualizarBadgeZeq(num, z, esParalelo) {
  const badge = document.getElementById(`badgeZeq_${num}`);
  if (!badge) return;
  const p = CZ.polar(z);
  const tag = modoActualCalc === 'DY' ? (num === 1 ? 'Z<sub>A</sub>' : (num === 2 ? 'Z<sub>B</sub>' : 'Z<sub>C</sub>')) : `Z<sub>${num}</sub>`;
  const extra = esParalelo ? '<span class="badge bg-warning text-dark me-1">&parallel; eq</span>' : '';
  badge.innerHTML = `${extra}${tag} = <b>${p.mag.toFixed(3)}&ang;${p.ang.toFixed(1)}&deg;&Omega;</b> <span class="text-muted">(${fmtCorto(z)})</span>`;
}

function calcularTransformacionDirecta() {
  const out = document.getElementById('resultadoCalcDirecta');
  if (!out) return;

  const z1 = obtenerImpedanciaRama(1);
  const z2 = obtenerImpedanciaRama(2);
  const z3 = obtenerImpedanciaRama(3);

  if (modoActualCalc === 'DY') {
    // MODO DELTA -> ESTRELLA
    const ZA = z1, ZB = z2, ZC = z3;
    const Z_sum = CZ.add(CZ.add(ZA, ZB), ZC);
    const pSum = CZ.polar(Z_sum);

    if (pSum.mag < 1e-12) {
      out.innerHTML = '<div class="alert alert-danger py-2 small">Suma de impedancias nula o singular.</div>';
      return;
    }

    // Z1 = (ZB * ZC) / Z_sum
    // Z2 = (ZA * ZC) / Z_sum
    // Z3 = (ZA * ZB) / Z_sum
    const Z1_res = CZ.div(CZ.mul(ZB, ZC), Z_sum);
    const Z2_res = CZ.div(CZ.mul(ZA, ZC), Z_sum);
    const Z3_res = CZ.div(CZ.mul(ZA, ZB), Z_sum);

    const pZ1 = CZ.polar(Z1_res);
    const pZ2 = CZ.polar(Z2_res);
    const pZ3 = CZ.polar(Z3_res);

    // Impedancias terminales ZT entre bornes
    const ZT_12 = CZ.add(Z1_res, Z2_res);
    const ZT_23 = CZ.add(Z2_res, Z3_res);
    const ZT_31 = CZ.add(Z3_res, Z1_res);

    const pZT12 = CZ.polar(ZT_12);
    const pZT23 = CZ.polar(ZT_23);
    const pZT31 = CZ.polar(ZT_31);

    out.innerHTML = `
      <div class="card p-3 border-0 bg-white shadow-sm" style="border-left:4px solid #10b981 !important;">
        <div class="d-flex justify-content-between align-items-center mb-2">
          <h6 class="fw-bold mb-0 text-success">
            🎯 Ramas de la Estrella Equivalente Resultante (Z<sub>1</sub>, Z<sub>2</sub>, Z<sub>3</sub>)
          </h6>
          <span class="badge bg-success font-monospace">&Sigma; Z<sub>&Delta;</sub> = ${pSum.mag.toFixed(3)}&ang;${pSum.ang.toFixed(2)}&deg; &Omega;</span>
        </div>

        <div class="row g-2 text-center my-2">
          <div class="col-md-4">
            <div class="p-3 border rounded-3 bg-light">
              <div class="small fw-bold text-muted">Brazo Z<sub>1</sub> (Terminal 1)</div>
              <div class="fs-5 fw-bold text-dark font-monospace">${pZ1.mag.toFixed(4)} &ang; ${pZ1.ang.toFixed(2)}&deg; &Omega;</div>
              <div class="small text-muted font-monospace">(${Z1_res.r.toFixed(4)} ${Z1_res.i >= 0 ? '+' : '−'} j${Math.abs(Z1_res.i).toFixed(4)} &Omega;)</div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="p-3 border rounded-3 bg-light">
              <div class="small fw-bold text-muted">Brazo Z<sub>2</sub> (Terminal 2)</div>
              <div class="fs-5 fw-bold text-dark font-monospace">${pZ2.mag.toFixed(4)} &ang; ${pZ2.ang.toFixed(2)}&deg; &Omega;</div>
              <div class="small text-muted font-monospace">(${Z2_res.r.toFixed(4)} ${Z2_res.i >= 0 ? '+' : '−'} j${Math.abs(Z2_res.i).toFixed(4)} &Omega;)</div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="p-3 border rounded-3 bg-light">
              <div class="small fw-bold text-muted">Brazo Z<sub>3</sub> (Terminal 3)</div>
              <div class="fs-5 fw-bold text-dark font-monospace">${pZ3.mag.toFixed(4)} &ang; ${pZ3.ang.toFixed(2)}&deg; &Omega;</div>
              <div class="small text-muted font-monospace">(${Z3_res.r.toFixed(4)} ${Z3_res.i >= 0 ? '+' : '−'} j${Math.abs(Z3_res.i).toFixed(4)} &Omega;)</div>
            </div>
          </div>
        </div>

        <!-- Tabla de comprobación terminal ZT -->
        <div class="mt-3 p-2 bg-light rounded-3 border">
          <div class="small fw-bold text-dark mb-1">
            🔍 Verificación de Impedancia Terminal Equivalente (Z<sub>T</sub> entre bornes externos):
          </div>
          <div class="table-responsive">
            <` + `table class="table table-sm table-bordered bg-white mb-0 text-center" style="font-size:0.83rem;">
              <thead class="table-light">
                <tr>
                  <th>Par de bornes</th>
                  <th>Cálculo desde la Estrella resultante</th>
                  <th>Cálculo desde el Delta original</th>
                  <th class="text-success">Impedancia Total Z<sub>T</sub></th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td class="fw-bold">Terminales 1 – 2</td>
                  <td>Z<sub>1</sub> + Z<sub>2</sub></td>
                  <td>Z<sub>C</sub> &parallel; (Z<sub>A</sub> + Z<sub>B</sub>)</td>
                  <td class="font-monospace fw-bold text-success">${pZT12.mag.toFixed(4)} &ang; ${pZT12.ang.toFixed(2)}&deg; &Omega;</td>
                </tr>
                <tr>
                  <td class="fw-bold">Terminales 2 – 3</td>
                  <td>Z<sub>2</sub> + Z<sub>3</sub></td>
                  <td>Z<sub>A</sub> &parallel; (Z<sub>B</sub> + Z<sub>C</sub>)</td>
                  <td class="font-monospace fw-bold text-success">${pZT23.mag.toFixed(4)} &ang; ${pZT23.ang.toFixed(2)}&deg; &Omega;</td>
                </tr>
                <tr>
                  <td class="fw-bold">Terminales 3 – 1</td>
                  <td>Z<sub>3</sub> + Z<sub>1</sub></td>
                  <td>Z<sub>B</sub> &parallel; (Z<sub>A</sub> + Z<sub>C</sub>)</td>
                  <td class="font-monospace fw-bold text-success">${pZT31.mag.toFixed(4)} &ang; ${pZT31.ang.toFixed(2)}&deg; &Omega;</td>
                </tr>
              </tbody>
            </` + `table>
          </div>
        </div>

      </div>`;
  } else {
    // MODO ESTRELLA -> DELTA
    const Z1 = z1, Z2 = z2, Z3 = z3;

    // Sigma_2 = Z1*Z2 + Z2*Z3 + Z3*Z1
    const p12 = CZ.mul(Z1, Z2);
    const p23 = CZ.mul(Z2, Z3);
    const p31 = CZ.mul(Z3, Z1);
    const Sigma2 = CZ.add(CZ.add(p12, p23), p31);
    const pSigma2 = CZ.polar(Sigma2);

    if (CZ.polar(Z1).mag < 1e-12 || CZ.polar(Z2).mag < 1e-12 || CZ.polar(Z3).mag < 1e-12) {
      out.innerHTML = '<div class="alert alert-danger py-2 small">Una o más ramas de la estrella tienen impedancia nula.</div>';
      return;
    }

    // ZA = Sigma2 / Z1
    // ZB = Sigma2 / Z2
    // ZC = Sigma2 / Z3
    const ZA_res = CZ.div(Sigma2, Z1);
    const ZB_res = CZ.div(Sigma2, Z2);
    const ZC_res = CZ.div(Sigma2, Z3);

    const pZA = CZ.polar(ZA_res);
    const pZB = CZ.polar(ZB_res);
    const pZC = CZ.polar(ZC_res);

    // Impedancias terminales ZT
    const ZT_12 = CZ.add(Z1, Z2);
    const ZT_23 = CZ.add(Z2, Z3);
    const ZT_31 = CZ.add(Z3, Z1);

    const pZT12 = CZ.polar(ZT_12);
    const pZT23 = CZ.polar(ZT_23);
    const pZT31 = CZ.polar(ZT_31);

    out.innerHTML = `
      <div class="card p-3 border-0 bg-white shadow-sm" style="border-left:4px solid #3b82f6 !important;">
        <div class="d-flex justify-content-between align-items-center mb-2">
          <h6 class="fw-bold mb-0 text-primary">
            🎯 Ramas del Delta Equivalente Resultante (Z<sub>A</sub>, Z<sub>B</sub>, Z<sub>C</sub>)
          </h6>
          <span class="badge bg-primary font-monospace">&Sigma;<sub>2</sub> = ${pSigma2.mag.toFixed(3)}&ang;${pSigma2.ang.toFixed(2)}&deg; &Omega;<sup>2</sup></span>
        </div>

        <div class="row g-2 text-center my-2">
          <div class="col-md-4">
            <div class="p-3 border rounded-3 bg-light">
              <div class="small fw-bold text-muted">Rama Z<sub>A</sub> (Nodos 2–3)</div>
              <div class="fs-5 fw-bold text-dark font-monospace">${pZA.mag.toFixed(4)} &ang; ${pZA.ang.toFixed(2)}&deg; &Omega;</div>
              <div class="small text-muted font-monospace">(${ZA_res.r.toFixed(4)} ${ZA_res.i >= 0 ? '+' : '−'} j${Math.abs(ZA_res.i).toFixed(4)} &Omega;)</div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="p-3 border rounded-3 bg-light">
              <div class="small fw-bold text-muted">Rama Z<sub>B</sub> (Nodos 1–3)</div>
              <div class="fs-5 fw-bold text-dark font-monospace">${pZB.mag.toFixed(4)} &ang; ${pZB.ang.toFixed(2)}&deg; &Omega;</div>
              <div class="small text-muted font-monospace">(${ZB_res.r.toFixed(4)} ${ZB_res.i >= 0 ? '+' : '−'} j${Math.abs(ZB_res.i).toFixed(4)} &Omega;)</div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="p-3 border rounded-3 bg-light">
              <div class="small fw-bold text-muted">Rama Z<sub>C</sub> (Nodos 1–2)</div>
              <div class="fs-5 fw-bold text-dark font-monospace">${pZC.mag.toFixed(4)} &ang; ${pZC.ang.toFixed(2)}&deg; &Omega;</div>
              <div class="small text-muted font-monospace">(${ZC_res.r.toFixed(4)} ${ZC_res.i >= 0 ? '+' : '−'} j${Math.abs(ZC_res.i).toFixed(4)} &Omega;)</div>
            </div>
          </div>
        </div>

        <!-- Tabla de comprobación terminal ZT -->
        <div class="mt-3 p-2 bg-light rounded-3 border">
          <div class="small fw-bold text-dark mb-1">
            🔍 Verificación de Impedancia Terminal Equivalente (Z<sub>T</sub> entre bornes externos):
          </div>
          <div class="table-responsive">
            <` + `table class="table table-sm table-bordered bg-white mb-0 text-center" style="font-size:0.83rem;">
              <thead class="table-light">
                <tr>
                  <th>Par de bornes</th>
                  <th>Cálculo desde la Estrella original</th>
                  <th>Cálculo desde el Delta resultante</th>
                  <th class="text-primary">Impedancia Total Z<sub>T</sub></th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td class="fw-bold">Terminales 1 – 2</td>
                  <td>Z<sub>1</sub> + Z<sub>2</sub></td>
                  <td>Z<sub>C</sub> &parallel; (Z<sub>A</sub> + Z<sub>B</sub>)</td>
                  <td class="font-monospace fw-bold text-primary">${pZT12.mag.toFixed(4)} &ang; ${pZT12.ang.toFixed(2)}&deg; &Omega;</td>
                </tr>
                <tr>
                  <td class="fw-bold">Terminales 2 – 3</td>
                  <td>Z<sub>2</sub> + Z<sub>3</sub></td>
                  <td>Z<sub>A</sub> &parallel; (Z<sub>B</sub> + Z<sub>C</sub>)</td>
                  <td class="font-monospace fw-bold text-primary">${pZT23.mag.toFixed(4)} &ang; ${pZT23.ang.toFixed(2)}&deg; &Omega;</td>
                </tr>
                <tr>
                  <td class="fw-bold">Terminales 3 – 1</td>
                  <td>Z<sub>3</sub> + Z<sub>1</sub></td>
                  <td>Z<sub>B</sub> &parallel; (Z<sub>A</sub> + Z<sub>C</sub>)</td>
                  <td class="font-monospace fw-bold text-primary">${pZT31.mag.toFixed(4)} &ang; ${pZT31.ang.toFixed(2)}&deg; &Omega;</td>
                </tr>
              </tbody>
            </` + `table>
          </div>
        </div>

      </div>`;
  }
}

function resetearParalelos() {
  [1, 2, 3].forEach(num => {
    estadoParalelo[num] = false;
    const div = document.getElementById(`divPar_${num}`);
    const btn = document.getElementById(`btnPar_${num}`);
    if (div) div.style.display = 'none';
    if (btn) {
      btn.className = 'btn btn-xs btn-outline-secondary py-0 px-1';
      btn.innerHTML = '+ Paralelo (&parallel;)';
    }
  });
}

function cargarCasoEj1Calc() {
  resetearParalelos();
  cambiarModoCalc('DY');
  document.getElementById('in1_r').value = '6';
  document.getElementById('in1_i').value = '0';
  document.getElementById('in2_r').value = '6';
  document.getElementById('in2_i').value = '0';
  document.getElementById('in3_r').value = '6';
  document.getElementById('in3_i').value = '0';
  calcularTransformacionDirecta();
}

function cargarCasoEj2Calc() {
  resetearParalelos();
  cambiarModoCalc('YD');
  document.getElementById('in1_r').value = '4';
  document.getElementById('in1_i').value = '0';
  document.getElementById('in2_r').value = '4';
  document.getElementById('in2_i').value = '0';
  document.getElementById('in3_r').value = '4';
  document.getElementById('in3_i').value = '0';
  calcularTransformacionDirecta();
}

function cargarCasoParalelosCalc() {
  cambiarModoCalc('DY');
  // Activar paralelo en rama 1 y 2
  estadoParalelo[1] = true;
  estadoParalelo[2] = true;
  estadoParalelo[3] = false;

  [1, 2].forEach(n => {
    document.getElementById(`divPar_${n}`).style.display = 'block';
    const btn = document.getElementById(`btnPar_${n}`);
    btn.className = 'btn btn-xs btn-danger py-0 px-1';
    btn.innerHTML = '&minus; Quitar &parallel;';
  });
  document.getElementById('divPar_3').style.display = 'none';
  document.getElementById('btnPar_3').className = 'btn btn-xs btn-outline-secondary py-0 px-1';
  document.getElementById('btnPar_3').innerHTML = '+ Paralelo (&parallel;)';

  // Rama A: 6 || j12
  document.getElementById('in1_r').value = '6';
  document.getElementById('in1_i').value = '0';
  document.getElementById('in1_rp').value = '0';
  document.getElementById('in1_ip').value = '12';

  // Rama B: 10 || -j10
  document.getElementById('in2_r').value = '10';
  document.getElementById('in2_i').value = '0';
  document.getElementById('in2_rp').value = '0';
  document.getElementById('in2_ip').value = '-10';

  // Rama C: 8 + j4
  document.getElementById('in3_r').value = '8';
  document.getElementById('in3_i').value = '4';

  calcularTransformacionDirecta();
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", () => setTimeout(calcularTransformacionDirecta, 80));
} else {
  setTimeout(calcularTransformacionDirecta, 80);
}
</script>
```
:::
