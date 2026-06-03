# Sistema de Predicción de Rotación de Personal (Machine Learning)

Este repositorio contiene una solución integral de analítica predictiva diseñada para el área de Recursos Humanos. El sistema utiliza algoritmos de aprendizaje supervisado para identificar patrones de comportamiento y predecir la probabilidad de renuncia de los empleados en un horizonte de 6 meses, permitiendo intervenciones preventivas basadas en datos.

## Estructura del Proyecto

El repositorio está organizado de la siguiente manera:

```text
├── docs/                        # Documentación técnica detallada de cada componente.
├── generador_dataset.py          # Script de generación de datos sintéticos con lógica de negocio.
├── notebook_modelos.ipynb       # Notebook principal: EDA, Modelado y Optimización.
├── requirements.txt             # Dependencias del proyecto.
├── .gitignore                   # Configuración para el control de versiones.
└── README.md                    # Documentación principal del sistema.
```

### Componentes Clave:
- **`generador_dataset.py`**: Motor de simulación estocástica que construye un conjunto de datos de empleados basándose en reglas de coherencia (relación entre satisfacción, carga horaria, salario y desempeño).
- **`notebook_modelos.ipynb`**: Pipeline completo de ciencia de datos que incluye Análisis Exploratorio de Datos (EDA) interactivo, entrenamiento de modelos competitivos y optimización de hiperparámetros.
- **`docs/`**: Carpeta que contiene explicaciones técnicas detalladas sobre la implementación de cada celda de procesamiento y algoritmos de modelado.

## Prerrequisitos e Instalación

Para garantizar un entorno de ejecución limpio y aislado, se recomienda el uso de un entorno virtual de Python.

### 1. Clonar el repositorio
```bash
git clone <url-del-repositorio>
cd aprendizaje-supervisado-prediccion-renuncias-ml
```

### 2. Configurar el Entorno Virtual
En Windows:
```powershell
python -m venv venv
.\venv\Scripts\activate
```

En macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

## Flujo de Ejecución

Siga estos pasos para reproducir los resultados del sistema:

### Paso 1: Generación de Datos
Ejecute el script generador para crear el archivo `dataset_empleados.csv` que servirá de base para el modelo.
```bash
python generador_dataset.py
```

### Paso 2: Análisis y Modelado
Abra el archivo `notebook_modelos.ipynb` en su entorno preferido (VS Code o Jupyter Notebook) y ejecute las celdas secuencialmente. El flujo incluye:
1.  **Carga y Estadísticas**: Validación inicial de la integridad de los datos.
2.  **Análisis Visual**: Identificación de factores críticos mediante Mapas de Calor y Boxplots.
3.  **Entrenamiento**: Comparación de Regresión Logística, Random Forest y Gradient Boosting.
4.  **Optimización**: Ajuste fino del modelo Gradient Boosting mediante `GridSearchCV` y validación cruzada.

## Tecnologías Utilizadas
- **Lenguaje**: Python 3.x
- **Procesamiento de Datos**: Pandas, NumPy
- **Visualización**: Plotly (Gráficos interactivos)
- **Machine Learning**: Scikit-Learn, XGBoost
- **Entorno**: Jupyter / Notebooks

---
**Nota Técnica**: El sistema implementa técnicas de prevención de *Data Leakage* mediante el uso de `StandardScaler` ajustado únicamente sobre el conjunto de entrenamiento.
