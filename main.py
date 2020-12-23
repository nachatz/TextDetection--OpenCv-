import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
#This tells us all of the strings in the image

### Detecting all strings
#Uses tesseract to yield all of the data on the image to strings.
def printStrings(img):
    print(pytesseract.image_to_string(img))


### Detecting characters
# Prints all of the data for each character found
def printCharacters(img):
    print(pytesseract.image_to_boxes(img))

# Detects all of the characters in the image.
# This is done by getting all of the boxes from the image
# that tesseract can read.
# Here we split each character into its own index and then we set the
# height width y and x
# Simply we draw rectangles around it from there
def detectChar(img):
    hImg, wImg, _ = img.shape
    boxes = pytesseract.image_to_boxes(img)

    for b in boxes.splitlines():
        print(b)
        b = b.split(' ')
        print(b)
        x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 0, 255), 3)
        cv2.putText(img, b[0], (x, hImg - y + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)


### Detecting words
# Same process, but with the image_to_data function which finds
# words in basic terms
def detectWords(img):
    hImg, wImg, _ = img.shape
    boxes = pytesseract.image_to_data(img)

    for x, b in enumerate(boxes.splitlines()):
        if (x != 0):
            b = b.split()
            print(b)
            if len(b) == 12:
                x,y,w,h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 3)
                cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)
                cv2.putText(img, "%: " + b[10], (x, y + 120), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

### Detecting digits
#Same as characters detection, but with a config to only look for digits

def detectDigits(img):
    hImg, wImg, _ = img.shape
    cong = r'--oem 3 --psm 6 outputbased digits'
    boxes = pytesseract.image_to_data(img, config=cong)

    for x, b in enumerate(boxes.splitlines()):
        if (x != 0):
            b = b.split()
            print(b)
            if len(b) == 12:
                x,y,w,h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 3)
                cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)



#Reads in the video
## for video feed

# cap = cv2.VideoCapture(0)
#Set width
# cap.set(3, 640)
#Set Height
# cap.set(4, 480)
#Set brightness
# cap.set(10, 100)
#
#Read each frame and display
# while True:
#     success, img = cap.read()
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     detectChar(img)
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break



img = cv2.imread("world.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
detectChar(img)
cv2.imshow("Output", img)
cv2.waitKey(0)

img = cv2.imread("world.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
detectWords(img)
cv2.imshow("Output", img)
cv2.waitKey(0)

img = cv2.imread("test.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
detectChar(img)
cv2.imshow("Output", img)
cv2.waitKey(0)

img = cv2.imread("test.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
detectWords(img)
cv2.imshow("Output", img)
cv2.waitKey(0)

img = cv2.imread("3.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
detectChar(img)
cv2.imshow("Output", img)
cv2.waitKey(0)


img = cv2.imread("5.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
detectChar(img)
cv2.imshow("Output", img)
cv2.waitKey(0)

