## 2.9 Concepto de Admitancia y sus componentes

La **Admitancia ($\mathbf{Y}$)** es la magnitud que expresa la facilidad que presenta un circuito o componente para el paso de la corriente alterna. Es el recíproco de la impedancia y se mide en **Siemens (S)** o **Mhos (℧)**.

$$\mathbf{Y} = \frac{1}{\mathbf{Z}} = G + jB$$

### Componentes de la Admitancia
1.  **Conductancia ($G$):** Es la parte real de la admitancia. Representa la facilidad que ofrece una resistencia al paso de la corriente. Se mide en Siemens.
    $$G = \frac{R}{R^2 + X^2} = \frac{R}{|Z|^2}$$
2.  **Susceptancia ($B$):** Es la parte imaginaria de la admitancia. Representa la facilidad que ofrecen los elementos reactivos (inductores y capacitores) al paso de la corriente.
    $$B = \frac{-X}{R^2 + X^2} = \frac{-X}{|Z|^2}$$
    *   **Susceptancia Inductiva ($B_L$):** $B_L = -\frac{1}{X_L} = -\frac{1}{\omega L}$
    *   **Susceptancia Capacitiva ($B_C$):** $B_C = \frac{1}{X_C} = \omega C$

### Leyes de Kirchhoff aplicadas con Admitancia
En circuitos de **paralelo**, el uso de la admitancia simplifica enormemente los cálculos, ya que las admitancias en paralelo se suman directamente (al igual que las impedancias en serie).

*   **Ley de Corrientes de Kirchhoff (LCK):** En un nodo, la suma fasorial de las corrientes es cero. Usando admitancia:
    $$\mathbf{I}_{total} = \mathbf{V} \cdot \mathbf{Y}_{total} = \mathbf{V} \cdot (\mathbf{Y}_1 + \mathbf{Y}_2 + \dots + \mathbf{Y}_n)$$
*   **Comportamiento del Voltaje:** En un circuito paralelo, **el voltaje es común** a todas las ramas. Esto significa que $\mathbf{V}$ es el fasor de referencia para analizar las corrientes de cada rama:
    $$\mathbf{V}_{total} = \mathbf{V}_1 = \mathbf{V}_2 = \dots = \mathbf{V}_n$$

### Diagramas Vectoriales (Fasoriales) en circuitos Serie-Paralelo

Los diagramas vectoriales son representaciones gráficas en el plano complejo que muestran la magnitud y el ángulo de fase de voltajes y corrientes.

**1. Circuito Serie (Referencia: Corriente $\mathbf{I}$)**
En un circuito serie, la corriente es común. Se toma $\mathbf{I}$ en el eje real (0°):
*   **$\mathbf{V}_R$**: Está en fase con $\mathbf{I}$ (0°).
*   **$\mathbf{V}_L$**: Adelanta a $\mathbf{I}$ en 90° (eje imaginario positivo).
*   **$\mathbf{V}_C$**: Retrasa a $\mathbf{I}$ en 90° (eje imaginario negativo).
*   **$\mathbf{V}_{total}$**: Es la suma fasorial $\mathbf{V}_R + \mathbf{V}_L + \mathbf{V}_C$. Su ángulo $\theta$ depende de si el circuito es inductivo o capacitivo.

**2. Circuito Paralelo (Referencia: Voltaje $\mathbf{V}$)**
En un circuito paralelo, el voltaje es común. Se toma $\mathbf{V}$ en el eje real (0°):
*   **$\mathbf{I}_R$**: Está en fase con $\mathbf{V}$ (0°).
*   **$\mathbf{I}_L$**: Retrasa a $\mathbf{V}$ en 90° (eje imaginario negativo).
*   **$\mathbf{I}_C$**: Adelanta a $\mathbf{V}$ en 90° (eje imaginario positivo).
*   **$\mathbf{I}_{total}$**: Es la suma fasorial de las corrientes de cada rama.

**3. Circuito Serie-Paralelo**
Se combina ambos enfoques. Se simplifica el circuito por bloques, aplicando las reglas de serie (misma corriente) y paralelo (mismo voltaje), y se construye el diagrama fasorial partiendo desde las ramas más internas hasta llegar a la fuente.

---

## 2.10 Concepto de Potencia Monofásica y Factor de Potencia

En corriente alterna, la potencia no es un valor único, ya que existen elementos que almacenan y devuelven energía (inductores y capacitores). Se definen tres tipos de potencia:

### Tipos de Potencia
1.  **Potencia Activa o Real ($P$):** Es la potencia que realmente se consume y se transforma en trabajo útil (calor, luz, movimiento). Se mide en **Watts (W)**.
    $$P = V_{rms} \cdot I_{rms} \cdot \cos(\theta)$$
2.  **Potencia Reactiva ($Q$):** Es la potencia que oscila entre la fuente y los elementos reactivos (campos magnéticos y eléctricos). No realiza trabajo útil pero es necesaria para el funcionamiento de motores y transformadores. Se mide en **Volt-Amperios Reactivos (VAR)**.
    $$Q = V_{rms} \cdot I_{rms} \cdot \sin(\theta)$$
3.  **Potencia Aparente ($S$):** Es la potencia total suministrada por la fuente. Es el producto vectorial del voltaje y la corriente. Se mide en **Volt-Amperios (VA)**.
    $$S = V_{rms} \cdot I_{rms} = \sqrt{P^2 + Q^2}$$

Estas tres potencias forman el **Triángulo de Potencias**, donde $S$ es la hipotenusa, $P$ el lado adyacente y $Q$ el lado opuesto.

### Factor de Potencia ($fp$)
El factor de potencia es la relación entre la potencia activa y la potencia aparente. Indica qué tan eficientemente se está utilizando la energía eléctrica.
$$fp = \cos(\theta) = \frac{P}{S}$$

*   **$fp = 1$ (Unitario):** Toda la potencia es activa (carga puramente resistiva).
*   **$fp < 1$ (Rezagado):** La corriente retrasa al voltaje (carga inductiva, $Q > 0$).
*   **$fp < 1$ (Adelantado):** La corriente adelanta al voltaje (carga capacitiva, $Q < 0$).

### Potencia en circuitos Serie-Paralelo
Para calcular la potencia total en un circuito mixto, se puede usar el **Teorema de Boucherot**, que establece que la potencia total activa y reactiva es la suma aritmética de las potencias de cada elemento:
$$P_{total} = \sum P_i \quad ; \quad Q_{total} = \sum Q_i$$
$$S_{total} = \sqrt{P_{total}^2 + Q_{total}^2} \quad ; \quad fp_{total} = \frac{P_{total}}{S_{total}}$$

---

## 2.11 Teorema de Thevenin y Norton para circuitos serie-paralelo

Estos teoremas permiten simplificar cualquier circuito lineal de CA (con fuentes y impedancias) a un circuito equivalente mucho más simple. En CA, se aplican usando **números complejos (fasores)** en lugar de resistencias.

### Teorema de Thevenin
Establece que cualquier circuito lineal de dos terminales puede reemplazarse por una **fuente de voltaje equivalente ($\mathbf{V}_{th}$)** en serie con una **impedancia equivalente ($\mathbf{Z}_{th}$)**.

**Procedimiento:**
1.  **$\mathbf{V}_{th}$ (Voltaje de Thevenin):** Es el voltaje de circuito abierto entre los dos terminales de interés (a y b). Se calcula usando las técnicas normales de análisis de circuitos (mallas, nodos, divisores).
2.  **$\mathbf{Z}_{th}$ (Impedancia de Thevenin):** Se calcula "apagando" las fuentes independientes:
    *   Fuentes de voltaje → se reemplazan por un **cortocircuito**.
    *   Fuentes de corriente → se reemplazan por un **circuito abierto**.
    *   Luego se calcula la impedancia equivalente vista desde los terminales a-b.
3.  **Carga ($\mathbf{Z}_L$):** Se conecta al circuito equivalente y la corriente de carga es:
    $$\mathbf{I}_L = \frac{\mathbf{V}_{th}}{\mathbf{Z}_{th} + \mathbf{Z}_L}$$

### Teorema de Norton
Establece que cualquier circuito lineal de dos terminales puede reemplazarse por una **fuente de corriente equivalente ($\mathbf{I}_N$)** en paralelo con una **impedancia equivalente ($\mathbf{Z}_N$)**.

**Procedimiento:**
1.  **$\mathbf{I}_N$ (Corriente de Norton):** Es la corriente de cortocircuito que fluye entre los terminales a-b cuando se conectan directamente.
2.  **$\mathbf{Z}_N$ (Impedancia de Norton):** Es idéntica a $\mathbf{Z}_{th}$. Se calcula apagando las fuentes independientes.
3.  **Relación con Thevenin:** Los circuitos son equivalentes mediante la transformación de fuentes:
    $$\mathbf{Z}_N = \mathbf{Z}_{th} \quad ; \quad \mathbf{V}_{th} = \mathbf{I}_N \cdot \mathbf{Z}_N$$

---

## 2.12 Conversión Estrella – Delta y viceversa

En circuitos serie-paralelo complejos, a menudo nos encontramos con configuraciones de impedancias que no están ni en serie ni en paralelo. Las configuraciones **Estrella (Y o T)** y **Delta (Δ o Π)** permiten transformar el circuito para poder simplificarlo.

> *Autora del apartado: G6_Melanie Hurtado*

### Configuración Estrella (Y)
Tres impedancias ($\mathbf{Z}_1, \mathbf{Z}_2, \mathbf{Z}_3$) conectadas a un nodo central común.

### Configuración Delta (Δ)
Tres impedancias ($\mathbf{Z}_A, \mathbf{Z}_B, \mathbf{Z}_C$) conectadas formando un lazo cerrado (triángulo).

### Conversión de Delta a Estrella (Δ → Y)
Dado un circuito Delta con impedancias $\mathbf{Z}_A, \mathbf{Z}_B, \mathbf{Z}_C$, las impedancias equivalentes en Estrella son:

$$\mathbf{Z}_1 = \frac{\mathbf{Z}_A \cdot \mathbf{Z}_B}{\mathbf{Z}_A + \mathbf{Z}_B + \mathbf{Z}_C}$$

$$\mathbf{Z}_2 = \frac{\mathbf{Z}_B \cdot \mathbf{Z}_C}{\mathbf{Z}_A + \mathbf{Z}_B + \mathbf{Z}_C}$$

$$\mathbf{Z}_3 = \frac{\mathbf{Z}_A \cdot \mathbf{Z}_C}{\mathbf{Z}_A + \mathbf{Z}_B + \mathbf{Z}_C}$$

**Regla mnemotécnica:** Cada impedancia de la Y es igual al producto de las dos impedancias de la Δ adyacentes al mismo nodo, dividido entre la suma de las tres impedancias de la Δ.

### Conversión de Estrella a Delta (Y → Δ)
Dado un circuito Estrella con impedancias $\mathbf{Z}_1, \mathbf{Z}_2, \mathbf{Z}_3$, las impedancias equivalentes en Delta son:

$$\mathbf{Z}_A = \frac{\mathbf{Z}_1\mathbf{Z}_2 + \mathbf{Z}_2\mathbf{Z}_3 + \mathbf{Z}_1\mathbf{Z}_3}{\mathbf{Z}_2}$$

$$\mathbf{Z}_B = \frac{\mathbf{Z}_1\mathbf{Z}_2 + \mathbf{Z}_2\mathbf{Z}_3 + \mathbf{Z}_1\mathbf{Z}_3}{\mathbf{Z}_1}$$

$$\mathbf{Z}_C = \frac{\mathbf{Z}_1\mathbf{Z}_2 + \mathbf{Z}_2\mathbf{Z}_3 + \mathbf{Z}_1\mathbf{Z}_3}{\mathbf{Z}_3}$$

**Regla mnemotécnica:** Cada impedancia de la Δ es igual a la suma de los productos de las impedancias de la Y tomadas de dos en dos, dividida entre la impedancia de la Y que está en el nodo opuesto.

### Aplicación en circuitos Serie-Paralelo
Cuando se tiene un circuito mixto con una configuración Y o Δ que impide ver elementos en serie o paralelo:
1.  Se identifica la configuración Y o Δ "bloqueante".
2.  Se aplica la transformación correspondiente (Δ→Y o Y→Δ) para obtener un circuito equivalente.
3.  El nuevo circuito resultante ahora sí tendrá elementos en serie y paralelo reconocibles.
4.  Se simplifica el circuito hasta obtener la impedancia total.
5.  *(Opcional)* Si se requieren valores internos originales, se regresa a la configuración original usando las relaciones de voltaje y corriente.

**Caso especial (Circuitos balanceados):**
Si las tres impedancias son iguales ($\mathbf{Z}_Y = \mathbf{Z}$ y $\mathbf{Z}_Δ = \mathbf{Z}'$), las fórmulas se simplifican notablemente:
*   **Δ → Y:** $\mathbf{Z}_Y = \frac{\mathbf{Z}_Δ}{3}$
*   **Y → Δ:** $\mathbf{Z}_Δ = 3 \cdot \mathbf{Z}_Y$