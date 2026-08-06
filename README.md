# Lab3-DataScience

## Selección de modelos

Para cumplir con los ejercicios 4, 5 y 6 del laboratorio decidimos entrenar y comparar cuatro modelos: dos CNN, una red fully-connected simple y un modelo de Random Forest.

### Random Forest

Entre las opciones que sugiere el enunciado (Random Forest, SVM, KNN) elegimos Random Forest. Con imágenes de 64x64 a color cada foto se convierte en más de 12,000 valores de entrada, y Random Forest maneja bien ese volumen de variables sin necesitar pasos extra de preprocesamiento como reducir dimensiones con PCA, que sí hubiera hecho falta para que SVM entrenara en un tiempo razonable. Además tiene hiperparámetros claros para ir ajustando (número de árboles, profundidad máxima) y así poder mostrar varias corridas comparando resultados, tal como pide la rúbrica. Descartamos KNN porque con tantas variables de entrada tiende a perder efectividad (curse of dimensionality) y es lento al momento de predecir sobre datos nuevos.

### Modelos CNN

Vamos a entrenar dos arquitecturas distintas para poder compararlas y quedarnos con la mejor:

- **CNN simple**: 2 a 3 bloques de convolución con 16, 32 y 64 filtros, con un poco de dropout para evitar sobreajuste. La idea es tener un modelo rápido de entrenar que sirva de punto de partida.
- **CNN profunda**: 4 bloques de convolución con 32, 64, 128 y 256 filtros, con batch normalization y más dropout. Buscamos que esta versión capture mejor los detalles finos que distinguen letras parecidas, como el grupo U/V/R/W/X que salió como el más confuso en el heatmap de similitud del EDA.

Comparar estas dos nos va a permitir discutir si vale la pena la complejidad extra de la red profunda o si el modelo simple ya es suficiente para el problema.

### Red neuronal simple

Como contraste armamos una red fully-connected: la imagen se aplana en un solo vector de números y pasa por una o dos capas densas (por ejemplo 512 neuronas y luego 128) antes de la capa de salida con 29 clases. A diferencia de una CNN, esta red no tiene forma de saber qué píxeles están cerca de cuáles, así que esperamos que su desempeño sea notablemente peor que el de las CNN. Esa comparación es justo lo que pide el ejercicio 5.
