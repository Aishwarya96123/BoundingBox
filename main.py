import cv2
import pytesseract
import numpy as np 
from PIL import Image 
import sys
from pytesseract import Output

img = cv2.imread('C:/Users/4122/Desktop/result.png')

d = pytesseract.image_to_data(img, output_type=Output.DICT)
n_boxes = len(d['level'])
for i in range(n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    

cv2.imshow('img', img)
cv2.waitKey(0)

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\4122\Desktop\Tesseract-OCR\tesseract.exe'

img = cv2.imread(r'C:\Users\4122\Desktop\result.png')
 
d = pytesseract.image_to_data(img, output_type=Output.DICT)
import pandas as pd
df=pd.DataFrame(d)
print (d)
#df.head()
print(d.keys()) 
print(d['text']) 
df.head() 
data = pd.read_excel('C:/Users/4122/Desktop/Copy of Copy of processheet2.xlsx')
data
excel_df=pd.DataFrame(data)
excel_df.columns=df.iloc[1]
excel_df.head()

LAdf=data['Local Authority'].dropna()
IDdf=data['Document ID'].dropna()
DAdf=data['Date1'].dropna()
LAdf.head()

LAlist=list(LAdf)
IDlist=list(IDdf)
DAlist=list(DAdf)

LAlist.pop(0)
IDlist.pop(0)
DAlist.pop(0)

print(LAlist)
print(IDlist)
print(DAlist)
###check if word is present in the document
mylist=[]
mylist.extend(LAlist)
mylist.extend(IDlist)
mylist.extend(DAlist)
print(mylist)
matching_string=[]

for i in mylist:
    if i in d['text']:
        matching_string.append(i)
print(matching_string)

for item in matching_string:
    left=df[df['text']==item].left
    height=df[df['text']==item].height
    top=df[df['text']==item].top
    width=df[df['text']==item].width
    left=list(left)
    height=list(height)
    top=list(top)
    width=list(width)
    left=left[0]
    width=width[0]
    height=height[0]
    top=top[0]
    (x, y, w, h) = (left, top, width, height)
    cv2.rectangle(img, (x-5, y-5), (x + w+15, y + h+15), (0, 255, 0), 2)

cv2.imwrite('‪image.png',img)
cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

