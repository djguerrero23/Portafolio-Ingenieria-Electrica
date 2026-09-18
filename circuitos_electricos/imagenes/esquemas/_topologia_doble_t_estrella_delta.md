```{=html}
<div class="my-4 d-flex justify-content-center">
<div class="border rounded-3 bg-white shadow-sm p-3 w-100" style="max-width: 920px;">
<svg viewBox="0 0 950 380" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display:block; font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;">

  <text x="220" y="30" font-size="16" font-weight="bold" fill="black" text-anchor="middle">Red en Doble T (Estrellas en Paralelo)</text>
  <text x="715" y="30" font-size="16" font-weight="bold" fill="black" text-anchor="middle">Red Equivalente en Doble Π (Deltas en Paralelo)</text>

  <!-- ============ DOBLE T (izquierda) ============ -->
  <!-- Buses de Entrada (1), Salida (2) y Tierra (0) -->
  <!-- Terminal Entrada A -->
  <line x1="40" y1="160" x2="90" y2="160" stroke="black" stroke-width="1.5"/>
  <circle cx="40" cy="160" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="28" y="164" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="end">A</text>

  <!-- Bus vertical nodo 1 -->
  <line x1="90" y1="95" x2="90" y2="225" stroke="black" stroke-width="1.5"/>

  <!-- Terminal Salida B -->
  <line x1="340" y1="160" x2="390" y2="160" stroke="black" stroke-width="1.5"/>
  <circle cx="390" cy="160" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="402" y="164" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="start">B</text>

  <!-- Bus vertical nodo 2 -->
  <line x1="340" y1="95" x2="340" y2="225" stroke="black" stroke-width="1.5"/>

  <!-- Bus de Tierra 0 -->
  <line x1="80" y1="290" x2="350" y2="290" stroke="black" stroke-width="1.5"/>
  <!-- Símbolo de Tierra -->
  <line x1="215" y1="290" x2="215" y2="305" stroke="black" stroke-width="1.5"/>
  <line x1="205" y1="305" x2="225" y2="305" stroke="black" stroke-width="1.5"/>
  <line x1="209" y1="310" x2="221" y2="310" stroke="black" stroke-width="1.5"/>
  <line x1="213" y1="315" x2="217" y2="315" stroke="black" stroke-width="1.5"/>

  <!-- T Superior (Estrella 1: Z1, Z2, Z3) -->
  <!-- Rama 1 -> O1: Z1 -->
  <line x1="90" y1="95" x2="215" y2="95" stroke="black" stroke-width="1.5"/>
  <rect x="132" y="85" width="40" height="20" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="152" y="99" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">1</tspan></text>

  <!-- Rama O1 -> 2: Z2 -->
  <line x1="215" y1="95" x2="340" y2="95" stroke="black" stroke-width="1.5"/>
  <rect x="258" y="85" width="40" height="20" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="278" y="99" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">2</tspan></text>

  <!-- Rama O1 -> 0: Z3 -->
  <line x1="215" y1="95" x2="215" y2="290" stroke="black" stroke-width="1.5"/>
  <rect x="205" y="145" width="20" height="40" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="238" y="170" font-size="13" font-style="italic" fill="black" text-anchor="start">Z<tspan baseline-shift="sub" font-size="0.7em">3</tspan></text>

  <!-- T Inferior (Estrella 2: Z4, Z5, Z6) -->
  <!-- Rama 1 -> O2: Z4 -->
  <line x1="90" y1="225" x2="215" y2="225" stroke="black" stroke-width="1.5"/>
  <rect x="132" y="215" width="40" height="20" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="152" y="229" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">4</tspan></text>

  <!-- Rama O2 -> 2: Z5 -->
  <line x1="215" y1="225" x2="340" y2="225" stroke="black" stroke-width="1.5"/>
  <rect x="258" y="215" width="40" height="20" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="278" y="229" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">5</tspan></text>

  <!-- Rama O2 -> 0: Z6 -->
  <rect x="205" y="245" width="20" height="35" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="238" y="267" font-size="13" font-style="italic" fill="black" text-anchor="start">Z<tspan baseline-shift="sub" font-size="0.7em">6</tspan></text>

  <!-- Nodos Izquierda -->
  <circle cx="90" cy="160" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="78" y="155" font-size="12" font-weight="bold" fill="black" text-anchor="end">1</text>

  <circle cx="340" cy="160" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="352" y="155" font-size="12" font-weight="bold" fill="black" text-anchor="start">2</text>

  <circle cx="215" cy="95" r="3" fill="black"/>
  <text x="215" y="80" font-size="12" font-weight="bold" font-style="italic" fill="black" text-anchor="middle">O₁</text>

  <circle cx="215" cy="225" r="3" fill="black"/>
  <text x="215" y="212" font-size="12" font-weight="bold" font-style="italic" fill="black" text-anchor="middle">O₂</text>

  <circle cx="215" cy="290" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="200" y="285" font-size="12" font-weight="bold" fill="black" text-anchor="end">0</text>

  <!-- ============ BADGE Y → Δ ============ -->
  <line x1="475" y1="50" x2="475" y2="330" stroke="#94a3b8" stroke-width="1" stroke-dasharray="6 6"/>
  <rect x="453" y="163" width="44" height="34" rx="5" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
  <text x="475" y="177" font-size="12" font-weight="bold" fill="black" text-anchor="middle">Y → Δ</text>
  <text x="475" y="190" font-size="13" font-weight="bold" fill="black" text-anchor="middle">→</text>

  <!-- ============ RED TRANSFORMADA (derecha) ============ -->
  <!-- Zona sombreada del Delta resultante -->
  <polygon points="590,130 840,130 715,270" fill="#3b82f6" opacity="0.10" stroke="none"/>

  <!-- Terminales In / Out Derecha -->
  <line x1="530" y1="130" x2="590" y2="130" stroke="black" stroke-width="1.5"/>
  <circle cx="530" cy="130" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="518" y="134" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="end">A</text>

  <line x1="840" y1="130" x2="900" y2="130" stroke="black" stroke-width="1.5"/>
  <circle cx="900" cy="130" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="912" y="134" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="start">B</text>

  <!-- Lados de la Delta Equivalente -->
  <!-- Rama 1 - 2 (In - Out superior) -->
  <line x1="590" y1="130" x2="840" y2="130" stroke="black" stroke-width="1.5"/>
  <rect x="665" y="118" width="100" height="24" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="715" y="134" font-size="12" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.75em">A1</tspan> ∥ Z<tspan baseline-shift="sub" font-size="0.75em">A2</tspan></text>

  <!-- Rama 1 - 0 (In - Tierra) -->
  <line x1="590" y1="130" x2="715" y2="270" stroke="black" stroke-width="1.5"/>
  <g transform="translate(642, 205) rotate(48)">
    <rect x="-48" y="-12" width="96" height="24" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="12" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.75em">B1</tspan> ∥ Z<tspan baseline-shift="sub" font-size="0.75em">B2</tspan></text>
  </g>

  <!-- Rama 2 - 0 (Out - Tierra) -->
  <line x1="840" y1="130" x2="715" y2="270" stroke="black" stroke-width="1.5"/>
  <g transform="translate(788, 205) rotate(-48)">
    <rect x="-48" y="-12" width="96" height="24" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="12" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.75em">C1</tspan> ∥ Z<tspan baseline-shift="sub" font-size="0.75em">C2</tspan></text>
  </g>

  <!-- Conexión a Tierra Derecha -->
  <line x1="715" y1="270" x2="715" y2="295" stroke="black" stroke-width="1.5"/>
  <line x1="705" y1="295" x2="725" y2="295" stroke="black" stroke-width="1.5"/>
  <line x1="709" y1="300" x2="721" y2="300" stroke="black" stroke-width="1.5"/>
  <line x1="713" y1="305" x2="717" y2="305" stroke="black" stroke-width="1.5"/>

  <!-- Nodos Derecha -->
  <circle cx="590" cy="130" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="580" y="122" font-size="12" font-weight="bold" fill="black" text-anchor="end">1</text>

  <circle cx="840" cy="130" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="850" y="122" font-size="12" font-weight="bold" fill="black" text-anchor="start">2</text>

  <circle cx="715" cy="270" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="730" y="274" font-size="12" font-weight="bold" fill="black" text-anchor="start">0</text>

</svg>
</div>
</div>
```

La red en **Doble T** (muy empleada en filtros de muesca o notch) está compuesta por dos redes en Estrella conectadas en paralelo compartiendo los nodos externos $(1)$, $(2)$ y la referencia $(0)$, pero con neutros aislados $O_1$ y $O_2$.

Para resolverla, se transforma cada red en $\text{Y}$ a su equivalente $\Delta$:

### 1. Transformación individual $\text{Y} \to \Delta$
- **Estrella 1** ($\mathbf{Z}_1, \mathbf{Z}_2, \mathbf{Z}_3$ con neutro $O_1$):
  $$
  \Sigma_{2,1} = \mathbf{Z}_1\mathbf{Z}_2 + \mathbf{Z}_2\mathbf{Z}_3 + \mathbf{Z}_3\mathbf{Z}_1
  $$
  $$
  \mathbf{Z}_{A1} = \frac{\Sigma_{2,1}}{\mathbf{Z}_3}, \qquad
  \mathbf{Z}_{B1} = \frac{\Sigma_{2,1}}{\mathbf{Z}_2}, \qquad
  \mathbf{Z}_{C1} = \frac{\Sigma_{2,1}}{\mathbf{Z}_1}
  $$

- **Estrella 2** ($\mathbf{Z}_4, \mathbf{Z}_5, \mathbf{Z}_6$ con neutro $O_2$):
  $$
  \Sigma_{2,2} = \mathbf{Z}_4\mathbf{Z}_5 + \mathbf{Z}_5\mathbf{Z}_6 + \mathbf{Z}_6\mathbf{Z}_4
  $$
  $$
  \mathbf{Z}_{A2} = \frac{\Sigma_{2,2}}{\mathbf{Z}_6}, \qquad
  \mathbf{Z}_{B2} = \frac{\Sigma_{2,2}}{\mathbf{Z}_5}, \qquad
  \mathbf{Z}_{C2} = \frac{\Sigma_{2,2}}{\mathbf{Z}_4}
  $$

### 2. Asociación en paralelo directo
Al estar ambas Deltas conectadas exactamente a los mismos tres nodos $(1, 2, 0)$, sus ramas homólogas quedan directamente en paralelo:

$$
\boxed{\mathbf{Z}_{12} = \mathbf{Z}_{A1} \parallel \mathbf{Z}_{A2}}, \qquad
\boxed{\mathbf{Z}_{10} = \mathbf{Z}_{B1} \parallel \mathbf{Z}_{B2}}, \qquad
\boxed{\mathbf{Z}_{20} = \mathbf{Z}_{C1} \parallel \mathbf{Z}_{C2}}
$$
