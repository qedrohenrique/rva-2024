import numpy as np
import cv2


def main():
    cap = cv2.VideoCapture(0)
    frame, boundary_box = select_object(cap)
    term_crit, roi_hist = get_metrics(frame, boundary_box)
    object_track(cap, term_crit, roi_hist, boundary_box)
    exit()

def select_object(cap):
    _, frame = cap.read()
    boundary_box = cv2.selectROI('Webcam', frame, False)

    return frame, boundary_box


def get_metrics(frame, boundary_box):
    x, y, w, h = boundary_box

    roi = frame[y:y + h, x:x + w]
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
    roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
    cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
    term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

    return term_crit, roi_hist


def object_track(cap, term_crit, roi_hist, boundary_box):
    while True:
        ret, frame = cap.read()

        if ret:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

            ret, track_window = cv2.meanShift(dst, boundary_box, term_crit)

            x, y, w, h = track_window
            img2 = cv2.rectangle(frame, (x, y), (x + w, y + h), 255, 2)
            cv2.imshow('Webcam', img2)

            if cv2.waitKey(1) == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

