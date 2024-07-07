from ultralytics import YOLO
import multiprocessing
import cv2

MODEL_PATH = 'model\yolov10\yolov10n.pt'
YAML_PATH = '.\datasets\data.yaml'


EPOCHS = 5
IMG_SIZE = 320
BATCH_SIZE = 8


def train():

    model = YOLO(MODEL_PATH)
    model.train(data=YAML_PATH,
                epochs=EPOCHS,
                imgsz=IMG_SIZE,
                batch=BATCH_SIZE)


TRAINED_MODEL_PATH = '.\\runs\detect\\train15\weights\\best.pt'
IMAGE_URL = '.\datasets\\test\images\helmet-98-_jpg.rf.1b419be3cdbc6ad2d9c36f7db3666d84.jpg'


def test():
    model = YOLO(TRAINED_MODEL_PATH)

    CONF_THRESHOLD = 0.3

    results = model(source=IMAGE_URL,
                    conf=CONF_THRESHOLD,
                    imgsz=IMG_SIZE)

    annotated_img = results[0].plot()
    cv2.imshow('ImageWindow', annotated_img)
    cv2.waitKey()


def val():

    model = YOLO(TRAINED_MODEL_PATH)

    model.val(data=YAML_PATH,
              imgsz=IMG_SIZE,
              split='test')


if __name__ == '__main__':
    multiprocessing.freeze_support()
    # train()
    # test()
    val()
