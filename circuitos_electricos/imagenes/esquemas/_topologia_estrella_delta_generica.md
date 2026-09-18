```{=html}
<div class="my-4 d-flex justify-content-center">
<div class="border rounded-3 bg-white shadow-sm p-3 w-100" style="max-width: 920px;">
<svg viewBox="0 0 950 300" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display:block; font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;">

  <text x="225" y="24" font-size="16" font-weight="bold" fill="black" text-anchor="middle">Red en Estrella (Y)</text>
  <text x="725" y="24" font-size="16" font-weight="bold" fill="black" text-anchor="middle">Red en Delta (Δ) equivalente</text>

  <!-- ============ ESTRELLA (izquierda) ============ -->
  <!-- O-A vertical -->
  <line x1="225" y1="185" x2="225" y2="60" stroke="black" stroke-width="1.5"/>
  <rect x="214" y="105" width="22" height="44" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="252" y="132" font-size="14" font-style="italic" fill="black" text-anchor="start">Z<tspan baseline-shift="sub" font-size="0.7em">1</tspan></text>

  <!-- O-B -->
  <line x1="225" y1="185" x2="355" y2="255" stroke="black" stroke-width="1.5"/>
  <g transform="translate(290, 220) rotate(28)">
    <rect x="-22" y="-11" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="14" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">2</tspan></text>
  </g>

  <!-- O-C -->
  <line x1="225" y1="185" x2="95" y2="255" stroke="black" stroke-width="1.5"/>
  <g transform="translate(160, 220) rotate(-28)">
    <rect x="-22" y="-11" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="14" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">3</tspan></text>
  </g>

  <!-- Nodo central -->
  <circle cx="225" cy="185" r="3" fill="black"/>
  <text x="205" y="191" font-size="13" font-weight="bold" font-style="italic" fill="black" text-anchor="end">O</text>

  <!-- Terminales Estrella -->
  <circle cx="225" cy="60"  r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="355" cy="255" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="95"  cy="255" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="225" y="44"  font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="middle">A</text>
  <text x="369" y="260" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="start">B</text>
  <text x="81"  y="260" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="end">C</text>

  <!-- ============ BADGE Y → Δ ============ -->
  <line x1="475" y1="45" x2="475" y2="275" stroke="#94a3b8" stroke-width="1" stroke-dasharray="6 6"/>
  <rect x="451" y="142" width="48" height="36" rx="6" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
  <text x="475" y="157" font-size="12" font-weight="bold" fill="black" text-anchor="middle">Y → Δ</text>
  <text x="475" y="171" font-size="13" font-weight="bold" fill="black" text-anchor="middle">→</text>

  <!-- ============ DELTA (derecha) ============ -->
  <polygon points="725,65 870,225 580,225" fill="#3b82f6" opacity="0.10" stroke="none"/>

  <!-- Rama A-B -->
  <line x1="725" y1="65" x2="870" y2="225" stroke="black" stroke-width="1.5"/>
  <g transform="translate(798, 145) rotate(48)">
    <rect x="-24" y="-11" width="48" height="22" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">AB</tspan></text>
  </g>

  <!-- Rama A-C -->
  <line x1="725" y1="65" x2="580" y2="225" stroke="black" stroke-width="1.5"/>
  <g transform="translate(652, 145) rotate(-48)">
    <rect x="-24" y="-11" width="48" height="22" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">CA</tspan></text>
  </g>

  <!-- Rama B-C -->
  <line x1="870" y1="225" x2="580" y2="225" stroke="black" stroke-width="1.5"/>
  <rect x="701" y="214" width="48" height="22" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="725" y="229" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">BC</tspan></text>

  <!-- Terminales Delta -->
  <circle cx="725" cy="65"  r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="870" cy="225" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <circle cx="580" cy="225" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="725" y="48" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="middle">A</text>
  <text x="885" y="230" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="start">B</text>
  <text x="565" y="230" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="end">C</text>
</svg>
</div>
</div>
```

En la transformación $\text{Y} \to \Delta$, cada impedancia del triángulo es la **suma de productos dos a dos** de las ramas de la estrella, dividida entre la rama de la estrella **opuesta** a la rama del triángulo que se calcula:

$$
\Sigma_2 = \mathbf{Z}_1\mathbf{Z}_2 + \mathbf{Z}_2\mathbf{Z}_3 + \mathbf{Z}_3\mathbf{Z}_1
$$

$$
\boxed{\mathbf{Z}_{AB} = \frac{\Sigma_2}{\mathbf{Z}_3}}, \qquad
\mathbf{Z}_{BC} = \frac{\Sigma_2}{\mathbf{Z}_1}, \qquad
\mathbf{Z}_{CA} = \frac{\Sigma_2}{\mathbf{Z}_2}
$$

Obsérvese la simetría: la rama del triángulo entre dos nodos se obtiene dividiendo entre la rama de la estrella del **tercer** nodo.