```{=html}
<!-- ================= ETAPA 1: ESTRELLA INTERNA A DELTA ================= -->
<div class="my-4 d-flex justify-content-center">
<div class="border rounded-3 bg-white shadow-sm p-3 w-100" style="max-width: 920px;">
<svg viewBox="0 0 950 300" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display:block; font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;">

  <text x="225" y="24" font-size="16" font-weight="bold" fill="black" text-anchor="middle">1. Anillo Δ + Estrella Interna (Y)</text>
  <text x="725" y="24" font-size="16" font-weight="bold" fill="black" text-anchor="middle">2. Transformación Y → Δ: Ramas en Paralelo</text>

  <!-- ============ 1. RED MIXTA (izquierda) ============ -->
  <!-- Anillo exterior: Delta A-B-C -->
  <!-- Rama A-B -->
  <line x1="225" y1="65" x2="370" y2="225" stroke="black" stroke-width="1.5"/>
  <g transform="translate(298, 145) rotate(48)">
    <rect x="-24" y="-11" width="48" height="22" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">AB</tspan></text>
  </g>

  <!-- Rama A-C -->
  <line x1="225" y1="65" x2="80" y2="225" stroke="black" stroke-width="1.5"/>
  <g transform="translate(152, 145) rotate(-48)">
    <rect x="-24" y="-11" width="48" height="22" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">CA</tspan></text>
  </g>

  <!-- Rama B-C -->
  <line x1="370" y1="225" x2="80" y2="225" stroke="black" stroke-width="1.5"/>
  <rect x="201" y="214" width="48" height="22" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="225" y="229" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">BC</tspan></text>

  <!-- Estrella interna: O-A -->
  <line x1="225" y1="170" x2="225" y2="65" stroke="black" stroke-width="1.5"/>
  <rect x="214" y="100" width="22" height="40" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="248" y="125" font-size="13" font-style="italic" fill="black" text-anchor="start">Z<tspan baseline-shift="sub" font-size="0.7em">a</tspan></text>

  <!-- Estrella interna: O-B -->
  <line x1="225" y1="170" x2="370" y2="225" stroke="black" stroke-width="1.5"/>
  <g transform="translate(298, 198) rotate(21)">
    <rect x="-20" y="-10" width="40" height="20" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">b</tspan></text>
  </g>

  <!-- Estrella interna: O-C -->
  <line x1="225" y1="170" x2="80" y2="225" stroke="black" stroke-width="1.5"/>
  <g transform="translate(152, 198) rotate(-21)">
    <rect x="-20" y="-10" width="40" height="20" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">c</tspan></text>
  </g>

  <circle cx="225" cy="170" r="3" fill="black"/>
  <text x="225" y="190" font-size="12" font-weight="bold" font-style="italic" fill="black" text-anchor="middle">O</text>

  <!-- Terminales Izquierda -->
  <circle cx="225" cy="65"  r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="370" cy="225" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="80"  cy="225" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="225" y="48" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="middle">A</text>
  <text x="385" y="230" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="start">B</text>
  <text x="65"  y="230" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="end">C</text>

  <text x="225" y="275" font-size="12" fill="#475569" text-anchor="middle">Impedancia equivalente vista entre terminales A y B</text>

  <!-- ============ BADGE Y → Δ ============ -->
  <line x1="475" y1="45" x2="475" y2="275" stroke="#94a3b8" stroke-width="1" stroke-dasharray="6 6"/>
  <rect x="443" y="142" width="64" height="36" rx="6" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
  <text x="475" y="157" font-size="11" font-weight="bold" fill="black" text-anchor="middle">Y → Δ</text>
  <text x="475" y="171" font-size="13" font-weight="bold" fill="black" text-anchor="middle">→</text>

  <!-- ============ 2. DELTA CON PARALELOS (derecha) ============ -->
  <polygon points="725,65 870,225 580,225" fill="#3b82f6" opacity="0.10" stroke="none"/>

  <!-- Rama A-B -->
  <line x1="725" y1="65" x2="870" y2="225" stroke="black" stroke-width="1.5"/>
  <g transform="translate(798, 145) rotate(48)">
    <rect x="-65" y="-12" width="130" height="24" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="11" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.75em">p1</tspan> = Z<tspan baseline-shift="sub" font-size="0.75em">AB</tspan> ∥ Z′<tspan baseline-shift="sub" font-size="0.75em">AB</tspan></text>
  </g>

  <!-- Rama A-C -->
  <line x1="725" y1="65" x2="580" y2="225" stroke="black" stroke-width="1.5"/>
  <g transform="translate(652, 145) rotate(-48)">
    <rect x="-65" y="-12" width="130" height="24" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="11" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.75em">p3</tspan> = Z<tspan baseline-shift="sub" font-size="0.75em">CA</tspan> ∥ Z′<tspan baseline-shift="sub" font-size="0.75em">CA</tspan></text>
  </g>

  <!-- Rama B-C -->
  <line x1="870" y1="225" x2="580" y2="225" stroke="black" stroke-width="1.5"/>
  <rect x="660" y="213" width="130" height="24" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="725" y="229" font-size="11" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.75em">p2</tspan> = Z<tspan baseline-shift="sub" font-size="0.75em">BC</tspan> ∥ Z′<tspan baseline-shift="sub" font-size="0.75em">BC</tspan></text>

  <!-- Terminales Derecha -->
  <circle cx="725" cy="65"  r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="870" cy="225" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="580" cy="225" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="725" y="48" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="middle">A</text>
  <text x="885" y="230" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="start">B</text>
  <text x="565" y="230" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="end">C</text>

  <text x="725" y="275" font-size="12" fill="#475569" text-anchor="middle">El nodo O desaparece y las ramas homólogas quedan en paralelo</text>
</svg>
</div>
</div>

<!-- ================= ETAPA 2: DELTA EQUIVALENTE A ESTRELLA FINAL ================= -->
<div class="my-4 d-flex justify-content-center">
<div class="border rounded-3 bg-white shadow-sm p-3 w-100" style="max-width: 920px;">
<svg viewBox="0 0 950 300" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display:block; font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;">

  <text x="225" y="24" font-size="16" font-weight="bold" fill="black" text-anchor="middle">2. Delta Consolidada (Zp1, Zp2, Zp3)</text>
  <text x="725" y="24" font-size="16" font-weight="bold" fill="black" text-anchor="middle">3. Estrella Final con Reducción Serie</text>

  <!-- ============ DELTA SIMPLIFICADA (izquierda) ============ -->
  <polygon points="225,65 370,225 80,225" fill="#3b82f6" opacity="0.10" stroke="none"/>

  <line x1="225" y1="65" x2="370" y2="225" stroke="black" stroke-width="1.5"/>
  <g transform="translate(298, 145) rotate(48)">
    <rect x="-24" y="-11" width="48" height="22" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">p1</tspan></text>
  </g>

  <line x1="225" y1="65" x2="80" y2="225" stroke="black" stroke-width="1.5"/>
  <g transform="translate(152, 145) rotate(-48)">
    <rect x="-24" y="-11" width="48" height="22" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">p3</tspan></text>
  </g>

  <line x1="370" y1="225" x2="80" y2="225" stroke="black" stroke-width="1.5"/>
  <rect x="201" y="214" width="48" height="22" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="225" y="229" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">p2</tspan></text>

  <!-- Terminales Delta Izquierda -->
  <circle cx="225" cy="65"  r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="370" cy="225" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="80"  cy="225" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="225" y="48" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="middle">A</text>
  <text x="385" y="230" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="start">B</text>
  <text x="65"  y="230" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="end">C</text>

  <text x="225" y="275" font-size="12" fill="#475569" text-anchor="middle">Transformación de la Delta equivalente a Estrella</text>

  <!-- ============ BADGE Δ → Y ============ -->
  <line x1="475" y1="45" x2="475" y2="275" stroke="#94a3b8" stroke-width="1" stroke-dasharray="6 6"/>
  <rect x="443" y="142" width="64" height="36" rx="6" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
  <text x="475" y="157" font-size="11" font-weight="bold" fill="black" text-anchor="middle">Δ → Y</text>
  <text x="475" y="171" font-size="13" font-weight="bold" fill="black" text-anchor="middle">→</text>

  <!-- ============ ESTRELLA FINAL (derecha) ============ -->
  <!-- N-A vertical -->
  <line x1="725" y1="185" x2="725" y2="60" stroke="black" stroke-width="1.5"/>
  <rect x="714" y="105" width="22" height="44" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="752" y="132" font-size="14" font-style="italic" fill="black" text-anchor="start">Z<tspan baseline-shift="sub" font-size="0.7em">1</tspan></text>

  <!-- N-B -->
  <line x1="725" y1="185" x2="855" y2="255" stroke="black" stroke-width="1.5"/>
  <g transform="translate(790, 220) rotate(28)">
    <rect x="-22" y="-11" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="14" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">2</tspan></text>
  </g>

  <!-- N-C -->
  <line x1="725" y1="185" x2="595" y2="255" stroke="black" stroke-width="1.5" stroke-dasharray="4 4"/>
  <g transform="translate(660, 220) rotate(-28)">
    <rect x="-22" y="-11" width="44" height="22" fill="white" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="0" y="4" font-size="14" font-style="italic" fill="#64748b" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">3</tspan></text>
  </g>

  <!-- Nodo neutro N -->
  <circle cx="725" cy="185" r="3" fill="black"/>
  <text x="705" y="191" font-size="13" font-weight="bold" font-style="italic" fill="black" text-anchor="end">N</text>

  <!-- Terminales Estrella Final -->
  <circle cx="725" cy="60"  r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="855" cy="255" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="595" cy="255" r="4" fill="white" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="725" y="44"  font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="middle">A</text>
  <text x="869" y="260" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="start">B</text>
  <text x="581" y="260" font-size="14" font-weight="bold" font-style="italic" fill="#64748b" text-anchor="end">C (abierto)</text>

  <text x="725" y="285" font-size="13" font-weight="bold" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">eq</tspan> (A–B) = Z<tspan baseline-shift="sub" font-size="0.7em">1</tspan> + Z<tspan baseline-shift="sub" font-size="0.7em">2</tspan></text>
</svg>
</div>
</div>
```

Ejemplo de **doble transformación**: ninguna dirección única resuelve la red en un solo paso. La estrategia consiste en encadenar $\text{Y} \to \Delta$ y posteriormente $\Delta \to \text{Y}$.

### Paso 1 — $\text{Y} \to \Delta$ (estrella interna)
Con $\Sigma_2 = \mathbf{Z}_a\mathbf{Z}_b + \mathbf{Z}_b\mathbf{Z}_c + \mathbf{Z}_c\mathbf{Z}_a$:

$$
\mathbf{Z}'_{AB} = \frac{\Sigma_2}{\mathbf{Z}_c}, \qquad
\mathbf{Z}'_{BC} = \frac{\Sigma_2}{\mathbf{Z}_a}, \qquad
\mathbf{Z}'_{CA} = \frac{\Sigma_2}{\mathbf{Z}_b}
$$

### Paso 2 — Paralelos
Cada rama del anillo externo queda en paralelo directo con la rama equivalente correspondiente, y el nodo interno $O$ desaparece:

$$
\mathbf{Z}_{p1} = \mathbf{Z}_{AB} \parallel \mathbf{Z}'_{AB}, \qquad
\mathbf{Z}_{p2} = \mathbf{Z}_{BC} \parallel \mathbf{Z}'_{BC}, \qquad
\mathbf{Z}_{p3} = \mathbf{Z}_{CA} \parallel \mathbf{Z}'_{CA}
$$

### Paso 3 — $\Delta \to \text{Y}$ (anillo combinado)
Con $\Sigma_p = \mathbf{Z}_{p1} + \mathbf{Z}_{p2} + \mathbf{Z}_{p3}$:

$$
\mathbf{Z}_1 = \frac{\mathbf{Z}_{p1}\,\mathbf{Z}_{p3}}{\Sigma_p}, \qquad
\mathbf{Z}_2 = \frac{\mathbf{Z}_{p1}\,\mathbf{Z}_{p2}}{\Sigma_p}, \qquad
\mathbf{Z}_3 = \frac{\mathbf{Z}_{p2}\,\mathbf{Z}_{p3}}{\Sigma_p}
$$

### Resultado final
Vista entre los terminales $A$ y $B$, con el terminal $C$ en circuito abierto (o conectado a otra parte de la red), la impedancia equivalente es una simple conexión en serie:

$$
\boxed{\mathbf{Z}_{eq} = \mathbf{Z}_1 + \mathbf{Z}_2}
$$