```{=html}
<div class="my-4 d-flex justify-content-center">
  <div class="border rounded-3 bg-white shadow-sm p-3 w-100" style="max-width: 860px;">
    <svg viewBox="0 0 860 330" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display:block; font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;">
      <!-- Definiciones de marcadores de flecha -->
      <defs>
        <marker id="arrowEqBlue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0284c7"/>
        </marker>
        <marker id="arrowEqPurple" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#7c3aed"/>
        </marker>
      </defs>

      <!-- ================= CONTENEDOR 1: RED DELTA ================= -->
      <rect x="25" y="20" width="360" height="290" rx="10" fill="#f8fafc" stroke="#0284c7" stroke-width="1.5" stroke-dasharray="6 4"/>
      <text x="205" y="44" font-size="13" font-weight="bold" fill="#0369a1" text-anchor="middle">RED DELTA (Δ)</text>

      <!-- Polígono interior sombreado -->
      <polygon points="205,80 325,230 85,230" fill="#3b82f6" opacity="0.10" stroke="none"/>

      <!-- Ramas Delta internas -->
      <!-- A - B -->
      <line x1="205" y1="80" x2="325" y2="230" stroke="black" stroke-width="1.5"/>
      <g transform="translate(265, 155) rotate(51)">
        <rect x="-22" y="-11" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
        <text x="0" y="4" font-size="12" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">AB</tspan></text>
      </g>

      <!-- A - C -->
      <line x1="205" y1="80" x2="85" y2="230" stroke="black" stroke-width="1.5"/>
      <g transform="translate(145, 155) rotate(-51)">
        <rect x="-22" y="-11" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
        <text x="0" y="4" font-size="12" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">CA</tspan></text>
      </g>

      <!-- B - C -->
      <line x1="325" y1="230" x2="85" y2="230" stroke="black" stroke-width="1.5"/>
      <rect x="183" y="219" width="44" height="22" fill="white" stroke="black" stroke-width="1.5"/>
      <text x="205" y="234" font-size="12" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">BC</tspan></text>

      <!-- Flechas de Corriente Terminal Externa (IA, IB, IC) -->
      <line x1="205" y1="52" x2="205" y2="72" stroke="#0284c7" stroke-width="2" marker-end="url(#arrowEqBlue)"/>
      <text x="218" y="64" font-size="11" font-weight="bold" fill="#0284c7">I<tspan baseline-shift="sub" font-size="0.7em">A</tspan></text>

      <line x1="355" y1="250" x2="333" y2="236" stroke="#0284c7" stroke-width="2" marker-end="url(#arrowEqBlue)"/>
      <text x="358" y="246" font-size="11" font-weight="bold" fill="#0284c7">I<tspan baseline-shift="sub" font-size="0.7em">B</tspan></text>

      <line x1="55" y1="250" x2="77" y2="236" stroke="#0284c7" stroke-width="2" marker-end="url(#arrowEqBlue)"/>
      <text x="42" y="246" font-size="11" font-weight="bold" fill="#0284c7">I<tspan baseline-shift="sub" font-size="0.7em">C</tspan></text>

      <!-- Terminales Externos Delta (A, B, C) -->
      <circle cx="205" cy="80"  r="4" fill="white" stroke="black" stroke-width="1.5"/>
      <text x="205" y="98" font-size="13" font-weight="bold" fill="black" text-anchor="middle">A</text>

      <circle cx="325" cy="230" r="4" fill="white" stroke="black" stroke-width="1.5"/>
      <text x="312" y="222" font-size="13" font-weight="bold" fill="black" text-anchor="end">B</text>

      <circle cx="85"  cy="230" r="4" fill="white" stroke="black" stroke-width="1.5"/>
      <text x="98"  y="222" font-size="13" font-weight="bold" fill="black" text-anchor="start">C</text>

      <!-- ================= ZONA CENTRAL: EQUIVALENCIA ================= -->
      <line x1="430" y1="40" x2="430" y2="295" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 4"/>
      <rect x="398" y="145" width="64" height="38" rx="6" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
      <text x="430" y="162" font-size="14" font-weight="bold" fill="black" text-anchor="middle">⇄</text>
      <text x="430" y="176" font-size="9" font-weight="bold" fill="#475569" text-anchor="middle">EQUIV</text>

      <!-- ================= CONTENEDOR 2: RED ESTRELLA ================= -->
      <rect x="475" y="20" width="360" height="290" rx="10" fill="#f8fafc" stroke="#7c3aed" stroke-width="1.5" stroke-dasharray="6 4"/>
      <text x="655" y="44" font-size="13" font-weight="bold" fill="#6d28d9" text-anchor="middle">RED ESTRELLA (Y)</text>

      <!-- Ramas Estrella internas -->
      <!-- O - A -->
      <line x1="655" y1="180" x2="655" y2="80" stroke="black" stroke-width="1.5"/>
      <rect x="645" y="112" width="20" height="38" fill="white" stroke="black" stroke-width="1.5"/>
      <text x="678" y="136" font-size="12" font-style="italic" fill="black" text-anchor="start">Z<tspan baseline-shift="sub" font-size="0.7em">A</tspan></text>

      <!-- O - B -->
      <line x1="655" y1="180" x2="775" y2="230" stroke="black" stroke-width="1.5"/>
      <g transform="translate(715, 205) rotate(23)">
        <rect x="-20" y="-10" width="40" height="20" fill="white" stroke="black" stroke-width="1.5"/>
        <text x="0" y="4" font-size="12" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">B</tspan></text>
      </g>

      <!-- O - C -->
      <line x1="655" y1="180" x2="535" y2="230" stroke="black" stroke-width="1.5"/>
      <g transform="translate(595, 205) rotate(-23)">
        <rect x="-20" y="-10" width="40" height="20" fill="white" stroke="black" stroke-width="1.5"/>
        <text x="0" y="4" font-size="12" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">C</tspan></text>
      </g>

      <!-- Nodo Neutro Central (O) -->
      <circle cx="655" cy="180" r="3" fill="black"/>
      <text x="655" y="198" font-size="12" font-weight="bold" font-style="italic" fill="black" text-anchor="middle">O</text>

      <!-- Flechas de Corriente Terminal Externa (IA, IB, IC) -->
      <line x1="655" y1="52" x2="655" y2="72" stroke="#7c3aed" stroke-width="2" marker-end="url(#arrowEqPurple)"/>
      <text x="668" y="64" font-size="11" font-weight="bold" fill="#7c3aed">I<tspan baseline-shift="sub" font-size="0.7em">A</tspan></text>

      <line x1="805" y1="250" x2="783" y2="236" stroke="#7c3aed" stroke-width="2" marker-end="url(#arrowEqPurple)"/>
      <text x="808" y="246" font-size="11" font-weight="bold" fill="#7c3aed">I<tspan baseline-shift="sub" font-size="0.7em">B</tspan></text>

      <line x1="505" y1="250" x2="527" y2="236" stroke="#7c3aed" stroke-width="2" marker-end="url(#arrowEqPurple)"/>
      <text x="492" y="246" font-size="11" font-weight="bold" fill="#7c3aed">I<tspan baseline-shift="sub" font-size="0.7em">C</tspan></text>

      <!-- Terminales Externos Estrella (A, B, C) -->
      <circle cx="655" cy="80"  r="4" fill="white" stroke="black" stroke-width="1.5"/>
      <text x="655" y="98" font-size="13" font-weight="bold" fill="black" text-anchor="middle">A</text>

      <circle cx="775" cy="230" r="4" fill="white" stroke="black" stroke-width="1.5"/>
      <text x="762" y="222" font-size="13" font-weight="bold" fill="black" text-anchor="end">B</text>

      <circle cx="535" cy="230" r="4" fill="white" stroke="black" stroke-width="1.5"/>
      <text x="548" y="222" font-size="13" font-weight="bold" fill="black" text-anchor="start">C</text>
    </svg>
  </div>
</div>
```
