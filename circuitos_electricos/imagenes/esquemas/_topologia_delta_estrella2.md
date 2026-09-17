```{=html}

<div class="my-4 d-flex justify-content-center">
<div class="border rounded-3 bg-white shadow-sm p-3 w-100" style="max-width: 100%;">
      <svg viewBox="10 10 760 320" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display:block; font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;">

      <!-- ================= 1. RED EN PUENTE (IRREDUCIBLE) ================= -->
      <text x="200" y="28" font-size="16" font-weight="bold" fill="black" text-anchor="middle">Topología de Puente (Irreducible)</text>

      <!-- Terminales Entrada / Salida Izquierda -->
      <line x1="40" y1="175" x2="100" y2="175" stroke="black" stroke-width="1.5"/>
      <circle cx="40" cy="175" r="4" fill="white" stroke="black" stroke-width="1.5"/>
      <text x="28" y="179" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="end">In</text>

      <line x1="300" y1="175" x2="360" y2="175" stroke="black" stroke-width="1.5"/>
      <circle cx="360" cy="175" r="4" fill="white" stroke="black" stroke-width="1.5"/>
      <text x="372" y="179" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="start">Out</text>

      <!-- Estructura del Rombo Izquierdo (100 a 300, centro X=200) -->
      <!-- Z1: Rama 1(100,175) a 3(200,75) -->
      <line x1="100" y1="175" x2="200" y2="75" stroke="black" stroke-width="1.5"/>
      <g transform="translate(150, 125) rotate(-45)">
        <rect x="-20" y="-10" width="40" height="20" fill="white" stroke="black" stroke-width="1.5"/>
        <text x="0" y="4" font-size="14" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">1</tspan></text>
      </g>

      <!-- Z2: Rama 3(200,75) a 2(300,175) -->
      <line x1="200" y1="75" x2="300" y2="175" stroke="black" stroke-width="1.5"/>
      <g transform="translate(250, 125) rotate(45)">
        <rect x="-20" y="-10" width="40" height="20" fill="white" stroke="black" stroke-width="1.5"/>
        <text x="0" y="4" font-size="14" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">2</tspan></text>
      </g>

      <!-- Z3: Rama 1(100,175) a 4(200,275) -->
      <line x1="100" y1="175" x2="200" y2="275" stroke="black" stroke-width="1.5"/>
      <g transform="translate(150, 225) rotate(45)">
        <rect x="-20" y="-10" width="40" height="20" fill="white" stroke="black" stroke-width="1.5"/>
        <text x="0" y="4" font-size="14" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">3</tspan></text>
      </g>

      <!-- Z4: Rama 4(200,275) a 2(300,175) -->
      <line x1="200" y1="275" x2="300" y2="175" stroke="black" stroke-width="1.5"/>
      <g transform="translate(250, 225) rotate(-45)">
        <rect x="-20" y="-10" width="40" height="20" fill="white" stroke="black" stroke-width="1.5"/>
        <text x="0" y="4" font-size="14" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">4</tspan></text>
      </g>

      <!-- Z5: Rama Central 3(200,75) a 4(200,275) -->
      <line x1="200" y1="75" x2="200" y2="275" stroke="black" stroke-width="1.5"/>
      <rect x="190" y="155" width="20" height="40" fill="white" stroke="black" stroke-width="1.5"/>
      <text x="215" y="179" font-size="14" font-style="italic" fill="black" text-anchor="start">Z<tspan baseline-shift="sub" font-size="0.7em">5</tspan></text>

      <!-- Nodos Izquierda -->
      <circle cx="100" cy="175" r="3" fill="black"/>
      <text x="90" y="165" font-size="12" fill="black">1</text>

      <circle cx="300" cy="175" r="3" fill="black"/>
      <text x="310" y="165" font-size="12" fill="black">2</text>

      <circle cx="200" cy="75" r="3" fill="black"/>
      <text x="200" y="60" font-size="12" fill="black" text-anchor="middle">3</text>

      <circle cx="200" cy="275" r="3" fill="black"/>
      <text x="200" y="295" font-size="12" fill="black" text-anchor="middle">4</text>

      <!-- Resalte visual de la Delta Izquierda a transformar -->
      <polygon points="100,175 200,75 200,275" fill="#3b82f6" opacity="0.10" stroke="none"/>

      <!-- ================= TRANSICIÓN CENTRAL (Δ → Y) ================= -->
      <line x1="440" y1="45" x2="440" y2="295" stroke="#94a3b8" stroke-width="1" stroke-dasharray="6 6"/>
      <rect x="418" y="153" width="44" height="34" rx="5" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
      <text x="440" y="167" font-size="12" font-weight="bold" fill="black" text-anchor="middle">Δ → Y</text>
      <text x="440" y="180" font-size="13" font-weight="bold" fill="black" text-anchor="middle">→</text>

      <!-- ================= 2. RED EQUIVALENTE SERIE-PARALELO (IDENTICAL ENVELOPE) ================= -->
      <text x="710" y="28" font-size="16" font-weight="bold" fill="black" text-anchor="middle">Equivalente Serie/Paralelo Reducible</text>

      <!-- Terminales Entrada / Salida Derecha -->
      <line x1="520" y1="175" x2="580" y2="175" stroke="black" stroke-width="1.5"/>
      <circle cx="520" cy="175" r="4" fill="white" stroke="black" stroke-width="1.5"/>
      <text x="508" y="179" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="end">In</text>

      <!-- Rama Za: entre Nodo 1 (580,175) y Nodo Neutro N (640,175) -->
      <line x1="580" y1="175" x2="640" y2="175" stroke="black" stroke-width="1.5"/>
      <rect x="592" y="165" width="36" height="20" fill="white" stroke="black" stroke-width="1.5"/>
      <text x="610" y="179" font-size="14" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">a</tspan></text>

      <!-- Rama Zb: entre Nodo N (640,175) y Nodo 3 (740,75) — dx=100,dy=100: mismo ángulo de 45° que el diagrama izquierdo -->
      <line x1="640" y1="175" x2="740" y2="75" stroke="black" stroke-width="1.5"/>
      <g transform="translate(690, 125) rotate(-45)">
        <rect x="-20" y="-10" width="40" height="20" fill="white" stroke="black" stroke-width="1.5"/>
        <text x="0" y="4" font-size="14" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">b</tspan></text>
      </g>

      <!-- Rama Zc: entre Nodo N (640,175) y Nodo 4 (740,275) — dx=100,dy=100: mismo ángulo de 45° -->
      <line x1="640" y1="175" x2="740" y2="275" stroke="black" stroke-width="1.5"/>
      <g transform="translate(690, 225) rotate(45)">
        <rect x="-20" y="-10" width="40" height="20" fill="white" stroke="black" stroke-width="1.5"/>
        <text x="0" y="4" font-size="14" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">c</tspan></text>
      </g>

      <!-- Z2: Rama 3(740,75) a 2(840,175) -->
      <line x1="740" y1="75" x2="840" y2="175" stroke="black" stroke-width="1.5"/>
      <g transform="translate(790, 125) rotate(45)">
        <rect x="-20" y="-10" width="40" height="20" fill="white" stroke="black" stroke-width="1.5"/>
        <text x="0" y="4" font-size="14" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">2</tspan></text>
      </g>

      <!-- Z4: Rama 4(740,275) a 2(840,175) -->
      <line x1="740" y1="275" x2="840" y2="175" stroke="black" stroke-width="1.5"/>
      <g transform="translate(790, 225) rotate(-45)">
        <rect x="-20" y="-10" width="40" height="20" fill="white" stroke="black" stroke-width="1.5"/>
        <text x="0" y="4" font-size="14" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">4</tspan></text>
      </g>

      <!-- Nodos Derecha -->
      <circle cx="580" cy="175" r="3" fill="black"/>
      <text x="570" y="165" font-size="12" fill="black">1</text>

      <circle cx="640" cy="175" r="3" fill="black"/>
      <text x="640" y="163" font-size="12" font-weight="bold" fill="black" text-anchor="middle">N</text>

      <circle cx="740" cy="75" r="3" fill="black"/>
      <text x="740" y="60" font-size="12" fill="black" text-anchor="middle">3</text>

      <circle cx="740" cy="275" r="3" fill="black"/>
      <text x="740" y="295" font-size="12" fill="black" text-anchor="middle">4</text>

      <line x1="840" y1="175" x2="900" y2="175" stroke="black" stroke-width="1.5"/>
      <circle cx="900" cy="175" r="4" fill="white" stroke="black" stroke-width="1.5"/>
      <text x="912" y="179" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="start">Out</text>

      <circle cx="840" cy="175" r="3" fill="black"/>
      <text x="850" y="165" font-size="12" fill="black">2</text>
    </svg>
  </div>
</div>
```

Las topologías que no pueden ser reducidas mediante asociaciones clásicas de serie y paralelo se denominan **redes puenteadas o complejas**. En estos circuitos, existen ramas que interconectan dos nodos de tal forma que la corriente tiene múltiples caminos de retorno, impidiendo que los componentes compartan exclusivamente la misma corriente (serie) o el mismo par de nodos (paralelo).

Para resolverlas, se emplea el **Teorema de Kennelly** (Transformación Estrella-Triángulo o $\text{Y}\text{–}\Delta$). A continuación se detallan tres ejemplos clásicos, su justificación topológica y cómo ejecutar matemáticamente la transformación para lograr un circuito equivalente reducible.

### 1. El Puente de Wheatstone Desbalanceado

Es la topología irreducible por excelencia en mediciones eléctricas e instrumentación.

* **Forma Irreducible:** Consiste en dos ramas en paralelo que están interconectadas en sus puntos medios por un resistor central. Si el puente está "desbalanceado" (el producto cruzado de sus resistencias no es igual), la corriente fluye por la rama central. El resistor central no está en serie con ninguno de los otros cuatro (las corrientes se dividen en los nodos), ni en paralelo (no comparte los mismos dos nodos con ningún otro resistor).
* **Topología Equivalente (Transformación $\Delta \to \text{Y}$):** Para hacerlo reducible, se toma uno de los "triángulos" formados en el puente (por ejemplo, el triángulo superior formado por los resistores $R_a$, $R_b$ y el central $R_c$) y se transforma en una "estrella" ($\text{Y}$) de resistores $R_1$, $R_2$ y $R_3$.
* **Ejecución del Cálculo ($\Delta \to \text{Y}$):**
  El valor de cada resistor de la nueva red en Estrella es igual al producto de los dos resistores del Triángulo que se conectan a ese mismo nodo, dividido por la suma de los tres resistores del Triángulo.

  $$R_1 = \frac{R_b \cdot R_c}{R_a + R_b + R_c}$$

  $$R_2 = \frac{R_a \cdot R_c}{R_a + R_b + R_c}$$

  $$R_3 = \frac{R_a \cdot R_b}{R_a + R_b + R_c}$$

  **Resultado topológico:** Tras aplicar esto, el resistor central desaparece. El circuito resultante tendrá dos ramas en serie pura, que luego quedarán en paralelo, resolviéndose el circuito entero.

### 2. Redes de Acoplamiento $\Pi$ (Pi) en Líneas de Transmisión

Utilizadas frecuentemente en el modelado de transformadores y líneas de transmisión (modelos de parámetros distribuidos).

* **Forma Irreducible:** Una red en $\Pi$ está formada por un resistor horizontal y dos resistores verticales conectados a tierra (o a una línea de retorno común). Si esta red se inserta entre una impedancia de fuente y una impedancia de carga, los componentes verticales no están en paralelo con la carga ni con la fuente, y el componente horizontal no está en serie con nada porque en cada extremo hay derivaciones.
* **Topología Equivalente (Transformación $\Delta \to \text{Y}$ / $\Pi \to \text{T}$):** Desde el punto de vista topológico, una red en $\Pi$ es exactamente igual a una red en Triángulo ($\Delta$), solo que el nodo inferior se dibuja estirado a lo largo de una línea. La equivalencia directa es transformarla en una red en "T" (Estrella o $\text{Y}$).
* **Ejecución del Cálculo ($\text{Y} \to \Delta$):**
  Si por el contrario tienes una red en T ($\text{Y}$) que bloquea una reducción y necesitas pasar a $\Pi$ ($\Delta$), la regla dictamina que cada resistor del Triángulo es igual a la suma de los productos cruzados de los resistores de la Estrella, dividida por el resistor de la Estrella opuesto al que se está calculando.

  $$R_a = \frac{R_1 R_2 + R_2 R_3 + R_3 R_1}{R_1}$$

  $$R_b = \frac{R_1 R_2 + R_2 R_3 + R_3 R_1}{R_2}$$

  $$R_c = \frac{R_1 R_2 + R_2 R_3 + R_3 R_1}{R_3}$$

  **Resultado topológico:** Al convertir de $\Pi$ a T, el resistor horizontal de la T queda en serie perfecta con la impedancia de carga, permitiendo colapsar esa malla.

### 3. Topología de Celosía o Puente Cruzado (Lattice Network)

Frecuente en filtros pasa-todo, ecualizadores de fase y análisis de cuadripolos.

* **Forma Irreducible:** Se dibuja típicamente como una caja o rectángulo donde hay componentes en los lados superior e inferior, y dos componentes que cruzan en diagonal el interior de la caja (formando una "X"). Ningún componente está en serie o en paralelo debido al cruce de las diagonales que conectan terminales de entrada y salida de forma opuesta.
* **Topología Equivalente (Redibujo y Transformación):**
  El primer paso no es una ecuación, sino un cambio de perspectiva topológica. Una red de celosía es, eléctricamente, un puente de Wheatstone dibujado de otra forma.
  1. Toma el nodo inferior de entrada y el nodo superior de salida, y visualízalos como los vértices laterales de un rombo.
  2. Al redibujar el circuito, los cruces en "X" se revelan como las ramas laterales de un puente.
  3. Una vez redibujado en forma de puente estándar, se aplica nuevamente la transformación $\Delta \to \text{Y}$ en uno de los nodos donde convergen tres resistores.

