```{=html}
<div class="my-4 d-flex justify-content-center">
<div class="border rounded-3 bg-white shadow-sm p-3 w-100" style="max-width: 920px;">
<svg viewBox="0 0 950 380" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display:block; font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;">

  <text x="230" y="30" font-size="16" font-weight="bold" fill="black" text-anchor="middle">Red en Puente Original (Irreducible)</text>
  <text x="705" y="30" font-size="16" font-weight="bold" fill="black" text-anchor="middle">Red Transformada (Serie–Paralelo)</text>

  <!-- ============ PUENTE (izquierda) ============ -->
  <!-- Zona sombreada de la Delta (Nodos 1-2-3) -->
  <polygon points="120,180 230,80 230,280" fill="#3b82f6" opacity="0.10" stroke="none"/>

  <!-- Terminales In / Out -->
  <line x1="50" y1="180" x2="120" y2="180" stroke="black" stroke-width="1.5"/>
  <circle cx="50" cy="180" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="38" y="184" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="end">A</text>

  <line x1="340" y1="180" x2="410" y2="180" stroke="black" stroke-width="1.5"/>
  <circle cx="410" cy="180" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="422" y="184" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="start">B</text>

  <!-- Ramas del puente -->
  <!-- 1 -> 2: Z1 -->
  <line x1="120" y1="180" x2="230" y2="80" stroke="black" stroke-width="1.5"/>
  <g transform="translate(175, 130) rotate(-42)">
    <rect x="-20" y="-10" width="40" height="20" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">1</tspan></text>
  </g>

  <!-- 1 -> 3: Z3 -->
  <line x1="120" y1="180" x2="230" y2="280" stroke="black" stroke-width="1.5"/>
  <g transform="translate(175, 230) rotate(42)">
    <rect x="-20" y="-10" width="40" height="20" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">3</tspan></text>
  </g>

  <!-- 2 -> 3: Z5 (transversal) -->
  <line x1="230" y1="80" x2="230" y2="280" stroke="black" stroke-width="1.5"/>
  <rect x="210" y="168" width="40" height="20" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="230" y="182" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">5</tspan></text>

  <!-- 2 -> 4: Z2 -->
  <line x1="230" y1="80" x2="340" y2="180" stroke="black" stroke-width="1.5"/>
  <g transform="translate(285, 130) rotate(42)">
    <rect x="-20" y="-10" width="40" height="20" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">2</tspan></text>
  </g>

  <!-- 3 -> 4: Z4 -->
  <line x1="230" y1="280" x2="340" y2="180" stroke="black" stroke-width="1.5"/>
  <g transform="translate(285, 230) rotate(-42)">
    <rect x="-20" y="-10" width="40" height="20" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">4</tspan></text>
  </g>

  <!-- Nodos del puente -->
  <circle cx="120" cy="180" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="108" y="174" font-size="12" font-weight="bold" fill="black" text-anchor="end">1</text>

  <circle cx="230" cy="80" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="230" y="65" font-size="12" font-weight="bold" fill="black" text-anchor="middle">2</text>

  <circle cx="230" cy="280" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="230" y="302" font-size="12" font-weight="bold" fill="black" text-anchor="middle">3</text>

  <circle cx="340" cy="180" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="352" y="174" font-size="12" font-weight="bold" fill="black" text-anchor="start">4</text>

  <!-- ============ Δ → Y ============ -->
  <line x1="475" y1="50" x2="475" y2="330" stroke="#94a3b8" stroke-width="1" stroke-dasharray="6 6"/>
  <rect x="453" y="163" width="44" height="34" rx="5" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
  <text x="475" y="177" font-size="12" font-weight="bold" fill="black" text-anchor="middle">Δ → Y</text>
  <text x="475" y="190" font-size="13" font-weight="bold" fill="black" text-anchor="middle">→</text>

  <!-- ============ RED TRANSFORMADA (derecha) ============ -->
  <!-- Terminales In / Out Derecha -->
  <line x1="510" y1="180" x2="560" y2="180" stroke="black" stroke-width="1.5"/>
  <circle cx="510" cy="180" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="498" y="184" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="end">A</text>

  <line x1="820" y1="180" x2="880" y2="180" stroke="black" stroke-width="1.5"/>
  <circle cx="880" cy="180" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="892" y="184" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="start">B</text>

  <!-- Estrella equivalente (ZA, ZB, ZC) -->
  <!-- Rama 1 -> O: ZA -->
  <line x1="560" y1="180" x2="640" y2="180" stroke="black" stroke-width="1.5"/>
  <rect x="580" y="170" width="40" height="20" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="600" y="184" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">A</tspan></text>

  <!-- Rama O -> 2: ZB -->
  <line x1="640" y1="180" x2="730" y2="80" stroke="black" stroke-width="1.5"/>
  <g transform="translate(685, 130) rotate(-48)">
    <rect x="-20" y="-10" width="40" height="20" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">B</tspan></text>
  </g>

  <!-- Rama O -> 3: ZC -->
  <line x1="640" y1="180" x2="730" y2="280" stroke="black" stroke-width="1.5"/>
  <g transform="translate(685, 230) rotate(48)">
    <rect x="-20" y="-10" width="40" height="20" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">C</tspan></text>
  </g>

  <!-- Ramas Z2 y Z4 -->
  <line x1="730" y1="80" x2="820" y2="180" stroke="black" stroke-width="1.5"/>
  <g transform="translate(775, 130) rotate(48)">
    <rect x="-20" y="-10" width="40" height="20" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">2</tspan></text>
  </g>

  <line x1="730" y1="280" x2="820" y2="180" stroke="black" stroke-width="1.5"/>
  <g transform="translate(775, 230) rotate(-48)">
    <rect x="-20" y="-10" width="40" height="20" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">4</tspan></text>
  </g>

  <!-- Nodos Derecha -->
  <circle cx="560" cy="180" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="548" y="174" font-size="12" font-weight="bold" fill="black" text-anchor="end">1</text>

  <circle cx="640" cy="180" r="3" fill="black"/>
  <text x="640" y="200" font-size="13" font-weight="bold" font-style="italic" fill="black" text-anchor="middle">O</text>

  <circle cx="730" cy="80" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="730" y="65" font-size="12" font-weight="bold" fill="black" text-anchor="middle">2</text>

  <circle cx="730" cy="280" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="730" y="302" font-size="12" font-weight="bold" fill="black" text-anchor="middle">3</text>

  <circle cx="820" cy="180" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="832" y="174" font-size="12" font-weight="bold" fill="black" text-anchor="start">4</text>

</svg>
</div>
</div>
```

En la red en puente original, el lazo formado por los nodos $(1)-(2)-(3)$ con ramas $\mathbf{Z}_1, \mathbf{Z}_3, \mathbf{Z}_5$ conforma un triángulo Delta que impide la reducción directa en serie o paralelo.

Al convertir dicha Delta a Estrella ($\Delta \to \text{Y}$), se introduce el nodo ficticio neutro $O$:

$$
\mathbf{Z}_\Sigma = \mathbf{Z}_1 + \mathbf{Z}_3 + \mathbf{Z}_5
$$

$$
\mathbf{Z}_A = \frac{\mathbf{Z}_1\,\mathbf{Z}_3}{\mathbf{Z}_\Sigma}, \qquad
\mathbf{Z}_B = \frac{\mathbf{Z}_1\,\mathbf{Z}_5}{\mathbf{Z}_\Sigma}, \qquad
\mathbf{Z}_C = \frac{\mathbf{Z}_3\,\mathbf{Z}_5}{\mathbf{Z}_\Sigma}
$$

La red queda transformada en una estructura totalmente reducible en **serie–paralelo**:

$$
\boxed{\mathbf{Z}_{eq} = \mathbf{Z}_A + \left[ (\mathbf{Z}_B + \mathbf{Z}_2) \parallel (\mathbf{Z}_C + \mathbf{Z}_4) \right]}
$$
