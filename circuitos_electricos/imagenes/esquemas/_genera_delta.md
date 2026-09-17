```{=html}
<div class="my-4 d-flex justify-content-center">
  <div class="border rounded-3 bg-white shadow-sm p-3 w-100" style="max-width: 440px;">
    <svg viewBox="0 0 380 320" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display:block; font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;">
      <!-- Fondo y defs -->
      <defs>
        <filter id="shadowFilterDelta" x="-10%" y="-10%" width="120%" height="120%">
          <feDropShadow dx="0" dy="1" stdDeviation="2" flood-opacity="0.08"/>
        </filter>
      </defs>

      <!-- ================= DELTA (Δ) ================= -->
      <text x="190" y="30" font-size="16" font-weight="800" fill="#0369a1" text-anchor="middle">Configuración Delta (Δ)</text>
      
      <!-- Ramas Delta -->
      <line x1="190" y1="70" x2="70" y2="250" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>
      <line x1="190" y1="70" x2="310" y2="250" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>
      <line x1="70" y1="250" x2="310" y2="250" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>

      <!-- Etiquetas de Impedancia Delta -->
      <!-- Z_C (Rama A-B / 1-2) -->
      <rect x="84" y="145" width="50" height="26" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" filter="url(#shadowFilterDelta)"/>
      <text x="109" y="163" font-size="14" font-weight="700" fill="#0f172a" text-anchor="middle">Z<tspan font-size="10" dy="3">C</tspan></text>

      <!-- Z_B (Rama A-C / 1-3) -->
      <rect x="246" y="145" width="50" height="26" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" filter="url(#shadowFilterDelta)"/>
      <text x="271" y="163" font-size="14" font-weight="700" fill="#0f172a" text-anchor="middle">Z<tspan font-size="10" dy="3">B</tspan></text>

      <!-- Z_A (Rama B-C / 2-3) -->
      <rect x="165" y="260" width="50" height="26" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" filter="url(#shadowFilterDelta)"/>
      <text x="190" y="278" font-size="14" font-weight="700" fill="#0f172a" text-anchor="middle">Z<tspan font-size="10" dy="3">A</tspan></text>

      <!-- Nodos Delta -->
      <!-- Nodo A -->
      <circle cx="190" cy="70" r="18" fill="#0284c7" opacity="0.18"/>
      <circle cx="190" cy="70" r="14" fill="#bfdbfe" stroke="#0284c7" stroke-width="2.8"/>
      <text x="190" y="75" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">A</text>

      <!-- Nodo B -->
      <circle cx="70" cy="250" r="18" fill="#0284c7" opacity="0.18"/>
      <circle cx="70" cy="250" r="14" fill="#bfdbfe" stroke="#0284c7" stroke-width="2.8"/>
      <text x="70" y="255" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">B</text>

      <!-- Nodo C -->
      <circle cx="310" cy="250" r="18" fill="#0284c7" opacity="0.18"/>
      <circle cx="310" cy="250" r="14" fill="#bfdbfe" stroke="#0284c7" stroke-width="2.8"/>
      <text x="310" y="255" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">C</text>
    </svg>
  </div>
</div>
```