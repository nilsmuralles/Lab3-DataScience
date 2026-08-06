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

### Plan de procesamiento de imágenes

Para entrenar los cuatro modelos vamos a reutilizar el preprocesamiento que ya ya definido, por ello el plan sería:

- **Submuestra**: 700 imágenes por clase (20,300 en total), ya dividida de forma estratificada en `train_split.csv`, `val_split.csv` y `test_split.csv` (70% / 15% / 15%).
- **Resolución**: las imágenes se redimensionan de 200x200 a 64x64 píxeles, para que el entrenamiento sea manejable en el tiempo del laboratorio.
- **Normalización**: los valores de los píxeles se escalan de 0-255 a un rango de 0 a 1 antes de entrar a cualquier modelo.
- **Formato de entrada según el modelo**: las dos CNN reciben la imagen como matriz (64x64x3, conservando la estructura espacial), mientras que la red fully-connected y el Random Forest reciben la imagen aplanada en un solo vector, porque ninguno de los dos entiende de estructura espacial.
- **Augmentation**: se deja para después de tener los modelos base entrenados (ejercicio 7), y solo con transformaciones que no cambien el significado de la seña, como pequeños giros o cambios de brillo. Un flip horizontal queda descartado porque invertiría la mano y podría convertir una seña en otra distinta.
