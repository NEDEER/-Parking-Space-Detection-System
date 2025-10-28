import cv2
import os
import pickle
import cvzone
w,h=50,100
cap=cv2.VideoCapture("C:/Users/NEDER/Desktop/Parking/parking.mp4")
os.chdir("C:/Users/NEDER/Desktop/Parking")
positions=[]
with open("placesPosition","rb") as f:
    positions=pickle.load(f)
    print(positions)

def checkParkingSpace(img, imgProcess):
    placecount=0
    for x,y in positions:
        place_img=imgProcess[y:y+h,x:x+w]
        pxcount=cv2.countNonZero(place_img)
        cvzone.putTextRect(img,str(pxcount),(x,y),scale=1,thickness=2,offset=0)
        print(pxcount)
        if pxcount<700:
            color=(0,255,0) #green
            placecount+=1
        else:
            
            color=(0,0,255)#red
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
    # Draw text vertically outside the loop
    x, y = 30, 60  # starting position
    text = "FREE " + str(placecount) + "/" + str(len(positions))
    # Loop through characters to draw vertically
    for ch in text:
        cvzone.putTextRect(img, ch, pos=(x, y), scale=2, thickness=2,
                    offset=10)
        y += 50
    #cvzone.putTextRect(img,f"Free: {placecount}/{len(positions)}",(100,150),scale=2,thickness=3,offset=0)
while True:
    success,img=cap.read()
    img = cv2.resize(img, (720, 480))
    edged=cv2.Canny(img,100,300)
    checkParkingSpace(img, edged)
    cv2.imshow("Video",img)
    # cv2.imshow("edged",edged)
    if cv2.waitKey(200) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

