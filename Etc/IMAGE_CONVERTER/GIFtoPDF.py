from PIL import Image
import os

# imageDir = r'C:\Users\Admin\Desktop\file' #

def makePdf(imageDir):
    os.chdir(imageDir)

# Retrieved from: https://www.kite.com/python/answers/how-to-list-all-subdirectories-and-files-in-a-given-directory-in-python
# modified by: loop-by
    for root, subdirectories, files in os.walk(os.getcwd()):
        for subdirectory in subdirectories:
            # print
            imageDir = os.path.join(root, subdirectory)
            os.chdir(imageDir)
            savedir = os.getcwd()[os.getcwd().rfind("\\")+1:len(os.getcwd())]

            # Orignially Written by: Vaibhav Singh
            # Retrieved from: https://stackoverflow.com/questions/27327513/create-pdf-from-a-list-of-images
            # modified by: loop-by
            for j in os.listdir(os.getcwd()):
                try:
                    os.chdir(imageDir)
                    fname, fext = os.path.splitext(j)
                    newfilename = fname + ".pdf"
                    im = Image.open(fname + fext)
                    if im.mode == "RGBA":
                        im = im.convert("RGB")
                    os.chdir(r'..')
                    if not os.path.exists(r'PDF'):
                        os.mkdir(r'PDF')
                    os.chdir(r'PDF')
                    if not os.path.exists(savedir):
                        os.mkdir(savedir)
                    os.chdir(savedir)
                    if not os.path.exists(newfilename):
                        im.save(newfilename, "PDF", resolution=100.0)
                except Exception as e:
                    pass

# makePdf(imageDir)
