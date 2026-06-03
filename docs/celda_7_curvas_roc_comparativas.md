# Celda 7: Análisis Visual de Curvas ROC Comparativas

La Curva ROC (Receiver Operating Characteristic) es una herramienta fundamental en la clasificación binaria para evaluar la capacidad de un modelo para distinguir entre clases (en este caso, empleados que renuncian vs. empleados que permanecen) a través de diversos umbrales de decisión.

## Librerías y Métodos Utilizados

- **Plotly Graph Objects (`go`)**: Empleado para construir una visualización altamente personalizada e interactiva.
- **Scikit-Learn (`roc_curve`)**: Función técnica que calcula los puntos de la curva (FPR y TPR) basados en las probabilidades predichas.

## Componentes Técnicos de la Gráfica

La visualización integra varios elementos clave para facilitar el diagnóstico del modelo:

1.  **Línea Base (Azar)**: Se incluye una línea punteada diagonal (`y = x`). Representa el desempeño de un clasificador puramente aleatorio. Cualquier modelo útil debe situarse significativamente por encima de esta línea.
2.  **Trazado de Curvas**: Se itera sobre los modelos entrenados, calculando sus tasas:
    -   **FPR (False Positive Rate)**: Proporción de empleados que NO renunciaron pero fueron clasificados erróneamente como renuncias.
    -   **TPR (True Positive Rate / Recall)**: Proporción de empleados que renunciaron y fueron correctamente identificados.
3.  **Integración de AUC**: El área bajo la curva (AUC) se incluye en la leyenda de cada modelo. Un AUC de 1.0 representa un modelo perfecto, mientras que 0.5 representa uno sin valor predictivo superior al azar.

## Lógica de Interpretación

Esta gráfica es la base para responder preguntas de negocio y técnicas sobre la selección del modelo:
- **Posicionamiento**: El modelo cuya curva esté más "pegada" a la esquina superior izquierda (coordenada 0,1) es el que posee el mejor equilibrio entre sensibilidad y especificidad.
- **Interactividad**: Gracias a `hovermode='x unified'`, el usuario puede comparar el desempeño exacto de los tres modelos para un mismo nivel de falsos positivos simultáneamente.

## Configuración del Layout

- **Dimensiones**: 800x600 px para una visualización clara en informes técnicos.
- **Hovers Personalizados**: Se configuran plantillas de información emergente para mostrar valores de FPR y TPR con precisión de dos decimales.

---

**Nota Técnica**: La curva ROC es independiente del balance de clases, lo que la convierte en una métrica de diagnóstico más robusta que el Accuracy cuando se comparan arquitecturas de modelos distintas.
