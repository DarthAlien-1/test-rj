import cv2
import numpy as np

def test_opencv_installation():
    assert cv2.__version__ is not None

def test_image_flip():
    dummy_img = np.array([[[1, 1, 1], [2, 2, 2]], 
                          [[3, 3, 3], [4, 4, 4]]], dtype=np.uint8)
    
    flipped = cv2.flip(dummy_img, 1)
    
    assert np.array_equal(flipped[0, 1], [1, 1, 1])
