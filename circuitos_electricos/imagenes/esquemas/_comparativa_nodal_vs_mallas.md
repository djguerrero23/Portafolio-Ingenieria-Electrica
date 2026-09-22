```{=html}
<div class="my-4 d-flex justify-content-center">
  <div class="border rounded-3 bg-white shadow-sm p-3 w-100" style="max-width: 980px;">
    <svg viewBox="0 0 960 430" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display:block; font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;">
      <defs>
        <!-- Marcador de flecha para corrientes de malla -->
        <marker id="arrow-mesh" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#dc2626" />
        </marker>
        <!-- Marcador de flecha para fuentes de corriente -->
        <marker id="arrow-source" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#059669" />
        </marker>
        <filter id="card-shadow" x="-5%" y="-5%" width="110%" height="110%">
          <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.08"/>
        </filter>
      </defs>

      <!-- ============================================================ -->
      <!-- PANEL IZQUIERDO: TOPOLOGÍA IDEAL PARA ANÁLISIS NODAL          -->
      <!-- ============================================================ -->
      <!-- Fondo contenedor izquierdo -->
      <rect x="15" y="15" width="455" height="400" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5" />
      
      <!-- Encabezado Nodal -->
      <rect x="35" y="28" width="195" height="28" rx="6" fill="#059669" />
      <text x="132" y="47" font-size="13" font-weight="700" fill="#ffffff" text-anchor="middle">RECOMENDADO: NODOS</text>
      
      <text x="35" y="78" font-size="14" font-weight="800" fill="#065f46">Topología en Paralelo / Nodal</text>
      <text x="35" y="96" font-size="12" fill="#047857">Pocos nodos esenciales y fuentes de corriente directas</text>

      <!-- Circuito Nodal -->
      <!-- Línea bus de referencia (Tierra) -->
      <line x1="50" y1="260" x2="430" y2="260" stroke="#0f172a" stroke-width="2.5" />
      <!-- Símbolo de tierra -->
      <g transform="translate(240, 260)">
        <line x1="0" y1="0" x2="0" y2="12" stroke="#0f172a" stroke-width="2" />
        <line x1="-14" y1="12" x2="14" y2="12" stroke="#0f172a" stroke-width="2" />
        <line x1="-9" y1="17" x2="9" y2="17" stroke="#0f172a" stroke-width="1.8" />
        <line x1="-4" y1="22" x2="4" y2="22" stroke="#0f172a" stroke-width="1.5" />
        <text x="24" y="16" font-size="11" font-weight="bold" fill="#64748b">Ref (0 V)</text>
      </g>

      <!-- Rama 1: Fuente de corriente Is1 (x=80) -->
      <line x1="80" y1="260" x2="80" y2="150" stroke="#0f172a" stroke-width="2" />
      <!-- Círculo fuente Is1 -->
      <circle cx="80" cy="205" r="18" fill="#ffffff" stroke="#059669" stroke-width="2" />
      <line x1="80" y1="216" x2="80" y2="194" stroke="#059669" stroke-width="2" marker-end="url(#arrow-source)" />
      <text x="50" y="210" font-size="12" font-weight="bold" fill="#059669" text-anchor="end">I<tspan baseline-shift="sub" font-size="0.75em">s1</tspan></text>

      <!-- Rama 2: Impedancia Z1 a tierra (x=160) -->
      <line x1="160" y1="260" x2="160" y2="150" stroke="#0f172a" stroke-width="2" />
      <rect x="149" y="185" width="22" height="42" rx="3" fill="#ffffff" stroke="#0f172a" stroke-width="1.8" />
      <text x="138" y="210" font-size="12" font-style="italic" font-weight="bold" fill="#0f172a" text-anchor="end">Z<tspan baseline-shift="sub" font-size="0.75em">1</tspan></text>

      <!-- Rama 3: Impedancia central Z12 de enlace entre Nodo 1 y 2 -->
      <line x1="80" y1="150" x2="400" y2="150" stroke="#0f172a" stroke-width="2" />
      <rect x="219" y="139" width="42" height="22" rx="3" fill="#ffffff" stroke="#0f172a" stroke-width="1.8" />
      <text x="240" y="132" font-size="12" font-style="italic" font-weight="bold" fill="#0f172a" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.75em">12</tspan></text>

      <!-- Rama 4: Impedancia Z2 a tierra (x=320) -->
      <line x1="320" y1="260" x2="320" y2="150" stroke="#0f172a" stroke-width="2" />
      <rect x="309" y="185" width="22" height="42" rx="3" fill="#ffffff" stroke="#0f172a" stroke-width="1.8" />
      <text x="342" y="210" font-size="12" font-style="italic" font-weight="bold" fill="#0f172a" text-anchor="start">Z<tspan baseline-shift="sub" font-size="0.75em">2</tspan></text>

      <!-- Rama 5: Fuente de corriente Is2 (x=400) -->
      <line x1="400" y1="260" x2="400" y2="150" stroke="#0f172a" stroke-width="2" />
      <!-- Círculo fuente Is2 -->
      <circle cx="400" cy="205" r="18" fill="#ffffff" stroke="#059669" stroke-width="2" />
      <line x1="400" y1="216" x2="400" y2="194" stroke="#059669" stroke-width="2" marker-end="url(#arrow-source)" />
      <text x="430" y="210" font-size="12" font-weight="bold" fill="#059669" text-anchor="start">I<tspan baseline-shift="sub" font-size="0.75em">s2</tspan></text>

      <!-- Destacar Nodos Esenciales -->
      <!-- Nodo 1 -->
      <circle cx="160" cy="150" r="7" fill="#059669" stroke="#ffffff" stroke-width="2" />
      <rect x="135" y="108" width="50" height="24" rx="12" fill="#059669" />
      <text x="160" y="124" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">V₁ (?)</text>

      <!-- Nodo 2 -->
      <circle cx="320" cy="150" r="7" fill="#059669" stroke="#ffffff" stroke-width="2" />
      <rect x="295" y="108" width="50" height="24" rx="12" fill="#059669" />
      <text x="320" y="124" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">V₂ (?)</text>

      <!-- Píldoras de Conclusión Nodal -->
      <rect x="35" y="300" width="415" height="100" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1" />
      <text x="48" y="322" font-size="12" font-weight="bold" fill="#059669">✅ Ventaja Nodal: Solo 2 ecuaciones lineales</text>
      <text x="48" y="342" font-size="11.5" fill="#334155">• Nodos independientes: <tspan font-weight="bold">N - 1 = 2 incógnitas (V₁, V₂)</tspan></text>
      <text x="48" y="360" font-size="11.5" fill="#334155">• Matriz [Y] ensamblable directamente por inspección visual</text>
      <text x="48" y="382" font-size="11.5" fill="#dc2626">❌ Por Mallas: Exigiría 4 mallas y tratar 2 supermallas</text>


      <!-- ============================================================ -->
      <!-- SEPARADOR CENTRAL                                            -->
      <!-- ============================================================ -->
      <line x1="480" y1="35" x2="480" y2="395" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="6 6" />
      <circle cx="480" cy="215" r="16" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5" />
      <text x="480" y="220" font-size="11" font-weight="bold" fill="#64748b" text-anchor="middle">VS</text>


      <!-- ============================================================ -->
      <!-- PANEL DERECHO: TOPOLOGÍA IDEAL PARA ANÁLISIS DE MALLAS        -->
      <!-- ============================================================ -->
      <!-- Fondo contenedor derecho -->
      <rect x="490" y="15" width="455" height="400" rx="10" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.5" />

      <!-- Encabezado Mallas -->
      <rect x="510" y="28" width="195" height="28" rx="6" fill="#dc2626" />
      <text x="607" y="47" font-size="13" font-weight="700" fill="#ffffff" text-anchor="middle">RECOMENDADO: MALLAS</text>

      <text x="510" y="78" font-size="14" font-weight="800" fill="#991b1b">Topología Plana en Escalera (Ladder)</text>
      <text x="510" y="96" font-size="12" fill="#b91c1c">Pocas ventanas cerradas y fuentes de tensión serie</text>

      <!-- Circuito Mallas (Escalera de 2 mallas) -->
      <!-- Línea exterior -->
      <!-- Malla 1: (545, 140) a (695, 260) -->
      <!-- Malla 2: (695, 140) a (845, 260) -->
      
      <!-- Línea inferior común -->
      <line x1="545" y1="260" x2="845" y2="260" stroke="#0f172a" stroke-width="2" />
      
      <!-- Rama Izquierda: Fuente de tensión Vs1 -->
      <line x1="545" y1="260" x2="545" y2="140" stroke="#0f172a" stroke-width="2" />
      <circle cx="545" cy="200" r="17" fill="#ffffff" stroke="#dc2626" stroke-width="2" />
      <text x="545" y="196" font-size="13" font-weight="bold" fill="#dc2626" text-anchor="middle">+</text>
      <text x="545" y="210" font-size="14" font-weight="bold" fill="#dc2626" text-anchor="middle">-</text>
      <text x="518" y="204" font-size="12" font-weight="bold" fill="#dc2626" text-anchor="end">V<tspan baseline-shift="sub" font-size="0.75em">s1</tspan></text>

      <!-- Rama Superior Malla 1: Impedancia Za -->
      <line x1="545" y1="140" x2="695" y2="140" stroke="#0f172a" stroke-width="2" />
      <rect x="599" y="129" width="42" height="22" rx="3" fill="#ffffff" stroke="#0f172a" stroke-width="1.8" />
      <text x="620" y="123" font-size="12" font-style="italic" font-weight="bold" fill="#0f172a" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.75em">a</tspan></text>

      <!-- Rama Central Compartida: Impedancia Zc -->
      <line x1="695" y1="140" x2="695" y2="260" stroke="#0f172a" stroke-width="2" />
      <rect x="684" y="180" width="22" height="42" rx="3" fill="#ffffff" stroke="#0f172a" stroke-width="1.8" />
      <text x="674" y="204" font-size="12" font-style="italic" font-weight="bold" fill="#0f172a" text-anchor="end">Z<tspan baseline-shift="sub" font-size="0.75em">c</tspan></text>

      <!-- Rama Superior Malla 2: Impedancia Zb -->
      <line x1="695" y1="140" x2="845" y2="140" stroke="#0f172a" stroke-width="2" />
      <rect x="749" y="129" width="42" height="22" rx="3" fill="#ffffff" stroke="#0f172a" stroke-width="1.8" />
      <text x="770" y="123" font-size="12" font-style="italic" font-weight="bold" fill="#0f172a" text-anchor="middle">Z<tspan baseline-shift="sub" font-size="0.75em">b</tspan></text>

      <!-- Rama Derecha: Fuente de tensión Vs2 -->
      <line x1="845" y1="140" x2="845" y2="260" stroke="#0f172a" stroke-width="2" />
      <circle cx="845" cy="200" r="17" fill="#ffffff" stroke="#dc2626" stroke-width="2" />
      <text x="845" y="196" font-size="13" font-weight="bold" fill="#dc2626" text-anchor="middle">+</text>
      <text x="845" y="210" font-size="14" font-weight="bold" fill="#dc2626" text-anchor="middle">-</text>
      <text x="872" y="204" font-size="12" font-weight="bold" fill="#dc2626" text-anchor="start">V<tspan baseline-shift="sub" font-size="0.75em">s2</tspan></text>

      <!-- Corriente de Malla 1 (Flecha circular horaria roja) -->
      <path d="M 610,182 A 20,20 0 1,1 628,212" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#arrow-mesh)" />
      <rect x="608" y="190" width="24" height="18" rx="4" fill="#fee2e2" />
      <text x="620" y="203" font-size="12" font-weight="bold" fill="#dc2626" text-anchor="middle">I₁</text>

      <!-- Corriente de Malla 2 (Flecha circular horaria roja) -->
      <path d="M 760,182 A 20,20 0 1,1 778,212" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#arrow-mesh)" />
      <rect x="758" y="190" width="24" height="18" rx="4" fill="#fee2e2" />
      <text x="770" y="203" font-size="12" font-weight="bold" fill="#dc2626" text-anchor="middle">I₂</text>

      <!-- Píldoras de Conclusión Mallas -->
      <rect x="510" y="300" width="415" height="100" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1" />
      <text x="523" y="322" font-size="12" font-weight="bold" fill="#dc2626">✅ Ventaja Mallas: Solo 2 ecuaciones lineales</text>
      <text x="523" y="342" font-size="11.5" fill="#334155">• Lazos independientes: <tspan font-weight="bold">M = 2 mallas simples (I₁, I₂)</tspan></text>
      <text x="523" y="360" font-size="11.5" fill="#334155">• Fuentes de tensión en serie entran directo en el vector [V]</text>
      <text x="523" y="382" font-size="11.5" fill="#d97706">⚠️ Por Nodos: Requiere 4 nodos y lidiar con fuentes de tensión</text>

    </svg>
  </div>
</div>
```
