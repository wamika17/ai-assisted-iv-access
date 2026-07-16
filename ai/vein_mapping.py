"""
--------------------------------------------------------
Vein Mapping

Author: Wamika Varada
--------------------------------------------------------
"""

import cv2


def detect_veins(segmented_image):

    contours, _ = cv2.findContours(

        segmented_image,

        cv2.RETR_EXTERNAL,

        cv2.CHAIN_APPROX_SIMPLE

    )

    return contours
