# Celda 2: Mapa de Calor de Correlaciones

Esta sección del análisis utiliza técnicas de visualización avanzada para identificar la fuerza y dirección de las relaciones lineales entre todas las variables numéricas del conjunto de datos, con especial énfasis en la variable objetivo `renuncia`.

## Librerías Utilizadas

- **Plotly Express (`px`)**: Empleada para la generación del mapa de calor interactivo (`imshow`).
- **Pandas (`df.corr`)**: Utilizada para calcular la matriz de coeficientes de correlación de Pearson.

## Lógica Técnica

El proceso se divide en dos pasos clave:

1.  **Cálculo de la Matriz**: Se genera una matriz de correlación redondeada a 3 decimales para mantener la precisión técnica sin saturar la visualización.
2.  **Visualización Interactiva**: A diferencia de los mapas estáticos, esta implementación permite la exploración de datos en tiempo real mediante *tooltips* al posicionar el cursor sobre cada celda.

## Configuración del Gráfico

El mapa de calor cuenta con las siguientes especificaciones técnicas:

- **Escala de Color (`RdBu_r`)**: Se utiliza una escala divergente (Rojo-Azul invertida). Los tonos rojos intensos indican correlaciones positivas fuertes, mientras que los azules indican correlaciones negativas.
- **Anotaciones Automáticas (`text_auto=True`)**: Inserta los valores numéricos de correlación directamente sobre las celdas para facilitar la lectura inmediata.
- **Dimensiones**: El layout se ajusta a 900x800 píxeles para garantizar que todas las etiquetas de las variables sean legibles sin solapamiento.

## Importancia en el Proyecto

El objetivo principal de este componente es identificar las tres correlaciones más fuertes con la variable `renuncia`. Esto permite validar si las reglas de negocio implementadas en la generación del dataset (como la relación entre satisfacción laboral y renuncia) se reflejan correctamente en los datos recolectados.

---

**Nota Técnica**: Una correlación cercana a 1 o -1 sugiere una relación lineal fuerte, mientras que valores cercanos a 0 indican independencia lineal entre las variables.
