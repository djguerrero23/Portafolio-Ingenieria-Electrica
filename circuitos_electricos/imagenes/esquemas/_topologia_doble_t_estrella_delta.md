```{=html}
<div class="my-4 d-flex justify-content-center">
  <div class="border rounded-3 bg-white shadow-sm p-3 w-100" style="max-width: 1100px;">
    <svg viewBox="10 10 760 320" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display:block; font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;">
      <!-- Defs para filtros de sombra -->
      <defs>
        <filter id="shadowFilterDobleT" x="-10%" y="-10%" width="120%" height="120%">
          <feDropShadow dx="0" dy="1" stdDeviation="2" flood-opacity="0.08"/>
        </filter>
      </defs>

      <!-- ================= 1. RED EN DOBLE T (ESTRELLAS INTERCONECTADAS) ================= -->
      <text x="185" y="24" font-size="15" font-weight="800" fill="#7c3aed" text-anchor="middle">Red en Doble T / Dos Estrellas (Y) en Paralelo</text>
      <text x="185" y="42" font-size="12" font-weight="600" fill="#64748b" text-anchor="middle">Irreducible por serie/paralelo (nodos O₁ y O₂ internos)</text>

      <!-- Bus de Entrada (1), Salida (2) y Referencia (0) -->
      <!-- Bus Entrada -->
      <line x1="40" y1="160" x2="80" y2="160" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>
      <line x1="80" y1="95" x2="80" y2="225" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>

      <!-- Bus Salida -->
      <line x1="290" y1="160" x2="330" y2="160" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>
      <line x1="290" y1="95" x2="290" y2="225" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>

      <!-- Bus Tierra/Referencia -->
      <line x1="70" y1="295" x2="300" y2="295" stroke="#64748b" stroke-width="2" stroke-linecap="round"/>
      <line x1="185" y1="295" x2="185" y2="310" stroke="#64748b" stroke-width="2"/>
      <line x1="175" y1="310" x2="195" y2="310" stroke="#64748b" stroke-width="2"/>
      <line x1="179" y1="315" x2="191" y2="315" stroke="#64748b" stroke-width="2"/>

      <!-- T Superior (Estrella 1: Z1, Z2, Z3) -->
      <line x1="80" y1="95" x2="185" y2="95" stroke="#7c3aed" stroke-width="2.6" stroke-linecap="round"/>
      <line x1="185" y1="95" x2="290" y2="95" stroke="#7c3aed" stroke-width="2.6" stroke-linecap="round"/>
      <line x1="185" y1="95" x2="185" y2="295" stroke="#7c3aed" stroke-width="2.4" stroke-dasharray="3 3"/>

      <!-- T Inferior (Estrella 2: Z4, Z5, Z6) -->
      <line x1="80" y1="225" x2="185" y2="225" stroke="#0284c7" stroke-width="2.6" stroke-linecap="round"/>
      <line x1="185" y1="225" x2="290" y2="225" stroke="#0284c7" stroke-width="2.6" stroke-linecap="round"/>
      <line x1="185" y1="225" x2="185" y2="295" stroke="#0284c7" stroke-width="2.6" stroke-linecap="round"/>

      <!-- Etiquetas Estrella 1 (Superior) -->
      <rect x="110" y="75" width="42" height="22" rx="5" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.3" filter="url(#shadowFilterDobleT)"/>
      <text x="131" y="90" font-size="12" font-weight="700" fill="#6d28d9" text-anchor="middle">Z<tspan font-size="8" dy="2">1</tspan></text>

      <rect x="215" y="75" width="42" height="22" rx="5" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.3" filter="url(#shadowFilterDobleT)"/>
      <text x="236" y="90" font-size="12" font-weight="700" fill="#6d28d9" text-anchor="middle">Z<tspan font-size="8" dy="2">2</tspan></text>

      <rect x="195" y="130" width="42" height="22" rx="5" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.3" filter="url(#shadowFilterDobleT)"/>
      <text x="216" y="145" font-size="12" font-weight="700" fill="#6d28d9" text-anchor="middle">Z<tspan font-size="8" dy="2">3</tspan></text>

      <!-- Etiquetas Estrella 2 (Inferior) -->
      <rect x="110" y="205" width="42" height="22" rx="5" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.3" filter="url(#shadowFilterDobleT)"/>
      <text x="131" y="220" font-size="12" font-weight="700" fill="#0369a1" text-anchor="middle">Z<tspan font-size="8" dy="2">4</tspan></text>

      <rect x="215" y="205" width="42" height="22" rx="5" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.3" filter="url(#shadowFilterDobleT)"/>
      <text x="236" y="220" font-size="12" font-weight="700" fill="#0369a1" text-anchor="middle">Z<tspan font-size="8" dy="2">5</tspan></text>

      <rect x="195" y="248" width="42" height="22" rx="5" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.3" filter="url(#shadowFilterDobleT)"/>
      <text x="216" y="263" font-size="12" font-weight="700" fill="#0369a1" text-anchor="middle">Z<tspan font-size="8" dy="2">6</tspan></text>

      <!-- Nodos Izquierda -->
      <circle cx="80" cy="160" r="11" fill="#bfdbfe" stroke="#0284c7" stroke-width="2"/>
      <text x="80" y="164" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">1</text>
      <text x="30" y="164" font-size="12" font-weight="800" fill="#0f172a" text-anchor="end">In</text>

      <circle cx="290" cy="160" r="11" fill="#bfdbfe" stroke="#0284c7" stroke-width="2"/>
      <text x="290" y="164" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">2</text>
      <text x="340" y="164" font-size="12" font-weight="800" fill="#0f172a" text-anchor="start">Out</text>

      <!-- Nodos Neutros Internos -->
      <circle cx="185" cy="95" r="9" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
      <text x="185" y="80" font-size="10" font-weight="800" fill="#6d28d9" text-anchor="middle">O₁</text>

      <circle cx="185" cy="225" r="9" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
      <text x="185" y="212" font-size="10" font-weight="800" fill="#0369a1" text-anchor="middle">O₂</text>

      <!-- ================= TRANSICIÓN CENTRAL (Y → Δ) ================= -->
      <line x1="385" y1="45" x2="385" y2="295" stroke="#e2e8f0" stroke-width="1.8" stroke-dasharray="6 6"/>
      <circle cx="385" cy="160" r="24" fill="#faf5ff" stroke="#7c3aed" stroke-width="2" filter="url(#shadowFilterDobleT)"/>
      <text x="385" y="155" font-size="11" font-weight="800" fill="#7c3aed" text-anchor="middle">Y → Δ</text>
      <text x="385" y="170" font-size="14" font-weight="800" fill="#7c3aed" text-anchor="middle">→</text>

      <!-- ================= 2. RED EQUIVALENTE EN DOBLE PI (DELTAS EN PARALELO) ================= -->
      <text x="585" y="24" font-size="15" font-weight="800" fill="#0369a1" text-anchor="middle">Red en Doble Π (Deltas en Paralelo)</text>
      <text x="585" y="42" font-size="12" font-weight="600" fill="#64748b" text-anchor="middle">Todas las ramas quedan en paralelo directo entre (1), (2) y (0)</text>

      <!-- Líneas de In y Out Derecha -->
      <line x1="435" y1="120" x2="480" y2="120" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>
      <line x1="690" y1="120" x2="735" y2="120" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>

      <!-- Triángulo Delta equivalente -->
      <!-- Rama Superior In-Out (1)-(2) -->
      <line x1="480" y1="120" x2="690" y2="120" stroke="#1e293b" stroke-width="3.2" stroke-linecap="round"/>
      
      <!-- Rama In-GND (1)-(0) -->
      <line x1="480" y1="120" x2="585" y2="275" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>

      <!-- Rama Out-GND (2)-(0) -->
      <line x1="690" y1="120" x2="585" y2="275" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>

      <!-- Conexión a Tierra Derecha -->
      <line x1="585" y1="275" x2="585" y2="295" stroke="#64748b" stroke-width="2"/>
      <line x1="575" y1="295" x2="595" y2="295" stroke="#64748b" stroke-width="2"/>
      <line x1="579" y1="300" x2="591" y2="300" stroke="#64748b" stroke-width="2"/>

      <!-- Etiquetas en Paralelo de la Delta -->
      <!-- Rama 1-2 (In-Out) -->
      <rect x="540" y="85" width="90" height="28" rx="6" fill="#f8fafc" stroke="#0284c7" stroke-width="1.6" filter="url(#shadowFilterDobleT)"/>
      <text x="585" y="103" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">Z<tspan font-size="9" dy="2">A1</tspan> || Z<tspan font-size="9" dy="2">A2</tspan></text>

      <!-- Rama 1-0 (In-Gnd) -->
      <rect x="475" y="200" width="90" height="28" rx="6" fill="#f8fafc" stroke="#0284c7" stroke-width="1.6" filter="url(#shadowFilterDobleT)"/>
      <text x="520" y="218" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">Z<tspan font-size="9" dy="2">B1</tspan> || Z<tspan font-size="9" dy="2">B2</tspan></text>

      <!-- Rama 2-0 (Out-Gnd) -->
      <rect x="610" y="200" width="90" height="28" rx="6" fill="#f8fafc" stroke="#0284c7" stroke-width="1.6" filter="url(#shadowFilterDobleT)"/>
      <text x="655" y="218" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">Z<tspan font-size="9" dy="2">C1</tspan> || Z<tspan font-size="9" dy="2">C2</tspan></text>

      <!-- Nodos Derecha -->
      <circle cx="480" cy="120" r="13" fill="#bfdbfe" stroke="#0284c7" stroke-width="2.5"/>
      <text x="480" y="124" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">1</text>
      <text x="425" y="124" font-size="12" font-weight="800" fill="#0f172a" text-anchor="end">In</text>

      <circle cx="690" cy="120" r="13" fill="#bfdbfe" stroke="#0284c7" stroke-width="2.5"/>
      <text x="690" y="124" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">2</text>
      <text x="745" y="124" font-size="12" font-weight="800" fill="#0f172a" text-anchor="start">Out</text>

      <circle cx="585" cy="275" r="11" fill="#cbd5e1" stroke="#475569" stroke-width="2"/>
      <text x="585" y="279" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">0</text>
    </svg>
  </div>
</div>
```
