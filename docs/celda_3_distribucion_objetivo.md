# Celda 3: Distribución de la Variable Objetivo (Renuncia)

Esta sección tiene como propósito fundamental evaluar el balance del conjunto de datos. El desbalance de clases es un fenómeno común en problemas de predicción de renuncias, donde la clase positiva (renuncia) suele ser minoritaria, lo cual impacta directamente en la elección de métricas de evaluación del modelo.

## Lógica de Procesamiento

Para generar la visualización, el script realiza las siguientes operaciones:

1.  **Agregación de Datos**: Utiliza `value_counts()` para obtener la frecuencia absoluta de cada categoría (0 y 1).
2.  **Formateo de Tabla**: Aplica `reset_index()` para transformar el resultado en un DataFrame compatible con las funciones de trazado de Plotly.
3.  **Cálculo de Proporción**: Ejecuta `value_counts(normalize=True)` para mostrar los porcentajes relativos de cada clase en la consola.

## Visualización Interactiva

Se implementa un gráfico de barras con las siguientes características técnicas:

- **Codificación Semántica de Colores**: 
    - **Verde (`#2ca02c`)**: Representa a los empleados que permanecen en la empresa (clase 0).
    - **Rojo (`#d62728`)**: Representa a los empleados que han renunciado (clase 1).
- **Etiquetas de Datos**: Los valores exactos se muestran sobre las barras (`textposition='outside'`) para evitar ambigüedades.
- **Eje Categórico**: Se fuerza el tipo de eje X a `category` para asegurar que las etiquetas 0 y 1 no sean tratadas como valores numéricos continuos.

## Análisis de Balanceo

El script imprime en consola la proporción de clases en formato porcentual. Este dato es crucial para decidir si se requieren técnicas de remuestreo (como SMOTE) o si basta con utilizar métricas robustas al desbalance como el F1-Score o el AUC-ROC en lugar del Accuracy simple.

---

**Nota Técnica**: Un dataset balanceado facilita el entrenamiento del modelo, mientras que uno muy desbalanceado podría sesgar las predicciones hacia la clase mayoritaria.
