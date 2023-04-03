import cv2
from PIL import Image
import pytesseract

PATH = './Image/example01.png'

im = Image.open(PATH)
print(im)
im.show()