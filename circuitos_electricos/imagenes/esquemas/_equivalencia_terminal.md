```{=html}
<div class="my-4 d-flex justify-content-center">
  <div class="border rounded-3 bg-white shadow-sm p-3 w-100" style="max-width: 820px;">
    <svg viewBox="0 0 780 340" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display:block; font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;">
      <!-- Filtros y Definiciones -->
      <defs>
        <filter id="shadowEq" x="-10%" y="-10%" width="120%" height="120%">
          <feDropShadow dx="0" dy="1.5" stdDeviation="2.5" flood-opacity="0.08"/>
        </filter>
        <marker id="arrowEq" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0284c7"/>
        </marker>
        <marker id="arrowEqPurple" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#7c3aed"/>
        </marker>
      </defs>

      <!-- ================= CONTENEDOR 1: RED DELTA ================= -->
      <!-- Caja de frontera terminal (envolvente) -->
      <rect x="25" y="20" width="310" height="295" rx="12" fill="#f8fafc" stroke="#0284c7" stroke-width="1.8" stroke-dasharray="6 4" opacity="0.95"/>
      <rect x="40" y="30" width="125" height="22" rx="5" fill="#e0f2fe"/>
      <text x="102" y="45" font-size="11" font-weight="800" fill="#0369a1" text-anchor="middle">RED DELTA (Δ)</text>

      <!-- Ramas Delta internas -->
      <line x1="180" y1="80" x2="70" y2="250" stroke="#1e293b" stroke-width="2.6" stroke-linecap="round"/>
      <line x1="180" y1="80" x2="290" y2="250" stroke="#1e293b" stroke-width="2.6" stroke-linecap="round"/>
      <line x1="70" y1="250" x2="290" y2="250" stroke="#1e293b" stroke-width="2.6" stroke-linecap="round"/>

      <!-- Impedancias Delta -->
      <!-- Z_C (Rama A-B) -->
      <rect x="88" y="145" width="46" height="24" rx="5" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.4" filter="url(#shadowEq)"/>
      <text x="111" y="161" font-size="12" font-weight="700" fill="#0f172a" text-anchor="middle">Z<tspan font-size="9" dy="2">C</tspan></text>

      <!-- Z_B (Rama A-C) -->
      <rect x="228" y="145" width="46" height="24" rx="5" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.4" filter="url(#shadowEq)"/>
      <text x="251" y="161" font-size="12" font-weight="700" fill="#0f172a" text-anchor="middle">Z<tspan font-size="9" dy="2">B</tspan></text>

      <!-- Z_A (Rama B-C) -->
      <rect x="157" y="258" width="46" height="24" rx="5" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.4" filter="url(#shadowEq)"/>
      <text x="180" y="274" font-size="12" font-weight="700" fill="#0f172a" text-anchor="middle">Z<tspan font-size="9" dy="2">A</tspan></text>

      <!-- Flechas de Corriente Terminal Externa (I_A, I_B, I_C) -->
      <line x1="180" y1="48" x2="180" y2="70" stroke="#0284c7" stroke-width="2" marker-end="url(#arrowEq)"/>
      <text x="195" y="60" font-size="11" font-weight="800" fill="#0284c7">I<tspan font-size="9" dy="2">A</tspan></text>

      <line x1="38" y1="272" x2="60" y2="256" stroke="#0284c7" stroke-width="2" marker-end="url(#arrowEq)"/>
      <text x="35" y="262" font-size="11" font-weight="800" fill="#0284c7">I<tspan font-size="9" dy="2">B</tspan></text>

      <line x1="322" y1="272" x2="300" y2="256" stroke="#0284c7" stroke-width="2" marker-end="url(#arrowEq)"/>
      <text x="318" y="262" font-size="11" font-weight="800" fill="#0284c7">I<tspan font-size="9" dy="2">C</tspan></text>

      <!-- Terminales Externos Delta (A, B, C) -->
      <!-- Terminal A -->
      <circle cx="180" cy="80" r="15" fill="#bfdbfe" stroke="#0284c7" stroke-width="2.5" filter="url(#shadowEq)"/>
      <text x="180" y="84" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">A</text>

      <!-- Terminal B -->
      <circle cx="70" cy="250" r="15" fill="#bfdbfe" stroke="#0284c7" stroke-width="2.5" filter="url(#shadowEq)"/>
      <text x="70" y="254" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">B</text>

      <!-- Terminal C -->
      <circle cx="290" cy="250" r="15" fill="#bfdbfe" stroke="#0284c7" stroke-width="2.5" filter="url(#shadowEq)"/>
      <text x="290" y="254" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">C</text>

     

      <!-- ================= CONTENEDOR 2: RED ESTRELLA ================= -->
      <!-- Caja de frontera terminal (envolvente) -->
      <rect x="445" y="20" width="310" height="295" rx="12" fill="#faf5ff" stroke="#7c3aed" stroke-width="1.8" stroke-dasharray="6 4" opacity="0.95"/>
      <rect x="460" y="30" width="135" height="22" rx="5" fill="#f3e8ff"/>
      <text x="527" y="45" font-size="11" font-weight="800" fill="#6b21a8" text-anchor="middle">RED ESTRELLA (Y)</text>

       <!-- ================= ZONA CENTRAL: EQUIVALENCIA ================= -->
      <line x1="390" y1="55" x2="390" y2="295" stroke="#e2e8f0" stroke-width="1.8" stroke-dasharray="4 4"/>
      
      <!-- Badge de Equivalencia -->
      <g transform="translate(390, 165)">
        <circle cx="0" cy="0" r="28" fill="#ffffff" stroke="#0ea5e9" stroke-width="2.2" filter="url(#shadowEq)"/>
        <text x="0" y="6" font-size="22" font-weight="900" fill="#0284c7" text-anchor="middle">⇄</text>
        <rect x="-65" y="36" width="130" height="26" rx="6" fill="#0f172a" filter="url(#shadowEq)"/>
        <text x="0" y="53" font-size="10.5" font-weight="700" fill="#f8fafc" text-anchor="middle">EQUIVALENCIA</text>
        
      </g>

      <!-- Ramas Estrella internas -->
      <line x1="600" y1="80" x2="600" y2="180" stroke="#1e293b" stroke-width="2.6" stroke-linecap="round"/>
      <line x1="490" y1="250" x2="600" y2="180" stroke="#1e293b" stroke-width="2.6" stroke-linecap="round"/>
      <line x1="710" y1="250" x2="600" y2="180" stroke="#1e293b" stroke-width="2.6" stroke-linecap="round"/>

      <!-- Impedancias Estrella -->
      <!-- Z_1 (Rama A-O) -->
      <rect x="612" y="115" width="46" height="24" rx="5" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.4" filter="url(#shadowEq)"/>
      <text x="635" y="131" font-size="12" font-weight="700" fill="#0f172a" text-anchor="middle">Z<tspan font-size="9" dy="2">1</tspan></text>

      <!-- Z_2 (Rama B-O) -->
      <rect x="506" y="198" width="46" height="24" rx="5" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.4" filter="url(#shadowEq)"/>
      <text x="529" y="214" font-size="12" font-weight="700" fill="#0f172a" text-anchor="middle">Z<tspan font-size="9" dy="2">2</tspan></text>

      <!-- Z_3 (Rama C-O) -->
      <rect x="650" y="198" width="46" height="24" rx="5" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.4" filter="url(#shadowEq)"/>
      <text x="673" y="214" font-size="12" font-weight="700" fill="#0f172a" text-anchor="middle">Z<tspan font-size="9" dy="2">3</tspan></text>

      <!-- Nodo Neutro Central (O) -->
      <circle cx="600" cy="180" r="13" fill="#f1f5f9" stroke="#64748b" stroke-width="2.2"/>
      <text x="600" y="184" font-size="11" font-weight="800" fill="#334155" text-anchor="middle">O</text>

      <!-- Flechas de Corriente Terminal Externa (I_A, I_B, I_C) -->
      <line x1="600" y1="48" x2="600" y2="70" stroke="#7c3aed" stroke-width="2" marker-end="url(#arrowEqPurple)"/>
      <text x="615" y="60" font-size="11" font-weight="800" fill="#7c3aed">I<tspan font-size="9" dy="2">A</tspan></text>

      <line x1="458" y1="272" x2="480" y2="256" stroke="#7c3aed" stroke-width="2" marker-end="url(#arrowEqPurple)"/>
      <text x="455" y="262" font-size="11" font-weight="800" fill="#7c3aed">I<tspan font-size="9" dy="2">B</tspan></text>

      <line x1="742" y1="272" x2="720" y2="256" stroke="#7c3aed" stroke-width="2" marker-end="url(#arrowEqPurple)"/>
      <text x="738" y="262" font-size="11" font-weight="800" fill="#7c3aed">I<tspan font-size="9" dy="2">C</tspan></text>

      <!-- Terminales Externos Estrella (A, B, C) -->
      <!-- Terminal A -->
      <circle cx="600" cy="80" r="15" fill="#ede9fe" stroke="#7c3aed" stroke-width="2.5" filter="url(#shadowEq)"/>
      <text x="600" y="84" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">A</text>

      <!-- Terminal B -->
      <circle cx="490" cy="250" r="15" fill="#ede9fe" stroke="#7c3aed" stroke-width="2.5" filter="url(#shadowEq)"/>
      <text x="490" y="254" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">B</text>

      <!-- Terminal C -->
      <circle cx="710" cy="250" r="15" fill="#ede9fe" stroke="#7c3aed" stroke-width="2.5" filter="url(#shadowEq)"/>
      <text x="710" y="254" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">C</text>
    </svg>
  </div>
</div>
```
