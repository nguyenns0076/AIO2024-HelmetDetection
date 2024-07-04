from ultralytics import YOLO

MODEL_PATH = 'model\yolov10\yolov10n.pt'
model = YOLO(MODEL_PATH)

model.info()

YAML_PATH = '.\datasets\data.yaml'
EPOCHS = 5
IMG_SIZE = 320
BATCH_SIZE = 8

model.train(data=YAML_PATH,
            epochs=EPOCHS,
            imgsz=IMG_SIZE,
            batch=BATCH_SIZE)
