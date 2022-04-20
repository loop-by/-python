from PIL import Image
import os
from os import listdir
from os.path import isfile, join

def makePDF(dir):
    images = [
        Image.open(dir+ "\\" + f)
        for f in listdir(dir) if isfile(join(dir, f))
    ]

    images[0].save(
        dir + ".pdf", "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
    )
