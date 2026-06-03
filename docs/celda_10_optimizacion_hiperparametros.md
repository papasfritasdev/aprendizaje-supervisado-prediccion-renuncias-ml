# Celda 10: Optimización de Hiperparámetros y Validación Cruzada

En esta fase final de modelado, se busca maximizar el rendimiento del algoritmo **Gradient Boosting** mediante técnicas avanzadas de ajuste y validación, asegurando que los resultados sean generalizables y no producto del azar en la división inicial de los datos.

## 1. Validación Cruzada (k-Fold Cross-Validation)

Antes de la optimización, se somete al modelo base a una validación cruzada con **k=5**. 

- **Metodología**: El conjunto de entrenamiento se divide en 5 subgrupos. El modelo se entrena 5 veces, rotando en cada iteración el subgrupo que actúa como validación.
- **Métrica Objetivo**: Se utiliza el **F1-Score** debido a su robustez frente al desbalance de clases.
- **Resultado Técnico**: Se reporta la **Media** (desempeño esperado) y la **Desviación Estándar** (consistencia del modelo). Una desviación baja indica que el modelo es estable y no depende de una partición específica de datos.

## 2. Ajuste de Hiperparámetros con `GridSearchCV`

Se implementa una búsqueda en rejilla (*Grid Search*) para encontrar la combinación óptima de parámetros que maximice el F1-Score.

### Espacio de Búsqueda (Hyperparameter Grid)

Se evaluaron 27 combinaciones diferentes (3x3x3) de los siguientes parámetros:
- **`n_estimators` ([50, 100, 200])**: Número de árboles secuenciales a construir.
- **`learning_rate` ([0.01, 0.05, 0.1])**: Controla la magnitud de la contribución de cada nuevo árbol al modelo final.
- **`max_depth` ([3, 4, 5])**: Limita la profundidad de los árboles para controlar la complejidad y evitar el sobreajuste (*overfitting*).

### Especificaciones de Ejecución
- **`n_jobs=-1`**: Optimización de recursos mediante el uso de todos los núcleos del procesador en paralelo.
- **`best_estimator_`**: Tras la búsqueda, el script extrae automáticamente el modelo con el mejor desempeño para su evaluación final.

## 3. Comparación de Modelos (Base vs. Optimizado)

El paso final consiste en una auditoría de rendimiento comparando el Gradient Boosting original contra su versión refinada. 

| Métrica | Propósito en la Comparación |
| :--- | :--- |
| **Accuracy** | Validación de la mejora general en la tasa de aciertos. |
| **Precisión/Recall** | Identificación de mejoras específicas en la detección de renuncias reales. |
| **F1-Score** | Indicador principal del éxito de la optimización. |
| **AUC-ROC** | Evaluación de la capacidad de separación de clases mejorada. |

## Conclusión Técnica

Este proceso de optimización garantiza que el modelo entregado sea la mejor versión posible dentro del espacio de búsqueda definido, proporcionando una base sólida para las recomendaciones estratégicas de Recursos Humanos.

---

**Nota Técnica**: El uso de `GridSearchCV` junto con validación cruzada integrada asegura que los parámetros seleccionados no solo funcionen bien en el conjunto de prueba, sino que sean robustos ante variaciones en los datos de entrada.
