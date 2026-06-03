# Documentación Técnica: Generador de Dataset

Este script se encarga de la creación de un conjunto de datos sintético diseñado para entrenar modelos de aprendizaje supervisado enfocados en la predicción de rotación de personal (attrition). La generación se basa en lógica estocástica y reglas de negocio predefinidas para garantizar coherencia y verosimilitud en los datos.

## Librerías y Dependencias

El script utiliza las siguientes librerías de Python:

- **NumPy (`numpy`)**: Utilizada para la generación de números aleatorios, vectorización de operaciones y manejo de distribuciones estadísticas.
- **Pandas (`pandas`)**: Utilizada para la estructuración de los datos en un DataFrame y la exportación a formato CSV.

## Lógica de Generación de Variables

La generación de datos se divide en tres fases principales: variables base, lógica de probabilidad condicional y ensamblaje final.

### 1. Variables Base (Features)

Se generan 350 registros iniciales con las siguientes características:

- **Edad**: Números enteros entre 22 y 60 años.
- **Años en la Empresa**: Calculados de forma dinámica para asegurar que nunca superen la edad del empleado (considerando una edad mínima de ingreso de 18 años) y limitados a un máximo de 20 años.
- **Salario Mensual**: Sigue una distribución normal centrada en $800 con desviaciones basadas en la antigüedad y la edad. Se aplica un "piso" salarial de $460 (ajustado a estándares de salario básico).
- **Desempeño y Capacitación**: 
    - `ultima_evaluacion_desempeno`: Valores continuos entre 0.0 y 1.0.
    - `capacitaciones_recibidas`: Valores enteros entre 0 y 5 por año.
- **Factores Operativos**: Se generan variables como horas extra, satisfacción laboral (escala 1-5), número de proyectos y distancia al lugar de trabajo mediante muestreo aleatorio uniforme.

### 2. Probabilidad de Ascenso

La variable `tiene_ascenso_ultimos_2_anios` no es puramente aleatoria; utiliza una distribución binomial donde la probabilidad de éxito se incrementa significativamente si la `ultima_evaluacion_desempeno` es superior a 0.7.

## Algoritmo de Variable Objetivo (`renuncia`)

Para evitar la aleatoriedad pura en la variable objetivo, se implementa un modelo de probabilidad acumulada basado en reglas de riesgo laboral:

1. **Probabilidad Base**: Se establece un riesgo inicial del 10% para todos los empleados.
2. **Factores de Riesgo (Incrementales)**:
    - **Condición Crítica**: Si la satisfacción es baja (<= 2) y las horas extra son altas (> 10), la probabilidad aumenta un **50%**.
    - **Insatisfacción**: Si solo la satisfacción es baja, aumenta un **25%**.
    - **Distancia**: Si el empleado vive a más de 40 km, aumenta un **10%**.
3. **Factores de Retención (Decrementales)**:
    - **Ascenso Reciente**: Si el empleado fue ascendido en los últimos 2 años, la probabilidad disminuye un **15%**.
4. **Normalización**: Las probabilidades finales se limitan (clipping) entre un 5% y 95% para mantener variabilidad estocástica.

Finalmente, la variable `renuncia` se genera mediante un ensayo de Bernoulli (distribución binomial con n=1) utilizando la probabilidad calculada para cada individuo.

## Salida de Datos

El script exporta un archivo llamado `dataset_empleados.csv` que contiene todas las variables generadas, listo para el Análisis Exploratorio de Datos (EDA) y el entrenamiento del modelo.

---

**Nota Técnica**: Se utiliza una semilla fija (`np.random.seed(42)`) para asegurar que la generación sea reproducible en diferentes entornos de ejecución.
