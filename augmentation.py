from tensorflow import keras
from tensorflow.keras import layers

RANDOM_SEED = 42

def get_augmentation_pipeline(seed: int = RANDOM_SEED) -> keras.Sequential:
    return keras.Sequential(
        [
            layers.RandomRotation(15 / 360, fill_mode="nearest", seed=seed),
            layers.RandomTranslation(0.1, 0.1, fill_mode="nearest", seed=seed),
            layers.RandomZoom(0.15, fill_mode="nearest", seed=seed),
            layers.RandomBrightness(0.2, value_range=(0.0, 1.0), seed=seed),
            layers.RandomContrast(0.2, seed=seed),
        ],
        name="asl_data_augmentation",
    )
