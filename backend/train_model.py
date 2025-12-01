import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing import image_dataset_from_directory
import matplotlib.pyplot as plt
import os, sys, json

# ======================================================================================
# 1. PATH SETTINGS
# ======================================================================================

BASE_DIR = r"C:\Users\HARSH\AI_breed_app\backend\IndianCattleBuffaloeBreeds-Dataset\breeds"
TRAIN_DIR = os.path.join(BASE_DIR, "train")
TEST_DIR = os.path.join(BASE_DIR, "test")

MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)

MODEL_PATH = os.path.join(MODEL_DIR, "fine_tuned_model.h5")
LABEL_PATH = os.path.join(MODEL_DIR, "labels.json")

# Verify dataset exists
if not os.path.exists(TRAIN_DIR):
    print(f"❌ Train folder not found: {TRAIN_DIR}")
    sys.exit(1)

if not os.path.exists(TEST_DIR):
    print(f"❌ Test folder not found: {TEST_DIR}")
    sys.exit(1)


# ======================================================================================
# 2. DATA LOADING
# ======================================================================================

IMG_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 10

print("Loading dataset...")
train_ds = image_dataset_from_directory(
    TRAIN_DIR,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)

test_ds = image_dataset_from_directory(
    TEST_DIR,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)

class_names = train_ds.class_names
print("\nClasses:", class_names)

train_ds = train_ds.prefetch(buffer_size=tf.data.AUTOTUNE)
test_ds = test_ds.prefetch(buffer_size=tf.data.AUTOTUNE)


# ======================================================================================
# 3. MobileNetV2 Fine-Tuned Model
# ======================================================================================

def build_finetuned_model():
    base_model = tf.keras.applications.MobileNetV2(
        weights='imagenet',
        include_top=False,
        input_shape=(224, 224, 3)
    )

    base_model.trainable = False  # freeze base for now

    model = models.Sequential([
        layers.Rescaling(1.0/255),
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.Dense(256, activation='relu'),
        layers.Dropout(0.3),
        layers.Dense(len(class_names), activation='softmax')
    ])

    model.compile(
        optimizer=tf.keras.optimizers.Adam(),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    return model


model = build_finetuned_model()
print("\nModel Summary:")
model.summary()


# ======================================================================================
# 4. TRAIN
# ======================================================================================

print("\nTraining MobileNetV2...")
history = model.fit(train_ds, validation_data=test_ds, epochs=EPOCHS)


# ======================================================================================
# 5. SAVE MODEL
# ======================================================================================

model.save(MODEL_PATH)
print(f"\n✅ Fine-tuned model saved at: {MODEL_PATH}")


# ======================================================================================
# 6. SAVE LABELS
# ======================================================================================

labels = {i: class_names[i] for i in range(len(class_names))}

with open(LABEL_PATH, "w") as f:
    json.dump(labels, f, indent=4)

print(f"✅ labels.json saved at: {LABEL_PATH}")


# ======================================================================================
# 7. PLOT ACCURACY (Optional)
# ======================================================================================

plt.plot(history.history['accuracy'], label='train')
plt.plot(history.history['val_accuracy'], label='val')
plt.title("Training Accuracy")
plt.legend()
plt.savefig("accuracy_plot.png")
plt.show()

print("\n🎉 Training Complete!")
