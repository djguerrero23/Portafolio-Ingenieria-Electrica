# Teoría de Corriente Alterna (CA)

## 2.1 Introducción a la teoría de corriente alterna
La corriente alterna, cuya abreviatura es **CA** (o **AC** por sus siglas en inglés), es un flujo de carga eléctrica que invierte su dirección de forma periódica. Este ciclo inicia desde cero, crece hasta un máximo positivo, disminuye a cero, invierte su polaridad, alcanza un máximo en la dirección opuesta (negativo), regresa al valor original y repite este ciclo indefinidamente.

*   **Período ($T$):** Es el intervalo de tiempo que tarda la onda en completar un ciclo completo.
*   **Frecuencia ($f$):** Es el número de ciclos o períodos que ocurren por segundo. Se mide en Hertz (Hz) y su relación con el período es $f = 1/T$.
*   **Amplitud ($V_m$ o $I_m$):** Es el valor máximo o pico que alcanza la onda en cualquier dirección (positiva o negativa).

Es el tipo de corriente eléctrica que tiene como principal característica que su magnitud y dirección varían cíclicamente, describiendo generalmente una forma de onda senoidal.

## 2.2 Cómo se produce (Obtiene)
Se produce mediante **generadores eléctricos** (alternadores) que utilizan el principio de la **inducción electromagnética**. Al girar una bobina conductora dentro de un campo magnético constante, o al girar un imán cerca de un conductor, se transforma la energía mecánica en energía eléctrica, cuyo flujo de electrones cambia de dirección de forma constante.

### Proceso de Producción
1.  **2.2.1 Conversión de movimiento:** Una fuente externa de energía primaria (agua, viento, vapor, etc.) mueve una turbina.
2.  **2.2.2 Giro del rotor:** La fuerza mecánica hace girar la parte móvil del generador, llamada rotor, dentro de un campo magnético.
3.  **2.2.3 Inducción en el estator:** El movimiento continuo de los conductores cortando las líneas de flujo magnético crea una tensión eléctrica (fuerza electromotriz) en los conductores fijos o estator.
4.  **2.2.4 Generación de la onda senoidal:** Debido a la geometría circular del rotor, el ángulo de corte con el campo magnético varía de forma senoidal. La polaridad sube y baja de positiva a negativa, invirtiendo la dirección de la corriente varias veces por segundo, generando la onda de CA pura.

## 2.3 Concepto de valor instantáneo, valor medio y valor eficaz

### Valor Instantáneo ($v(t)$ o $i(t)$)
Es el valor que toma la señal en un instante de tiempo específico $t$. Para una onda senoidal, se expresa como:
$$v(t) = V_m \sin(\omega t + \theta)$$
Donde $V_m$ es la amplitud, $\omega$ es la frecuencia angular y $\theta$ es la fase inicial.

### Valor Medio ($V_{med}$)
Matemáticamente, es la integral de una señal en un periodo dividida sobre la duración de dicho periodo. Desde el punto de vista circuital, representa el componente de corriente directa (DC) de una señal.
$$V_{med} = \frac{1}{T} \int_{0}^{T} f(t) \, dt$$
*(Nota: Para una onda senoidal pura, el valor medio en un ciclo completo es cero, por lo que usualmente se calcula en un semiciclo).*

### Valor Eficaz o RMS ($V_{eficaz}$)
El valor eficaz (Root Mean Square) de una señal periódica es aquel valor de corriente o voltaje continuo (DC) que **produce la misma potencia media (calor)** sobre una carga resistiva que la señal de CA.
$$V_{eficaz} = \sqrt{\frac{1}{T} \int_{0}^{T} [f(t)]^2 \, dt}$$

#### Demostración del Valor Eficaz para una onda senoidal
Sea $v(t) = V_m \sin(\omega t)$. Sustituimos en la fórmula:
$$V_{eficaz} = \sqrt{\frac{1}{T} \int_{0}^{T} [V_m \sin(\omega t)]^2 \, dt} = \sqrt{\frac{V_m^2}{T} \int_{0}^{T} \sin^2(\omega t) \, dt}$$

Usando la identidad trigonométrica $\sin^2(x) = \frac{1 - \cos(2x)}{2}$:
$$V_{eficaz} = \sqrt{\frac{V_m^2}{T} \int_{0}^{T} \frac{1 - \cos(2\omega t)}{2} \, dt}$$

La integral de $\cos(2\omega t)$ en un periodo completo es cero. Nos queda:
$$V_{eficaz} = \sqrt{\frac{V_m^2}{2T} \int_{0}^{T} 1 \, dt} = \sqrt{\frac{V_m^2}{2T} [t]_0^T} = \sqrt{\frac{V_m^2}{2T} (T)} = \sqrt{\frac{V_m^2}{2}}$$

**Conclusión:** 
$$V_{eficaz} = \frac{V_m}{\sqrt{2}} \approx 0.707 V_m$$

## 2.4 Definición y diferencia entre Fasor y Vector

*   **Vector:** Es una entidad matemática que posee magnitud, dirección y sentido. Se utiliza para representar cantidades físicas en el **espacio** (como fuerza, velocidad o campo eléctrico).
*   **Fasor:** Es un número complejo que representa una función senoidal cuya frecuencia angular ($\omega$) es constante. Posee magnitud (generalmente el valor RMS) y fase (ángulo). Se utiliza para representar cantidades eléctricas en el **dominio de la frecuencia**.

**Diferencias principales:**
1.  **Dominio:** Los vectores representan fenómenos espaciales; los fasores representan fenómenos que varían en el tiempo (señales senoidales).
2.  **Rotación:** Un fasor se puede visualizar como un vector que rota en el plano complejo a una velocidad angular $\omega$. Su proyección en el eje imaginario genera la onda senoidal en el tiempo.
3.  **Frecuencia:** En el análisis fasorial, la frecuencia $\omega$ se asume implícita y constante para todo el circuito, por lo que no se incluye en la notación del fasor (ej. $\mathbf{V} = V_{rms} \angle \theta$).

## 2.5 Concepto de Impedancia y sus componentes
La **Impedancia ($\mathbf{Z}$)** es la oposición total que presenta un circuito al paso de una corriente alterna. Se mide en Ohmios ($\Omega$) y es un número complejo:
$$\mathbf{Z} = R + jX$$

**Componentes:**
1.  **Resistencia ($R$):** Oposición al flujo de corriente que disipa energía en forma de calor (Efecto Joule). No depende de la frecuencia.
2.  **Reactancia ($X$):** Oposición al paso de corriente causada por los campos eléctricos y magnéticos (elementos que almacenan energía, no la disipan). Depende directamente de la frecuencia. Se divide en:
    *   **Reactancia Inductiva ($X_L$):** Oposición presentada por un inductor. Aumenta con la frecuencia.
        $$X_L = \omega L = 2\pi f L$$
    *   **Reactancia Capacitiva ($X_C$):** Oposición presentada por un capacitor. Disminuye con la frecuencia.
        $$X_C = \frac{1}{\omega C} = \frac{1}{2\pi f C}$$

## 2.6 Configuración de un circuito serie – paralelo y leyes de Kirchhoff

En los circuitos de CA, las configuraciones **serie-paralelo** combinan elementos donde algunos comparten la misma corriente (serie) y otros comparten el mismo voltaje (paralelo). Para su análisis, se utilizan los fasores y la aritmética de números complejos.

**Leyes de Kirchhoff en CA:**
*   **Ley de Corrientes de Kirchhoff (LCK):** La suma fasorial de las corrientes que entran a un nodo es igual a la suma de las corrientes que salen.
    $$\sum \mathbf{I}_{entrada} = \sum \mathbf{I}_{salida} \quad \Rightarrow \quad \sum_{k=1}^{n} \mathbf{I}_k = 0$$
*   **Ley de Voltajes de Kirchhoff (LKV):** La suma fasorial de las caídas de voltaje alrededor de cualquier malla cerrada es igual a la suma fasorial de las fuentes de voltaje en esa malla.
    $$\sum_{k=1}^{n} \mathbf{V}_k = 0$$

## 2.7 Regla del Divisor de Tensión en circuitos serie (con demostración)

En un circuito de CA en serie, el voltaje total se divide entre las impedancias. El voltaje a través de una impedancia específica es proporcional a su valor respecto a la impedancia total.

**Fórmula general:**
$$\mathbf{V}_x = \mathbf{V}_{total} \left( \frac{\mathbf{Z}_x}{\mathbf{Z}_{total}} \right)$$

**Demostración:**
Consideremos un circuito serie con una fuente $\mathbf{V}_{total}$ y dos impedancias $\mathbf{Z}_1$ y $\mathbf{Z}_2$.
1. La impedancia total es: $\mathbf{Z}_{total} = \mathbf{Z}_1 + \mathbf{Z}_2$
2. Por la Ley de Ohm en CA, la corriente que circula por el circuito serie es: $\mathbf{I} = \frac{\mathbf{V}_{total}}{\mathbf{Z}_{total}}$
3. El voltaje en la impedancia $\mathbf{Z}_2$ es: $\mathbf{V}_2 = \mathbf{I} \cdot \mathbf{Z}_2$
4. Sustituyendo la corriente del paso 2 en la ecuación del paso 3:
   $$\mathbf{V}_2 = \left( \frac{\mathbf{V}_{total}}{\mathbf{Z}_{total}} \right) \mathbf{Z}_2 = \mathbf{V}_{total} \left( \frac{\mathbf{Z}_2}{\mathbf{Z}_1 + \mathbf{Z}_2} \right)$$
*(Queda demostrada la regla).*

## 2.8 Regla del Divisor de Corriente en circuitos paralelos (con demostración)

En un circuito de CA en paralelo, la corriente total se divide entre las ramas. La corriente a través de una rama es inversamente proporcional a su impedancia.

**Fórmula general (para dos ramas):**
$$\mathbf{I}_1 = \mathbf{I}_{total} \left( \frac{\mathbf{Z}_2}{\mathbf{Z}_1 + \mathbf{Z}_2} \right)$$

**Demostración:**
Consideremos dos impedancias $\mathbf{Z}_1$ y $\mathbf{Z}_2$ en paralelo, alimentadas por una corriente total $\mathbf{I}_{total}$.
1. La impedancia equivalente del paralelo es: $\mathbf{Z}_{eq} = \frac{\mathbf{Z}_1 \mathbf{Z}_2}{\mathbf{Z}_1 + \mathbf{Z}_2}$
2. El voltaje común en el paralelo es: $\mathbf{V} = \mathbf{I}_{total} \cdot \mathbf{Z}_{eq}$
3. La corriente que pasa por la rama $\mathbf{Z}_1$ es: $\mathbf{I}_1 = \frac{\mathbf{V}}{\mathbf{Z}_1}$
4. Sustituimos el voltaje del paso 2:
   $$\mathbf{I}_1 = \frac{\mathbf{I}_{total} \cdot \mathbf{Z}_{eq}}{\mathbf{Z}_1} = \mathbf{I}_{total} \left( \frac{\frac{\mathbf{Z}_1 \mathbf{Z}_2}{\mathbf{Z}_1 + \mathbf{Z}_2}}{\mathbf{Z}_1} \right)$$
5. Simplificando $\mathbf{Z}_1$ en el numerador y denominador:
   $$\mathbf{I}_1 = \mathbf{I}_{total} \left( \frac{\mathbf{Z}_2}{\mathbf{Z}_1 + \mathbf{Z}_2} \right)$$
*(Queda demostrada la regla).*