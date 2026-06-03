# Celda 9: Análisis de Importancia de las Variables (Feature Importance)

Esta sección permite "abrir la caja negra" de los modelos de ensamble (**Random Forest** y **Gradient Boosting**) para entender qué características del dataset tienen un mayor impacto en la predicción de la renuncia de un empleado.

## Fundamento Técnico

Los modelos basados en árboles de decisión calculan la importancia de una variable basándose en cuánto reduce cada característica la impureza (Gini o Entropía) a lo largo de todos los árboles del modelo. Una variable con alta importancia es aquella que se utiliza con frecuencia para realizar divisiones críticas en los datos, permitiendo separar eficientemente a los empleados que renuncian de los que se quedan.

## Implementación de la Visualización

El script realiza los siguientes pasos para los modelos de ensamble:

1.  **Extracción de Atributos**: Accede a la propiedad `.feature_importances_` del modelo ya entrenado.
2.  **Estructuración de Datos**: Crea un DataFrame de Pandas vinculando cada valor de importancia con el nombre de su variable correspondiente.
3.  **Ordenamiento**: Clasifica las variables de forma ascendente para optimizar la visualización en un gráfico de barras horizontales.
4.  **Graficación Interactiva**: Utiliza `px.bar` con una escala de color `Viridis`, donde los colores más brillantes resaltan las variables con mayor peso predictivo.

## Valor para el Negocio y el Informe

Este análisis es fundamental para responder preguntas críticas como:
- ¿Coinciden las variables más importantes con la lógica de negocio definida inicialmente (ej. Satisfacción y Horas Extra)?
- ¿Existen variables inesperadas que el modelo ha detectado como predictores clave?
- ¿Qué factores debería priorizar RRHH en sus planes de retención para reducir la rotación?

## Especificaciones del Gráfico

- **Orientación**: Horizontal (`h`), facilitando la lectura de los nombres de las variables en el eje Y.
- **Interactividad**: Permite visualizar el porcentaje exacto de contribución de cada variable mediante el cursor.
- **Dimensiones**: 850x500 px, diseñadas para una integración limpia en presentaciones técnicas.

---

**Nota Técnica**: La suma de todas las importancias en un modelo de este tipo siempre es igual a 1 (o 100%). Esto permite interpretar cada barra como el porcentaje de influencia de esa variable específica sobre el comportamiento global del modelo.
