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

## Ejercicio 4 — Circuito con Fuentes Controladas (VCVS + CCCS)

::: {style="float: right; width: 48%; max-width: 450px; margin: 0 0 1rem 1.5rem;"}
![](imagenes/Ejercicio4Nodal.png){width=100% fig-align="center"}
:::

### Enunciado

Para el circuito mostrado en el esquema, que incorpora una fuente de tensión controlada por tensión (VCVS) de valor $0.1\,\mathbf{V}_o$ y una fuente de corriente controlada por corriente (CCCS) de valor $8\,\mathbf{I}_o$:

1. **Variables de control:** Expresar $\mathbf{V}_o$ e $\mathbf{I}_o$ en términos de las tensiones nodales.
2. **Formulación Matricial:** Plantear las ecuaciones nodales tratando adecuadamente la VCVS y la CCCS.
3. **Cálculo de Potenciales:** Determinar las tensiones nodales $\mathbf{V}_A$, $\mathbf{V}_B$, $\mathbf{V}_C$ y la tensión de salida $\mathbf{V}_o$.

### Solución Paso a Paso

**Paso 1 — Definición de nodos y variables de control.**

Sea el nodo de referencia la rama inferior (tierra, $0\,\text{V}$). Los nodos esenciales son:

* **Nodo A:** unión de la fuente $8\angle 20°\,\text{V}$, la resistencia $4\,\Omega$ y el terminal positivo de la VCVS.
* **Nodo B:** terminal negativo de la VCVS, unión con la CCCS $8\mathbf{I}_o$ y el condensador $-j5\,\Omega$.
* **Nodo C:** unión del condensador $-j5\,\Omega$, la inductancia $j5\,\Omega$ y la resistencia $10\,\Omega$. Aquí se mide $\mathbf{V}_o$.

Las variables de control se expresan como:

$$\mathbf{V}_o = \mathbf{V}_C$$

$$\mathbf{I}_o = \frac{\mathbf{V}_B - \mathbf{V}_A}{4} \qquad \text{(sentido de B hacia A, según el esquema)}$$

**Paso 2 — Ecuación de ligadura de la VCVS.**

La VCVS impone la relación:

$$\mathbf{V}_A - \mathbf{V}_B = 0.1\,\mathbf{V}_o = 0.1\,\mathbf{V}_C$$

Como el nodo A está fijado por la fuente independiente:

$$\mathbf{V}_A = 8\angle 20°\,\text{V}$$

se obtiene la ecuación de ligadura:

$$\mathbf{V}_B = 8\angle 20° - 0.1\,\mathbf{V}_C \qquad \text{[Ligadura]}$$

**Paso 3 — LCK en el nodo B.**

Corrientes que salen del nodo B:

* Hacia A por $4\,\Omega$: $\dfrac{\mathbf{V}_B - \mathbf{V}_A}{4} = \mathbf{I}_o$
* Hacia tierra por la CCCS: $8\,\mathbf{I}_o$
* Hacia C por $-j5\,\Omega$: $\dfrac{\mathbf{V}_B - \mathbf{V}_C}{-j5}$

Balance de corrientes:

$$\frac{\mathbf{V}_B - \mathbf{V}_A}{4} + 8\,\mathbf{I}_o + \frac{\mathbf{V}_B - \mathbf{V}_C}{-j5} = 0$$

Sustituyendo $\mathbf{I}_o$:

$$\frac{9(\mathbf{V}_B - \mathbf{V}_A)}{4} + j\frac{\mathbf{V}_B - \mathbf{V}_C}{5} = 0 \qquad \text{[Ecuación B]}$$

**Paso 4 — LCK en el nodo C.**

Corrientes que salen de C:

* Hacia B por $-j5\,\Omega$: $\dfrac{\mathbf{V}_C - \mathbf{V}_B}{-j5}$
* A tierra por $j5\,\Omega$: $\dfrac{\mathbf{V}_C}{j5}$
* A tierra por $10\,\Omega$: $\dfrac{\mathbf{V}_C}{10}$

Balance de corrientes:

$$\frac{\mathbf{V}_C - \mathbf{V}_B}{-j5} + \frac{\mathbf{V}_C}{j5} + \frac{\mathbf{V}_C}{10} = 0$$

Simplificando:

$$-\frac{j\mathbf{V}_B}{5} + \frac{\mathbf{V}_C}{10} = 0 \implies \boxed{\mathbf{V}_C = j2\,\mathbf{V}_B} \qquad \text{[Ecuación C]}$$

**Paso 5 — Sustitución y resolución.**

Sustituyendo $\mathbf{V}_C = j2\,\mathbf{V}_B$ en la Ecuación B:

$$\frac{9(\mathbf{V}_B - \mathbf{V}_A)}{4} + \frac{j\mathbf{V}_B(1 - j2)}{5} = 0$$

$$\frac{9\mathbf{V}_B}{4} - \frac{9\mathbf{V}_A}{4} + \frac{(2 + j)\mathbf{V}_B}{5} = 0$$

$$\mathbf{V}_B\left(\frac{9}{4} + \frac{2+j}{5}\right) = \frac{9\mathbf{V}_A}{4}$$

$$(2.65 + j0.2)\,\mathbf{V}_B = 2.25\,\mathbf{V}_A$$

Despejando $\mathbf{V}_B$:

$$\mathbf{V}_B = \frac{2.25 \cdot 8\angle 20°}{2.6575\angle 4.32°} = 6.774\angle 15.68°\,\text{V}$$

$$\boxed{\mathbf{V}_B \approx 6.774\angle 15.68°\,\text{V} \approx 6.52 + j1.83\,\text{V}}$$

Calculando $\mathbf{V}_C$:

$$\mathbf{V}_C = j2\,\mathbf{V}_B = 2\angle 90° \cdot 6.774\angle 15.68° = 13.548\angle 105.68°\,\text{V}$$

$$\boxed{\mathbf{V}_o = \mathbf{V}_C \approx 13.55\angle 105.68°\,\text{V} \approx -3.66 + j13.04\,\text{V}}$$

**Paso 6 — Verificación por LCK.**

Sustituyendo los valores numéricos en la Ecuación B:

* $\mathbf{V}_A = 7.518 + j2.736\,\text{V}$
* $\mathbf{V}_B = 6.522 + j1.832\,\text{V}$
* $\mathbf{V}_C = -3.66 + j13.04\,\text{V}$

Término 1:

$$\frac{9(\mathbf{V}_B - \mathbf{V}_A)}{4} = \frac{9(-0.996 - j0.904)}{4} = -2.241 - j2.034$$

Término 2:

$$j\frac{\mathbf{V}_B - \mathbf{V}_C}{5} = j\frac{10.182 - j11.208}{5} = 2.242 + j2.036$$

Suma de ambos términos:

$$(-2.241 + 2.242) + j(-2.034 + 2.036) \approx 0 \quad ✔$$

La ecuación de LCK se satisface, confirmando la consistencia del resultado.

::: {.callout-important}
### 📌 Observación clave: pérdida de simetría

La presencia simultánea de una VCVS y una CCCS introduce **dos acoplamientos asimétricos** en el circuito:

1. La VCVS acopla el nodo A con el nodo C mediante la variable de control $\mathbf{V}_o$.
2. La CCCS acopla el nodo B consigo mismo mediante la variable de control $\mathbf{I}_o$, que depende de $\mathbf{V}_B - \mathbf{V}_A$.

Como consecuencia, la matriz de admitancias **no es simétrica** ($\mathbf{Y}_{ij} \neq \mathbf{Y}_{ji}$) y el sistema debe resolverse por sustitución directa o por formulación matricial aumentada, **no por simple inspección**.
:::

**Paso 7 — Cálculo de la corriente de control.**

$$\mathbf{I}_o = \frac{\mathbf{V}_B - \mathbf{V}_A}{4} = \frac{-0.996 - j0.904}{4} = -0.249 - j0.226\,\text{A}$$

$$\boxed{\mathbf{I}_o \approx 0.336\angle -137.8°\,\text{A}}$$

El signo negativo de la parte real e imaginaria indica que la corriente instantánea circula en sentido opuesto al supuesto durante parte del ciclo, lo cual es coherente con el desfase introducido por la VCVS.

## Ejercicio 5 — Circuito Mixto con Fuente de Tensión y Fuente de Corriente

::: {style="float: right; width: 48%; max-width: 450px; margin: 0 0 1rem 1.5rem;"}
![](imagenes/Ejercicio5Nodal.png){width=100% fig-align="center"}
:::

### Enunciado

Para el circuito mostrado en el esquema, que opera en régimen permanente sinusoidal:

1. **Identificación de nodos:** Determinar el número de nodos esenciales y elegir la referencia.
2. **Formulación Matricial:** Plantear el sistema $[\mathbf{Y}][\mathbf{V}] = [\mathbf{I}]$ por inspección directa.
3. **Cálculo del potencial nodal:** Determinar la tensión fasorial $\mathbf{V}$ en el nodo superior.

### Solución Paso a Paso

**Paso 1 — Identificación de nodos y referencia.**

* **Nodo de referencia:** La tierra inferior (conectada al terminal negativo de la fuente de $120\angle -15^\circ\,\text{V}$).
* **Nodo 1:** Nodo entre la resistencia de $40\,\Omega$ y la inductancia $j20\,\Omega$. Llamémoslo $\mathbf{V}_1$.
* **Nodo 2:** Nodo superior derecho, donde se conectan la fuente de corriente, el condensador y la resistencia de $50\,\Omega$. Es la tensión pedida $\mathbf{V}$.

**Paso 2 — Ecuación de ligadura de la fuente de tensión.**

La fuente de $120\angle -15^\circ\,\text{V}$ está conectada a referencia por su terminal negativo, así que fija directamente el potencial del nodo 1:

$$\mathbf{V}_1 = 120\angle -15^\circ\,\text{V} = 115.91 - j31.06\,\text{V}$$

**Paso 3 — LCK en el nodo 2 (única incógnita).**

En el nodo 2 confluyen:

* Corriente que entra desde el nodo 1 a través de la rama serie $40\,\Omega + j20\,\Omega$:
  $$\mathbf{I}_{12} = \frac{\mathbf{V}_1 - \mathbf{V}}{40 + j20}$$

* Fuente de corriente $6\angle 30^\circ\,\text{A}$ **inyectando** al nodo 2 (la flecha apunta hacia abajo, hacia tierra; según el símbolo, entra al nodo desde arriba, pero como está conectada a tierra, **sale** del nodo 2 hacia tierra). Adoptamos el criterio de la regla de oro: fuentes que **entran** al nodo suman positivo.

* Corriente por el condensador $-j30\,\Omega$:
  $$\mathbf{I}_C = \frac{\mathbf{V}}{-j30} = j\frac{\mathbf{V}}{30}$$

* Corriente por la resistencia $50\,\Omega$:
  $$\mathbf{I}_R = \frac{\mathbf{V}}{50}$$

Aplicando LCK (corrientes salientes = corrientes entrantes):

$$\frac{\mathbf{V} - \mathbf{V}_1}{40 + j20} + \frac{\mathbf{V}}{-j30} + \frac{\mathbf{V}}{50} = 6\angle 30^\circ$$

**Paso 4 — Agrupación y resolución.**

Pasando $\mathbf{V}_1$ al lado derecho:

$$\mathbf{V}\left[\frac{1}{40 + j20} + \frac{1}{-j30} + \frac{1}{50}\right] = 6\angle 30^\circ + \frac{\mathbf{V}_1}{40 + j20}$$

Calculamos cada admitancia:

$$\mathbf{Y}_{40+j20} = \frac{1}{40 + j20} = \frac{40 - j20}{40^2 + 20^2} = \frac{40 - j20}{2000} = 0.02 - j0.01\,\text{S}$$

$$\mathbf{Y}_{-j30} = \frac{1}{-j30} = j\frac{1}{30} = j0.0333\,\text{S}$$

$$\mathbf{Y}_{50} = \frac{1}{50} = 0.02\,\text{S}$$

Suma de admitancias:

$$\mathbf{Y}_{\text{total}} = (0.02 - j0.01) + j0.0333 + 0.02 = 0.04 + j0.0233\,\text{S}$$

Término independiente:

$$\frac{\mathbf{V}_1}{40 + j20} = (0.02 - j0.01)(115.91 - j31.06)$$

$$= 0.02(115.91) - 0.02(j31.06) - j0.01(115.91) + j0.01(j31.06)$$

$$= 2.318 - j0.621 - j1.159 - 0.311$$

$$= 2.007 - j1.780\,\text{A}$$

$$6\angle 30^\circ = 5.196 + j3.0\,\text{A}$$

Término derecho total:

$$\mathbf{I}_{\text{total}} = (5.196 + j3.0) + (2.007 - j1.780) = 7.203 + j1.220\,\text{A}$$

Finalmente:

$$\mathbf{V} = \frac{7.203 + j1.220}{0.04 + j0.0233} = \frac{7.203 + j1.220}{0.0463\angle 30.22^\circ}$$

$$= \frac{7.306\angle 9.62^\circ}{0.0463\angle 30.22^\circ} = 157.8\angle -20.6^\circ\,\text{V}$$

$$\boxed{\mathbf{V} \approx 157.8\,\angle\,-20.6^\circ\,\text{V}}$$

**Paso 5 — Verificación por LCK.**

Comprobamos que la corriente total que sale del nodo 2 hacia las tres ramas coincide con la que entra desde el nodo 1 más la fuente:

$$\mathbf{I}_{\text{sale}} = \frac{\mathbf{V} - \mathbf{V}_1}{40 + j20} + \frac{\mathbf{V}}{-j30} + \frac{\mathbf{V}}{50}$$

$$= \frac{(157.8\angle -20.6^\circ) - (120\angle -15^\circ)}{44.72\angle 26.57^\circ} + \frac{157.8\angle -20.6^\circ}{30\angle -90^\circ} + \frac{157.8\angle -20.6^\circ}{50}$$

$$= \frac{148.4 - j55.5 - 115.9 + j31.1}{44.72\angle 26.57^\circ} + 5.26\angle 69.4^\circ + 3.156\angle -20.6^\circ$$

$$= \frac{32.5 - j24.4}{44.72\angle 26.57^\circ} + 5.26\angle 69.4^\circ + 3.156\angle -20.6^\circ$$

$$= 0.909\angle -63.4^\circ + 5.26\angle 69.4^\circ + 3.156\angle -20.6^\circ$$

$$= (0.408 - j0.812) + (1.850 + j4.925) + (2.954 - j1.111) = 5.212 + j3.002 \approx 6\angle 30^\circ\,\text{A}$$

✔ Coincide con la fuente de corriente. **Verificación exitosa.**

## Ejercicio 6 — Red en Puente de CA: Transformación Fasorial y Eficiencia Nodal

::: {style="float: right; width: 45%; max-width: 440px; margin: 0 0 1rem 1.5rem;"}
![](imagenes/Eje6NOdal.png){width=100% fig-align="center"}
:::

### Enunciado

Para el circuito en puente de corriente alterna alimentado por una fuente sinusoidal $\mathbf{E} = 10\angle 0^\circ\,\text{V}$ a una frecuencia $f = 100\,\text{Hz}$:

1. **Modelado en el Dominio Fasorial:** Determinar la pulsación angular $\omega$, las reactancias de los elementos dinámicos y las impedancias/admitancias complejas de las 5 ramas pasivas ($\mathbf{Z}_1$ a $\mathbf{Z}_5$).
2. **Evaluación de Complejidad Topológica:** Justificar cuantitativamente por qué el análisis nodal reduce la dimensión del problema a un sistema $2 \times 2$, frente a las 3 ecuaciones que exigiría el método de mallas.
3. **Formulación y Resolución Nodal:** Tomando el nodo inferior como referencia (tierra, $0\,\text{V}$), plantear el sistema matricial de admitancias $[\mathbf{Y}][\mathbf{V}] = [\mathbf{I}]$ y resolver los potenciales nodales $\mathbf{V}_A$ (nodo central izquierdo) y $\mathbf{V}_B$ (nodo central derecho).
4. **Respuesta en el Detector:** Calcular la tensión fasorial diferencial $\mathbf{V}_{AB}$ en el resistor central $R_5 = 500\,\Omega$ y la corriente fasorial $\mathbf{I}_5$ que fluye a través de él.

### Solución Paso a Paso

**Paso 1 — Parámetros en el Dominio Fasorial.**

La frecuencia angular de excitación es:

$$\omega = 2\pi f = 2\pi(100) \approx 628.32\,\text{rad/s}$$

Calculamos las impedancias y admitancias complejas de cada rama:

* **Rama 1 ($R_1 \parallel C_1$):**
  $$X_{C1} = \frac{1}{\omega C_1} = \frac{1}{(628.32)(10 \times 10^{-6})} \approx 159.15\,\Omega \implies \mathbf{Z}_{C1} = -j159.15\,\Omega$$
  $$\mathbf{Z}_1 = \frac{R_1 \cdot (-jX_{C1})}{R_1 - jX_{C1}} = \frac{100(-j159.15)}{100 - j159.15} \approx \mathbf{71.70 - j45.05\,\Omega}$$
  Su admitancia de rama se obtiene sumando conductancia y susceptancia en paralelo:
  $$\mathbf{Y}_1 = \frac{1}{R_1} + j\omega C_1 = \frac{1}{100} + j(628.32)(10 \times 10^{-6}) = \mathbf{0.01 + j0.006283\,\text{S}}$$

* **Rama 2 ($R_2$):**
  $$\mathbf{Z}_2 = 200\,\Omega \implies \mathbf{Y}_2 = \frac{1}{200} = \mathbf{0.005\,\text{S}}$$

* **Rama 3 ($R_3$):**
  $$\mathbf{Z}_3 = 300\,\Omega \implies \mathbf{Y}_3 = \frac{1}{300} \approx \mathbf{0.003333\,\text{S}}$$

* **Rama 4 ($R_4$ en serie con $L_4$):**
  $$X_{L4} = \omega L_4 = (628.32)(0.1) \approx 62.83\,\Omega$$
  $$\mathbf{Z}_4 = R_4 + jX_{L4} = \mathbf{400 + j62.83\,\Omega}$$
  $$\mathbf{Y}_4 = \frac{1}{400 + j62.83} = \frac{400 - j62.83}{400^2 + 62.83^2} = \frac{400 - j62.83}{163948} \approx \mathbf{0.002440 - j0.000383\,\text{S}}$$

* **Rama 5 ($R_5$, puente central):**
  $$\mathbf{Z}_5 = 500\,\Omega \implies \mathbf{Y}_5 = \frac{1}{500} = \mathbf{0.002\,\text{S}}$$

**Paso 2 — Análisis de Complejidad: Nodal ($2 \times 2$) vs Mallas ($3 \times 3$).**

* **Método de Mallas:** El puente con la fuente de alimentación contiene **3 ventanas planares independientes** (mallas $I_1, I_2, I_3$), exigiendo resolver un sistema de 3 ecuaciones complejas acopladas.
* **Método Nodal:** La red posee 4 nodos esenciales. Al asignar el nodo inferior como referencia ($0\,\text{V}$), la fuente independiente $\mathbf{E} = 10\angle 0^\circ\,\text{V}$ queda conectada directamente entre el nodo superior y tierra, **fijando de forma unívoca el potencial superior**:
  $$\mathbf{V}_{\text{superior}} = \mathbf{E} = 10\angle 0^\circ\,\text{V}$$
  Por lo tanto, **solo restan 2 incógnitas nodales**: el nodo izquierdo $\mathbf{V}_A$ y el nodo derecho $\mathbf{V}_B$. El sistema se reduce drásticamente a una matriz de **$2 \times 2$**.

**Paso 3 — Formulación Matricial Nodal.**

Planteamos las ecuaciones de Kirchhoff de corriente (LCK) para los dos nodos libres:

* **LCK en el Nodo A (entre $\mathbf{Z}_1$, $\mathbf{Z}_3$ y $\mathbf{Z}_5$):**
  $$(\mathbf{V}_A - \mathbf{E})\mathbf{Y}_1 + \mathbf{V}_A \mathbf{Y}_3 + (\mathbf{V}_A - \mathbf{V}_B)\mathbf{Y}_5 = 0$$
  $$\mathbf{V}_A (\underbrace{\mathbf{Y}_1 + \mathbf{Y}_3 + \mathbf{Y}_5}_{\mathbf{Y}_{AA}}) - \mathbf{V}_B (\underbrace{\mathbf{Y}_5}_{-\mathbf{Y}_{AB}}) = \mathbf{E}\mathbf{Y}_1$$

  Calculando coeficientes:
  $$\mathbf{Y}_{AA} = (0.01 + j0.006283) + 0.003333 + 0.002 = \mathbf{0.015333 + j0.006283\,\text{S}}$$
  $$\mathbf{Y}_{AB} = \mathbf{Y}_{BA} = -\mathbf{Y}_5 = \mathbf{-0.002\,\text{S}}$$
  $$\mathbf{I}_A = \mathbf{E}\mathbf{Y}_1 = 10(0.01 + j0.006283) = \mathbf{0.10 + j0.06283\,\text{A}}$$

* **LCK en el Nodo B (entre $\mathbf{Z}_2$, $\mathbf{Z}_4$ y $\mathbf{Z}_5$):**
  $$(\mathbf{V}_B - \mathbf{E})\mathbf{Y}_2 + \mathbf{V}_B \mathbf{Y}_4 + (\mathbf{V}_B - \mathbf{V}_A)\mathbf{Y}_5 = 0$$
  $$-\mathbf{V}_A (\mathbf{Y}_5) + \mathbf{V}_B (\underbrace{\mathbf{Y}_2 + \mathbf{Y}_4 + \mathbf{Y}_5}_{\mathbf{Y}_{BB}}) = \mathbf{E}\mathbf{Y}_2$$

  Calculando coeficientes:
  $$\mathbf{Y}_{BB} = 0.005 + (0.002440 - j0.000383) + 0.002 = \mathbf{0.009440 - j0.000383\,\text{S}}$$
  $$\mathbf{I}_B = \mathbf{E}\mathbf{Y}_2 = 10(0.005) = \mathbf{0.05 + j0\,\text{A}}$$

Sistema Matricial $[\mathbf{Y}][\mathbf{V}] = [\mathbf{I}]$:
$$
\begin{bmatrix}
0.015333 + j0.006283 & -0.002 \\
-0.002 & 0.009440 - j0.000383
\end{bmatrix}
\begin{bmatrix}
\mathbf{V}_A \\
\mathbf{V}_B
\end{bmatrix}
=
\begin{bmatrix}
0.10 + j0.06283 \\
0.05
\end{bmatrix}
$$

**Paso 4 — Resolución por Regla de Cramer.**

Calculamos el determinante principal $\Delta_Y$:

$$\Delta_Y = \mathbf{Y}_{AA}\mathbf{Y}_{BB} - (\mathbf{Y}_{AB})^2$$
$$\Delta_Y = (0.015333 + j0.006283)(0.009440 - j0.000383) - (-0.002)^2$$
$$\Delta_Y \approx \mathbf{0.00014315 + j0.00005344\,\text{S}^2} = \mathbf{1.528 \times 10^{-4}\angle 20.47^\circ\,\text{S}^2}$$

Determinante para $\mathbf{V}_A$:
$$\Delta_{V_A} = \det\begin{bmatrix} 0.10 + j0.06283 & -0.002 \\ 0.05 & 0.009440 - j0.000383 \end{bmatrix} \approx \mathbf{0.0010681 + j0.0005548\,\text{V}\cdot\text{S}}$$
$$\mathbf{V}_A = \frac{\Delta_{V_A}}{\Delta_Y} \approx \mathbf{7.818 + j0.957\,\text{V}} = \boxed{\mathbf{7.88\,\angle\,6.98^\circ\,\text{V}}}$$

Determinante para $\mathbf{V}_B$:
$$\Delta_{V_B} = \det\begin{bmatrix} 0.015333 + j0.006283 & 0.10 + j0.06283 \\ -0.002 & 0.05 \end{bmatrix} \approx \mathbf{0.0009667 + j0.0004398\,\text{V}\cdot\text{S}}$$
$$\mathbf{V}_B = \frac{\Delta_{V_B}}{\Delta_Y} \approx \mathbf{6.934 + j0.484\,\text{V}} = \boxed{\mathbf{6.95\,\angle\,4.00^\circ\,\text{V}}}$$

**Paso 5 — Tensión y Corriente en el Resistor del Puente ($R_5$).**

La tensión de desbalance en los terminales de $R_5$ (de izquierda a derecha):

$$\mathbf{V}_{AB} = \mathbf{V}_A - \mathbf{V}_B = (7.818 + j0.957) - (6.934 + j0.484) = \mathbf{0.885 + j0.473\,\text{V}}$$
$$\boxed{\mathbf{V}_{AB} \approx 1.003\,\angle\,28.12^\circ\,\text{V}}$$

La corriente fasorial que atraviesa el puente (de $A$ hacia $B$) es:

$$\mathbf{I}_5 = \frac{\mathbf{V}_{AB}}{R_5} = \frac{1.003\angle 28.12^\circ}{500} = \mathbf{2.007 \times 10^{-3}\angle 28.12^\circ\,\text{A}}$$
$$\boxed{\mathbf{I}_5 \approx 2.01\,\angle\,28.12^\circ\,\text{mA}}$$

::: {.callout-tip}
### 💡 Conclusión y Comparativa con Mallas
Observa que la corriente $\mathbf{I}_5$ coincide de forma exacta con la corriente obtenida al resolver las 3 mallas simultáneas ($\mathbf{I}_3 - \mathbf{I}_2 = 2.01\angle 28.12^\circ\,\text{mA}$). Sin embargo, mediante **análisis nodal**, el circuito se resolvió invirtiendo una simple matriz de $2 \times 2$, ahorrando más del 50% del esfuerzo algebraico gracias a la conexión a tierra de la fuente.
:::

---

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
