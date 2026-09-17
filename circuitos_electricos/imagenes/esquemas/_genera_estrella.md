```{=html}
<div class="my-4 d-flex justify-content-center">
  <div class="border rounded-3 bg-white shadow-sm p-3 w-100" style="max-width: 440px;">
    <svg viewBox="0 0 380 320" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display:block; font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;">
      <!-- Fondo y defs -->
      <defs>
        <filter id="shadowFilterEstrella" x="-10%" y="-10%" width="120%" height="120%">
          <feDropShadow dx="0" dy="1" stdDeviation="2" flood-opacity="0.08"/>
        </filter>
      </defs>

      <!-- ================= ESTRELLA (Y) ================= -->
      <text x="190" y="30" font-size="16" font-weight="800" fill="#7c3aed" text-anchor="middle">Configuración Estrella (Y)</text>

      <!-- Ramas Estrella -->
      <line x1="190" y1="70" x2="190" y2="175" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>
      <line x1="70" y1="250" x2="190" y2="175" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>
      <line x1="310" y1="250" x2="190" y2="175" stroke="#1e293b" stroke-width="2.8" stroke-linecap="round"/>

      <!-- Etiquetas de Impedancia Estrella -->
      <!-- Z_1 (Rama A-O) -->
      <rect x="202" y="110" width="48" height="26" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" filter="url(#shadowFilterEstrella)"/>
      <text x="226" y="128" font-size="14" font-weight="700" fill="#0f172a" text-anchor="middle">Z<tspan font-size="10" dy="3">1</tspan></text>

      <!-- Z_2 (Rama B-O) -->
      <rect x="90" y="196" width="48" height="26" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" filter="url(#shadowFilterEstrella)"/>
      <text x="114" y="214" font-size="14" font-weight="700" fill="#0f172a" text-anchor="middle">Z<tspan font-size="10" dy="3">2</tspan></text>

      <!-- Z_3 (Rama C-O) -->
      <rect x="242" y="196" width="48" height="26" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" filter="url(#shadowFilterEstrella)"/>
      <text x="266" y="214" font-size="14" font-weight="700" fill="#0f172a" text-anchor="middle">Z<tspan font-size="10" dy="3">3</tspan></text>

      <!-- Nodo Neutro (O) -->
      <circle cx="190" cy="175" r="16" fill="#64748b" opacity="0.15"/>
      <circle cx="190" cy="175" r="12" fill="#f1f5f9" stroke="#64748b" stroke-width="2.4"/>
      <text x="190" y="179" font-size="12" font-weight="800" fill="#334155" text-anchor="middle">O</text>

      <!-- Nodos Estrella Externos -->
      <!-- Nodo A -->
      <circle cx="190" cy="70" r="18" fill="#7c3aed" opacity="0.18"/>
      <circle cx="190" cy="70" r="14" fill="#ede9fe" stroke="#7c3aed" stroke-width="2.8"/>
      <text x="190" y="75" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">A</text>

      <!-- Nodo B -->
      <circle cx="70" cy="250" r="18" fill="#7c3aed" opacity="0.18"/>
      <circle cx="70" cy="250" r="14" fill="#ede9fe" stroke="#7c3aed" stroke-width="2.8"/>
      <text x="70" y="255" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">B</text>

      <!-- Nodo C -->
      <circle cx="310" cy="250" r="18" fill="#7c3aed" opacity="0.18"/>
      <circle cx="310" cy="250" r="14" fill="#ede9fe" stroke="#7c3aed" stroke-width="2.8"/>
      <text x="310" y="255" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">C</text>
    </svg>
  </div>
</div>
```
