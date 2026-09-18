```{=html}
<div class="my-4 d-flex justify-content-center">
  <div class="border rounded-3 bg-white shadow-sm p-3 w-100" style="max-width: 440px;">
    <svg viewBox="0 0 380 300" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display:block; font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;">

      <text x="190" y="26" font-size="16" font-weight="bold" fill="black" text-anchor="middle">Configuración Delta (Δ)</text>
      
      <!-- Polígono sombreado interior -->
      <polygon points="190,65 315,225 65,225" fill="#3b82f6" opacity="0.10" stroke="none"/>

      <!-- Ramas Delta -->
      <!-- Rama A - B -->
      <line x1="190" y1="65" x2="315" y2="225" stroke="black" stroke-width="1.5"/>
      <g transform="translate(252, 145) rotate(52)">
        <rect x="-22" y="-11" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
        <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">AB</tspan></text>
      </g>

      <!-- Rama A - C -->
      <line x1="190" y1="65" x2="65" y2="225" stroke="black" stroke-width="1.5"/>
      <g transform="translate(128, 145) rotate(-52)">
        <rect x="-22" y="-11" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
        <text x="0" y="4" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">CA</tspan></text>
      </g>

      <!-- Rama B - C -->
      <line x1="315" y1="225" x2="65" y2="225" stroke="black" stroke-width="1.5"/>
      <rect x="168" y="214" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
      <text x="190" y="229" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">BC</tspan></text>

      <!-- Terminales y Nodos -->
      <!-- Nodo A -->
      <circle cx="190" cy="65"  r="4" fill="white" stroke="black" stroke-width="1.5"/>
      <text x="190" y="48" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="middle">A</text>

      <!-- Nodo B -->
      <circle cx="315" cy="225" r="4" fill="white" stroke="black" stroke-width="1.5"/>
      <text x="330" y="230" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="start">B</text>

      <!-- Nodo C -->
      <circle cx="65"  cy="225" r="4" fill="white" stroke="black" stroke-width="1.5"/>
      <text x="50"  y="230" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="end">C</text>

      <text x="190" y="275" font-size="12" fill="#475569" text-anchor="middle">Ramas entre pares de nodos: Z<tspan baseline-shift="sub" font-size="0.75em">AB</tspan>, Z<tspan baseline-shift="sub" font-size="0.75em">BC</tspan>, Z<tspan baseline-shift="sub" font-size="0.75em">CA</tspan></text>
    </svg>
  </div>
</div>
```