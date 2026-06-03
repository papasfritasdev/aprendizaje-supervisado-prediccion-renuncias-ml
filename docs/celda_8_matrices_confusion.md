# Celda 8: Análisis de Matrices de Confusión

La matriz de confusión es una herramienta de diagnóstico que permite desglosar el desempeño de un clasificador binario, mostrando la relación exacta entre las predicciones del modelo y los valores reales del dataset de prueba.

## Implementación Técnica

Para cada modelo entrenado, el script ejecuta el siguiente flujo:
1.  **Generación de Predicciones**: Se obtienen las clasificaciones binarias (`y_pred`) para el conjunto de prueba escalado.
2.  **Cálculo de la Matriz**: Se utiliza `confusion_matrix` de Scikit-Learn para calcular la frecuencia de aciertos y errores.
3.  **Visualización**: Se emplea `px.imshow` para crear un mapa de calor interactivo en escala de azules (`Blues`), facilitando la identificación visual de las áreas con mayor densidad de registros.

## Interpretación de Cuadrantes (Contexto de Negocio)

La matriz se divide en cuatro cuadrantes fundamentales, cuya interpretación es crítica para la toma de decisiones en RRHH:

| Cuadrante | Nombre Técnico | Significado para el Negocio |
| :--- | :--- | :--- |
| **Superior Izquierdo (0,0)** | **Verdadero Negativo (TN)** | Empleados que el modelo predijo que se quedarían y efectivamente permanecieron. |
| **Superior Derecho (0,1)** | **Falso Positivo (FP)** | **Falsa Alarma**: Empleados que se quedan, pero el modelo predijo que renunciarían. Implica un costo de intervención innecesario. |
| **Inferior Izquierdo (1,0)** | **Falso Negativo (FN)** | **Fuga no Detectada**: Empleados que renunciaron, pero el modelo predijo que se quedarían. Es el error más costoso por la pérdida de talento. |
| **Inferior Derecho (1,1)** | **Verdadero Positivo (TP)** | Empleados que el modelo predijo correctamente que renunciarían, permitiendo una intervención preventiva. |

## Especificaciones de Visualización

- **Etiquetado Claro**: Los ejes están explícitamente etiquetados como "Predicción del Modelo" y "Realidad", con las categorías "Se Queda (0)" y "Renuncia (1)".
- **Legibilidad**: Se aumenta el tamaño de fuente del texto interno a 20 puntos para asegurar que los valores numéricos sean el foco de atención.
- **Interactividad**: Permite explorar las cantidades exactas mediante *tooltips* al interactuar con el gráfico.

---

**Nota Técnica**: Una diagonal principal (de arriba-izquierda a abajo-derecha) con valores altos indica un modelo con alta precisión y exhaustividad. Los valores fuera de esa diagonal representan los errores del sistema.
