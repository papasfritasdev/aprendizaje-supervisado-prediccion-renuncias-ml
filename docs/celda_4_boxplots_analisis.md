# Celda 4: Análisis de Distribución mediante Boxplots

En esta etapa del Análisis Exploratorio de Datos (EDA), se utilizan diagramas de caja (boxplots) para comparar visualmente cómo varían el salario y la satisfacción laboral entre los empleados que permanecieron en la empresa y aquellos que renunciaron.

## Objetivos del Análisis

El uso de boxplots permite identificar patrones críticos como:
- **Diferencia de Medianas**: Determinar si el salario promedio es significativamente menor en el grupo que renuncia.
- **Dispersión (IQR)**: Observar el rango intercuartílico para entender la variabilidad de la satisfacción en cada grupo.
- **Detección de Outliers**: Identificar casos excepcionales (ej. empleados con salarios altos que renuncian).

## Visualizaciones Implementadas

Se generan dos gráficos independientes utilizando `plotly.express`:

### 1. Salario Mensual vs Renuncia
Este gráfico muestra la distribución económica de ambos grupos. 
- **Eje Y**: Representa el salario en dólares ($).
- **Eje X**: Categoriza por estado de renuncia (0 o 1).
- **Propósito**: Validar si existe una brecha salarial que actúe como incentivo para la rotación.

### 2. Satisfacción Laboral vs Renuncia
Este gráfico analiza la percepción subjetiva del empleado.
- **Eje Y**: Escala de Likert del 1 al 5.
- **Eje X**: Categoriza por estado de renuncia.
- **Propósito**: Confirmar si los niveles bajos de satisfacción (1 y 2) están concentrados en el grupo de renuncia, tal como se definió en la lógica de generación del dataset.

## Especificaciones Técnicas

- **Interactividad**: Al ser gráficos de Plotly, el usuario puede ver los valores exactos de los cuartiles (Q1, Q3), la mediana, los valores máximos/mínimos y los bigotes (*whiskers*) al pasar el cursor.
- **Consistencia Visual**: Se mantiene el código de colores institucional (Verde para permanencia, Rojo para renuncia) y se fuerza el eje X como tipo categórico para evitar interpretaciones numéricas erróneas.

---

**Nota Técnica**: El boxplot es superior a una simple barra de promedios porque permite ver la forma de la distribución y la concentración de los datos en diferentes rangos.
