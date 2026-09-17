```{=html}
<div class="my-4 d-flex justify-content-center">
  <div class="border rounded-3 bg-white shadow-sm p-3 w-100" style="max-width: 780px;">
    <svg viewBox="0 0 740 320" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display:block; font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;">
      <!-- Fondo y defs -->
      <defs>
        <filter id="shadowFilter" x="-10%" y="-10%" width="120%" height="120%">
          <feDropShadow dx="0" dy="1" stdDeviation="2" flood-opacity="0.08"/>
        </filter>
      </defs>

      <!-- Divisor central y símbolo de transformación -->
      <line x1="370" y1="40" x2="370" y2="290" stroke="#e2e8f0" stroke-width="1.8" stroke-dasharray="6 6"/>
      <circle cx="370" cy="165" r="22" fill="#f0f9ff" stroke="#0284c7" stroke-width="2" filter="url(#shadowFilter)"/>
      <text x="370" y="172" font-size="18" font-weight="800" fill="#0284c7" text-anchor="middle">⇄</text>

      <!-- ================= DELTA (Δ) ================= -->
      <text x="190" y="30" font-size="16" font-weight="800" fill="#0369a1" text-anchor="middle">Configuración Delta (Δ)</text>
      
      <!-- Ramas Delta -->
      <line x1="190" y1="70" x2="70" y2="250" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>
      <line x1="190" y1="70" x2="310" y2="250" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>
      <line x1="70" y1="250" x2="310" y2="250" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>

      <!-- Etiquetas de Impedancia Delta -->
      <!-- Z_C (Rama 1-2) -->
      <rect x="84" y="145" width="50" height="26" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" filter="url(#shadowFilter)"/>
      <text x="109" y="163" font-size="14" font-weight="700" fill="#0f172a" text-anchor="middle">Z<tspan font-size="10" dy="3">C</tspan></text>

      <!-- Z_B (Rama 1-3) -->
      <rect x="246" y="145" width="50" height="26" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" filter="url(#shadowFilter)"/>
      <text x="271" y="163" font-size="14" font-weight="700" fill="#0f172a" text-anchor="middle">Z<tspan font-size="10" dy="3">B</tspan></text>

      <!-- Z_A (Rama 2-3) -->
      <rect x="165" y="260" width="50" height="26" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" filter="url(#shadowFilter)"/>
      <text x="190" y="278" font-size="14" font-weight="700" fill="#0f172a" text-anchor="middle">Z<tspan font-size="10" dy="3">A</tspan></text>

      <!-- Nodos Delta -->
      <!-- Nodo 1 -->
      <circle cx="190" cy="70" r="18" fill="#0284c7" opacity="0.18"/>
      <circle cx="190" cy="70" r="14" fill="#bfdbfe" stroke="#0284c7" stroke-width="2.8"/>
      <text x="190" y="75" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">1</text>

      <!-- Nodo 2 -->
      <circle cx="70" cy="250" r="18" fill="#0284c7" opacity="0.18"/>
      <circle cx="70" cy="250" r="14" fill="#bfdbfe" stroke="#0284c7" stroke-width="2.8"/>
      <text x="70" y="255" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">2</text>

      <!-- Nodo 3 -->
      <circle cx="310" cy="250" r="18" fill="#0284c7" opacity="0.18"/>
      <circle cx="310" cy="250" r="14" fill="#bfdbfe" stroke="#0284c7" stroke-width="2.8"/>
      <text x="310" y="255" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">3</text>

      <!-- ================= ESTRELLA (Y) ================= -->
      <text x="550" y="30" font-size="16" font-weight="800" fill="#7c3aed" text-anchor="middle">Configuración Estrella (Y)</text>

      <!-- Ramas Estrella -->
      <line x1="550" y1="70" x2="550" y2="175" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>
      <line x1="430" y1="250" x2="550" y2="175" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>
      <line x1="670" y1="250" x2="550" y2="175" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>

      <!-- Etiquetas de Impedancia Estrella -->
      <!-- Z_1 (Rama 1-O) -->
      <rect x="562" y="110" width="48" height="26" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" filter="url(#shadowFilter)"/>
      <text x="586" y="128" font-size="14" font-weight="700" fill="#0f172a" text-anchor="middle">Z<tspan font-size="10" dy="3">1</tspan></text>

      <!-- Z_2 (Rama 2-O) -->
      <rect x="450" y="196" width="48" height="26" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" filter="url(#shadowFilter)"/>
      <text x="474" y="214" font-size="14" font-weight="700" fill="#0f172a" text-anchor="middle">Z<tspan font-size="10" dy="3">2</tspan></text>

      <!-- Z_3 (Rama 3-O) -->
      <rect x="602" y="196" width="48" height="26" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" filter="url(#shadowFilter)"/>
      <text x="626" y="214" font-size="14" font-weight="700" fill="#0f172a" text-anchor="middle">Z<tspan font-size="10" dy="3">3</tspan></text>

      <!-- Nodo Neutro (O) -->
      <circle cx="550" cy="175" r="16" fill="#64748b" opacity="0.15"/>
      <circle cx="550" cy="175" r="12" fill="#f1f5f9" stroke="#64748b" stroke-width="2.4"/>
      <text x="550" y="179" font-size="12" font-weight="800" fill="#334155" text-anchor="middle">O</text>

      <!-- Nodos Estrella Externos -->
      <!-- Nodo 1 -->
      <circle cx="550" cy="70" r="18" fill="#7c3aed" opacity="0.18"/>
      <circle cx="550" cy="70" r="14" fill="#ede9fe" stroke="#7c3aed" stroke-width="2.8"/>
      <text x="550" y="75" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">1</text>

      <!-- Nodo 2 -->
      <circle cx="430" cy="250" r="18" fill="#7c3aed" opacity="0.18"/>
      <circle cx="430" cy="250" r="14" fill="#ede9fe" stroke="#7c3aed" stroke-width="2.8"/>
      <text x="430" y="255" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">2</text>

      <!-- Nodo 3 -->
      <circle cx="670" cy="250" r="18" fill="#7c3aed" opacity="0.18"/>
      <circle cx="670" cy="250" r="14" fill="#ede9fe" stroke="#7c3aed" stroke-width="2.8"/>
      <text x="670" y="255" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">3</text>
    </svg>
  </div>
</div>
```