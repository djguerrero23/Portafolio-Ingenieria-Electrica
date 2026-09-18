```{=html}
<!-- ================= ETAPA 1: CELOSÍA A PUENTE ================= -->
<div class="my-4 d-flex justify-content-center">
<div class="border rounded-3 bg-white shadow-sm p-3 w-100" style="max-width: 920px;">
<svg viewBox="0 0 950 300" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display:block; font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;">

  <text x="225" y="24" font-size="16" font-weight="bold" fill="black" text-anchor="middle">1. Red de Celosía (Lattice)</text>
  <text x="725" y="24" font-size="16" font-weight="bold" fill="black" text-anchor="middle">2. Redibujado en Topología de Puente</text>

  <!-- ============ 1. CELOSÍA ============ -->
  <!-- Rama superior Za -->
  <line x1="80" y1="80" x2="370" y2="80" stroke="black" stroke-width="1.5"/>
  <rect x="203" y="69" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="225" y="84" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">a</tspan></text>

  <!-- Rama inferior Zb -->
  <line x1="80" y1="230" x2="370" y2="230" stroke="black" stroke-width="1.5"/>
  <rect x="203" y="219" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="225" y="234" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">b</tspan></text>

  <!-- Diagonal a-d (Zc) -->
  <line x1="80" y1="80" x2="370" y2="230" stroke="black" stroke-width="1.5"/>
  <g transform="translate(160, 121) rotate(27)">
    <rect x="-22" y="-11" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">c</tspan></text>
  </g>

  <!-- Diagonal b-c (Zd) -->
  <line x1="80" y1="230" x2="370" y2="80" stroke="black" stroke-width="1.5"/>
  <g transform="translate(160, 189) rotate(-27)">
    <rect x="-22" y="-11" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">d</tspan></text>
  </g>

  <!-- Cruce sin conexión -->
  <circle cx="225" cy="155" r="4.5" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="225" y="180" font-size="11" fill="#64748b" text-anchor="middle">cruce sin conexión</text>

  <!-- Terminales -->
  <circle cx="80"  cy="80"  r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="80"  cy="230" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="370" cy="80"  r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="370" cy="230" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="65"  y="84"  font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="end">a</text>
  <text x="65"  y="234" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="end">b</text>
  <text x="385" y="84"  font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="start">c</text>
  <text x="385" y="234" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="start">d</text>

  <text x="225" y="275" font-size="12" fill="#475569" text-anchor="middle">Entrada entre a–b · Salida entre c–d</text>

  <!-- ============ BADGE Redibujado ============ -->
  <line x1="475" y1="45" x2="475" y2="275" stroke="#94a3b8" stroke-width="1" stroke-dasharray="6 6"/>
  <rect x="443" y="142" width="64" height="36" rx="6" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
  <text x="475" y="157" font-size="11" font-weight="bold" fill="black" text-anchor="middle">redibuja</text>
  <text x="475" y="171" font-size="13" font-weight="bold" fill="black" text-anchor="middle">→</text>

  <!-- ============ 2. PUENTE EQUIVALENTE ============ -->
  <polygon points="580,155 725,60 725,250" fill="#3b82f6" opacity="0.10" stroke="none"/>

  <!-- a-c : Za -->
  <line x1="580" y1="155" x2="725" y2="60" stroke="black" stroke-width="1.5"/>
  <g transform="translate(652, 107) rotate(-33)">
    <rect x="-22" y="-11" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">a</tspan></text>
  </g>

  <!-- c-b : Zd -->
  <line x1="725" y1="60" x2="870" y2="155" stroke="black" stroke-width="1.5"/>
  <g transform="translate(798, 107) rotate(33)">
    <rect x="-22" y="-11" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">d</tspan></text>
  </g>

  <!-- b-d : Zb -->
  <line x1="870" y1="155" x2="725" y2="250" stroke="black" stroke-width="1.5"/>
  <g transform="translate(798, 203) rotate(-33)">
    <rect x="-22" y="-11" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">b</tspan></text>
  </g>

  <!-- d-a : Zc -->
  <line x1="725" y1="250" x2="580" y2="155" stroke="black" stroke-width="1.5"/>
  <g transform="translate(652, 203) rotate(33)">
    <rect x="-22" y="-11" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">c</tspan></text>
  </g>

  <!-- Carga central ZL entre c y d -->
  <line x1="725" y1="60" x2="725" y2="250" stroke="black" stroke-width="1.5"/>
  <rect x="714" y="133" width="22" height="44" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="748" y="160" font-size="14" font-style="italic" fill="black" text-anchor="start">Z<tspan baseline-shift="sub" font-size="0.7em">L</tspan></text>

  <!-- Nodos Puente -->
  <circle cx="580" cy="155" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="870" cy="155" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="725" cy="60"  r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="725" cy="250" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="565" y="160" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="end">a</text>
  <text x="885" y="160" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="start">b</text>
  <text x="725" y="45"  font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="middle">c</text>
  <text x="725" y="272" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="middle">d</text>

  <text x="725" y="290" font-size="12" fill="#475569" text-anchor="middle">Lazo Delta formado por nodos (a, c, d)</text>
</svg>
</div>
</div>

<!-- ================= ETAPA 2: PUENTE A ESTRELLA SERIE-PARALELO ================= -->
<div class="my-4 d-flex justify-content-center">
<div class="border rounded-3 bg-white shadow-sm p-3 w-100" style="max-width: 920px;">
<svg viewBox="0 0 950 300" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display:block; font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;">

  <text x="225" y="24" font-size="16" font-weight="bold" fill="black" text-anchor="middle">2. Puente con Lazo Δ (a, c, d)</text>
  <text x="725" y="24" font-size="16" font-weight="bold" fill="black" text-anchor="middle">3. Red Resultante Serie–Paralelo</text>

  <!-- ============ PUENTE (izquierda) ============ -->
  <polygon points="80,155 225,60 225,250" fill="#3b82f6" opacity="0.10" stroke="none"/>

  <line x1="80" y1="155" x2="225" y2="60" stroke="black" stroke-width="1.5"/>
  <g transform="translate(152, 107) rotate(-33)">
    <rect x="-22" y="-11" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">a</tspan></text>
  </g>

  <line x1="225" y1="60" x2="370" y2="155" stroke="black" stroke-width="1.5"/>
  <g transform="translate(298, 107) rotate(33)">
    <rect x="-22" y="-11" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">d</tspan></text>
  </g>

  <line x1="370" y1="155" x2="225" y2="250" stroke="black" stroke-width="1.5"/>
  <g transform="translate(298, 203) rotate(-33)">
    <rect x="-22" y="-11" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">b</tspan></text>
  </g>

  <line x1="225" y1="250" x2="80" y2="155" stroke="black" stroke-width="1.5"/>
  <g transform="translate(152, 203) rotate(33)">
    <rect x="-22" y="-11" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">c</tspan></text>
  </g>

  <!-- Carga ZL -->
  <line x1="225" y1="60" x2="225" y2="250" stroke="black" stroke-width="1.5"/>
  <rect x="214" y="133" width="22" height="44" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="248" y="160" font-size="14" font-style="italic" fill="black" text-anchor="start">Z<tspan baseline-shift="sub" font-size="0.7em">L</tspan></text>

  <!-- Nodos Puente Izquierda -->
  <circle cx="80"  cy="155" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="370" cy="155" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="225" cy="60"  r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="225" cy="250" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="65"  y="160" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="end">a</text>
  <text x="385" y="160" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="start">b</text>
  <text x="225" y="45"  font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="middle">c</text>
  <text x="225" y="272" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="middle">d</text>

  <!-- ============ BADGE Δ → Y ============ -->
  <line x1="475" y1="45" x2="475" y2="275" stroke="#94a3b8" stroke-width="1" stroke-dasharray="6 6"/>
  <rect x="451" y="142" width="48" height="36" rx="6" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
  <text x="475" y="157" font-size="12" font-weight="bold" fill="black" text-anchor="middle">Δ → Y</text>
  <text x="475" y="171" font-size="13" font-weight="bold" fill="black" text-anchor="middle">→</text>

  <!-- ============ ESTRELLA RESULTANTE (derecha) ============ -->
  <!-- a -> N : Z1 -->
  <line x1="580" y1="155" x2="680" y2="155" stroke="black" stroke-width="1.5"/>
  <rect x="608" y="144" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="630" y="159" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">1</tspan></text>

  <!-- N -> c : Z2 -->
  <line x1="680" y1="155" x2="745" y2="60" stroke="black" stroke-width="1.5"/>
  <g transform="translate(712, 107) rotate(-55)">
    <rect x="-22" y="-11" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">2</tspan></text>
  </g>

  <!-- N -> d : Z3 -->
  <line x1="680" y1="155" x2="745" y2="250" stroke="black" stroke-width="1.5"/>
  <g transform="translate(712, 203) rotate(55)">
    <rect x="-22" y="-11" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">3</tspan></text>
  </g>

  <!-- c -> b : Zd -->
  <line x1="745" y1="60" x2="870" y2="155" stroke="black" stroke-width="1.5"/>
  <g transform="translate(808, 107) rotate(37)">
    <rect x="-22" y="-11" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">d</tspan></text>
  </g>

  <!-- d -> b : Zb -->
  <line x1="745" y1="250" x2="870" y2="155" stroke="black" stroke-width="1.5"/>
  <g transform="translate(808, 203) rotate(-37)">
    <rect x="-22" y="-11" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">b</tspan></text>
  </g>

  <!-- Nodos y terminales Derecha -->
  <circle cx="580" cy="155" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="870" cy="155" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="680" cy="155" r="3" fill="black"/>
  <circle cx="745" cy="60"  r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="745" cy="250" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="565" y="160" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="end">a</text>
  <text x="885" y="160" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="start">b</text>
  <text x="680" y="176" font-size="13" font-weight="bold" fill="black" text-anchor="middle">N</text>
  <text x="745" y="45"  font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="middle">c</text>
  <text x="745" y="272" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="middle">d</text>

  <text x="725" y="290" font-size="12" fill="#475569" text-anchor="middle">Reducción directa: Z<tspan baseline-shift="sub" font-size="0.7em">1</tspan> + [(Z<tspan baseline-shift="sub" font-size="0.7em">2</tspan> + Z<tspan baseline-shift="sub" font-size="0.7em">d</tspan>) ∥ (Z<tspan baseline-shift="sub" font-size="0.7em">3</tspan> + Z<tspan baseline-shift="sub" font-size="0.7em">b</tspan>)]</text>
</svg>
</div>
</div>
```

La celosía es eléctricamente un puente cuyos cruces en "X" son las ramas diagonales **sin conexión entre sí**. Redibujada como rombo, aparece el triángulo $(a, c, d)$ formado por $\mathbf{Z}_a$, $\mathbf{Z}_c$ y la carga $\mathbf{Z}_L$, que se transforma en estrella con centro $N$:

$$
\mathbf{Z}_\Sigma = \mathbf{Z}_a + \mathbf{Z}_c + \mathbf{Z}_L
$$

$$
\boxed{\mathbf{Z}_1 = \frac{\mathbf{Z}_a\,\mathbf{Z}_c}{\mathbf{Z}_\Sigma}}, \qquad
\mathbf{Z}_2 = \frac{\mathbf{Z}_a\,\mathbf{Z}_L}{\mathbf{Z}_\Sigma}, \qquad
\mathbf{Z}_3 = \frac{\mathbf{Z}_c\,\mathbf{Z}_L}{\mathbf{Z}_\Sigma}
$$

**Resultado topológico:** la red resultante es puramente serie–paralelo: desde $a$ se llega a $N$ por $\mathbf{Z}_1$, y de $N$ a $b$ hay dos ramas en paralelo, $(\mathbf{Z}_2 + \mathbf{Z}_d)$ y $(\mathbf{Z}_3 + \mathbf{Z}_b)$:

$$
\boxed{\mathbf{Z}_{eq} = \mathbf{Z}_1 + \left[ (\mathbf{Z}_2 + \mathbf{Z}_d) \parallel (\mathbf{Z}_3 + \mathbf{Z}_b) \right]}
$$