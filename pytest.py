print("hello world from eclipse")
ide="eclipse"
print(ide)
#===============================================================================
# num=int(raw_input('Enter input:'))
#===============================================================================
file=open('input','r')
num=int(file.readline())
if num%2 == 0:
    print "blue"
else:
    print "red"
for line in file:
    print line

p=[43,'abc']
x=[18,p,'times\n york']
print x
x[1].append(12)
print len(x)
import pickle
file=open('datatest','w')
pickle.dump(x,file)
file.close()

file=open('datatest','r')
y=pickle.load(file)
print y

import cv2.cv as cv
import time

cv.NamedWindow("camera", 1)

capture = cv.CaptureFromCAM(0)

while True:
    img = cv.QueryFrame(capture)
    cv.ShowImage("camera", img)
    if cv.WaitKey(10) == 27:
        break
cv.DestroyAllWindows()
   