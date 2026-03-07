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