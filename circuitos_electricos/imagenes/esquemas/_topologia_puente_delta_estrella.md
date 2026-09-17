```{=html}
<div class="my-4 d-flex justify-content-center">
  <div class="border rounded-3 bg-white shadow-sm p-3 w-100" style="max-width: 820px;">
    <svg viewBox="0 0 780 340" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display:block; font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;">
      <!-- Defs para sombras y flechas -->
      <defs>
        <filter id="shadowFilterPuente" x="-10%" y="-10%" width="120%" height="120%">
          <feDropShadow dx="0" dy="1" stdDeviation="2" flood-opacity="0.08"/>
        </filter>
      </defs>

      <!-- ================= 1. PUENTE ORIGINAL (NO REDUCIBLE) ================= -->
      <text x="195" y="26" font-size="15" font-weight="800" fill="#0369a1" text-anchor="middle">Red en Puente Original (No Reducible en Serie/Paralelo)</text>
      <text x="195" y="44" font-size="12" font-weight="600" fill="#64748b" text-anchor="middle">Lazo en Delta formado por los nodos (1)-(2)-(3)</text>

      <!-- Resaltado del triángulo Delta -->
      <polygon points="100,170 190,75 190,265" fill="#e0f2fe" opacity="0.45" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="4 4"/>

      <!-- Terminales y líneas de entrada/salida -->
      <line x1="30" y1="170" x2="100" y2="170" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>
      <line x1="280" y1="170" x2="350" y2="170" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>

      <!-- Ramas del Puente -->
      <line x1="100" y1="170" x2="190" y2="75" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>
      <line x1="100" y1="170" x2="190" y2="265" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>
      <line x1="190" y1="75" x2="190" y2="265" stroke="#0284c7" stroke-width="3.2" stroke-linecap="round"/> <!-- Puente Z5 -->
      <line x1="190" y1="75" x2="280" y2="170" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>
      <line x1="190" y1="265" x2="280" y2="170" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>

      <!-- Etiquetas de Impedancia Puente -->
      <!-- Z1 -->
      <rect x="115" y="105" width="46" height="24" rx="5" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.3" filter="url(#shadowFilterPuente)"/>
      <text x="138" y="122" font-size="13" font-weight="700" fill="#0f172a" text-anchor="middle">Z<tspan font-size="9" dy="2">1</tspan></text>

      <!-- Z3 -->
      <rect x="115" y="205" width="46" height="24" rx="5" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.3" filter="url(#shadowFilterPuente)"/>
      <text x="138" y="222" font-size="13" font-weight="700" fill="#0f172a" text-anchor="middle">Z<tspan font-size="9" dy="2">3</tspan></text>

      <!-- Z5 (Rama transversal) -->
      <rect x="202" y="158" width="46" height="24" rx="5" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5" filter="url(#shadowFilterPuente)"/>
      <text x="225" y="175" font-size="13" font-weight="800" fill="#0369a1" text-anchor="middle">Z<tspan font-size="9" dy="2">5</tspan></text>

      <!-- Z2 -->
      <rect x="225" y="105" width="46" height="24" rx="5" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.3" filter="url(#shadowFilterPuente)"/>
      <text x="248" y="122" font-size="13" font-weight="700" fill="#0f172a" text-anchor="middle">Z<tspan font-size="9" dy="2">2</tspan></text>

      <!-- Z4 -->
      <rect x="225" y="205" width="46" height="24" rx="5" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.3" filter="url(#shadowFilterPuente)"/>
      <text x="248" y="222" font-size="13" font-weight="700" fill="#0f172a" text-anchor="middle">Z<tspan font-size="9" dy="2">4</tspan></text>

      <!-- Nodos Puente -->
      <!-- Terminal In A -->
      <circle cx="30" cy="170" r="5" fill="#0f172a"/>
      <text x="18" y="174" font-size="13" font-weight="800" fill="#0f172a" text-anchor="end">A (+)</text>

      <!-- Nodo 1 -->
      <circle cx="100" cy="170" r="13" fill="#bfdbfe" stroke="#0284c7" stroke-width="2.5"/>
      <text x="100" y="174" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">1</text>

      <!-- Nodo 2 -->
      <circle cx="190" cy="75" r="13" fill="#bfdbfe" stroke="#0284c7" stroke-width="2.5"/>
      <text x="190" y="79" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">2</text>

      <!-- Nodo 3 -->
      <circle cx="190" cy="265" r="13" fill="#bfdbfe" stroke="#0284c7" stroke-width="2.5"/>
      <text x="190" y="269" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">3</text>

      <!-- Nodo 4 -->
      <circle cx="280" cy="170" r="13" fill="#bfdbfe" stroke="#0284c7" stroke-width="2.5"/>
      <text x="280" y="174" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">4</text>

      <!-- Terminal Out B -->
      <circle cx="350" cy="170" r="5" fill="#0f172a"/>
      <text x="362" y="174" font-size="13" font-weight="800" fill="#0f172a" text-anchor="start">B (−)</text>

      <!-- ================= TRANSICIÓN CENTRAL (Δ → Y) ================= -->
      <line x1="390" y1="45" x2="390" y2="295" stroke="#e2e8f0" stroke-width="1.8" stroke-dasharray="6 6"/>
      <circle cx="390" cy="170" r="24" fill="#f0f9ff" stroke="#0284c7" stroke-width="2" filter="url(#shadowFilterPuente)"/>
      <text x="390" y="165" font-size="11" font-weight="800" fill="#0284c7" text-anchor="middle">Δ → Y</text>
      <text x="390" y="180" font-size="14" font-weight="800" fill="#0284c7" text-anchor="middle">→</text>

      <!-- ================= 2. RED EQUIVALENTE EN SERIE-PARALELO ================= -->
      <text x="585" y="26" font-size="15" font-weight="800" fill="#7c3aed" text-anchor="middle">Red Transformada (Totalmente Reducible)</text>
      <text x="585" y="44" font-size="12" font-weight="600" fill="#64748b" text-anchor="middle">Z<tspan font-size="9">eq</tspan> = Z<tspan font-size="9">A</tspan> + (Z<tspan font-size="9">B</tspan> + Z<tspan font-size="9">2</tspan>) || (Z<tspan font-size="9">C</tspan> + Z<tspan font-size="9">4</tspan>)</text>

      <!-- Terminales y líneas de entrada/salida derecha -->
      <line x1="420" y1="170" x2="470" y2="170" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>
      <line x1="680" y1="170" x2="750" y2="170" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>

      <!-- Estrella equivalente (ZA, ZB, ZC) conectada a neutro O -->
      <line x1="470" y1="170" x2="535" y2="170" stroke="#7c3aed" stroke-width="3" stroke-linecap="round"/> <!-- ZA -->
      <line x1="535" y1="170" x2="600" y2="75" stroke="#7c3aed" stroke-width="3" stroke-linecap="round"/> <!-- ZB -->
      <line x1="535" y1="170" x2="600" y2="265" stroke="#7c3aed" stroke-width="3" stroke-linecap="round"/> <!-- ZC -->

      <!-- Ramas restantes Z2 y Z4 -->
      <line x1="600" y1="75" x2="680" y2="170" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>
      <line x1="600" y1="265" x2="680" y2="170" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>

      <!-- Etiquetas de Impedancia Reducida -->
      <!-- ZA -->
      <rect x="480" y="140" width="46" height="24" rx="5" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.5" filter="url(#shadowFilterPuente)"/>
      <text x="503" y="157" font-size="13" font-weight="800" fill="#6d28d9" text-anchor="middle">Z<tspan font-size="9" dy="2">A</tspan></text>

      <!-- ZB -->
      <rect x="540" y="105" width="46" height="24" rx="5" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.5" filter="url(#shadowFilterPuente)"/>
      <text x="563" y="122" font-size="13" font-weight="800" fill="#6d28d9" text-anchor="middle">Z<tspan font-size="9" dy="2">B</tspan></text>

      <!-- ZC -->
      <rect x="540" y="205" width="46" height="24" rx="5" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.5" filter="url(#shadowFilterPuente)"/>
      <text x="563" y="222" font-size="13" font-weight="800" fill="#6d28d9" text-anchor="middle">Z<tspan font-size="9" dy="2">C</tspan></text>

      <!-- Z2 -->
      <rect x="635" y="105" width="46" height="24" rx="5" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.3" filter="url(#shadowFilterPuente)"/>
      <text x="658" y="122" font-size="13" font-weight="700" fill="#0f172a" text-anchor="middle">Z<tspan font-size="9" dy="2">2</tspan></text>

      <!-- Z4 -->
      <rect x="635" y="205" width="46" height="24" rx="5" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.3" filter="url(#shadowFilterPuente)"/>
      <text x="658" y="222" font-size="13" font-weight="700" fill="#0f172a" text-anchor="middle">Z<tspan font-size="9" dy="2">4</tspan></text>

      <!-- Nodos Reducidos -->
      <!-- Terminal In A -->
      <circle cx="420" cy="170" r="5" fill="#0f172a"/>
      <text x="408" y="174" font-size="13" font-weight="800" fill="#0f172a" text-anchor="end">A (+)</text>

      <!-- Nodo 1 -->
      <circle cx="470" cy="170" r="12" fill="#bfdbfe" stroke="#0284c7" stroke-width="2.5"/>
      <text x="470" y="174" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">1</text>

      <!-- Nodo Neutro O (Estrella) -->
      <circle cx="535" cy="170" r="14" fill="#ede9fe" stroke="#7c3aed" stroke-width="2.5"/>
      <text x="535" y="174" font-size="12" font-weight="800" fill="#6d28d9" text-anchor="middle">O</text>

      <!-- Nodo 2 -->
      <circle cx="600" cy="75" r="12" fill="#bfdbfe" stroke="#0284c7" stroke-width="2.5"/>
      <text x="600" y="79" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">2</text>

      <!-- Nodo 3 -->
      <circle cx="600" cy="265" r="12" fill="#bfdbfe" stroke="#0284c7" stroke-width="2.5"/>
      <text x="600" y="269" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">3</text>

      <!-- Nodo 4 -->
      <circle cx="680" cy="170" r="12" fill="#bfdbfe" stroke="#0284c7" stroke-width="2.5"/>
      <text x="680" y="174" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">4</text>

      <!-- Terminal Out B -->
      <circle cx="750" cy="170" r="5" fill="#0f172a"/>
      <text x="762" y="174" font-size="13" font-weight="800" fill="#0f172a" text-anchor="start">B (−)</text>
    </svg>
  </div>
</div>
```
