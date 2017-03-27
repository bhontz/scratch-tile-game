"""
    SplitImageIntoTiles.py
    
    Created for Scratch Tile Game STEM training project 3/26/2017.  See Scratch project: "Tile Game Brad Head"
    
    Takes a 4:3 aspect ratio image (i.e. standard iPhone landscape size) and splits it into 9 160 x 120 px tiles after resizing
    the orginal image to Scratch's stage size of 480 x 360 px.
    
    * NOTE * YOU MAY WISH TO SAVE A COPY OF YOUR ORIGINAL IMAGE TO AVOID RESIZING THE ORIGINAL !!!
    
    I manually create a "blank" image of 160 x 120 px in GIMP (I stroke the border to dress it up).
    
    The resulant image tiles, which are written to the desktop, are imported as sprites into Scratch
   
"""

from PIL import Image   # pip install pillow  - the pillow module will install PIL
import os

def resize(infile, targetwidth):
    img = Image.open(infile)
    wpercent = (targetwidth / float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((targetwidth, hsize), Image.ANTIALIAS)
    img.save(infile)     

def crop(infile,height,width):
    im = Image.open(infile)
    imgwidth, imgheight = im.size
    for i in range(imgheight / height):
        for j in range(imgwidth / width):
            box = (j*width, i*height, (j+1)*width, (i+1)*height)
            yield im.crop(box)

        
if __name__ == '__main__':
    
    infile='/users/admin/desktop/clockface.jpg'   # path to your iPhone portrait aspect photo
    
    targetwidth = 480
    width=160   # 160 x 120 yields 9 equal pieces of a 480 x 360 px image
    height=120
    start_num=1
    
    resize(infile, targetwidth)  # first resize the original image to Scratch's stage size of 480 x 360 px
    
    for k, piece in enumerate(crop(infile,height,width),start_num):   # now break the image up into up into 9 even tiles
        img=Image.new('RGB', (width, height), 255)
        img.paste(piece)
        path=os.path.join(os.path.split(infile)[0],"TILE-%s.jpg" % k)
        img.save(path)
    
            