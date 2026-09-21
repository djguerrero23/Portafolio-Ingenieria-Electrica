```{=html}
<div class="my-4 d-flex justify-content-center">
<div class="border rounded-3 bg-white shadow-sm p-3 w-100" style="max-width: 520px;">
<svg viewBox="0 0 465 400" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display:block; font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;">

  <text x="232" y="28" font-size="16" font-weight="bold" fill="black" text-anchor="middle">Red en Doble T (Ejercicio 8)</text>

  <!-- Terminal A -->
  <line x1="35" y1="160" x2="85" y2="160" stroke="black" stroke-width="1.5"/>
  <circle cx="35" cy="160" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="22" y="164" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="end">A</text>

  <!-- Bus vertical nodo 1 -->
  <line x1="85" y1="100" x2="85" y2="220" stroke="black" stroke-width="1.5"/>

  <!-- Terminal B -->
  <line x1="380" y1="160" x2="430" y2="160" stroke="black" stroke-width="1.5"/>
  <circle cx="430" cy="160" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="442" y="164" font-size="14" font-weight="bold" font-style="italic" fill="black" text-anchor="start">B</text>

  <!-- Bus vertical nodo 2 -->
  <line x1="380" y1="100" x2="380" y2="220" stroke="black" stroke-width="1.5"/>

  <!-- T Superior: Z1 (1->O1) y Z2 (O1->2) -->
  <line x1="85" y1="100" x2="232" y2="100" stroke="black" stroke-width="1.5"/>
  <rect x="112" y="89" width="58" height="22" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="141" y="104" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">1</tspan> = 2 &Omega;</text>

  <line x1="232" y1="100" x2="380" y2="100" stroke="black" stroke-width="1.5"/>
  <rect x="293" y="89" width="58" height="22" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="322" y="104" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">2</tspan> = 2 &Omega;</text>

  <!-- O1 -->
  <circle cx="232" cy="100" r="3" fill="black"/>
  <text x="232" y="85" font-size="12" font-weight="bold" font-style="italic" fill="black" text-anchor="middle">O<tspan baseline-shift="sub" font-size="0.7em">1</tspan></text>

  <!-- Z3: O1 -> O2 (baja desde O1 hasta el nodo central O2 en la línea de Z4 y Z5) -->
  <line x1="232" y1="100" x2="232" y2="135" stroke="black" stroke-width="1.5"/>
  <rect x="221" y="135" width="22" height="40" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="252" y="159" font-size="13" font-style="italic" fill="black" text-anchor="start">Z<tspan baseline-shift="sub" font-size="0.7em">3</tspan> = &minus;j4 &Omega;</text>
  <line x1="232" y1="175" x2="232" y2="220" stroke="black" stroke-width="1.5"/>

  <!-- T Inferior: Z4 (1->O2) y Z5 (O2->2) -->
  <line x1="85" y1="220" x2="232" y2="220" stroke="black" stroke-width="1.5"/>
  <rect x="112" y="209" width="58" height="22" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="141" y="224" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">4</tspan> = j4 &Omega;</text>

  <line x1="232" y1="220" x2="380" y2="220" stroke="black" stroke-width="1.5"/>
  <rect x="293" y="209" width="58" height="22" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="322" y="224" font-size="13" font-style="italic" fill="black" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.7em">5</tspan> = j4 &Omega;</text>

  <!-- O2 (centro de la T inferior, ubicado en la intersección exacta con Z4 y Z5) -->
  <circle cx="232" cy="220" r="3.5" fill="black"/>
  <text x="246" y="214" font-size="12" font-weight="bold" font-style="italic" fill="black" text-anchor="start">O<tspan baseline-shift="sub" font-size="0.7em">2</tspan></text>

  <!-- Z6: O2 -> tierra (0) -->
  <line x1="232" y1="220" x2="232" y2="255" stroke="black" stroke-width="1.5"/>
  <rect x="221" y="255" width="22" height="35" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="252" y="279" font-size="13" font-style="italic" fill="black" text-anchor="start">Z<tspan baseline-shift="sub" font-size="0.7em">6</tspan> = 2 &Omega;</text>

  <!-- Bus de tierra -->
  <line x1="232" y1="290" x2="232" y2="305" stroke="black" stroke-width="1.5"/>
  <line x1="70" y1="305" x2="395" y2="305" stroke="black" stroke-width="1.5"/>
  <text x="215" y="300" font-size="12" font-weight="bold" fill="black" text-anchor="end">0</text>

  <!-- Símbolo de tierra -->
  <line x1="220" y1="320" x2="244" y2="320" stroke="black" stroke-width="1.5"/>
  <line x1="225" y1="327" x2="239" y2="327" stroke="black" stroke-width="1.5"/>
  <line x1="230" y1="334" x2="234" y2="334" stroke="black" stroke-width="1.5"/>
  <line x1="232" y1="305" x2="232" y2="320" stroke="black" stroke-width="1.5"/>

  <!-- Nodos 1 y 2 -->
  <circle cx="85" cy="160" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="72" y="155" font-size="12" font-weight="bold" fill="black" text-anchor="end">1</text>

  <circle cx="380" cy="160" r="4" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="393" y="155" font-size="12" font-weight="bold" fill="black" text-anchor="start">2</text>

</svg>
</div>
</div>
```
