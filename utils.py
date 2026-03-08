import fitz  
import numpy as np
import cv2

def pdf_to_image(pdf_path):
    doc = fitz.open(pdf_path)
    page = doc[0] 
    pix = page.get_pixmap(dpi=300)
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
    
    if pix.n == 4:
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    
    return img

import cv2

def draw_boxes(image, boxes):

    for box in boxes:
        pts = [(int(x), int(y)) for x, y in box]

        cv2.line(image, pts[0], pts[1], (0,255,0), 2)
        cv2.line(image, pts[1], pts[2], (0,255,0), 2)
        cv2.line(image, pts[2], pts[3], (0,255,0), 2)
        cv2.line(image, pts[3], pts[0], (0,255,0), 2)

    return image