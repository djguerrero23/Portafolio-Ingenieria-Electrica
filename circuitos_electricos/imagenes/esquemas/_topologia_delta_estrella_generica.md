```{=html}
<div class="my-4 d-flex justify-content-center">
<div class="border rounded-3 bg-white shadow-sm p-3 w-100" style="max-width: 920px;">
<svg viewBox="0 0 950 300" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display:block; font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;">

  <text x="225" y="24" font-size="16" font-weight="bold" fill="black" text-anchor="middle">Red en Delta (Δ)</text>
  <text x="725" y="24" font-size="16" font-weight="bold" fill="black" text-anchor="middle">Red en Estrella (Y) equivalente</text>

  <!-- ============ DELTA (izquierda) ============ -->
  <polygon points="225,65 370,225 80,225" fill="#3b82f6" opacity="0.10" stroke="none"/>

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

  <!-- Terminales Delta -->
  <circle cx="225" cy="65"  r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="370" cy="225" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="80"  cy="225" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="225" y="48" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="middle">A</text>
  <text x="385" y="230" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="start">B</text>
  <text x="65"  y="230" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="end">C</text>

  <!-- ============ BADGE Δ → Y ============ -->
  <line x1="475" y1="45" x2="475" y2="275" stroke="#94a3b8" stroke-width="1" stroke-dasharray="6 6"/>
  <rect x="451" y="142" width="48" height="36" rx="6" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
  <text x="475" y="157" font-size="12" font-weight="bold" fill="black" text-anchor="middle">Δ → Y</text>
  <text x="475" y="171" font-size="13" font-weight="bold" fill="black" text-anchor="middle">→</text>

  <!-- ============ ESTRELLA (derecha) ============ -->
  <!-- O-A vertical -->
  <line x1="725" y1="185" x2="725" y2="60" stroke="black" stroke-width="1.5"/>
  <rect x="714" y="105" width="22" height="44" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="752" y="132" font-size="14" font-style="italic" fill="black" text-anchor="start">Z<tspan baseline-shift="sub" font-size="0.7em">A</tspan></text>

  <!-- O-B -->
  <line x1="725" y1="185" x2="855" y2="255" stroke="black" stroke-width="1.5"/>
  <g transform="translate(790, 220) rotate(28)">
    <rect x="-22" y="-11" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="14" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">B</tspan></text>
  </g>

  <!-- O-C -->
  <line x1="725" y1="185" x2="595" y2="255" stroke="black" stroke-width="1.5"/>
  <g transform="translate(660, 220) rotate(-28)">
    <rect x="-22" y="-11" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="14" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">C</tspan></text>
  </g>

  <!-- Nodo central -->
  <circle cx="725" cy="185" r="3" fill="black"/>
  <text x="705" y="191" font-size="13" font-weight="bold" font-style="italic" fill="black" text-anchor="end">O</text>

  <!-- Terminales Estrella -->
  <circle cx="725" cy="60"  r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="855" cy="255" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="595" cy="255" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="725" y="44"  font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="middle">A</text>
  <text x="869" y="260" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="start">B</text>
  <text x="581" y="260" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="end">C</text>
</svg>
</div>
</div>
```

En la transformación $\Delta \to \text{Y}$, cada impedancia de la estrella se obtiene como el **producto de las dos impedancias del triángulo que concurren en ese nodo**, dividido entre la suma de las tres impedancias del triángulo:

$$
\mathbf{Z}_\Sigma = \mathbf{Z}_{AB} + \mathbf{Z}_{BC} + \mathbf{Z}_{CA}
$$

$$
\boxed{\mathbf{Z}_A = \frac{\mathbf{Z}_{AB}\,\mathbf{Z}_{CA}}{\mathbf{Z}_\Sigma}}, \qquad
\mathbf{Z}_B = \frac{\mathbf{Z}_{AB}\,\mathbf{Z}_{BC}}{\mathbf{Z}_\Sigma}, \qquad
\mathbf{Z}_C = \frac{\mathbf{Z}_{BC}\,\mathbf{Z}_{CA}}{\mathbf{Z}_\Sigma}
$$

En corriente alterna cada impedancia es compleja ($\mathbf{Z} = R + jX$), por lo que el producto y la suma deben efectuarse en forma **rectangular o polar con rigor fasorial**.
