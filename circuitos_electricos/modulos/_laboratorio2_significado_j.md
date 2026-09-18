::: {.card-module}
### 🔬 Laboratorio Interactivo — ¿Qué significa realmente multiplicar por $j$? {.unnumbered}

En el plano complejo, $j$ no es solamente un símbolo algebraico.

**Multiplicar un número complejo por $j$ produce una rotación de $+90^\circ$** sin cambiar su magnitud.

Partiremos del número complejo: $z=1$

y aplicaremos sucesivamente la operación: $z \rightarrow jz \rightarrow j^2z \rightarrow j^3z \rightarrow j^4z$

Observa cómo una operación algebraica produce directamente un movimiento geométrico:

$$
\boxed{\text{multiplicar por } j \;\equiv\; \text{rotar } +90^\circ}
$$

---

## 🎯 Objetivo

Convertir el significado de $j$ en una **experiencia visual y algebraica**.

Al experimentar, debes descubrir que:

$$
j\cdot 1 = j
$$

$$
j\cdot j = j^2 = -1
$$

$$
j\cdot(-1) = -j
$$

$$
j\cdot(-j) = -j^2 = 1
$$

Por tanto:

$$
\boxed{j^4 = 1}
$$

y cada multiplicación por $j$ corresponde a una rotación de $90^\circ$.

```{=html}
<!-- ============================================================
     LABORATORIO 2 — EL SIGNIFICADO DE j
     Autocontenido para incluir en Quarto
     
     Todas las clases, IDs y funciones utilizan el prefijo lab2_
     para evitar conflictos con otros laboratorios.
     ============================================================ -->

<div class="lab2-wrapper">

  <!-- ==========================================================
       1. ENCABEZADO CONCEPTO CENTRAL
       ========================================================== -->

  <div class="p-3 mb-3 rounded-3 border shadow-sm"
       style="background:linear-gradient(135deg,#f8fafc,#eef6ff);
              border-left:5px solid #2563eb !important;">

    <div class="d-flex flex-wrap justify-content-between align-items-center gap-2">

      <div>
        <div class="small text-uppercase fw-bold text-primary mb-1"
             style="letter-spacing:.06em;">
          Operador complejo
        </div>

        <div class="fs-5 fw-bold">
          Multiplicar por <i>j</i> es rotar +90&deg;
        </div>
      </div>

      <div class="text-center px-3 py-2 rounded-3 bg-white border">
        <span class="small text-muted d-block">
          Regla geométrica
        </span>
        <strong class="text-primary">
          &times; <i>j</i> &hArr; +90&deg;
        </strong>
      </div>

    </div>

  </div>


  <!-- ==========================================================
       2. SECUENCIA VISUAL
       ========================================================== -->

  <div class="lab2-sequence-card p-3 mb-3 rounded-3 border shadow-sm bg-white">

    <div class="d-flex justify-content-between align-items-center mb-2">

      <div>
        <strong>
          <i class="bi bi-arrow-repeat me-1 text-primary"></i>
          Secuencia de rotación
        </strong>

        <div class="small text-muted">
          Cada pulsación aplica nuevamente la operación &times; <i>j</i>.
        </div>
      </div>

      <span id="lab2_stepBadge"
            class="badge bg-primary">
        Paso 0
      </span>

    </div>


    <div class="lab2-chain" id="lab2_chain">

      <div class="lab2-node active" data-step="0">
        <span class="lab2-node-value">1</span>
        <span class="lab2-node-angle">0°</span>
      </div>

      <div class="lab2-arrow">
        <span>&times; <i>j</i></span>
        <i class="bi bi-arrow-right"></i>
      </div>

      <div class="lab2-node" data-step="1">
        <span class="lab2-node-value"><i>j</i></span>
        <span class="lab2-node-angle">+90°</span>
      </div>

      <div class="lab2-arrow">
        <span>&times; <i>j</i></span>
        <i class="bi bi-arrow-right"></i>
      </div>

      <div class="lab2-node" data-step="2">
        <span class="lab2-node-value">-1</span>
        <span class="lab2-node-angle">180°</span>
      </div>

      <div class="lab2-arrow">
        <span>&times; <i>j</i></span>
        <i class="bi bi-arrow-right"></i>
      </div>

      <div class="lab2-node" data-step="3">
        <span class="lab2-node-value">-<i>j</i></span>
        <span class="lab2-node-angle">270°</span>
      </div>

      <div class="lab2-arrow">
        <span>&times; <i>j</i></span>
        <i class="bi bi-arrow-right"></i>
      </div>

      <div class="lab2-node" data-step="4">
        <span class="lab2-node-value">1</span>
        <span class="lab2-node-angle">360°</span>
      </div>

    </div>

  </div>


  <!-- ==========================================================
       3. CONTROLES
       ========================================================== -->

  <div class="lab2-controls-row mb-3">

    <div class="lab2-control-card p-3 rounded-3 border shadow-sm bg-white">

      <div class="small text-muted mb-1">
        Número complejo actual
      </div>

      <div id="lab2_currentComplex"
           class="fs-4 fw-bold text-primary">
        1
      </div>

    </div>


    <div class="lab2-control-card p-3 rounded-3 border shadow-sm bg-white">

      <div class="small text-muted mb-1">
        Operación
      </div>

      <div id="lab2_operation"
           class="fs-4 fw-bold">
        Inicial
      </div>

    </div>


    <div class="lab2-control-card p-3 rounded-3 border shadow-sm bg-white">

      <div class="small text-muted mb-1">
        Ángulo
      </div>

      <div id="lab2_angle"
           class="fs-4 fw-bold text-success">
        0°
      </div>

    </div>


    <div class="lab2-control-card p-3 rounded-3 border shadow-sm bg-white">

      <div class="small text-muted mb-1">
        Magnitud
      </div>

      <div id="lab2_magnitude"
           class="fs-4 fw-bold text-secondary">
        1
      </div>

    </div>

  </div>


  <!-- ==========================================================
       4. BOTONES DE EXPERIMENTACIÓN
       ========================================================== -->

  <div class="p-3 mb-3 rounded-3 border shadow-sm bg-light">

    <div class="d-flex flex-wrap justify-content-center gap-2">

      <button type="button"
              class="btn btn-primary fw-bold px-4"
              onclick="lab2_multiplyJ()">

        <i class="bi bi-arrow-clockwise me-1"></i>
        Multiplicar por <i>j</i>
      </button>


      <button type="button"
              class="btn btn-outline-primary fw-bold"
              onclick="lab2_multiplyMinusJ()">

        &times; (-<i>j</i>)
      </button>


      <button type="button"
              class="btn btn-outline-secondary"
              onclick="lab2_reset()">

        <i class="bi bi-arrow-counterclockwise me-1"></i>
        Reiniciar
      </button>

    </div>

  </div>


  <!-- ==========================================================
       5. VISUALIZACIÓN PRINCIPAL
       ========================================================== -->

  <div class="lab2-main-grid mb-3">


    <!-- PLANO COMPLEJO -->

    <div class="lab2-canvas-box p-2 rounded-3 border shadow-sm bg-white">

      <div class="d-flex justify-content-between align-items-center px-2 py-1">

        <span class="badge bg-secondary">
          <i class="bi bi-grid-3x3 me-1"></i>
          Plano complejo
        </span>

        <span id="lab2_rotationBadge"
              class="badge bg-primary">
          0°
        </span>

      </div>

      <div class="d-flex justify-content-center">
        <canvas id="lab2_complexCanvas"
                width="480"
                height="360">
        </canvas>
      </div>

      <div class="text-center small text-muted pb-2">
        El módulo permanece constante; la dirección cambia 90° por cada &times; <i>j</i>.
      </div>

    </div>


    <!-- INFORMACIÓN ALGEBRAICA -->

    <div class="lab2-algebra-box p-3 rounded-3 border shadow-sm bg-white">

      <div class="badge bg-secondary mb-2">
        Interpretación algebraica
      </div>

      <div id="lab2_algebraTitle"
           class="fs-5 fw-bold mb-3">
        Punto de partida
      </div>


      <div class="lab2-equation-box mb-3">

        <div class="small text-muted mb-1">
          Operación realizada
        </div>

        <div id="lab2_equation"
             class="fs-4 text-center fw-bold">
          <i>z</i> = 1
        </div>

      </div>


      <div class="lab2-result-box mb-3">

        <div class="small text-muted mb-1">
          Resultado
        </div>

        <div id="lab2_result"
             class="display-6 fw-bold text-primary text-center">
          1
        </div>

      </div>


      <div class="small text-muted">

        <div class="d-flex justify-content-between border-bottom py-2">
          <span>Parte real</span>
          <strong id="lab2_real">1</strong>
        </div>

        <div class="d-flex justify-content-between border-bottom py-2">
          <span>Parte imaginaria</span>
          <strong id="lab2_imag">0</strong>
        </div>

        <div class="d-flex justify-content-between border-bottom py-2">
          <span>Forma polar</span>
          <strong id="lab2_polar">1 &ang; 0°</strong>
        </div>

        <div class="d-flex justify-content-between py-2">
          <span>Módulo</span>
          <strong id="lab2_modulus">1</strong>
        </div>

      </div>

    </div>

  </div>


  <!-- ==========================================================
       6. EXPLICACIÓN DINÁMICA
       ========================================================== -->

  <div class="p-3 mb-3 rounded-3"
       style="background:#f0fdf4;
              border-left:4px solid #16a34a;">

    <div class="d-flex gap-2">

      <div class="fs-4 text-success">
        <i class="bi bi-lightbulb-fill"></i>
      </div>

      <div>

        <strong id="lab2_insightTitle">
          Observa
        </strong>

        <div id="lab2_insightText"
             class="mt-1">
          Partimos de 1, ubicado sobre el eje real positivo.
          Al multiplicar por <i>j</i>, el vector debe girar +90°.
        </div>

      </div>

    </div>

  </div>


  <!-- ==========================================================
       7. DEMOSTRACIÓN GENERAL
       ========================================================== -->

  <div class="p-3 rounded-3 border shadow-sm bg-white">

    <div class="small text-uppercase fw-bold text-muted mb-2"
         style="letter-spacing:.05em;">
      La regla general
    </div>

    <div class="text-center fs-5 mb-3 p-3 bg-light rounded-3 border">

      <div class="mb-1"><i>z</i> = <i>x</i> + <i>j</i><i>y</i></div>
      <div class="mb-2"><i>j</i><i>z</i> = <i>j</i>(<i>x</i> + <i>j</i><i>y</i>) = <i>j</i><i>x</i> + <i>j</i><sup>2</sup><i>y</i></div>
      <div class="fs-4 fw-bold text-primary p-2 border rounded bg-white d-inline-block shadow-sm">
        <i>j</i><i>z</i> = -<i>y</i> + <i>j</i><i>x</i>
      </div>

    </div>

    <div class="row g-2 text-center">

      <div class="col-md-4">
        <div class="p-2 rounded-3 bg-light border">
          <div class="small text-muted">
            Parte real
          </div>
          <strong>
            <i>x</i> &rarr; -<i>y</i>
          </strong>
        </div>
      </div>

      <div class="col-md-4">
        <div class="p-2 rounded-3 bg-light border">
          <div class="small text-muted">
            Parte imaginaria
          </div>
          <strong>
            <i>y</i> &rarr; <i>x</i>
          </strong>
        </div>
      </div>

      <div class="col-md-4">
        <div class="p-2 rounded-3 bg-light border">
          <div class="small text-muted">
            Rotación
          </div>
          <strong class="text-primary">
            +90°
          </strong>
        </div>
      </div>

    </div>

  </div>


  <!-- ==========================================================
       CSS
       ========================================================== -->

  <style>

    .lab2-wrapper {
      width: 100%;
      margin: 0 auto;
    }

    .lab2-sequence-card {
      overflow-x: auto;
    }

    .lab2-chain {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      min-width: 760px;
      padding: 10px 4px;
    }

    .lab2-node {
      width: 88px;
      min-width: 88px;
      padding: 9px 5px;
      border: 1px solid #cbd5e1;
      border-radius: 10px;
      background: #f8fafc;
      text-align: center;
      transition:
        transform .25s ease,
        border-color .25s ease,
        background .25s ease,
        box-shadow .25s ease;
    }

    .lab2-node.active {
      border-color: #2563eb;
      background: #eff6ff;
      box-shadow: 0 0 0 2px rgba(37,99,235,.10);
      transform: translateY(-3px);
    }

    .lab2-node-value {
      display: block;
      font-size: 1.2rem;
      font-weight: 700;
      min-height: 30px;
    }

    .lab2-node-angle {
      display: block;
      font-size: .72rem;
      color: #64748b;
      margin-top: 2px;
    }

    .lab2-arrow {
      min-width: 62px;
      text-align: center;
      color: #2563eb;
      font-size: .75rem;
      font-weight: 700;
    }

    .lab2-arrow i {
      display: block;
      font-size: 1.1rem;
      margin-top: 2px;
    }

    .lab2-controls-row {
      display: flex !important;
      flex-direction: row !important;
      flex-wrap: nowrap !important;
      gap: 10px;
      width: 100%;
    }

    .lab2-control-card {
      flex: 1 1 0 !important;
      min-width: 0 !important;
    }

    .lab2-main-grid {
      display: grid;
      grid-template-columns: 1.35fr 1fr;
      gap: 12px;
      align-items: stretch;
    }

    .lab2-canvas-box {
      min-width: 0;
    }

    #lab2_complexCanvas {
      width: 100%;
      max-width: 480px;
      height: auto;
      display: block;
      touch-action: none;
    }

    .lab2-algebra-box {
      min-width: 0;
    }

    .lab2-equation-box {
      padding: 12px;
      border-radius: 10px;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
    }

    .lab2-result-box {
      padding: 14px;
      border-radius: 10px;
      background: #eff6ff;
      border: 1px solid #bfdbfe;
    }

    @media (max-width: 850px) {

      .lab2-main-grid {
        grid-template-columns: 1fr;
      }

    }

    @media (max-width: 650px) {

      .lab2-controls-row {
        flex-wrap: wrap !important;
      }

      .lab2-control-card {
        flex: 1 1 calc(50% - 10px) !important;
      }

    }

    @media (max-width: 420px) {

      .lab2-control-card {
        flex: 1 1 100% !important;
      }

    }

  </style>


  <!-- ==========================================================
       JAVASCRIPT
       ========================================================== -->

  <script>

    const lab2_state = {

      step: 0,

      /*
       * Estados:
       *
       * 0 -> 1
       * 1 -> j
       * 2 -> -1
       * 3 -> -j
       * 4 -> 1
       */

      values: [
        { re: 1,  im: 0, label: "1",  angle: 0   },
        { re: 0,  im: 1, label: "j",  angle: 90  },
        { re: -1, im: 0, label: "-1", angle: 180 },
        { re: 0,  im: -1,label: "-j", angle: 270 },
        { re: 1,  im: 0, label: "1",  angle: 360 }
      ],

      operation: "Inicial"
    };


    /*
     * ----------------------------------------------------------
     * FORMATEO
     * ----------------------------------------------------------
     */

    function lab2_formatNumber(value) {

      if (Math.abs(value) < 1e-10) {
        return "0";
      }

      if (Math.abs(value - Math.round(value)) < 1e-10) {
        return String(Math.round(value));
      }

      return value.toFixed(3);

    }


    function lab2_complexHTML(re, im) {

      const r = lab2_formatNumber(re);
      const i = lab2_formatNumber(Math.abs(im));

      if (Math.abs(im) < 1e-10) {
        return r;
      }

      if (Math.abs(re) < 1e-10) {

        if (Math.abs(im - 1) < 1e-10) {
          return "j";
        }

        if (Math.abs(im + 1) < 1e-10) {
          return "-j";
        }

        return `${lab2_formatNumber(im)}j`;
      }

      const signo = im >= 0 ? "+" : "-";

      return `${r} ${signo} ${i}j`;

    }


    /*
     * ----------------------------------------------------------
     * MULTIPLICACIÓN POR j
     *
     * (x + jy)j
     *
     * = xj + jyj
     *
     * = xj + j²y
     *
     * = -y + jx
     * ----------------------------------------------------------
     */

    function lab2_multiplyComplexByJ(re, im) {

      return {
        re: -im,
        im: re
      };

    }


    /*
     * ----------------------------------------------------------
     * MULTIPLICACIÓN POR -j
     * ----------------------------------------------------------
     */

    function lab2_multiplyComplexByMinusJ(re, im) {

      return {
        re: im,
        im: -re
      };

    }


    /*
     * ----------------------------------------------------------
     * BOTÓN ×j
     * ----------------------------------------------------------
     */

    function lab2_multiplyJ() {

      const prevStep = lab2_state.step;
      let nextStep;

      if (lab2_state.step < 4) {
        nextStep = lab2_state.step + 1;
      } else {
        /*
         * Después de 360° volvemos a avanzar desde 90° (paso 1).
         */
        nextStep = 1;
      }

      lab2_state.prevStep = prevStep;
      lab2_state.step = nextStep;
      lab2_state.opType = "j";
      lab2_state.operation = "Multiplicar por <i>j</i> (+90&deg;)";

      lab2_update();

    }


    /*
     * ----------------------------------------------------------
     * BOTÓN ×(-j)
     * ----------------------------------------------------------
     */

    function lab2_multiplyMinusJ() {

      const prevStep = lab2_state.step;
      let nextStep;

      if (prevStep === 0 || prevStep === 4) {
        nextStep = 3;
      } else if (prevStep === 1) {
        nextStep = 0;
      } else if (prevStep === 2) {
        nextStep = 1;
      } else if (prevStep === 3) {
        nextStep = 2;
      }

      lab2_state.prevStep = prevStep;
      lab2_state.step = nextStep;
      lab2_state.opType = "minus_j";
      lab2_state.operation = "Multiplicar por (-<i>j</i>) (-90&deg;)";

      lab2_update();

    }


    /*
     * ----------------------------------------------------------
     * REINICIO
     * ----------------------------------------------------------
     */

    function lab2_reset() {

      lab2_state.prevStep = null;
      lab2_state.step = 0;
      lab2_state.opType = "init";
      lab2_state.operation = "Inicial";

      lab2_update();

    }


    /*
     * ----------------------------------------------------------
     * ACTUALIZACIÓN GENERAL
     * ----------------------------------------------------------
     */

    function lab2_update() {

      const item = lab2_state.values[lab2_state.step];

      const re = item.re;
      const im = item.im;

      const magnitude = Math.sqrt(re * re + im * im);

      let angle = item.angle;

      /*
       * Para presentación usamos el intervalo:
       * 0° ... 360°
       */
      if (angle === 360) {
        angle = 360;
      }

      /*
       * Elementos de interfaz
       */

      const current =
        document.getElementById("lab2_currentComplex");

      const operation =
        document.getElementById("lab2_operation");

      const angleEl =
        document.getElementById("lab2_angle");

      const magnitudeEl =
        document.getElementById("lab2_magnitude");

      const equation =
        document.getElementById("lab2_equation");

      const result =
        document.getElementById("lab2_result");

      const real =
        document.getElementById("lab2_real");

      const imag =
        document.getElementById("lab2_imag");

      const polar =
        document.getElementById("lab2_polar");

      const modulus =
        document.getElementById("lab2_modulus");

      const badge =
        document.getElementById("lab2_rotationBadge");

      const stepBadge =
        document.getElementById("lab2_stepBadge");


      const itemDisplay = (item.label === "j" ? "<i>j</i>" : (item.label === "-j" ? "-<i>j</i>" : item.label));

      if (current)
        current.innerHTML = itemDisplay;

      if (operation)
        operation.innerHTML =
          lab2_state.operation;

      if (angleEl)
        angleEl.innerHTML =
          `${angle}&deg;`;

      if (magnitudeEl)
        magnitudeEl.innerHTML =
          lab2_formatNumber(magnitude);

      if (badge)
        badge.innerHTML =
          `${angle}&deg;`;

      if (stepBadge)
        stepBadge.textContent =
          `Paso ${lab2_state.step}`;


      /*
       * Resultado algebraico
       */

      if (result)
        result.innerHTML = itemDisplay;


      if (real)
        real.textContent =
          lab2_formatNumber(re);

      if (imag)
        imag.textContent =
          lab2_formatNumber(im);

      if (modulus)
        modulus.textContent =
          lab2_formatNumber(magnitude);


      /*
       * Forma polar
       */

      if (polar)
        polar.innerHTML =
          `${lab2_formatNumber(magnitude)} &ang; ${angle}&deg;`;


      /*
       * Ecuación construida dinámicamente según la operación y el estado de partida
       */

      if (equation) {

        let html = "";

        if (lab2_state.opType === "init" || lab2_state.prevStep === null) {

          html = "<i>z</i> = 1";

        } else {

          const fromItem = lab2_state.values[lab2_state.prevStep];
          const fromLabel = fromItem.label;
          const fromDisplay = (fromLabel === "j" ? "<i>j</i>" : (fromLabel === "-j" ? "(-<i>j</i>)" : (fromLabel === "-1" ? "(-1)" : fromLabel)));
          const toDisplay = itemDisplay;

          if (lab2_state.opType === "j") {

            if (fromLabel === "1") {
              html = `${fromDisplay} &times; <i>j</i> = ${toDisplay}`;
            } else if (fromLabel === "j") {
              html = `${fromDisplay} &times; <i>j</i> = <i>j</i><sup>2</sup> = ${toDisplay}`;
            } else if (fromLabel === "-1") {
              html = `${fromDisplay} &times; <i>j</i> = ${toDisplay}`;
            } else if (fromLabel === "-j") {
              html = `${fromDisplay} &times; <i>j</i> = -<i>j</i><sup>2</sup> = 1`;
            }

          } else if (lab2_state.opType === "minus_j") {

            if (fromLabel === "1") {
              html = `${fromDisplay} &times; (-<i>j</i>) = ${toDisplay}`;
            } else if (fromLabel === "j") {
              html = `${fromDisplay} &times; (-<i>j</i>) = -<i>j</i><sup>2</sup> = -(-1) = 1`;
            } else if (fromLabel === "-1") {
              html = `${fromDisplay} &times; (-<i>j</i>) = <i>j</i>`;
            } else if (fromLabel === "-j") {
              html = `${fromDisplay} &times; (-<i>j</i>) = <i>j</i><sup>2</sup> = -1`;
            }

          }

        }

        equation.innerHTML = html;

      }


      /*
       * Título e interpretación dinámica
       */

      const title =
        document.getElementById("lab2_algebraTitle");

      const insightTitle =
        document.getElementById("lab2_insightTitle");

      const insightText =
        document.getElementById("lab2_insightText");

      if (lab2_state.opType === "init" || lab2_state.prevStep === null) {

        if (title) title.textContent = "Punto de partida";
        if (insightTitle) insightTitle.textContent = "Observa";
        if (insightText) {
          insightText.innerHTML =
            "Partimos de 1, ubicado sobre el eje real positivo. " +
            "Su magnitud es 1 y su ángulo es 0&deg;.";
        }

      } else {

        const fromItem = lab2_state.values[lab2_state.prevStep];
        const fromLabel = fromItem.label;
        const fromDisp = (fromLabel === "j" ? "<i>j</i>" : (fromLabel === "-j" ? "-<i>j</i>" : fromLabel));
        const toDisp = itemDisplay;

        if (lab2_state.opType === "j") {

          if (title) title.textContent = "Rotación antihoraria (+90°)";
          if (insightTitle) insightTitle.textContent = "Multiplicación por j";
          if (insightText) {
            insightText.innerHTML =
              `Al multiplicar por <i>j</i>, el fasor rota <strong>+90&deg;</strong> en sentido antihorario: ` +
              `<strong>${fromDisp}</strong> &rarr; <strong>${toDisp}</strong>. La magnitud (|<i>z</i>| = 1) no cambia.`;
          }

        } else if (lab2_state.opType === "minus_j") {

          if (title) title.textContent = "Rotación horaria (-90°)";
          if (insightTitle) insightTitle.textContent = "Multiplicación por (-j)";
          if (insightText) {
            insightText.innerHTML =
              `Al multiplicar por (-<i>j</i>), el fasor rota <strong>-90&deg;</strong> en sentido horario: ` +
              `<strong>${fromDisp}</strong> &rarr; <strong>${toDisp}</strong>. La magnitud (|<i>z</i>| = 1) no cambia.`;
          }

        }

      }


      /*
       * Actualizar cadena superior
       */

      document
        .querySelectorAll(".lab2-node")
        .forEach((node, index) => {

          node.classList.toggle(
            "active",
            index === lab2_state.step
          );

        });


      /*
       * Redibujar
       */

      lab2_drawCanvas();


      /*
       * Intentar actualizar MathJax si está disponible.
       */

      if (window.MathJax && MathJax.typesetPromise) {

        MathJax.typesetPromise();

      }

    }


    /*
     * ----------------------------------------------------------
     * DIBUJO DEL PLANO COMPLEJO
     * ----------------------------------------------------------
     */

    function lab2_drawCanvas() {

      const canvas =
        document.getElementById("lab2_complexCanvas");

      if (!canvas) return;

      const ctx =
        canvas.getContext("2d");

      const w = canvas.width;
      const h = canvas.height;

      const cx = w / 2;
      const cy = h / 2;

      /*
       * Limpiar
       */

      ctx.clearRect(0, 0, w, h);


      /*
       * Parámetros geométricos
       */

      const radius = 115;


      /*
       * Fondo
       */

      ctx.fillStyle = "#ffffff";

      ctx.fillRect(0, 0, w, h);


      /*
       * Cuadrícula
       */

      ctx.strokeStyle = "#f1f5f9";
      ctx.lineWidth = 1;

      for (let x = 20; x < w; x += 25) {

        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, h);
        ctx.stroke();

      }

      for (let y = 20; y < h; y += 25) {

        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(w, y);
        ctx.stroke();

      }


      /*
       * Ejes
       */

      ctx.strokeStyle = "#94a3b8";
      ctx.lineWidth = 1.5;

      ctx.beginPath();
      ctx.moveTo(28, cy);
      ctx.lineTo(w - 28, cy);
      ctx.stroke();

      ctx.beginPath();
      ctx.moveTo(cx, 25);
      ctx.lineTo(cx, h - 25);
      ctx.stroke();


      /*
       * Flechas de los ejes
       */

      ctx.fillStyle = "#64748b";

      ctx.beginPath();
      ctx.moveTo(w - 25, cy);
      ctx.lineTo(w - 35, cy - 5);
      ctx.lineTo(w - 35, cy + 5);
      ctx.closePath();
      ctx.fill();

      ctx.beginPath();
      ctx.moveTo(cx, 20);
      ctx.lineTo(cx - 5, 30);
      ctx.lineTo(cx + 5, 30);
      ctx.closePath();
      ctx.fill();


      /*
       * Etiquetas de ejes
       */

      ctx.font = "bold 13px sans-serif";
      ctx.fillStyle = "#475569";

      ctx.fillText(
        "Re",
        w - 48,
        cy - 10
      );

      ctx.fillText(
        "+j Im",
        cx + 10,
        35
      );


      /*
       * Circunferencia unitaria
       */

      ctx.beginPath();

      ctx.arc(
        cx,
        cy,
        radius,
        0,
        2 * Math.PI
      );

      ctx.strokeStyle = "#cbd5e1";
      ctx.lineWidth = 1.4;
      ctx.setLineDash([5,5]);
      ctx.stroke();
      ctx.setLineDash([]);


      /*
       * Puntos cardinales
       */

      const points = [

        { x: 1,  y: 0, label: "1",  lx: 8,  ly: 4  },
        { x: 0,  y: 1, label: "j",  lx: 8,  ly: -8 },
        { x: -1, y: 0, label: "-1", lx: -25, ly: 4 },
        { x: 0,  y: -1,label: "-j", lx: 8,  ly: 20 }

      ];


      ctx.font = "bold 14px sans-serif";

      points.forEach(p => {

        const px =
          cx + p.x * radius;

        const py =
          cy - p.y * radius;

        ctx.fillStyle = "#64748b";

        ctx.beginPath();

        ctx.arc(
          px,
          py,
          4,
          0,
          2 * Math.PI
        );

        ctx.fill();

        ctx.fillText(
          p.label,
          px + p.lx,
          py + p.ly
        );

      });


      /*
       * Estado actual
       */

      const item =
        lab2_state.values[lab2_state.step];

      const x =
        item.re;

      const y =
        item.im;

      const angle =
        item.angle * Math.PI / 180;


      /*
       * Vector anterior para mostrar el giro
       */

      let previousStep =
        lab2_state.step - 1;

      if (previousStep < 0)
        previousStep = 4;

      const previous =
        lab2_state.values[previousStep];

      const prevX =
        previous.re;

      const prevY =
        previous.im;


      /*
       * Vector anterior
       */

      if (lab2_state.step !== 0) {

        ctx.strokeStyle = "#cbd5e1";
        ctx.lineWidth = 2;
        ctx.setLineDash([5,4]);

        ctx.beginPath();

        ctx.moveTo(
          cx,
          cy
        );

        ctx.lineTo(
          cx + prevX * radius,
          cy - prevY * radius
        );

        ctx.stroke();

        ctx.setLineDash([]);

      }


      /*
       * Arco de rotación
       */

      if (lab2_state.step !== 0) {

        let startAngle =
          Math.atan2(-prevY, prevX);

        let endAngle =
          Math.atan2(-y, x);

        /*
         * Para mantener visualmente el sentido
         * antihorario matemático.
         */

        ctx.beginPath();

        ctx.arc(
          cx,
          cy,
          38,
          startAngle,
          endAngle,
          true
        );

        ctx.strokeStyle = "#f59e0b";
        ctx.lineWidth = 3;
        ctx.stroke();

      }


      /*
       * Vector actual
       */

      const vx =
        cx + x * radius;

      const vy =
        cy - y * radius;


      ctx.strokeStyle = "#2563eb";
      ctx.fillStyle = "#2563eb";
      ctx.lineWidth = 4;

      ctx.beginPath();

      ctx.moveTo(cx, cy);
      ctx.lineTo(vx, vy);

      ctx.stroke();


      /*
       * Punta de flecha
       */

      const head = 13;

      const direction =
        Math.atan2(
          vy - cy,
          vx - cx
        );


      ctx.beginPath();

      ctx.moveTo(
        vx,
        vy
      );

      ctx.lineTo(
        vx - head * Math.cos(direction - Math.PI / 6),
        vy - head * Math.sin(direction - Math.PI / 6)
      );

      ctx.lineTo(
        vx - head * Math.cos(direction + Math.PI / 6),
        vy - head * Math.sin(direction + Math.PI / 6)
      );

      ctx.closePath();

      ctx.fill();


      /*
       * Punto extremo
       */

      ctx.beginPath();

      ctx.arc(
        vx,
        vy,
        6,
        0,
        2 * Math.PI
      );

      ctx.fill();


      /*
       * Etiqueta del vector
       */

      ctx.font =
        "bold 15px sans-serif";

      ctx.fillStyle =
        "#2563eb";

      const labelOffset = 18;

      ctx.fillText(
        item.label,
        vx + labelOffset * Math.cos(angle),
        vy - labelOffset * Math.sin(angle)
      );


      /*
       * Texto central de la operación
       */

      if (lab2_state.step !== 0) {

        ctx.font =
          "bold 14px sans-serif";

        ctx.fillStyle =
          "#d97706";

        ctx.textAlign =
          "center";

        ctx.fillText(
          "× j  →  +90°",
          cx,
          h - 18
        );

        ctx.textAlign =
          "left";

      }


      /*
       * Origen
       */

      ctx.fillStyle =
        "#0f172a";

      ctx.beginPath();

      ctx.arc(
        cx,
        cy,
        4,
        0,
        2 * Math.PI
      );

      ctx.fill();

    }


    /*
     * ----------------------------------------------------------
     * INICIALIZACIÓN
     * ----------------------------------------------------------
     */

    function lab2_init() {

      lab2_update();

    }


    if (document.readyState === "loading") {

      document.addEventListener(
        "DOMContentLoaded",
        lab2_init
      );

    } else {

      setTimeout(
        lab2_init,
        50
      );

    }

  </script>

</div>
```

:::