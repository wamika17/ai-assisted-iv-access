
import cv2


def segment_veins(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (5,5), 0)

    segmented = cv2.adaptiveThreshold(

        blurred,

        255,

        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,

        cv2.THRESH_BINARY,

        11,

        2

    )

    return segmented
