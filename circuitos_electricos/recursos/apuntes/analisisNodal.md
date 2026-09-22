---
title: "Análisis Nodal en Corriente Alterna"
subtitle: "Formulación sistemática por Ley de Corrientes de Kirchhoff (LCK) y Matriz de Admitancias Complejas"
description: "Guía maestra y rigurosa de análisis nodal en CA: criterios de decisión (Nodos vs Mallas), formulación matricial [Y][V] = [I], tratamiento de supernodos, fuentes controladas y resolución paso a paso."
author: "David Guerrero"
date: "2026-09-16"
categories: [Métodos de Redes, Análisis Nodal, Admitancias, LCK, Circuitos CA, Supernodos]
format:
  html:
    toc: true
    toc-depth: 3
    number-sections: true
---

::: {.hero-banner-modern}
# Análisis Nodal en Régimen Sinusoidal Permanente {.unnumbered}
**Formulación sistemática de redes eléctricas mediante potenciales de nodo y leyes de corrientes.**

El método de análisis nodal es la herramienta fundamental más potente en la ingeniería eléctrica moderna. Constituye la base algorítmica de los simuladores computacionales (SPICE, EMTP) y del análisis de flujos de potencia en sistemas eléctricos, permitiendo resolver cualquier red lineal independientemente de su complejidad o topología.
:::

---

# Criterio de Decisión: ¿Cuándo utilizar Análisis Nodal?

Antes de plantear ecuaciones, un ingeniero debe seleccionar la técnica de análisis óptima evaluando la topología de la red:

::: {.grid}

::: {.g-col-12 .g-col-md-6}
::: {.card-module style="border-top: 4px solid #059669;"}
### ✅ ¿Cuándo es PREFERIBLE el Análisis Nodal?

1. **Menor número de incógnitas:** Cuando el número de nodos esenciales independientes $(N_e - 1)$ es menor que el número de mallas independientes $(B - N_e + 1)$.
2. **Abundancia de fuentes de corriente:** Las fuentes de corriente independientes fijan directamente los términos del vector de inyección $[\mathbf{I}]$ sin añadir ecuaciones auxiliares.
3. **Fuentes de tensión conectadas a referencia:** Fijan directamente el potencial del nodo ($\mathbf{V}_k = \mathbf{V}_s$), reduciendo la dimensión del sistema en una incógnita por cada fuente.
4. **Redes No Planares (Cruces tridimensionales de ramas):** El método de mallas **no se puede aplicar** en redes no planares (redes que no pueden dibujarse en un plano sin cruce de conductores). El análisis nodal es universal y funciona en cualquier topología.
5. **Formulación computacional directa:** La matriz de admitancias de barra $[\mathbf{Y}]$ se puede ensamblar por inspección directa mediante reglas topológicas simples.

![](imagenes/topologia_optima_nodal.jpg){width=95% fig-align="center"}
:::
:::

::: {.g-col-12 .g-col-md-6}
::: {.card-module style="border-top: 4px solid #dc2626;"}
### ❌ ¿Cuándo es MEJOR el Análisis de Mallas?

1. **Muchas fuentes de tensión en serie con ramas:** Las fuentes de tensión facilitan el planteamiento de tensiones de malla (LKT) sin requerir supernodos.
2. **Menor número de mallas que de nodos:** Redes en cascada o circuitos escalera (ladder networks) donde hay pocas mallas y muchos nodos.
3. **Múltiples fuentes de tensión flotantes:** Si hay demasiadas fuentes de tensión no conectadas a tierra, el análisis nodal requiere múltiples supernodos y ecuaciones de ligadura simultáneas.
4. **Variables de interés en serie:** Cuando el objetivo principal es calcular la corriente de una malla específica o rama en serie.

![](imagenes/topologia_optima_mallas.jpg){width=95% fig-align="center"}
:::
:::

:::

{{< include imagenes/esquemas/_comparativa_nodal_vs_mallas.md >}}

---

# Fundamento Físico y Matemático

::: {.callout-note}
### ⚡ Principio Físico: Conservación de la Carga (LCK)
En cualquier instante $t$ y en régimen permanente sinusoidal, la carga eléctrica no puede acumularse en un nodo ideal sin capacitancia parásita concentrada. Por tanto, la suma fasorial de las corrientes que abandonan cualquier nodo cerrado $\mathcal{S}_k$ es idénticamente nula:

$$\sum_{m \in \text{adyacentes}} \mathbf{I}_{km} = \mathbf{I}_{s,k}$$

Donde $\mathbf{I}_{km}$ es la corriente que fluye del nodo $k$ al nodo $m$, e $\mathbf{I}_{s,k}$ es la corriente neta inyectada por fuentes externas conectadas al nodo $k$.
:::

### Relación Constitutiva de Rama en el Dominio Fasorial

Para una rama conectada entre el nodo $i$ (potencial $\mathbf{V}_i$) y el nodo $j$ (potencial $\mathbf{V}_j$) con impedancia $\mathbf{Z}_{ij}$ y admitancia $\mathbf{Y}_{ij} = \dfrac{1}{\mathbf{Z}_{ij}}$:

$$\mathbf{I}_{ij} = \frac{\mathbf{V}_i - \mathbf{V}_j}{\mathbf{Z}_{ij}} = \mathbf{Y}_{ij}(\mathbf{V}_i - \mathbf{V}_j)$$

Al sustituir esta expresión en la LCK de cada nodo $i$, agrupamos los términos asociados a cada potencial nodal:

$$\mathbf{V}_i \underbrace{\left(\sum_{j} \mathbf{Y}_{ij}\right)}_{\mathbf{Y}_{ii}} - \sum_{j \neq i} \mathbf{V}_j \underbrace{\left(\mathbf{Y}_{ij}\right)}_{-\mathbf{Y}_{ij}} = \mathbf{I}_{\text{inyectada}, i}$$

---

# Formulación Matricial por Inspección: $[\mathbf{Y}][\mathbf{V}] = [\mathbf{I}]$

Para una red con $N$ nodos independientes (excluyendo el nodo de referencia asignado como tierra, $\mathbf{V}_{\text{ref}} = 0\text{ V}$):

$$
\begin{bmatrix}
\mathbf{Y}_{11} & \mathbf{Y}_{12} & \cdots & \mathbf{Y}_{1N} \\
\mathbf{Y}_{21} & \mathbf{Y}_{22} & \cdots & \mathbf{Y}_{2N} \\
\vdots & \vdots & \ddots & \vdots \\
\mathbf{Y}_{N1} & \mathbf{Y}_{N2} & \cdots & \mathbf{Y}_{NN}
\end{bmatrix}
\begin{bmatrix}
\mathbf{V}_1 \\
\mathbf{V}_2 \\
\vdots \\
\mathbf{V}_N
\end{bmatrix}
=
\begin{bmatrix}
\mathbf{I}_1 \\
\mathbf{I}_2 \\
\vdots \\
\mathbf{I}_N
\end{bmatrix}
$$

### Reglas de Ensamblaje Directo de la Matriz $[\mathbf{Y}]$

::: {.callout-important}
### 📌 Reglas de Oro para la Matriz de Admitancias $[\mathbf{Y}]$

1. **Admitancias Propias (Diagonal Principal $\mathbf{Y}_{ii}$):**
   $$\mathbf{Y}_{ii} = \sum (\text{Admitancias complejas de todas las ramas conectadas directamente al nodo } i)$$
   * Siempre lleva signo **positivo**.
   * Su parte real representa la conductancia propia ($G_{ii} \ge 0$) y su parte imaginaria la susceptancia propia ($B_{ii}$).

2. **Admitancias Mutuas (Elementos Fuera de la Diagonal $\mathbf{Y}_{ij}$ con $i \neq j$):**
   $$\mathbf{Y}_{ij} = -\sum (\text{Admitancias complejas conectadas directamente entre el nodo } i \text{ y el nodo } j)$$
   * Siempre lleva signo **negativo**.
   * En circuitos pasivos recíprocos (sin fuentes controladas), la matriz es estrictamente simétrica: $\mathbf{Y}_{ij} = \mathbf{Y}_{ji}$.

3. **Vector de Inyección de Corrientes ($\mathbf{I}_i$):**
   $$\mathbf{I}_i = \sum \mathbf{I}_{\text{fuentes independientes que ENTRAN al nodo } i} - \sum \mathbf{I}_{\text{fuentes independientes que SALEN del nodo } i}$$
:::

---

# Tratamiento de Casos Especiales
```{mermaid}
%%| fig-width: 8
%%| fig-align: center
flowchart TD
    A["¿Qué tipos de fuentes<br/>contiene la red?"] --> B["Solo fuentes<br/>de corriente"]
    A --> C["Fuentes<br/>de tensión"]

    B --> B1["Inspección directa<br/>[Y][V] = [I] pura"]

    C --> D["Conectada a<br/>referencia"]
    C --> E["Flotante"]

    D --> D1["Fija potencial directo:<br/><b>V<sub>k</sub> = V<sub>fuente</sub></b><br/>(elimina una incógnita)"]

    E --> E1["Requiere SUPERNODO:<br/>LCK global +<br/>ecuación de ligadura"]

    classDef ok fill:#d1fae5,stroke:#059669,stroke-width:2px,color:#065f46
    classDef warn fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#92400e
    classDef neutral fill:#e0e7ff,stroke:#4f46e5,stroke-width:2px,color:#3730a3

    class B1 ok
    class D1 ok
    class E1 warn
    class A neutral
```


## Caso 1: Fuente de Tensión Conectada a Referencia

Si una fuente ideal de tensión $\mathbf{V}_s$ se encuentra conectada entre el nodo $k$ y el nodo de referencia:
* El potencial del nodo $k$ queda fijado de forma unívoca:
  $$\mathbf{V}_k = \mathbf{V}_s$$
* El nodo $k$ deja de ser una incógnita. Se elimina su fila en el sistema o se transfiere como término conocido al vector independiente del lado derecho.

## Caso 2: Fuente de Tensión Flotante — Concepto de Supernodo

Cuando una fuente de tensión (independiente o controlada) une dos nodos no referenciales $k$ y $m$, la corriente $\mathbf{I}_{\text{fuente}}$ que la atraviesa es una incógnita indeterminada a priori por la ley de Ohm ($\Delta \mathbf{V} / 0$).

::: {.callout-warning}
### ⚠️ Metodología del Supernodo
1. **Frontera del Supernodo:** Se dibuja una superficie cerrada que engloba a la fuente de tensión y a los dos nodos $k$ y $m$ que conecta.
2. **Ecuación de LCK Global:** Se suma algebraicamente la corriente de todas las ramas externas que salen del supernodo:
   $$\sum \mathbf{I}_{\text{salientes del nodo } k} + \sum \mathbf{I}_{\text{salientes del nodo } m} = \sum \mathbf{I}_{\text{fuentes inyectadas}}$$
3. **Ecuación de Ligadura de Potencial (LKT interna):** La diferencia de potencial entre los dos nodos está rígidamente fijada por la fuente:
   $$\mathbf{V}_k - \mathbf{V}_m = \mathbf{V}_{\text{fuente}}$$
   *(donde el nodo $k$ se conecta al terminal positivo de la fuente).*
4. **Elementos en Paralelo con la Fuente:** Cualquier impedancia conectada en paralelo directo con la fuente de tensión queda dentro del supernodo y **no altera las ecuaciones nodales externas**.
:::

## Caso 3: Circuitos con Fuentes Controladas (Dependientes)

Las fuentes dependientes introducen acoplamientos asimétricos en el circuito:

1. Trata la fuente controlada inicialmente como si fuera una fuente independiente ordinaria.
2. Expresa la **variable de control** (sea una tensión $\mathbf{V}_x$ o una corriente $\mathbf{I}_x$) en términos estrictos de las tensiones nodales del circuito:
   * Si depende de una tensión: $\mathbf{V}_x = \mathbf{V}_a - \mathbf{V}_b$.
   * Si depende de una corriente: $\mathbf{I}_x = \mathbf{Y}_{ab}(\mathbf{V}_a - \mathbf{V}_b)$.
3. Sustituye la variable de control y transfiere todos los coeficientes que involucren potenciales incógnitas al lado izquierdo de la ecuación matricial.
4. **Consecuencia física:** La matriz $[\mathbf{Y}]$ pierde la simetría ($\mathbf{Y}_{ij} \neq \mathbf{Y}_{ji}$).

---

# Algoritmo Maestro de 5 Pasos para Resolver Cualquier Red Nodal

::: {.callout-tip}
### 📋 Protocolo de Ejecución Sistemática

* **Paso 1 (Dominio Fasorial):** Transforma todas las fuentes temporales a fasores ($\mathbf{V}_s = V_m \angle \theta$, $\mathbf{I}_s = I_m \angle \theta$) y calcula las impedancias ($\mathbf{Z}_R = R$, $\mathbf{Z}_L = j\omega L$, $\mathbf{Z}_C = -j/(\omega C)$) y admitancias complejas ($\mathbf{Y} = 1/\mathbf{Z}$).
* **Paso 2 (Elección Estratégica de Referencia):** Identifica los $N_e$ nodos esenciales. Selecciona como nodo de referencia ($0\text{ V}$) el nodo que conecte la mayor cantidad de ramas o el nodo común al mayor número de fuentes de tensión.
* **Paso 3 (Identificación de Nodos Fijos y Supernodos):**
  * Asigna los valores de los nodos conectados a fuentes con referencia.
  * Encierra cada fuente flotante en un supernodo y formula su ecuación de ligadura.
* **Paso 4 (Planteamiento de Ecuaciones LCK):** Escribe la LCK para cada nodo libre y cada supernodo expresando las corrientes como $\mathbf{Y}(\mathbf{V}_i - \mathbf{V}_j)$.
* **Paso 5 (Resolución Matricial y Variables Secundarias):** Ensambla el sistema $[\mathbf{Y}][\mathbf{V}] = [\mathbf{I}]$, resuelve mediante determinantes (Cramer) o inversión matricial y calcula las corrientes de rama deseadas $\mathbf{I}_{ij} = \mathbf{Y}_{ij}(\mathbf{V}_i - \mathbf{V}_j)$ o potencias complejas $\mathbf{S} = \mathbf{V}\mathbf{I}^*$.
:::

---

# Ejemplos Resueltos

## Ejercicio 1 — Formulación por Inspección Directa (3 Nodos, Fuentes de Corriente)



::: {style="float: right; width: 48%; max-width: 450px; margin: 0 0 1rem 1.5rem;"}
![](imagenes/Eje1Nodal.jpg){width=100% fig-align="center"}
:::
### Enunciado

Para el circuito eléctrico en régimen permanente sinusoidal mostrado en el esquema:

1. **Formulación Matricial:** Calcular las admitancias de rama $\mathbf{Y}_1, \mathbf{Y}_2, \mathbf{Y}_{12}$ y ensamblar directamente por inspección visual el sistema de ecuaciones nodales $[\mathbf{Y}][\mathbf{V}] = [\mathbf{I}]$.
2. **Determinante de Red:** Evaluar el determinante nodal $\Delta_Y$ de la matriz de admitancias complejas.
3. **Cálculo de Potenciales:** Resolver el sistema matricial mediante determinantes (Regla de Cramer) para determinar los fasores de tensión de nodo $\mathbf{V}_1$ y $\mathbf{V}_2$ en forma rectangular y polar.
  


### Solución Paso a Paso

**Paso 1 — Construcción de los coeficientes de la Matriz de Admitancias $[\mathbf{Y}]$:**
* **Admitancia propia del nodo 1 ($\mathbf{Y}_{11}$):**
  $$\mathbf{Y}_{11} = \mathbf{Y}_1 + \mathbf{Y}_{12} = (0.05 - j0.05) + j0.2 = \mathbf{0.05 + j0.15\,\text{S}}$$
* **Admitancia propia del nodo 2 ($\mathbf{Y}_{22}$):**
  $$\mathbf{Y}_{22} = \mathbf{Y}_2 + \mathbf{Y}_{12} = 0.05 + j0.2 = \mathbf{0.05 + j0.20\,\text{S}}$$
* **Admitancia mutua entre nodos 1 y 2 ($\mathbf{Y}_{12} = \mathbf{Y}_{21}$):**
  $$\mathbf{Y}_{12} = -\mathbf{Y}_{12,\text{rama}} = -(j0.2) = \mathbf{-j0.20\,\text{S}}$$

**Paso 2 — Vector de corrientes inyectadas $[\mathbf{I}]$:**
$$\mathbf{I}_1 = 4 + j0\,\text{A}, \qquad \mathbf{I}_2 = 0 + j2\,\text{A}$$

**Paso 3 — Sistema Matricial:**
$$
\begin{bmatrix}
0.05 + j0.15 & -j0.20 \\
-j0.20 & 0.05 + j0.20
\end{bmatrix}
\begin{bmatrix}
\mathbf{V}_1 \\
\mathbf{V}_2
\end{bmatrix}
=
\begin{bmatrix}
4 \\
j2
\end{bmatrix}
$$

**Paso 4 — Cálculo del Determinante $\Delta_Y$:**
$$\Delta_Y = (0.05 + j0.15)(0.05 + j0.20) - (-j0.20)^2$$
$$\Delta_Y = (0.0025 + j0.01 + j0.0075 - 0.03) - (-0.04) = (-0.0275 + j0.0175) + 0.04 = \mathbf{0.0125 + j0.0175\,\text{S}^2}$$

**Paso 5 — Aplicación de la Regla de Cramer:**
$$\mathbf{V}_1 = \frac{\det\begin{bmatrix} 4 & -j0.20 \\ j2 & 0.05 + j0.20 \end{bmatrix}}{\Delta_Y} = \frac{4(0.05 + j0.20) - (j2)(-j0.20)}{0.0125 + j0.0175} = \frac{(0.20 + j0.80) - (0.40)}{0.0125 + j0.0175} = \frac{-0.20 + j0.80}{0.0125 + j0.0175}$$

Multiplicando por el conjugado:
$$\mathbf{V}_1 = \frac{(-0.20 + j0.80)(0.0125 - j0.0175)}{0.0125^2 + 0.0175^2} = \frac{(-0.0025 + j0.0035 + j0.01 + 0.014)}{0.00015625 + 0.00030625} = \frac{0.0115 + j0.0135}{0.0004625} \approx \mathbf{24.86 + j29.19\,\text{V}}$$
$$\boxed{\mathbf{V}_1 \approx 38.34\,\angle\,49.57^\circ\,\text{V}}$$

De igual forma para $\mathbf{V}_2$:
$$\mathbf{V}_2 = \frac{\det\begin{bmatrix} 0.05 + j0.15 & 4 \\ -j0.20 & j2 \end{bmatrix}}{\Delta_Y} = \frac{(0.05 + j0.15)(j2) - (-j0.20)(4)}{0.0125 + j0.0175} = \frac{(-0.30 + j0.10) + j0.80}{0.0125 + j0.0175} = \frac{-0.30 + j0.90}{0.0125 + j0.0175}$$
$$\mathbf{V}_2 = \frac{(-0.30 + j0.90)(0.0125 - j0.0175)}{0.0004625} = \frac{0.0120 + j0.0165}{0.0004625} \approx \mathbf{25.95 + j35.68\,\text{V}}$$
$$\boxed{\mathbf{V}_2 \approx 44.12\,\angle\,53.97^\circ\,\text{V}}$$

---

## Ejercicio 2 — Circuito con Supernodo Flotante

::: {style="float: right; width: 48%; max-width: 450px; margin: 0 0 1rem 1.5rem;"}
![](imagenes/Eje2Nodal.jpg){width=100% fig-align="center"}
:::

### Enunciado
En el circuito de corriente alterna mostrado en el esquema, una fuente de tensión ideal conecta dos nodos no referenciales sin impedancia serie en su rama, originando un **supernodo**:\
1. **Ecuación de Ligadura:** Establecer la relación de potenciales nodales impuesta por la fuente de tensión flotante $\mathbf{V}_s$. \
2. **LCK Global del Supernodo:** Plantear la ecuación de balance de corrientes en la superficie cerrada del supernodo (1-2).\
3. **Tensiones y Corrientes:** Determinar las tensiones fasoriales de nodo $\mathbf{V}_1$ y $\mathbf{V}_2$, así como la corriente neta suministrada por la fuente de tensión flotante.

### Solución Paso a Paso

**Paso 1 — Definición del Supernodo (1-2):**
Encerramos la fuente $\mathbf{V}_s$ y los nodos 1 y 2 en una sola frontera cerrada.

**Paso 2 — Ecuación de LCK del Supernodo (1-2):**
La suma de corrientes salientes del supernodo hacia tierra debe ser igual a la corriente inyectada:
$$\mathbf{I}_{1 \to 0} + \mathbf{I}_{2 \to 0} = \mathbf{I}_s$$
$$\mathbf{Y}_1 \mathbf{V}_1 + \mathbf{Y}_2 \mathbf{V}_2 = j3$$
$$0.2 \mathbf{V}_1 + j0.1 \mathbf{V}_2 = j3 \qquad \text{[Ecuación 1]}$$

**Paso 3 — Ecuación de Ligadura de la Fuente de Tensión:**
$$\mathbf{V}_1 - \mathbf{V}_2 = 20 \implies \mathbf{V}_1 = \mathbf{V}_2 + 20 \qquad \text{[Ecuación 2]}$$

**Paso 4 — Sustitución y Resolución:**
Sustituyendo la Ecuación 2 en la Ecuación 1:
$$0.2(\mathbf{V}_2 + 20) + j0.1 \mathbf{V}_2 = j3$$
$$4 + (0.2 + j0.1)\mathbf{V}_2 = j3$$
$$(0.2 + j0.1)\mathbf{V}_2 = -4 + j3$$

$$\mathbf{V}_2 = \frac{-4 + j3}{0.2 + j0.1} = \frac{(-4 + j3)(0.2 - j0.1)}{0.2^2 + 0.1^2} = \frac{(-0.8 + j0.4 + j0.6 + 0.3)}{0.05} = \frac{-0.5 + j1.0}{0.05} = \mathbf{-10 + j20\,\text{V}}$$
$$\boxed{\mathbf{V}_2 = -10 + j20\,\text{V} \approx 22.36\,\angle\,116.57^\circ\,\text{V}}$$

Calculamos $\mathbf{V}_1$:
$$\mathbf{V}_1 = \mathbf{V}_2 + 20 = (-10 + j20) + 20 = \mathbf{10 + j20\,\text{V}}$$
$$\boxed{\mathbf{V}_1 = 10 + j20\,\text{V} \approx 22.36\,\angle\,63.43^\circ\,\text{V}}$$

**Paso 5 — Corriente suministrada por la fuente flotante ($\mathbf{I}_{\text{fuente}}$):**
Aplicando LCK exclusivamente en el nodo 1:
$$\mathbf{I}_{\text{fuente}} = \mathbf{I}_{1 \to 0} = \mathbf{Y}_1 \mathbf{V}_1 = 0.2(10 + j20) = \mathbf{2 + j4\,\text{A} \approx 4.47\,\angle\,63.43^\circ\,\text{A}}$$

---

## Ejercicio 3 — Circuito con Fuente Dependiente / Controlada (VCCS)

::: {style="float: right; width: 48%; max-width: 450px; margin: 0 0 1rem 1.5rem;"}
![](imagenes/Eje3Nodal.jpg){width=100% fig-align="center"}
:::

### Enunciado

Para el circuito mostrado en el esquema, el cual incorpora una fuente de corriente dependiente controlada por la tensión del nodo 1 ($\mathbf{I}_x = 0.5\,\mathbf{V}_1$):\
1. **Formulación Matricial:** Plantear las ecuaciones de nodo considerando la fuente dependiente y transferir los términos de control a la matriz de admitancias para obtener el sistema $[\mathbf{Y}][\mathbf{V}] = [\mathbf{I}]$.\
2. **Pérdida de Simetría:** Comprobar y explicar analíticamente la asimetría de la matriz de admitancias ($\mathbf{Y}_{12} \neq \mathbf{Y}_{21}$).\
3. **Tensiones y Verificación:** Determinar las tensiones nodales $\mathbf{V}_1$ y $\mathbf{V}_2$, y evaluar el valor y sentido real de la corriente suministrada por la fuente controlada.

### Solución Paso a Paso

**Paso 1 — Planteamiento inicial como fuente independiente.**

Tratamos provisionalmente la VCCS como si fuera una fuente independiente $\mathbf{I}_x$ inyectando al nodo 2. Las ecuaciones nodales por inspección directa son:

$$
\begin{aligned}
(\mathbf{Y}_1 + \mathbf{Y}_{12})\,\mathbf{V}_1 - \mathbf{Y}_{12}\,\mathbf{V}_2 &= \mathbf{I}_{s1} \\
-\mathbf{Y}_{12}\,\mathbf{V}_1 + (\mathbf{Y}_2 + \mathbf{Y}_{12})\,\mathbf{V}_2 &= \mathbf{I}_{x}
\end{aligned}
$$

Sustituyendo valores numéricos:

$$
\begin{aligned}
(0.1 + 0.2)\,\mathbf{V}_1 - 0.2\,\mathbf{V}_2 &= 2 \\
-0.2\,\mathbf{V}_1 + (0.05 + 0.2)\,\mathbf{V}_2 &= \mathbf{I}_{x}
\end{aligned}
$$

$$
\begin{aligned}
0.3\,\mathbf{V}_1 - 0.2\,\mathbf{V}_2 &= 2 \\
-0.2\,\mathbf{V}_1 + 0.25\,\mathbf{V}_2 &= \mathbf{I}_{x}
\end{aligned}
$$

**Paso 2 — Expresar la variable de control en términos de tensiones nodales.**

La variable de control es $\mathbf{V}_x = \mathbf{V}_1$, por lo que:

$$\mathbf{I}_{x} = g_m \mathbf{V}_1 = 0.5\,\mathbf{V}_1$$

**Paso 3 — Sustituir y transferir términos al lado izquierdo.**

Reemplazando en la segunda ecuación:

$$-0.2\,\mathbf{V}_1 + 0.25\,\mathbf{V}_2 = 0.5\,\mathbf{V}_1$$

Pasando el término dependiente de $\mathbf{V}_1$ al lado izquierdo:

$$-0.2\,\mathbf{V}_1 - 0.5\,\mathbf{V}_1 + 0.25\,\mathbf{V}_2 = 0$$

$$-0.7\,\mathbf{V}_1 + 0.25\,\mathbf{V}_2 = 0$$

**Paso 4 — Sistema matricial final.**

$$
\begin{bmatrix}
0.3 & -0.2 \\
-0.7 & 0.25
\end{bmatrix}
\begin{bmatrix}
\mathbf{V}_1 \\
\mathbf{V}_2
\end{bmatrix}
=
\begin{bmatrix}
2 \\
0
\end{bmatrix}
$$

::: {.callout-important}
### 📌 Observación clave: pérdida de simetría

Compárese la matriz $[\mathbf{Y}]$ resultante:

$$
[\mathbf{Y}] =
\begin{bmatrix}
0.3 & -0.2 \\
-0.7 & 0.25
\end{bmatrix}
$$

El elemento $\mathbf{Y}_{21} = -0.7$ **ya no es igual** a $\mathbf{Y}_{12} = -0.2$. La fuente controlada ha introducido un acoplamiento asimétrico: la tensión del nodo 1 afecta la corriente inyectada al nodo 2, pero no al revés. Esta es la firma matemática de una fuente dependiente en el análisis nodal.
:::

**Paso 5 — Resolución por Regla de Cramer.**

Determinante principal:

$$\Delta_Y = (0.3)(0.25) - (-0.2)(-0.7) = 0.075 - 0.14 = -0.065\,\text{S}^2$$

Tensión del nodo 1:

$$\mathbf{V}_1 = \frac{\det\begin{bmatrix} 2 & -0.2 \\ 0 & 0.25 \end{bmatrix}}{\Delta_Y} = \frac{(2)(0.25) - (-0.2)(0)}{-0.065} = \frac{0.5}{-0.065} \approx -7.692\,\text{V}$$

Tensión del nodo 2:

$$\mathbf{V}_2 = \frac{\det\begin{bmatrix} 0.3 & 2 \\ -0.7 & 0 \end{bmatrix}}{\Delta_Y} = \frac{(0.3)(0) - (2)(-0.7)}{-0.065} = \frac{1.4}{-0.065} \approx -21.538\,\text{V}$$

$$
\boxed{\mathbf{V}_1 \approx -7.69\,\text{V}, \qquad \mathbf{V}_2 \approx -21.54\,\text{V}}
$$

**Paso 6 — Verificación de la corriente controlada.**

$$\mathbf{I}_{x} = g_m \mathbf{V}_1 = 0.5(-7.692) = -3.846\,\text{A}$$

Es decir, la VCCS en realidad **absorbe** corriente del nodo 2 (inyecta corriente negativa), lo cual es consistente con el signo negativo de $\mathbf{V}_1$. Este tipo de verificación es esencial: un resultado con signo inesperado suele revelar un error de convenio, no de álgebra.

# Verificación Computacional en Python

Para verificar sistemas de cualquier orden de forma automatizada mediante álgebra matricial compleja:

```python
import numpy as np

# Definición del sistema matricial [Y][V] = [I] para el Ejercicio 1
Y = np.array([
    [0.05 + 0.15j,  0.00 - 0.20j],
    [0.00 - 0.20j,  0.05 + 0.20j]
], dtype=complex)

I = np.array([
    4.0 + 0.0j,
    0.0 + 2.0j
], dtype=complex)

# Resolución del sistema lineal de ecuaciones
V = np.linalg.solve(Y, I)

print("--- RESULTADOS NODALES EXACTOS ---")
for i, v in enumerate(V, start=1):
    modulo = np.abs(v)
    fase_deg = np.rad2deg(np.angle(v))
    print(f"V_{i} = {v.real:8.4f} + j{v.imag:8.4f} V  |  {modulo:8.4f} ∠ {fase_deg:6.2f}° V")
```

---

# Errores Frecuentes y Consejos Prácticos

::: {.callout-note}
### 🧠 Errores Comunes en Exámenes y Diseños

1. **Confusión entre Impedancias y Admitancias:** El error más común al llenar $[\mathbf{Y}]$ es colocar $\mathbf{Z}$ en vez de su inverso $\mathbf{Y} = 1/\mathbf{Z}$. ¡Recuerda que en una rama inductiva con $\mathbf{Z} = j\omega L$, la admitancia es $\mathbf{Y} = -j/(\omega L)$ con signo negativo!
2. **Signo de los elementos mutuos $\mathbf{Y}_{ij}$:** Los elementos fuera de la diagonal SIEMPRE deben llevar el signo menos exterior: $-\mathbf{Y}_{\text{enlace}}$.
3. **Intentar plantear LCK directa en una fuente ideal de tensión:** Nunca apliques LCK en un nodo conectado a una fuente de tensión a menos que conozcas o aisles la corriente de la fuente mediante un supernodo.
4. **Convenio de signos de corrientes inyectadas:** Fuentes que entran al nodo suman positivo ($+$), fuentes que salen restan ($-$).
:::

---

# Navegación del Módulo

<div class="d-flex flex-wrap gap-2 my-3">
  <a href="delta_estrella.qmd" class="btn btn-outline-secondary"><i class="bi bi-arrow-left me-1"></i> Transformación Δ–Y</a>
  <a href="analisis_mallas.qmd" class="btn btn-primary"><i class="bi bi-grid me-1"></i> Siguiente: Análisis de Mallas</a>
  <a href="circuito_thevenin.qmd" class="btn btn-outline-primary"><i class="bi bi-cpu me-1"></i> Teorema de Thévenin</a>
  <a href="circuito_norton.qmd" class="btn btn-outline-primary"><i class="bi bi-bezier2 me-1"></i> Teorema de Norton</a>
  <a href="index.qmd" class="btn btn-outline-secondary"><i class="bi bi-house me-1"></i> Índice</a>
</div>
