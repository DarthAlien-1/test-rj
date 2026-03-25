import cv2
import numpy as np

def test_opencv_installation():
    # Test kung tama ang setup ng library
    assert cv2.__version__ is not None

def test_image_flip():
    # Gagawa tayo ng fake image (2x2 pixels)
    dummy_img = np.array([[[1, 1, 1], [2, 2, 2]], 
                          [[3, 3, 3], [4, 4, 4]]], dtype=np.uint8)
    
    # I-flip
    flipped = cv2.flip(dummy_img, 1)
    
    # I-check kung nabaliktad nga (yung [1,1,1] naging nasa kanan)
    assert np.array_equal(flipped[0, 1], [1, 1, 1])