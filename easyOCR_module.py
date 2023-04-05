import easyocr
import cv2
import sys

def main():
    reader = easyocr.Reader(['id'],False)
    path_img = sys.argv[1]
    image = cv2.imread(path_img)
    image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imwrite('./hasil.jpg',image_gray)
    hasil = reader.readtext('./hasil.jpg')
    hasil = ' '.join([row[1] for row in hasil])
    with open(r'C:\Users\alrav\Desktop\OCR_hasil.txt', 'w') as f:
        f.writelines(hasil)
    
if '__main__' == __name__:
    main()