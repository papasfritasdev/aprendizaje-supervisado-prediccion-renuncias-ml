# Análisis Exploratorio de Datos (EDA): Estadísticas Descriptivas

Esta sección del análisis se enfoca en la carga inicial de los datos y la extracción de métricas estadísticas fundamentales para comprender la distribución y naturaleza de las variables del dataset de empleados.

## Librerías y Dependencias

Para el análisis y visualización, se utilizan las siguientes herramientas:

- **Pandas (`pandas`)**: Estructura de datos y análisis estadístico descriptivo.
- **Plotly Express & Graph Objects (`plotly`)**: Librerías utilizadas para la creación de gráficos interactivos de alta calidad.
- **NumPy (`numpy`)**: Soporte para operaciones matemáticas y manejo de arreglos vectorizados.

## Carga de Datos

El sistema carga el archivo `dataset_empleados.csv` generado previamente, el cual contiene las métricas de desempeño, demografía y la variable objetivo de renuncia para cada empleado.

## Análisis Estadístico Descriptivo

Se ejecuta el método `.describe()` sobre el DataFrame para obtener un resumen cuantitativo detallado. Este análisis incluye:

| Métrica | Descripción |
| :--- | :--- |
| **Count** | Cantidad total de registros (útil para detectar valores nulos). |
| **Mean (Media)** | Valor promedio de cada variable (ej. salario promedio, edad media). |
| **Std (Desviación)** | Medida de dispersión de los datos respecto a la media. |
| **Min / Max** | Valores extremos que permiten identificar rangos y posibles outliers. |
| **Percentiles (25%, 50%, 75%)** | Distribución de los datos por cuartiles, facilitando la identificación del sesgo (skewness). |

### Implementación Técnica

La visualización de estas métricas se optimiza mediante:
1.  **Redondeo**: Se limitan los resultados a 2 decimales para mejorar la legibilidad técnica.
2.  **Display**: Se utiliza la función `display()` propia de entornos interactivos para renderizar las tablas estadísticas en formato enriquecido.

---

**Nota Técnica**: La revisión de estas estadísticas es el primer paso crítico para validar que la lógica de generación del dataset se haya aplicado correctamente (por ejemplo, verificando que la edad mínima sea 22 y el salario no sea menor al piso establecido).
