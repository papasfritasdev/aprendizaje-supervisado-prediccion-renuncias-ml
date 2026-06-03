# Celda 5: Preprocesamiento y División del Conjunto de Datos

Esta fase es crítica para garantizar la validez científica del modelo. Se enfoca en la preparación de las características (features) y la segmentación de los datos para el entrenamiento y la evaluación posterior.

## Librerías y Dependencias

Se introducen componentes esenciales de **Scikit-Learn**:
- `train_test_split`: Para la división estocástica del dataset.
- `StandardScaler`: Para la normalización de variables numéricas.
- `LogisticRegression`, `RandomForestClassifier`, `GradientBoostingClassifier`: Algoritmos que se implementarán en etapas posteriores.
- `metrics`: Suite completa para la evaluación del desempeño.

## 1. División del Dataset (Hold-out Method)

Se aplica la técnica de *Hold-out* con las siguientes especificaciones:
- **Proporción**: 80% para entrenamiento (`X_train`) y 20% para pruebas (`X_test`).
- **Reproducibilidad**: Se utiliza `random_state=42`, lo que asegura que cualquier desarrollador que ejecute el código obtenga exactamente la misma división de registros.
- **Separación de Objetivo**: La variable `renuncia` se aisla en el vector `y`, mientras que el resto de las columnas conforman la matriz de características `X`.

## 2. Estandarización de Variables (Feature Scaling)

Para algoritmos sensibles a la magnitud de los datos (como la Regresión Logística), se aplica un escalado estándar (Z-score normalization).

### Prevención del Data Leakage (Filtrado de Información)

Una de las reglas de oro implementadas en esta celda es el manejo diferenciado del escalador:
1.  **Ajuste y Transformación (`fit_transform`)**: Se aplica únicamente sobre el conjunto de **entrenamiento**. El escalador "aprende" la media y la desviación estándar solo de estos datos.
2.  **Solo Transformación (`transform`)**: Se aplica sobre el conjunto de **prueba**. Se utilizan los parámetros (media y std) aprendidos del entrenamiento para transformar los datos de prueba. 

**¿Por qué es importante?** Esto garantiza que ninguna información estadística del conjunto de prueba "se filtre" hacia el entrenamiento del modelo, simulando un escenario real donde el modelo se enfrenta a datos nuevos y desconocidos.

## Variables Procesadas

Se seleccionaron específicamente las variables continuas y discretas no binarias para el escalado:
- Edad, años en la empresa, salario mensual, horas extra, satisfacción, etc.
- Se omiten variables que ya están en formato binario (como ascensos) para preservar su interpretación directa.

---

**Nota Técnica**: Al finalizar esta celda, los datos están listos en términos de escala y segmentación para alimentar los algoritmos de clasificación.
