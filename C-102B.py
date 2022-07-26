import cv2
import dropbox
import time
import random
startTime = time.time()
def takeSnapshot():
    n = random.randint(0,100)
    vco = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = vco.read()
        print(ret)
        imagename = "img"+ str(n) + ".png"
        cv2.imwrite(imagename,frame)
        startTime = time.time()
        result = False
    return imagename
    print("Snapshot taken")
    
    vco.release()
    cv2.destroyAllWindows()

def uploadFile(imagename):
    accessToken = "sl.BKSAC2YornLX37TC_-IrIhc9gHsvJKUoXoYmZBQoocbvocisS02rQzKJVgFFhzOU56GxAI_a07mYaekALeSC0mmi6aw4M2Dnqj_YWBhMpMHjq8BtUEjMBKTj_99uSDyz-5KGKL3ZKHX8"
    file = imagename
    file2 = "/newimages/" + imagename
    dbx = dropbox.Dropbox(accessToken)
    with open(file2, "rb") as f:
        dbx.files_upload(f.read(),file2,mode = dropbox.files.WriteMode.overwrite)
        print("File uploaded")

def main():
    while(True):
        if((time.time()-startTime)>=3):
            name = takeSnapshot()
            uploadFile(name)

main()            



