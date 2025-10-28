import cv2
import pickle
import os 
os.chdir("C:/Users/NEDER/Desktop/Parking")
cap = cv2.VideoCapture("C:/Users/NEDER/Desktop/Parking/parking.mp4")
w,h=50,110
pts=[]
try:
    with open("placesPosition","rb") as f:
        pts=pickle.load(f)



except:

    print("No file found")


def mouse(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        pts.append((x,y))
    if event == cv2.EVENT_MBUTTONDOWN:
        pts.pop(-1) #remove the last point
    with open("placesPosition","wb") as f:
        pickle.dump(pts,f) #save the points to the file
   
while True:
    success, img = cap.read()
    img=cv2.resize(img,(720,480))
    for X,Y in pts:
        cv2.rectangle(img,(X,Y),(X+w,Y+h),(0,0,255),2)
           

    cv2.imshow("Image", img)

    cv2.setMouseCallback("Image",mouse)
    
    
    if cv2.waitKey(200) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
