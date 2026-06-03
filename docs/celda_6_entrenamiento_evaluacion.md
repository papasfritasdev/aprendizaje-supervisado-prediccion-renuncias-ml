# Celda 6: Entrenamiento y Evaluación Comparativa de Modelos

En esta etapa, se procede con la implementación de tres algoritmos de clasificación supervisada para comparar su efectividad en la predicción de renuncias laborales. Se utiliza un enfoque sistemático para garantizar que todos los modelos se evalúen bajo las mismas condiciones.

## Algoritmos Implementados

Se han seleccionado tres arquitecturas con diferentes niveles de complejidad y fundamentos matemáticos:

1.  **Regresión Logística**: Actúa como el modelo base de referencia (*baseline*). Es un modelo lineal fácil de interpretar y computacionalmente eficiente.
2.  **Random Forest**: Un modelo de ensamble tipo *bagging* basado en múltiples árboles de decisión. Es robusto frente a valores atípicos y captura relaciones no lineales.
3.  **Gradient Boosting**: Un modelo de ensamble tipo *boosting* que construye árboles de forma secuencial para corregir los errores de los anteriores. Generalmente ofrece el mayor rendimiento predictivo.

## Metodología de Evaluación

El script automatiza el flujo de trabajo mediante un bucle que realiza los siguientes pasos para cada modelo:

### 1. Entrenamiento (`fit`)
El modelo aprende los patrones de los datos utilizando el conjunto `X_train_scaled` y las etiquetas `y_train`.

### 2. Predicción y Probabilidades
- **`predict`**: Genera la clasificación binaria final (0 o 1).
- **`predict_proba`**: Obtiene la probabilidad de pertenencia a la clase 1 (renuncia), necesaria para el cálculo del AUC-ROC.

### 3. Cálculo de Métricas Técnicas
Se calculan cinco indicadores clave para un análisis exhaustivo:

- **Accuracy**: Proporción total de predicciones correctas.
- **Precisión**: Capacidad del modelo para no marcar como positivo un caso que es negativo (evitar falsos positivos).
- **Recall (Sensibilidad)**: Capacidad del modelo para encontrar todos los casos positivos reales (evitar falsos negativos).
- **F1-Score**: Media armónica entre Precisión y Recall, ideal para evaluar el modelo cuando existe cierto desbalance de clases.
- **AUC-ROC**: Mide la capacidad de discriminación del modelo entre las dos clases a través de diferentes umbrales.

## Resultados Consolidados

El resultado final se presenta en una tabla de Pandas (`df_resultados`), redondeada a 3 decimales, facilitando la comparación directa entre algoritmos. 

---

**Nota Técnica**: El parámetro `zero_division=0` en la métrica de precisión se utiliza para manejar casos donde el modelo no predice ninguna renuncia, evitando errores de ejecución y asegurando la estabilidad del script.
