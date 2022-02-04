from email.mime import image
import dropbox
import cv2
import time
import random 

start=time.time()
def takeSnapshot():
    videoCaptureObject=cv2.VideoCapture(0)
    flag=True
    minutes=300
    now=time.time()
    number=random.randint(1,900)
    print(now)
    print(start)
    while(flag==True):
        ret,frame=videoCaptureObject.read()
        img_name="image1.png"+number
        cv2.imwrite(img_name,frame)
        flag=False
        if(start-now<300):
            flag=True
        else:
            flag=False
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    return img_name

def upload_file(image):
    destination="/testfolder2/"+(image)
    access_token='sl.BBbjM6jyS9G7wS0nEN1Tp0DezwravSklg7Rs0bXJpFWVjNfjHqAM7QRpTx4xrA3ly6hMC-tLvbywaqu3pcru4mWa9i94A5gSsXBSoGj3E8Xu251wl1VUJbNf7_SOJpJnG5r2V68s7Tc'
    dbx=dropbox.Dropbox(access_token)
    f=open(image,'rb')
    dbx.files_upload(f.read(),destination)

def main():
    image=takeSnapshot()
    upload_file(image)

main()
