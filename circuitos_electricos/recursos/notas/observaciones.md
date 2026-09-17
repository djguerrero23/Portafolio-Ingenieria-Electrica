

# Auditoría y recomendaciones — Fasores V3

**Página revisada:** `teoria_fasores_V3.html`  
**Proyecto:** Portafolio de Ingeniería Eléctrica  
**Fecha de revisión:** 13 de septiembre de 2026

---

## 1. Veredicto general

La V3 ya no se percibe como una simple página de apuntes. Tiene características de un **recurso educativo serio de Ingeniería Eléctrica**.

La valoración general de la revisión fue:

| Aspecto | Valoración |
|---|---:|
| Rigor técnico | 9/10 |
| Organización | 9.5/10 |
| Progresión pedagógica | 9/10 |
| Matemática | 9/10 |
| Conexión física–matemática | 9.5/10 |
| Ejercicios | 9/10 |
| Interactividad | 8/10 |
| Identidad propia | 9.5/10 |
| Potencial futuro | 10/10 |

La recomendación principal NO es añadir grandes cantidades de teoría.

La evolución debería ser:

> **V3 = guía teórica sólida**  
> **V4 = guía + laboratorio interactivo**

---

# 2. Lo que está especialmente bien

## 2.1. La arquitectura pedagógica

La secuencia actual es muy buena:

**señal sinusoidal → fasor → normalización → RMS → condiciones de uso → plano complejo → cuadrantes → operador j → operaciones complejas → impedancia → RLC → circuito completo → diagrama fasorial → ejercicios → herramientas → cadena causal.**

Esto crea una progresión natural:

\[
\boxed{
\text{fenómeno}
\rightarrow
\text{representación}
\rightarrow
\text{matemática}
\rightarrow
\text{modelo eléctrico}
}
\]

---

## 2.2. La idea central de la página

La frase:

> **"El análisis fasorial no consiste en memorizar conversiones. Consiste en aprender una cadena de razonamiento."**

es una excelente declaración pedagógica.

La página no presenta simplemente fórmulas; intenta que el estudiante comprenda la secuencia:

\[
\text{Señal temporal}
\rightarrow
\text{Coseno canónico}
\rightarrow
\text{Fasor}
\rightarrow
\text{Álgebra compleja}
\rightarrow
\text{Circuito CA}
\]

Esta idea debería mantenerse y convertirse incluso en la **identidad pedagógica del portal**.

---

# 3. La explicación de qué es un fasor está bien planteada

La V3 presenta:

\[
v(t)=V_m\cos(\omega t+\phi)
\]

y:

\[
\mathbf V=V_m\angle\phi
\]

y luego:

\[
v(t)=\operatorname{Re}\{\mathbf V e^{j\omega t}\}
\]

Además aclara:

> **Fasor ≠ señal temporal**

Esto es conceptualmente importante.

### Mejora recomendada

Agregar explícitamente:

\[
V_m e^{j(\omega t+\phi)}
=
\underbrace{V_m e^{j\phi}}_{\text{fasor}}
\underbrace{e^{j\omega t}}_{\text{evolución temporal}}
\]

Esto permite ver exactamente qué parte representa el fasor y qué parte corresponde a la evolución temporal.

---

# 4. Mejorar la metáfora de "foto instantánea"

Si se utiliza la metáfora del vector rotatorio como "foto", debe dejarse claro que es solamente una analogía.

Un estudiante podría interpretar erróneamente que:

> "El fasor es simplemente el vector en t = 0."

Es más preciso explicar que el fasor separa la información de amplitud/fase de la dependencia temporal común:

\[
\mathbf V=V_m e^{j\phi}
\]

mientras:

\[
e^{j\omega t}
\]

describe la evolución temporal.

---

# 5. Excelente tratamiento de seno, coseno y signos

La normalización previa:

\[
V_m\cos(\omega t+\phi)
\]

está muy bien planteada.

Especialmente buena es la idea:

> **Primero normaliza la función. Después extrae el fasor.**

Esto evita que el estudiante memorice una fórmula diferente para cada combinación de seno, coseno y signo.

La filosofía correcta es:

\[
\boxed{
\text{normalizar}
\rightarrow
\text{extraer fasor}
}
\]

---

# 6. Muy buena inclusión de RMS

La V3 diferencia claramente:

\[
V_m
\]

de:

\[
V_{rms}
\]

y advierte:

> **Nunca mezcles valores RMS con valores pico sin realizar la conversión correspondiente.**

Esto debe conservarse porque es uno de los errores más frecuentes en Circuitos Eléctricos.

### Mejora opcional

Usar una convención visual fuerte:

- Fasor pico: \(\mathbf V_p\)
- Fasor RMS: \(\mathbf V_{rms}\)

y mantenerla consistentemente en ejemplos y ejercicios.

---

# 7. Excelente sección: "¿Cuándo puedo utilizar fasores?"

Es una mejora importante de la V3.

La página especifica que el análisis fasorial convencional requiere:

- señales sinusoidales;
- régimen permanente;
- frecuencia determinada;
- sistemas lineales donde el método sea aplicable.

También se explica que:

\[
x(t)=\sin(10t)+\sin(100t)
\]

no puede representarse mediante un único fasor.

Esto da madurez conceptual a la página.

---

# 8. La sección de cuadrantes es una de las fortalezas

La introducción de:

\[
\boxed{\theta=\operatorname{atan2}(y,x)}
\]

es excelente.

También es muy buena la explicación de por qué:

\[
\arctan(y/x)
\]

puede entregar el cuadrante incorrecto.

El ejemplo:

\[
-3+j4
\]

y:

\[
126.87^\circ
\]

es muy apropiado.

La incorporación de métodos para calculadoras Casio también convierte el conocimiento matemático en una herramienta práctica para exámenes y laboratorio.

---

# 9. La sección del operador j es particularmente fuerte

La idea:

\[
\boxed{j=1\angle90^\circ}
\]

y:

\[
j\mathbf Z
=
|\mathbf Z|\angle(\theta+90^\circ)
\]

es excelente.

Permite conectar:

\[
+j
\rightarrow
+90^\circ
\rightarrow
\text{inductivo}
\]

y:

\[
-j
\rightarrow
-90^\circ
\rightarrow
\text{capacitivo}
\]

La frase:

> **"En fasores, j no es simplemente una letra algebraica. Es un operador que representa un desplazamiento angular de +90°."**

es una de las ideas que conviene conservar como eje de la página.

---

# 10. ELI e ICE

La página acierta al presentar ELI e ICE como memoria y no como demostración.

La mejora ideal sería reforzar la cadena:

\[
\boxed{
\text{ecuación física}
\rightarrow
\text{derivada/integral}
\rightarrow
j
\rightarrow
\pm90^\circ
\rightarrow
\text{ELI/ICE}
}
\]

De esta manera:

**ELI/ICE es la conclusión, no el punto de partida.**

---

# 11. Impedancia: excelente puente hacia Ingeniería Eléctrica

La transición:

\[
\mathbf V=\mathbf I\mathbf Z
\]

y:

\[
\mathbf Z=R+jX
\]

es el punto donde la matemática compleja adquiere significado eléctrico.

La cadena recomendada para reforzar todavía más esta idea es:

\[
\text{ecuación temporal}
\rightarrow
\text{representación fasorial}
\rightarrow
\text{impedancia}
\rightarrow
\mathbf V=\mathbf Z\mathbf I
\]

Por ejemplo:

\[
v_R=Ri
\]

\[
v_L=L\frac{di}{dt}
\]

\[
i_C=C\frac{dv}{dt}
\]

se transforman en:

\[
Z_R=R
\]

\[
Z_L=j\omega L
\]

\[
Z_C=\frac{1}{j\omega C}
\]

y finalmente:

\[
\boxed{\mathbf V=\mathbf Z\mathbf I}
\]

---

# 12. Ejemplo RLC integrado

El ejemplo RLC es uno de los puntos fuertes porque demuestra el verdadero propósito de los fasores.

La secuencia es:

\[
v(t)
\rightarrow
\mathbf V
\rightarrow
\mathbf Z
\rightarrow
\mathbf I
\rightarrow
i(t)
\]

También aparecen las tensiones individuales:

\[
V_R
\]

\[
V_L
\]

\[
V_C
\]

y la suma fasorial.

Esto es exactamente el tipo de ejemplo que conecta la matemática con la interpretación física.

---

# 13. Mejora prioritaria: hacer visible el diagrama fasorial

Después de calcular:

\[
V_R,\quad V_L,\quad V_C
\]

el estudiante debería poder ver una representación vectorial dinámica.

Idealmente permitir:

- activar/desactivar \(I\);
- activar/desactivar \(V_R\);
- activar/desactivar \(V_L\);
- activar/desactivar \(V_C\);
- activar/desactivar \(V_T\).

Así:

\[
\boxed{
V_R+V_L+V_C=V_T
}
\]

deja de ser solamente una igualdad matemática y se convierte en una suma geométrica visible.

---

# 14. Ejercicios: muy buena progresión

La clasificación actual es adecuada:

### Nivel 1
Fundamentos y transformaciones.

### Nivel 2
Operaciones complejas e impedancias.

### Nivel 3
Circuitos RLC.

Esto genera una progresión razonable desde la matemática hasta la aplicación eléctrica.

---

# 15. Mejora de los ejercicios: aprendizaje activo

Actualmente la página puede funcionar como guía de estudio con soluciones.

Para una futura versión interactiva sería mejor:

\[
\boxed{
\text{enunciado}
\rightarrow
\text{intenta}
\rightarrow
\text{pista}
\rightarrow
\text{solución}
\rightarrow
\text{comprobación}
}
\]

Ejemplo:

\[
Z=6+j8
\]

Pregunta:

> ¿Cuál es su forma polar?

Primero permitir que el estudiante responda.

Después:

**Mostrar pista**

> ¿En qué cuadrante está?

Finalmente:

\[
Z=10\angle53.13^\circ
\]

Esto desarrolla razonamiento en lugar de lectura pasiva.

---

# 16. Pequeña precisión técnica sobre impedancia

Cuando se afirma:

\[
\theta_Z>0\rightarrow\text{inductivo}
\]

\[
\theta_Z=0\rightarrow\text{resistivo}
\]

\[
\theta_Z<0\rightarrow\text{capacitivo}
\]

es correcto para impedancias pasivas.

Como mejora de precisión, puede indicarse:

> Para una impedancia pasiva \(Z=R+jX\), con \(R\geq0\), el signo de \(X\) determina el carácter inductivo o capacitivo.

No es una corrección urgente; es una mejora de precisión conceptual.

---

# 17. La gran oportunidad: convertir la página en un laboratorio

La recomendación principal para la V4 es:

> **No agregar más teoría por agregar teoría. Hacer que el estudiante experimente con las ideas.**

La web tiene una ventaja que un libro no puede aprovechar igual:

\[
\boxed{
\text{hacer visible la física detrás de las ecuaciones}
}
\]

---

# 18. Principio de interacción

Cada interacción debería seguir:

\[
\boxed{
\text{cambiar una variable}
\rightarrow
\text{observar}
\rightarrow
\text{predecir}
\rightarrow
\text{calcular}
\rightarrow
\text{interpretar}
}
\]

No se trata de hacer una página llena de animaciones.

La interacción debe existir cuando ayuda a comprender algo que el texto no puede mostrar tan bien.

---

# 19. Laboratorio 1 — Señal ↔ Fasor

Controles:

- amplitud;
- frecuencia;
- fase;
- pico/RMS;
- tiempo.

Mostrar simultáneamente:

\[
v(t)
\]

y:

\[
\mathbf V
\]

Al mover el tiempo:

- cambia el punto de la sinusoidal;
- rota el vector;
- cambia el valor instantáneo;
- cambia el ángulo instantáneo.

### Objetivo

Que el estudiante comprenda:

\[
\boxed{
\text{señal temporal}
\leftrightarrow
\text{fasor}
}
\]

---

# 20. Laboratorio 2 — El significado de j

Partir de:

\[
1
\]

y permitir:

\[
1
\rightarrow
j
\rightarrow
-1
\rightarrow
-j
\rightarrow
1
\]

Cada pulsación de \(\times j\) gira el vector 90°.

Mostrar:

\[
\boxed{
\text{multiplicar por }j
=
\text{rotar }90^\circ
}
\]

### Objetivo

Convertir el significado de \(j\) en una experiencia visual.

---

# 21. Laboratorio 3 — Complejo ↔ Polar

Controles:

\[
x
\]

\[
y
\]

Mostrar:

\[
x+jy
\]

\[
r\angle\theta
\]

\[
r=\sqrt{x^2+y^2}
\]

\[
\theta=\operatorname{atan2}(y,x)
\]

El punto se mueve por el plano complejo mientras se actualizan automáticamente magnitud, ángulo y cuadrante.

---

# 22. Laboratorio 4 — RLC

Controles:

\[
R,\ L,\ C,\ f
\]

Mostrar:

\[
X_L=\omega L
\]

\[
X_C=-\frac{1}{\omega C}
\]

\[
Z=R+j(X_L+X_C)
\]

\[
|Z|
\]

\[
\angle Z
\]

\[
I=\frac{V}{Z}
\]

y el diagrama fasorial.

Este sería probablemente el laboratorio con mayor impacto pedagógico.

---

# 23. Frecuencia como variable experimental

Permitir mover:

\[
f
\]

y observar:

\[
f\uparrow
\Rightarrow
X_L\uparrow
\]

mientras:

\[
f\uparrow
\Rightarrow
|X_C|\downarrow
\]

y finalmente observar el efecto sobre:

\[
Z
\]

e:

\[
I
\]

Esto permite enseñar relaciones causales y no solamente fórmulas.

---

# 24. Laboratorio de resonancia

Mostrar una gráfica:

\[
|I|\quad \text{vs.}\quad f
\]

El estudiante modifica la frecuencia y observa el máximo de corriente.

Después aparece:

\[
X_L=X_C
\]

\[
\omega L=\frac{1}{\omega C}
\]

\[
\boxed{
f_0=\frac{1}{2\pi\sqrt{LC}}
}
\]

La idea es:

> **observar → descubrir → formalizar**

en lugar de:

> memorizar → aplicar.

---

# 25. Predice antes de calcular

Esta debería convertirse en una mecánica recurrente.

Ejemplo:

\[
Z=20-j15\ \Omega
\]

Pregunta:

> ¿La corriente estará adelantada o atrasada respecto a la tensión?

Después de responder:

\[
\angle Z<0
\]

por tanto:

\[
\angle I=-\angle Z>0
\]

Resultado:

\[
\boxed{I\text{ adelanta a }V}
\]

Esto desarrolla intuición.

---

# 26. "Construye el circuito"

A futuro podría existir una interfaz con:

```text
COMPONENTES

[R] [L] [C]
```
