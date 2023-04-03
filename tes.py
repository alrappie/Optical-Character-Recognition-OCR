import cv2
PATH = './Image/example02.jpg'
image = cv2.imread(PATH)
cv2.imshow('Original',image)
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()
