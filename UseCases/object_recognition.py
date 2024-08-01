import os

from ultralytics import YOLO
import cv2

current_dir = os.path.dirname(os.path.abspath(__file__))


RED = (255, 0, 0)
IMAGE_SAMPLE = cv2.imread(os.path.join(current_dir, "img.png"))


def main():
    model, classNames = get_model_data()
    webcam_recognition(model, classNames)
    # image_recognition(model, classNames, IMAGE_SAMPLE)
    exit()

def get_model_data():
    return (YOLO("../yolo-Weights/yolov8n.pt"),
            ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
             "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
             "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
             "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
             "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
             "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
             "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
             "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
             "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
             "teddy bear", "hair drier", "toothbrush"
             ])


def get_font_data(x, y):
    return [x, y], cv2.FONT_HERSHEY_DUPLEX, 2, RED, 2


def webcam_recognition(webcam_model, webcam_classnames):
    # Webcam and model setup
    cap = cv2.VideoCapture(0)
    cap.set(3, 800)
    cap.set(4, 600)

    if not cap.isOpened():
        print("Couldn't open camera")
        exit(1)

    while True:
        success, img = cap.read()
        recognitions = webcam_model(img, stream=True)

        for r in recognitions:
            for box in r.boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                cv2.rectangle(img, (x1, y1), (x2, y2), RED, 2)

                className = webcam_classnames[int(box.cls[0])]
                pos, font, fontScale, fontColor, fontWeight = get_font_data(x1, y1)

                cv2.putText(img, className, pos, font, fontScale, fontColor, fontWeight)

        cv2.imshow('Webcam', img)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    exit(0)


def image_recognition(image_model, image_classnames, image):
    recognitions = image_model(image)

    if len(recognitions) != 0:
        for r in recognitions:
            for box in r.boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                cv2.rectangle(image, (x1, y1), (x2, y2), RED, 2)

                className = image_classnames[int(box.cls[0])]
                pos, font, fontScale, fontColor, fontWeight = get_font_data(x1, y1)

                cv2.putText(image, className, pos, font, fontScale, fontColor, fontWeight)

    cv2.imshow("Result", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
